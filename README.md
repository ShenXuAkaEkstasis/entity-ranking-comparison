# Entity Ranking Comparison

## Overview

This project investigates whether traditional popularity-based rankings and knowledge graph-based entity importance rankings capture the same notion of importance.

Using movie entities as a case study, this research compares IMDb user ranking with Wikipedia hyperlink network PageRank.

The goal is to explore whether knowledge graph structures can reveal important entities that are not fully captured by conventional ranking systems.

---

## Research Questions

### RQ1
How strongly does traditional user-based ranking correlate with knowledge graph centrality?

### RQ2
Do popularity rankings and graph-based rankings identify the same top entities?

### RQ3
Can knowledge graph ranking reveal entities with high structural importance but lower conventional ranking positions?

---

## Dataset

Dataset construction:

- 482 movie entities
- IMDb metadata
- Wikidata entity identifiers
- English Wikipedia hyperlink network

Wikipedia pages are treated as nodes, and hyperlinks between movie pages are modeled as directed edges.

Final graph:

- Nodes: 482
- Edges: 13,690
- Average Degree: 56.80
- Density: 0.059049
- Connected Components: 1

---

## Methodology

### Knowledge Graph Construction

The project:

1. Collects movie entities from IMDb datasets.
2. Matches entities with Wikidata identifiers.
3. Extracts Wikipedia page hyperlinks.
4. Builds a directed entity graph.

### Ranking Methods

Two ranking systems are compared:

### IMDb Ranking

Represents audience-based popularity and rating preference.

### Wikipedia PageRank

Represents structural importance within the knowledge network.

---

## Experiments

### Experiment 1: Rank Correlation

Spearman correlation between IMDb ranking and Wikipedia PageRank:


Spearman rho = 0.2275
p-value < 0.001


The result indicates a statistically significant but weak correlation.

---

### Experiment 2: Top-K Overlap

Overlap between IMDb top entities and PageRank top entities:

| Top K | Overlap |
|---|---|
| Top 10 | 10% |
| Top 25 | 24% |
| Top 50 | 30% |
| Top 100 | 34% |

The limited overlap suggests that the two ranking systems capture different dimensions of entity importance.

---

### Experiment 3: Divergence Analysis

Examples where Wikipedia PageRank identifies higher structural importance:

- Titanic
- Avatar
- Crouching Tiger, Hidden Dragon
- E.T. the Extra-Terrestrial
- Slumdog Millionaire

Examples where IMDb ranking is higher than graph centrality:

- Fight Club
- 12 Angry Men
- Whiplash
- Seven Samurai
- The Godfather Part II

---

## Repository Structure


scripts/
Data collection and analysis scripts

data/
Local generated datasets

results/
Experimental outputs

figures/
Visualization results


---

## Reproduction

Install dependencies:

```bash
pip install -r requirements.txt

Run scripts sequentially:

python3 scripts/01_prepare_dataset.py
python3 scripts/02_match_wikidata.py
python3 scripts/03_download_links.py
python3 scripts/04_build_graph.py
python3 scripts/05_compare.py
python3 scripts/06_figures.py
python3 scripts/07_topk_overlap.py
python3 scripts/08_divergence_analysis.py
python3 scripts/09_graph_statistics.py
Research Direction

This project explores the difference between popularity ranking and knowledge-based entity ranking, providing an empirical foundation for understanding entity importance in AI-era information systems.


保存。

然后：

```bash
git add README.md
git commit -m "Add project README"
git push