from pathlib import Path
import networkx as nx

ROOT = Path(__file__).resolve().parent.parent

GRAPH_FILE = ROOT / "data" / "movie_graph.graphml"

G = nx.read_graphml(GRAPH_FILE)

print("=== Graph Statistics ===")

print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")

density = nx.density(G)

print(f"Density: {density:.6f}")

avg_degree = sum(dict(G.degree()).values()) / G.number_of_nodes()

print(f"Average Degree: {avg_degree:.2f}")

components = nx.number_weakly_connected_components(G)

print(f"Weakly Connected Components: {components}")

largest_component = max(
    nx.weakly_connected_components(G),
    key=len
)

print(
    f"Largest Component Size: {len(largest_component)}"
)

print(
    f"Coverage: {len(largest_component)/G.number_of_nodes():.2%}"
)

ROOT.joinpath("results").mkdir(exist_ok=True)

with open(
    ROOT / "results" / "graph_statistics.txt",
    "w"
) as f:
    f.write(
        f"Nodes: {G.number_of_nodes()}\n"
        f"Edges: {G.number_of_edges()}\n"
        f"Density: {density:.6f}\n"
        f"Average Degree: {avg_degree:.2f}\n"
        f"Weak Components: {components}\n"
        f"Largest Component: {len(largest_component)}\n"
    )

print("\nSaved graph_statistics.txt")