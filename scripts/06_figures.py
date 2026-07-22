from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent

df = pd.read_csv(ROOT / "results" / "comparison.csv")

ROOT.joinpath("figures").mkdir(exist_ok=True)

plt.figure(figsize=(8,6))

plt.scatter(
    df["imdb_rank"],
    df["pagerank_rank"],
    s=18,
    alpha=0.6
)

plt.xlabel("IMDb Rank")
plt.ylabel("Wikipedia PageRank")
plt.title("IMDb Rank vs Wikipedia PageRank")

plt.tight_layout()

plt.savefig(
    ROOT / "figures" / "rank_scatter.png",
    dpi=300
)

print("Saved figures/rank_scatter.png")