---
id: <leave blank -- will be assigned by reviewers>
title: Consensus Stability Implications of Transaction Fee Structures and Sequencers
team: Waylon Jepsen, (Add your name here) joint effort from Colorado State University and The University of Tennessee, Dr. Amani Alterweh will lead the study.
created: 2022-02-21
---

# Consensus Stability Implications of Transaction Fee Structures and Sequencers
  
We will study the implications of different fee structures and transaction sequencer mechanisms. Because transaction ordering and fee mechanisms play a critical role in different MEV strategies, it is imperative to classify and examine the impacts of these mechanisms. We will identify the cost of censorship, dominant searcher strategies, and look for consensus stability implications similar to deep reorgs in other protocols. We will study avalanche, Solana, Algorand, Cosmos, Starknet, and Polygon. We will identify trade-offs from different sequencers mechanisms and fee structures. We will publish a paper with our results. 

## Background and Problem Statement
  
The negative implications of deep reorg attacks were articulated clearly in [Flash Boys 2.0](https://arxiv.org/abs/1904.05234) paper. We aim to examine similar concerns in a variety of other protocols. 

## Plan and Deliverables
  
For each of the examined protocols, we will
- Derive closed-form equations for the cost of censorship
- Attempt to identify dominant MEV strategies
- Identify any consensus stability implications
  
We will then
  
- Evaluate the tradeoffs of different fee and sequencer mechanisms. 
- We will produce and submit a paper for peer-reviewed publication outlining our findings in detail.

## References
- [Flash Boys 2.0](https://arxiv.org/abs/1904.05234)
- [Early Exploration in Solana](https://utonium.medium.com/mev-in-solana-an-early-exploration-4d7421b1f49b)
- [Algorand White paper](https://arxiv.org/abs/1607.01341)
- [Solana White paper](https://solana.com/solana-whitepaper.pdf)
- [Avalanch White paper](https://assets.website-files.com/5d80307810123f5ffbb34d6e/6009805681b416f34dcae012_Avalanche%20Consensus%20Whitepaper.pdf)
- [Polygon light paper](https://polygon.technology/lightpaper-polygon.pdf)
