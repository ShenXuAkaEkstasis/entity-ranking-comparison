from pathlib import Path
from urllib.parse import unquote
import time
import requests
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = ROOT / "data" / "movies_wikidata.csv"
OUTPUT_FILE = ROOT / "data" / "edges.csv"
PROGRESS_FILE = ROOT / "data" / "link_progress.csv"

API_URL = "https://en.wikipedia.org/w/api.php"

HEADERS = {
    "User-Agent": "EntityRankingComparison/1.0"
}

movies = pd.read_csv(INPUT_FILE)

movies = movies.dropna(
    subset=["qid", "wikipedia_title"]
).copy()

movies["wikipedia_title"] = (
    movies["wikipedia_title"]
    .astype(str)
    .map(unquote)
    .str.replace("_", " ", regex=False)
)

title_to_qid = dict(
    zip(
        movies["wikipedia_title"],
        movies["qid"]
    )
)

valid_titles = set(title_to_qid.keys())

if PROGRESS_FILE.exists():
    progress_df = pd.read_csv(PROGRESS_FILE)
    completed_titles = set(progress_df["source_title"])
else:
    progress_df = pd.DataFrame(
        columns=[
            "source_qid",
            "source_title",
            "target_qid",
            "target_title"
        ]
    )
    completed_titles = set()

all_edges = progress_df.to_dict("records")


def get_page_links(title):
    links = []
    continue_token = None

    while True:
        params = {
            "action": "query",
            "format": "json",
            "prop": "links",
            "titles": title,
            "pllimit": "max",
            "redirects": 1
        }

        if continue_token:
            params["plcontinue"] = continue_token

        for attempt in range(5):
            try:
                response = requests.get(
                    API_URL,
                    params=params,
                    headers=HEADERS,
                    timeout=30
                )

                response.raise_for_status()
                data = response.json()
                break

            except Exception as error:
                if attempt == 4:
                    print(f"Failed: {title}")
                    print(error)
                    return links

                time.sleep(2 ** attempt)

        pages = data.get("query", {}).get("pages", {})

        for page in pages.values():
            for link in page.get("links", []):
                linked_title = link.get("title")

                if linked_title:
                    links.append(linked_title)

        continue_token = data.get(
            "continue",
            {}
        ).get("plcontinue")

        if not continue_token:
            break

        time.sleep(0.1)

    return links


total = len(movies)

for index, row in movies.iterrows():
    source_title = row["wikipedia_title"]
    source_qid = row["qid"]

    if source_title in completed_titles:
        continue

    page_links = get_page_links(source_title)

    matched_targets = set(page_links).intersection(valid_titles)

    for target_title in matched_targets:
        target_qid = title_to_qid[target_title]

        if target_qid == source_qid:
            continue

        all_edges.append({
            "source_qid": source_qid,
            "source_title": source_title,
            "target_qid": target_qid,
            "target_title": target_title
        })

    completed_titles.add(source_title)

    pd.DataFrame(all_edges).drop_duplicates().to_csv(
        PROGRESS_FILE,
        index=False
    )

    print(
        f"{len(completed_titles)}/{total} "
        f"| {source_title} "
        f"| links found: {len(matched_targets)}"
    )

    time.sleep(0.2)

edges_df = pd.DataFrame(all_edges)

edges_df = edges_df.drop_duplicates(
    subset=["source_qid", "target_qid"]
)

edges_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print(f"\nSaved {len(edges_df)} edges")
print(f"Output: {OUTPUT_FILE}")