from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    ROOT / "results" / "comparison.csv"
)

print("Columns:")
print(df.columns.tolist())


# 自动识别标题字段
if "title" in df.columns:
    title_col = "title"
elif "primaryTitle" in df.columns:
    title_col = "primaryTitle"
elif "title_x" in df.columns:
    title_col = "title_x"
else:
    title_col = None


# PageRank high but IMDb lower
pagerank_gain = df.sort_values(
    "pagerank_rank"
).head(50)

pagerank_gain = pagerank_gain.sort_values(
    "imdb_rank",
    ascending=False
).head(20)


# IMDb high but PageRank lower
imdb_gain = df.sort_values(
    "imdb_rank"
).head(50)

imdb_gain = imdb_gain.sort_values(
    "pagerank_rank",
    ascending=False
).head(20)


pagerank_gain.to_csv(
    ROOT / "results" / "pagerank_over_imdb.csv",
    index=False
)

imdb_gain.to_csv(
    ROOT / "results" / "imdb_over_pagerank.csv",
    index=False
)


print("\n=== PageRank high but IMDb lower ===")

cols = ["imdb_rank", "pagerank_rank"]

if title_col:
    cols.insert(0, title_col)

print(
    pagerank_gain[cols].to_string(index=False)
)


print("\n=== IMDb high but PageRank lower ===")

print(
    imdb_gain[cols].to_string(index=False)
)


print("\nSaved divergence analysis files.")