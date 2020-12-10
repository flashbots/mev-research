---
id: 2
title: MEV and Liquidations
team: Kaihua Qin, Liyi Zhou, Arthur Gervais
created: 2020-12-10
paper: 1
---

# Summary
With over 6B USD total value locked for the top 3 lending protocols alone, this use case has grown into a substantial DeFi market. Lending entails the risks of a diminishing collateral value, which may render debt unhealthy. Unhealthy debt is typically resolved through liquidations, a process of selling collateral at a discount to liquidators.

One dominant liquidation design is the fixed spread liquidation mechanism, used by Aave, Compound and dYdX. Interestingly, the fraction of the collateral that a liquidator can purchase at a discount amounts to 50% for Aave and Compound, and even 100% for dYdX (commonly referred to as close factor). It therefore appears that the fixed spread liquidation mechanisms are benefitting the liquidators more than the borrowers.

Drawing the link to MEV, each liquidation event may qualify as Miner Extractable Value (MEV). For example, in a recent price oracle manipulation attack, a liquidator performed an oracle price post and liquidated millions of USD within one transaction, yielding a profit of nearly 4M USD. 

The goal of this FRP is to offer a systematization of existing liquidation mechanisms and consistent measurements of the past and current DeFi liquidation state. We aim to investigate alternative liquidation designs in an effort to mitigate MEV from liquidation events.

## Background and Problem Statement

The goal of this FRP is to study the past and current status of blockchain liquidation. Specifically, we would like to answer the following questions:
- What is the monthly accumulated liquidation profit for Aave, Compound, dYdX, MakerDAO?
- What gas price distributions are being paid for the liquidation events?
- What are the different liquidation methods, and how do they differ with respect to MEV? Which liquidation mechanism avoids MEV?
- How sensitive are current debts to liquidation (by how much would an adversary need to manipulate a price oracle)? An MEV miner could try to manipulate an oracle to extract this MEV.
- How can we design a possible liquidation mechanism that mitigates MEV?

## Plan and Deliverables

- We plan to write a comprehensive paper about liquidations in DeFi.
- Our report is envisioned to contain multiple figures/quantitative results regarding: 
  - Monthly liquidation profits for MakerDAO/Aave/Compound/dYdX.
  - Understand the gas prices of liquidation events. Is there a way to avoid gas fee bidding contests in liquidations in an effort to preserve valuable block-space?
  - Quantify the liquidation sensitivity (how much collateral is liquidated given a % price decline of the collateral) for MakerDAO/Aave/Compound/dYdX and most of the assets on these platforms.
  - How many liquidation events are profitable to the liquidator?
  - How many liquidations make use of flash loans?
 
- We plan to systematize the different liquidation mechanisms in an effort to understand their strengths and weaknesses.
- We would love to integrate with the inspectors of the flashbots dashboard to crawl our data. Yet, we haven’t been able to look into further technical details of how they work and what the current architecture is. If too complicated we can also proceed with our current geth-based infrastructure.
- We plan to design a new liquidation mechanism that would prevent or mitigate MEV. There may be an inherent tension between a minimal MEV that must remain for the system to sustain, and we would like to better understand this tension.

## References
[Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges](https://arxiv.org/pdf/1904.05234.pdf)

[Liquidations: DeFi on a Knife-edge](https://arxiv.org/pdf/2009.13235.pdf)

[On the Security and Performance of Proof of Work Blockchains](https://eprint.iacr.org/2016/555.pdf)

[Optimal Bidding Strategy for Maker Auctions](https://arxiv.org/pdf/2009.07086.pdf)

[https://zengo.com/defi-research-understanding-compound-liquidators/](https://zengo.com/defi-research-understanding-compound-liquidators/)
