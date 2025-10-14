---
id: 53
title: Free Option Problem of ePBS and Simulating Ethereum's Geographical Decentralization
team: Fei Wu
created: 2025-07-15
status: completed
---

# FRP: Free Option Problem of ePBS and Simulating Ethereum's Geographical Decentralization

The purpose of this FRP is twofold. One is to study the free option problem of ePBS. The other one is to contribute to an ongoing project in collaboration with Flashbots on simulating Ethereum's geographical decentralization.

## Background and Problem Statement
### Free Option Problem of ePBS
EIP-7732 enshrined Proposer-Builder Separation (ePBS) has been scheduled for inclusion in the upcoming Glamsterdam upgrade. However, its dual PTC deadline design [1] and the requirement that builders publish the execution payload introduce a problem: builders have an option to prevent the payload from becoming canonical by withholding the payload/blobs if publishing the block is no longer profitable. It is known as the free option problem [2]. The research question is to understand the extent to which the ePBS free option problem will lead to missed blocks and degrade network liveness.

### Geographical Decentralization Simulation
Currently, Ethereum validators cluster in the EU and US East, where latency advantages persist. Beyond latency, it is important to understand whether protocol designs, such as PBS, can influence validator incentives, and consequently, Ethereum's geographical (de)centralization [3].

## Plan and Deliverables
### Free Option Problem of ePBS
The most valuable use case of the free option is to revert (CEX-)DEX trades once the external market price moves in an unfavorable direction before the builder is about to publish the payload. We plan to model the builder’s decision process in exercising the free option and reverting DEX trades, and to identify the factors contributing to the problem—such as liquidity, price volatility, and block composition. 

Moreover, by leveraging existing data and results in our previous paper on CEX-DEX arbitrages [4], we can empirically estimate the value of the free option and the probability of the builder exercising the free option in historical blocks. This will allow us to quantitatively understand the nature and scale of the problem.


### Geographical Decentralization Simulation
We plan to formulate an agent-based model as the foundation for a simulation framework (consider the MEV-Boost auction simulation framework [5] as an exmaple) that reproduces Ethereum validator behavior under different protocol designs (e.g., PBS vs. local block building). Through this framework, we aim to analyze how different protocol designs affect validator incentives and geographical distribution, thereby improving our understanding of how protocol design influences geographical (de)centralization dynamics.

**Deliverable**: Posts on Flashbots Collective and papers

## References

[1] Anders Elowsson. Dual-deadline PTC vote in ePBS. https://notes.ethereum.org/@anderselowsson/Dual-deadlinePTCvote

[2] Julian Ma, Barnabe Monnot, Francesco D’Amato, Michael Neuder, Potuz, and Terence Tsao. Free option problem. https://efdn.notion.site/Free-option-problem-837cdbf06d4c4870b79a840dd5c45a38

[3] Phil Daian. Decentralized crypto needs you: to be a geographical decentralization maxi. https://collective.flashbots.net/t/decentralized-crypto-needs-you-to-be-a-geographical-decentralization-maxi/1385

[4] Fei Wu, Danning Sui, Thomas Thiery, and Mallesh Pai. Measuring cex-dex extractedvalue and searcher profitability: The darkest of the mev dark forest.https://arxiv.org/abs/2507.13023

[5] Fei Wu and Thomas Thiery. MEV-Boost Auction Simulation Framework. https://github.com/M1kuW1ll/MMASim
## Outputs
The project results in two posts on Flashbots Collective and two papers on arxiv:

**The Free Option Problem in ePBS,** https://collective.flashbots.net/t/the-free-option-problem-in-epbs/5115

**The Free Option Problem in ePBS, Part II,** https://collective.flashbots.net/t/the-free-option-problem-in-epbs-part-ii/5145

**The Free Option Problem of ePBS,** https://arxiv.org/abs/2509.24849

**Designing Ethereum's Geographical (De)Centralization Beyond the Atlantic,** https://arxiv.org/abs/2509.21475
