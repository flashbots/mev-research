---
id: 
title: Solving the User-Searcher Trust Issues with MPC (Stage 2)
team: Ariel Futoransky and Sergio Demian Lerner (Fairgate Labs)
created: 2023-07-18
---

# Solving the User-Searcher Trust Issues with MPC (Stage 2)



## Background and Problem Statement
This is the second stage of a research on using custom optimized implementation of the Yao's protocol to address the trust issues in the User-Searcher Trust interaction. In the first stage, we focused on choosing the right MPC layer. In this second stage, we focus on the modeling of the problem such that the circuit can be shortened, compressed, or computed more efficiently. We center our research on efficiently handling a large RAM. We plan to analyze different solutions, including a new RAM consistency protocol based on public address/private data. We aim to answer the following questions:

1. Is it possible to express the back-running predicates as a variant of MPC RAM program instead of a standalone circuit?
2. What is the impact of the choice of the RAM memory consistency protocol on the performance ?
3. Which memory consistency schemes can be used securely to improve performance without incurring the ORAM cost? 


Our thesis is that the Flashbots’ User-Searcher use case requires access to large RAM in any realistic scenario, and any protocol lacking an efficient RAM access and memory consistency protocol will fail to meet expectations. 
During our research, we will compare a PoC solution to the problem using registers and using RAM memory secured by a memory consistency sub-protocol. We will provide the results and source code associated with each test. 

While we address the questions, we aim to test a novel and promising memory consistency protocol and analyze how it performs in practice. If our results are encouraging, this would yield a strong indicator that Flashbot’s MPC use-cases have practical solutions. A follow-up work would be required to publish formal soundness and privacy proofs for this new memory consistency sub-protocol. 

## Plan and Deliverables

Respond to the questions asked. Produce supporting test code and benchmarks. 

Estimated time: 3 months.

## References

- [Backrunning Private Transactions Using Multi-Party Computation](https://writings.flashbots.net/backrunning-private-txs-MPC)
- [Constant-Round Maliciously Secure Two-Party Computation in the RAM Model](https://link.springer.com/article/10.1007/s00145-019-09321-3)
