---
id: 36
title: Solving the User-Searcher Trust Issues with MPC (Stage 1)
team: Ariel Futoransky and Sergio Demian Lerner (Fairgate Labs)
created: 2023-07-18
status: stagnant
---

# Solving the User-Searcher Trust Issues with MPC (Stage 1)



## Background and Problem Statement
In a recent [article](https://writings.flashbots.net/backrunning-private-txs-MPC), the Flashbots team describes the results of a research on how to apply MPC to solve a trust problem between the user and a searcher of MEV, by enabling the user to be compensated for a back-running arbitration transaction found by the searcher. The research analyzes a restricted (simplified) model. While the results are theoretically useful, the performance obtained prevents this technique from being of practical use today.

We identify several suboptimal choices related to the cryptographic protocol (provided by the MP-SPDZ lib) and we intend to show that using the adequate protocol and pragmatic tradeoffs, together with specific innovations, we can achieve practical feasibility.
Due to the large number of optimizations, trade-offs and design decisions involved, we split our research into 2 stages. In the first stage we aim to answer the following core questions:

1. Is there a setup where MPC in the semi-honest setting can satisfy the problem security and privacy requirements ?
2. What known or new optimizations can be applied to reduce circuit size or improve overall performance?
3. What trade-offs can be used to achieve practical feasibility, considering the relationship between bandwidth, delay, and processing costs ?


Our  thesis is that the Yao protocol in the semi-honest setting together with an efficient innovative memory-consistency protocol can yield a practical viable solution to the restricted user-searcher model.
During our research, we will describe the theory behind each improvement and implement a series of tests using a PoC MPC framework. Each test aims to address one of the research questions. If the test results match our expectations, this will be a strong indicator that a custom MPC implementation can be the starting point to address more complex trust issues within the Flashbots ecosystem as pairwise interactions, considering game-theoretic elements such as cooperation, double-negotiation and DoS threats.

The long term vision is that MPC can be the backbone of Flashbots ecosystem, helping the ecosystem become maximally decentralized.

## Plan and Deliverables

Respond to the fundamental questions asked. Produce supporting test code and benchmarks. 

Estimated time: 3 months.

## References

- [Backrunning Private Transactions Using Multi-Party Computation](https://writings.flashbots.net/backrunning-private-txs-MPC)
- [Concretely efficient secure multi-party computation protocols: survey and more](https://sands.edpsciences.org/articles/sands/full_html/2022/01/sands20210001/sands20210001.html)
