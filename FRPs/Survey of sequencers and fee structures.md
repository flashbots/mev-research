---
id: <leave blank -- will be assigned by reviewers>
title: Survey of Sequencers and Fee Structures
team: Waylon Jepsen, William Scarbro, and Michael Boyle, Dr. Amani Alterweh will lead the study.
created: 2022-02-21
---

# Consensus Stability Implications of Transaction Fee Structures and Sequencers
  
We will study the implications of different fee structures and transaction sequencer mechanisms. Because transaction ordering and fee mechanisms play a critical role in different MEV strategies, it is imperative to classify and examine the impacts of these mechanisms. We will identify the cost of censorship and dominant searcher strategies to look for consensus stability implications similar to deep reorgs in other protocols. We will study Avalanche, Solana, and Polygon, identify trade-offs from different sequencer mechanisms and fee structures, and publish our results. This work lays the foundation for future peer-reviewed papers in this domain.
We will extend the protocol survey to include Cosmos, Starknet, Fantom, and Celo if the study goes well. We are open to suggestions as well.

## Background and Problem Statement
  
The negative implications of deep reorg attacks were articulated clearly in [Flash Boys 2.0](https://arxiv.org/abs/1904.05234) paper. We aim to examine similar concerns in a variety of other protocols. 

## Plan and Deliverables
  
- We plan to begin setting up network nodes when relevant and within the constraints of our resources to assist with this study and future work. 
  
For each of the examined protocols, we will
  
- Identify Fee Structures and Transaction Sequencers
- Derive closed-form equations for the cost of censorship from fee structures
- Attempt to identify dominant MEV strategies used the in the wild by examing public mempool and transaction history
- Identify any consensus stability implications from dominant MEV strategies and Transaction Sequencers

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
- [An Empirical Study of Frontrunning on the Ethereum Blockchain](https://arxiv.org/abs/2102.03347)
