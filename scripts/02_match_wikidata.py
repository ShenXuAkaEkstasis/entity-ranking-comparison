from pathlib import Path
import time
import requests
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

movies = pd.read_csv(ROOT / "data" / "movies.csv")

URL = "https://query.wikidata.org/sparql"

HEADERS = {
    "User-Agent": "EntityRankingComparison/1.0",
    "Accept": "application/sparql-results+json"
}

results = []

for i, row in movies.iterrows():

    imdb = row["tconst"]

    query = f"""
    SELECT ?item ?article
    WHERE {{
      ?item wdt:P345 "{imdb}" .

      ?article schema:about ?item ;
               schema:isPartOf <https://en.wikipedia.org/> .
    }}
    LIMIT 1
    """

    try:
        r = requests.get(
            URL,
            params={"query": query},
            headers=HEADERS,
            timeout=30,
        )

        r.raise_for_status()

        bindings = r.json()["results"]["bindings"]

        if bindings:
            qid = bindings[0]["item"]["value"].split("/")[-1]
            wiki = bindings[0]["article"]["value"]
            title = wiki.split("/")[-1]
        else:
            qid = None
            wiki = None
            title = None

    except Exception:
        qid = None
        wiki = None
        title = None

    results.append({
        "tconst": imdb,
        "primaryTitle": row["primaryTitle"],
        "qid": qid,
        "wikipedia_title": title,
        "wikipedia_url": wiki,
    })

    if (i + 1) % 20 == 0:
        print(f"{i+1}/{len(movies)}")

    time.sleep(0.1)

df = pd.DataFrame(results)

df.to_csv(ROOT / "data" / "movies_wikidata.csv", index=False)

print(df.head())

print(f"\nMatched: {df['qid'].notna().sum()} / {len(df)}")