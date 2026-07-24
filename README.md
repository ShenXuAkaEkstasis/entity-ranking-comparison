# Entity Ranking Comparison: A Dual-Signal Framework for AI Knowledge Systems

This repository contains the research materials and experimental resources for:

**Representing Entity Importance in AI Knowledge Systems: A Dual-Signal Framework of Audience Evaluation and Structural Authority**

## Paper

**Shen Xu (2026)**

arXiv preprint:

https://arxiv.org/abs/2607.20925

## Overview

AI knowledge systems increasingly rely on representations of entity importance for retrieval, recommendation, evidence selection, and knowledge-intensive reasoning.

However, entity importance is often simplified into a single ranking score, which may overlook different forms of importance that matter for different AI tasks.

This research introduces a dual-signal framework that represents entity importance through two complementary dimensions:

- **Audience Evaluation** — how entities are perceived and valued by audiences
- **Structural Authority** — how entities are positioned and connected within knowledge networks

The goal is not to create another ranking algorithm, but to investigate whether multiple importance signals should be preserved before AI systems perform task-specific selection or aggregation.

## Research Question

Can entity importance in AI knowledge systems be adequately represented by a single signal?

This project examines whether audience-based evaluation and network-based authority capture different aspects of entity importance.

## Methodology

The empirical validation uses movie entities as the evaluation domain.

Data sources:

- IMDb non-commercial datasets for audience evaluation signals
- Wikidata for entity alignment
- English Wikipedia hyperlink networks for structural authority analysis

Structural authority is estimated using PageRank on the Wikipedia knowledge network.

## Key Findings

Experiments on:

- 482 entities
- 13,690 directed relationships

show that:

- Audience Evaluation and Structural Authority are statistically related but largely non-redundant
- The correlation between the two dimensions is significant but weak
- High-ranking entities in one dimension do not necessarily dominate the other dimension

These results suggest that AI knowledge systems may benefit from maintaining multiple dimensions of entity importance rather than collapsing them into a single scalar score.

## Repository Structure

- figures/
  - figure1_framework.pdf
  - figure2_rank_correlation.pdf
  - figure3_topk_overlap.pdf

- paper/
  - Representing_Entity_Importance.pdf

- references.bib

- README.md

## Citation

If you find this work useful, please cite:

Xu, Shen. (2026). Representing Entity Importance in AI Knowledge Systems: A Dual-Signal Framework of Audience Evaluation and Structural Authority. arXiv:2607.20925.

BibTeX:

@article{xu2026entityimportance,
  title={Representing Entity Importance in AI Knowledge Systems: A Dual-Signal Framework of Audience Evaluation and Structural Authority},
  author={Xu, Shen},
  journal={arXiv preprint arXiv:2607.20925},
  year={2026}
}

## Research Context

This project is part of ongoing research on:

- AI knowledge systems
- Entity representation
- Information retrieval
- Agentic search environments
- AI-mediated discovery and decision systems

## License

This repository contains research materials associated with the arXiv preprint.
