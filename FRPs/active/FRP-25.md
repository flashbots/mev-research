---
id: 25
title: Quantifying Fairness Granularity For FCFS Chains
team: @saharAP @emmanuel-awosika 
created: 2022-09-18
status: active
---

# Quantifying Fairness Granularity For First-Come-First-Serve (FCFS) Chains
## Background and Problem Statement

L2 solutions have different roles in their systems: sequencer, executor, aggregator, and challenger [1]. Also, transaction ordering and execution can be separated in rollup protocols but in practice, they can be gathered in a single node; however, the role of the sequencers themselves in ordering and censoring transactions can cause potential MEVs [2]. Moreover, I believe that a single sequencer may cause some problems. Not only it is logically under the control of a single authority and we should trust it not to frontrun, but also technically it could be a single point of failure (as it has already happened before to Arbitrum). One of the ideas is to have decentralized permissioned sequencer nodes, which we will discuss and investigate its challenges during this research. It is worth mentioning that Arbitrum stated that it intends to move toward decentralized sequencing. It means that eventually the task of transaction ordering will be given to a distributed committee of sequencers which comes to a consensus on ordering [3]. 

Some rollups (e.g., Arbitrum/Optimism) use some form of the first-come-first-serve (FCFS) ordering policy that guarantees transactions (sent to the sequencer's private mempool) are ordered as received, so that reduces MEV significantly. but it may have some consequences. Using the FCFS ordering strategy can increase the number of spam transactions to guarantee their early inclusion in the batch, and hence, it can lead to a waste of block space. On the other hand, in the FCFS approach, any transaction that enters the queue first is processed first. As a result, the network latency would be a critical issue. More specifically, it would not be fair for users with high network latency and far from the sequencer’s node as their transactions will arrive in the queue later than the others. It seems the issues mentioned will still not be resolved using decentralized sequencing with the FCFS ordering policy. Finally, to the best of my knowledge, the FCFS itself cannot prevent censoring transactions as a malicious sequencer can still prevent a transaction to include in a batch. (Arbitrum/Optimism uses some force transaction inclusion mechanisms to bypass the sequencer).

 Our work is focus on FCFS ordering relies on a “fairness granularity”, i.e., the interval during which all transactions received are assumed to occur at the same time. As seen in the Themis paper [4], receive-order fairness (i.e., executing transactions strictly according to timestamps) requires using the finest possible fairness granularity (i.e., granularity is zero or close to zero). 

However, we know a low fairness granularity has negative second-order effects, such as encouraging MEV searchers to collude and colocate with sequencers/validators to achieve optimal ordering (e.g., to execute frontrunning). We also know that the fairness granularity must not be arbitrarily large, or else the possibility of an adversary frontrunning a transaction increases. 

This research project aims to quantify the “burst period” on FCFS chains as the basis of developing a better fairness granularity for fair-ordering that achieves “batch-order fairness” (i.e., transactions in the same interval receive similar timestamps). We consider the burst period as the average time between the occurrences of two trades. 

## Plan and Deliverables

The plan will focus on fair ordering approaches in rollup chains to reduce MEV. We try to investigate and solve some challenges on FCFS policy as one of the current promising ordering strategies. Here are the main objectives:

1. Quantify the value of the “burst period” by evaluating the average time between the occurrences of    two trades on AMM and order book DEXs on an FCFS chain (Arbitrum). 

2. As a second indicator for the granularity interval, the “average time period” of the maximum MEV load in each block can be quantified (using the same data from #1). 

3. Obtain the optimal fairness granularity for fair-ordering that incorporates elements of a frequent batch auction (i.e., FBA-FCFS). We aim to achieve this objective by applying the calculated “burst period” and the "average time period" to develop a reasonable interval for batch auctions in FCFS chains. 

Project Deliverables: 

- A formal research paper discussing results and evaluations

- Blog post targeted at non-technical audiences 

## References

1. [Validating Bridges as a Scaling Solution for Blockchains](https://eprint.iacr.org/2021/1589.pdf)
2. [MEV and Me](https://research.paradigm.xyz/MEV)
3. [The Sequencer and Censorship Resistance](https://developer.arbitrum.io/sequencer)
4. [Themis](https://eprint.iacr.org/2021/1465.pdf)
