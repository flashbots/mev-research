---
id: 21
title: MEV in fixed gas price blockchains
team:  @facuzeta
created: 2022-08-11
status: completed
---

# Background and Problem Statement

As we know, MEV has been extensively studied [1], from mathematical models to data analysis applications. In most scientific papers, researchers have worked with the Ethereum blockchain almost exclusively, so extending results to other blockchains might not be trivial. Understandably, one of the most particular aspects that makes it so complex is Gas bidding.

In Ethereum, the miners pick up transactions from the mempool and propose a block with a subset of transactions in an arbitrary order. However, this arbitrary order is not random; many miners use gas to sort transactions and create new blocks since this strategy maximizes their reward. But this is not the case for all blockchains. Blockchains based on Tendermint don't take dynamic gas prices into account to prioritize transactions. They use a fixed gas price and process transactions in the same order in which the validators receive them. This difference could heavily impact the role and behavior of MEV searchers. In Blockchains with fixed gas prices, the only resource that searchers have is to recognize an MEV opportunity before other actors and respond quickly enough. This contrast could have enormous repercussions on the opportunities that MEV searchers choose to pursue. For example: What strategy do non-privileged actors use to front-run a transaction if they could not offer a higher gas price to allocate their transaction earlier in the block? 

We believe the blockchains that don't use gas to prioritize transactions present MEV opportunities with their own different dynamics. As we have previously mentioned, even though MEV has been extensively studied  (market designs and their implications [2], MEV in other Blockchains [3], among others), to our knowledge, there is not a full understanding of MEV in Blockchains with fixed gas price mechanisms. Therefore, we propose the following general objective of this FRP: To study the MEV opportunities in a blockchain using a fixed gas price. To contribute to this general object, we propose to study this in Terra blockchains.

## Plan and Deliverables

We propose to:

- Setup a framework to store blocks and transactions to perform the analysis
- Create mechanisms to identify exploited MEV opportunities
- Create an MEV explorer for Terra (similar to Flashbots explore dashboard)
- Analyze the data and publish the results in academic papers and/or blogs post


## References

[1] Daian, Philip, et al. "Flash boys 2.0: Frontrunning in decentralized exchanges, miner extractable value, and consensus instability." 2020 IEEE Symposium on Security and Privacy (SP). IEEE, 2020.

[2] Why your blockchain needs an MEV solution - Hasu (Flashbots)

[3] A brief Survey of MEV on Ethereum, BSC, Avalanche and Polygon in 2021 - Alex Obadia (Flashbots) 

[4] https://explore.flashbots.net/ 

## Output
Paper: https://arxiv.org/abs/2303.04242
Blog Post: https://collective.flashbots.net/t/frp-21-mev-in-fixed-gas-price-blockchains/1400
