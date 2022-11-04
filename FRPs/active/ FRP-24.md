---
id: 24
title: On the quantification of MEV on L2s
team: @IlluvatarEru, @0xpanoramix
created: 2022-08-10
status: active
---

# On the quantification of MEV on L2s

&ensp; While most of the research on MEV has been done on Ethereum, we do not know how much MEV is actually happening on other chains. The latest research on the subject ([[1]](######1.)) dates from a year ago and encountered several obstacles - as a matter of fact, quantifying MEV on L2s is no trivial task.
We want to overcome the obstacles that were encountered in [[1]](######1.) by porting `mev-inspect-py` on L2s and analyze the extracted MEV (quantify and classify it) and measure its impact in terms of PGAs.

&ensp;Quantifying the extracted and extractable MEV on L2s as well as the impact in terms of PGAs can give MEV searchers some insights on potential opportunities on these chains and give the public an idea of how detrimental (or not) is the impact of MEV on L2s and whether it needs to be addressed or not.

## Background and Problem Statement

&ensp; With Flashbot's `mev-inspect-py` it is easy to see how much MEV is happening on Ethereum, but what about Polygon? Optimism? Arbitrum? No one knows. We want to broaden the public knowledge of what is happening on L2s by quantifying (how much historical profit per block?) and classifying (Is it only arbitrage? Liquidation? Something else?) the MEV that takes place on L2s.
We also aim at measuring how much has been spent on PGAs, to measure the impact of MEV on L2 gas prices.

## Plan and Deliverables
Describe the planned approach to the problem, including potential time allocations and partitioning into phases. List the artifacts or intended deliverables of the proposal.
We plan on following the below steps:
1. Porting `mev-inspect-py` to work for L2s (priority given to Polygon, Optimism and Arbitrum)
2. Quantifying historical mev profit by block
3. Quantifying extracted mev by domain (arbitrage, liquidation, the rest)
4. Quantifying how much has been spent on PGAs _(Optional?)_

We expect that most of the time is going to be spent on porting `mev-inspect-py` to work for L2s, due to the big differences with Ethereum in terms of tx tracing, tx frequency etc.

The major challenge that we see is finding a way to replay transactions on Polygon due the high frequency of transactions.

### Deliverables:
1. Forks of `mev-inspect-py` that work for the aforementioned L2s
2. A research paper explaining the methodology and results
3. A presentation to the Flashbots team

## References

###### 1. [MEV on L2](https://timroughgarden.github.io/fob21/reports/r11.pdf) by FlashBabies (Huy Ha, Vasiliki Vlachou, Quintus Kilbourn, and Cesare De Michellis).
###### 2. [Introducing MEV support for Polygon](https://blog.marlin.org/introducing-mev-support-for-polygon) by Roshan Raghupathy.
