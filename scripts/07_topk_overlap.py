from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    ROOT / "results" / "comparison.csv"
)

results = []

for k in [10, 25, 50, 100]:

    imdb_top = set(
        df.nsmallest(k, "imdb_rank")["qid"]
    )

    pagerank_top = set(
        df.nsmallest(k, "pagerank_rank")["qid"]
    )

    overlap = len(
        imdb_top.intersection(pagerank_top)
    )

    results.append({
        "Top_K": k,
        "Overlap": overlap,
        "Overlap_Rate": overlap / k
    })

result_df = pd.DataFrame(results)

print(result_df)

result_df.to_csv(
    ROOT / "results" / "topk_overlap.csv",
    index=False
)

print("\nSaved topk_overlap.csv")