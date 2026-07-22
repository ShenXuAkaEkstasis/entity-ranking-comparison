from pathlib import Path
import gzip
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

basics = ROOT / "raw_data" / "title.basics.tsv.gz"
ratings = ROOT / "raw_data" / "title.ratings.tsv.gz"

print("Loading IMDb data...")

basics_df = pd.read_csv(
    gzip.open(basics, "rt", encoding="utf-8"),
    sep="\t",
    low_memory=False
)

ratings_df = pd.read_csv(
    gzip.open(ratings, "rt", encoding="utf-8"),
    sep="\t"
)

print("Filtering movies...")

df = basics_df.merge(ratings_df, on="tconst")

df = df[df["titleType"] == "movie"]
df = df[df["isAdult"] == 0]
df = df[df["startYear"] != "\\N"]
df = df[df["averageRating"] >= 7.0]
df = df[df["numVotes"] >= 50000]

df = df.sort_values(
    ["averageRating", "numVotes"],
    ascending=[False, False]
).head(500)

output = ROOT / "data" / "movies.csv"

df[[
    "tconst",
    "primaryTitle",
    "startYear",
    "averageRating",
    "numVotes"
]].to_csv(output, index=False)

print(df[[
    "primaryTitle",
    "averageRating",
    "numVotes"
]].head(20))

print(f"\nSaved {len(df)} movies -> {output}")