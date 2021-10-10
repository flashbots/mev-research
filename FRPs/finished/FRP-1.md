---
id: 1
title: MEV Taxonomy
team: @fiiiu
created: 2021-03-04
status: finished
---

# MEV Taxonomy

While the MEV concept as such was introduced in 2019 in the [Flashboys 2.0 paper](https://arxiv.org/abs/1904.05234), since which plenty of discussion has taken place on its quantification and its different sources, we still lack a clear classification of MEV. In this proposal, we aim at establishing a clear-cut taxonomy of MEV to which we can reference our engineering efforts.

## Background and Problem Statement
A lot has been said about the risks of MEV, and several attempts have been made at measuring it, each proposing a different classification strategy (see References section). While there's a priori no particular classification that trumps the rest, it is useful for our engineering efforts to have one that we can reference in order to avoid ambiguity. This is important in particular in our measurement dashboards, where different quantification strategies might yield widely different results.

## Plan and Deliverables
We will tackle the issue along 4 dimensions:
1. Naming: what to call each concept around MEV.
2. Dynamics: how the different "parts" of MEV interact with each other.
3. Sources: what are the various (known) sources of MEV.
4. Ethics: what is good and what is bad MEV.

We aim at delivering a blogpost tackling these 4 areas, acknowledging that this consists in just one among many valid approaches. In the case of MEV sources, in particular, there's always going to be room for further unforseen MEV extraction strategies.


## References
- https://arxiv.org/abs/1904.05234
- https://arxiv.org/abs/2101.05511
- https://arxiv.org/abs/2102.03347
