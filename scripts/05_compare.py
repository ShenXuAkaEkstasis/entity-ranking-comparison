from pathlib import Path
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parent.parent

movies = pd.read_csv(ROOT / "data" / "movies.csv")
wikidata = pd.read_csv(ROOT / "data" / "movies_wikidata.csv")
pagerank = pd.read_csv(ROOT / "data" / "pagerank.csv")

df = movies.merge(
    wikidata[["tconst", "qid"]],
    on="tconst"
)

df = df.merge(
    pagerank,
    on="qid"
)

df["imdb_rank"] = (
    df["averageRating"]
      .rank(ascending=False, method="first")
)

df["pagerank_rank"] = (
    df["pagerank"]
      .rank(ascending=False, method="first")
)

rho, p = spearmanr(
    df["imdb_rank"],
    df["pagerank_rank"]
)

print(f"Movies: {len(df)}")
print(f"Spearman rho: {rho:.4f}")
print(f"P-value: {p:.6g}")

ROOT.joinpath("results").mkdir(exist_ok=True)

df.to_csv(
    ROOT / "results" / "comparison.csv",
    index=False
)