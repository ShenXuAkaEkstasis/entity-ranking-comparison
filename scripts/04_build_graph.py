from pathlib import Path
import pandas as pd
import networkx as nx

ROOT = Path(__file__).resolve().parent.parent

edges = pd.read_csv(ROOT / "data" / "edges.csv")

G = nx.DiGraph()

for _, row in edges.iterrows():
    G.add_edge(row["source_qid"], row["target_qid"])

print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")

nx.write_graphml(
    G,
    ROOT / "data" / "movie_graph.graphml"
)

pagerank = nx.pagerank(
    G,
    alpha=0.85
)

df = pd.DataFrame(
    pagerank.items(),
    columns=["qid", "pagerank"]
)

df = df.sort_values(
    "pagerank",
    ascending=False
)

df.to_csv(
    ROOT / "data" / "pagerank.csv",
    index=False
)

print(df.head(20))

print("\nSaved pagerank.csv")