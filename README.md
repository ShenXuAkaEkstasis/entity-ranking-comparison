# Entity Importance Representation for AI Knowledge Systems

## Overview

This repository supports the study **“Representing Entity Importance in AI Knowledge Systems: A Dual-Signal Framework of Audience Evaluation and Structural Authority.”**

The study treats entity importance as a knowledge-representation problem. Instead of compressing importance into one scalar score, it preserves two interpretable dimensions:

- **Audience evaluation, `A(e)`:** an IMDb rating-based audience ranking constructed from average user ratings, with vote count used for eligibility and tie breaking.
- **Structural authority, `S(e)`:** PageRank calculated over a directed network of hyperlinks among English Wikipedia movie pages.

The entity representation is:

```text
I(e) = [A(e), S(e)]
```

The study tests whether these dimensions are sufficiently redundant to be collapsed into one score. It does **not** use IMDb's proprietary popularity chart, Wikipedia pageviews, or Wikidata PageRank.

## Research Questions

1. Are audience evaluation and structural authority sufficiently correlated to be treated as one dimension of entity importance?
2. Do the two dimensions produce the same high-priority entity sets?
3. What information is exposed by entities whose positions diverge strongly across the two dimensions?

## Dataset Construction

The candidate set is built from IMDb non-commercial datasets:

- `raw_data/title.basics.tsv.gz`
- `raw_data/title.ratings.tsv.gz`

Records are retained when they:

- have `titleType = movie`;
- have `isAdult = 0`;
- have a known release year;
- have `averageRating >= 7.0`;
- have `numVotes >= 50000`.

Eligible records are sorted by average rating in descending order and then by vote count in descending order. The first 500 records form the candidate set.

Each candidate is aligned to Wikidata through IMDb identifier property `P345`, and the corresponding English Wikipedia article is retrieved when available. The final analytical sample contains 482 entities that have usable cross-source mappings and participate in the induced hyperlink graph.

## Knowledge-Network Construction

English Wikipedia pages are represented as nodes, and hyperlinks among the aligned movie pages are represented as directed edges.

The graph-construction process:

1. queries the English Wikipedia MediaWiki Action API;
2. resolves redirects and follows continuation tokens;
3. retains links only when both source and target belong to the aligned movie set;
4. removes self-links;
5. collapses duplicate source-target pairs.

Final graph statistics:

- Nodes: 482
- Directed edges: 13,690
- Average degree: 56.80
- Density: 0.059049
- Weakly connected components: 1

## Operationalized Dimensions

### Audience Evaluation

Within the final 482-entity sample, movies are ordered by weighted average IMDb user rating in descending order. Vote count resolves equal-rating cases. This dimension represents audience evaluation, not direct exposure, attention, or population-level popularity.

### Structural Authority

PageRank is calculated on the directed Wikipedia hyperlink graph with NetworkX using:

```python
nx.pagerank(G, alpha=0.85)
```

PageRank scores are sorted in descending order and converted to ordinal ranks.

## Main Results

- Spearman correlation: `rho = 0.2275`, `p < 0.001`
- Top-10 overlap: 10%
- Top-25 overlap: 24%
- Top-50 overlap: 30%
- Top-100 overlap: 34%

The results indicate that audience evaluation and structural authority are non-redundant dimensions. The paper argues that AI knowledge systems should preserve them separately before task-specific aggregation or entity selection.

## Repository Structure

```text
raw_data/       IMDb source files supplied locally by the user
scripts/        Data preparation, entity alignment, graph construction, and analysis
data/           Derived intermediate datasets
results/        Ranking and statistical outputs
figures/        Generated figures
```

## Installation

Python 3.9 or later is recommended.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Execution Order

```bash
python scripts/01_prepare_dataset.py
python scripts/02_match_wikidata.py
python scripts/03_download_links.py
python scripts/04_build_graph.py
python scripts/05_compare.py
python scripts/06_figures.py
python scripts/07_topk_overlap.py
python scripts/08_divergence_analysis.py
python scripts/09_graph_statistics.py
```

The Wikidata and Wikipedia stages require internet access and depend on public endpoints. Live reruns may differ if external datasets or pages change. The derived datasets, scripts, and results reported in the manuscript are archived in commit `9f14a19`.

## Data Sources

- IMDb Non-Commercial Datasets
- Wikidata Query Service
- English Wikipedia MediaWiki Action API
