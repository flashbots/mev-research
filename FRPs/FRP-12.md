---
id: 12
title: MEV after EIP-1559
team: @fiiiu @kristofgazso
created: 2021-06-06
status: in progress
---

# MEV after EIP-1559


## Background and Problem Statement
EIP-1559 is hotly debated upcoming EIP that is being introduced in the London Hardfork. It will significantly alter Ethereum's fee mechanism, crucially resulting in most of the transaction fee being burned and eliminating 0 gas price transactions. We propose to examine the effects of EIP-1559 on MEV extraction and, by extension, the Flashbots project.

Some limitations to this project include the uncertainty underlying the community's reaction once EIP-1559 is in production as well as the relatively close deadline to make meaningful recommendations to the Flashbots project on their proposed adaptations to the EIP.

## Plan and Deliverables
The proposed deliverable is a blogpost that covers
- the changes in risk of deviations from the protocol due to dangerous MEV
- the changes to the UX of Flashbots, especially concerning the lack of 0 gas price transactions
- the redundancy of the EIP's miner tip due to Flashbots' priority queue
- the reflection of the power that Flashbots (as an institution) acquired from the implementation of the EIP.

## References
Reference current relevant literature or past work pertaining to the research question(s) at stake.
* [Transaction Fee Mechanism Design for the Ethereum Blockchain: An Economic Analysis of EIP-1559](https://timroughgarden.org/papers/eip1559.pdf)
