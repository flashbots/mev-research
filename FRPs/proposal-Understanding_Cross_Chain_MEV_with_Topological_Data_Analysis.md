---
id: <leave blank -- will be assigned by reviewers>
title: Understanding Cross-Chain MEV with Topological Data Analysis
team: <team that will carry out the proposal, with a designated lead>
created: <2022-11-19>
---


# Background and problem statement

## Background
Topological data analysis (TDA) is a powerful data analytics technique that uses the underlying topological and geometric structures of data to create non-trivial, meaningful categories. The Mapper algorithm is a TDA tool that transforms data, which lives in a continuous Reeb space, to a simplicial complex, a topological combinatorial graph which lives in a discrete space. TDA started to turn heads when the Mapper algorithm was used to identify a highly treatable cluster of breast cancer patients from a highly dimensional dataset in 2011. 

The Mapper algorithm was applied to analyze MEV volume in the Olympus Ecosystem [^mev_tda] and was able to identify statistically distinct clusters of economic behavior from MEV atomic arbitrage [^ohm_arbitrage] volume on Ethereum and liquidation volume on Arbitrum + Ethereum. Olympus was chosen as a proof of concept protocol because OHM liquidity is entirely on-chain. OHM also contained historical data of liquidations occuring from Rari (ethereum) and vesta (arbitrum) that could be included in the dataset. Initial discussion can be found on the Flashbots forum [here.](https://collective.flashbots.net/t/using-topological-data-analysis-to-identify-distinct-mev-behavior/702)

Already, TDA has delivered novel insights and I believe we are just starting to scratch the surface of possibilities to further understand cross chain MEV volume flows. There is an entire suite of next generation analytical tools from TDA that can be further applied to obtain novel insights of MEV behavior on blockchains. 


## Problem statement
There has been very little research done to date on understanding how well-known MEV bot behaviors such as atomic arbitrage and liquidation bots comingle. There has been even less robust statistical analysis on historical blockchain data to gain further insights into MEV dynamics.  

Further, classifying pattern recognition algorithms to identify new MEV behavior is complex due to the highly interconnected nature of the blockchain. TDA introduces a suite of robust topological techniques that are well suited to obtain further insights into the connectivity of MEV behavior on blockchains


# Plan and deliverables

## Plan

1) Create a more robust MEV address list than the current Flashbots arbitrageur list (I previously identified some critical issues that make the Flashbots list too inaccurate to use) composed of addresses that participate in atomic arbitrage and liquidations. Extend this to Arbitrum.

2) Setup cross-chain subgraph pipeline to obtain historical data for analysis.

3) Use topological data analysis techniques to analyze MEV address activity using the list built from 1. Extend this to Arbitrum.

## Deliverables

- Open source jupyter notebook models, open source data pipeline code
- Academic level research paper
- Presentation at international conferences.

# References

[^mev_tda]: https://github.com/Evan-Kim2028/tda_ohm_analysis/blob/main/Using_Topological_Data_Analysis_to_Identify_MEV_Behavior.pdf

[^ohm_arbitrage]: https://mirror.xyz/evandekim.eth/Mc11J16dVP7Ervk1r2Sx_wkJ7dzb7Ce60Y2EpbRBlHY
