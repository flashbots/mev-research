---
id: <leave blank -- will be assigned by reviewers>
title: MEV on Rollups
team: @saharAP @emmanuel-awosika 
created: 2022-09-18
---

# MEV on Rollups
## Background and Problem Statement

MEV in L2 protocols is one of the research areas offered by Flashbots. Given the rise of different L2 solutions and the migration of many Defi projects to these networks, this topic will be of interest to many researchers. As a result, MEV opportunities that are mostly related to Defi projects could also move to these L2 protocols.

L2 solutions have come to the world based on the idea of having scalable networks with minimum gas cost. Previous solutions had data availability issues. After that, other protocols were proposed that solved the data availability problem but had some trust assumptions which undermined the validity of the data placed on the mainnet. The ultimate L2 proposed solutions so far are rollups which are trustless bridges in which they validate every bunch of transactions before publishing on the L1 network. Rollups are divided into two main categories based on their validation method: optimistic rollups and zero-knowledge base rollups. L2 solutions have different roles in their systems: sequencer, executor, aggregator, and challenger [1]. Also, transaction ordering and execution can be separated in rollup protocols but in practice, they can be gathered in a single node; however, the role of the sequencers themselves in ordering and censoring transactions can cause potential MEVs [2]. Moreover, I believe that a single sequencer may cause some problems. Not only it is logically under the control of a single authority and we should trust it not to frontrun, but also technically it could be a single point of failure (as it has already happened before to Arbitrum). One of the ideas is to have decentralized permissioned sequencer nodes, which we will discuss and investigate its challenges during this research. It is worth mentioning that Arbitrum stated that it intends to move toward decentralized sequencing. It means that eventually the task of transaction ordering will be given to a distributed committee of sequencers which comes to a consensus on ordering [3]. 

Some rollups (e.g., Arbitrum/Optimism) use some form of the first-come-first-serve (FCFS) ordering policy that guarantees transactions (sent to the sequencer's private mempool) are ordered as received, so that reduces MEV significantly. but it may have some consequences. Using the FCFS ordering strategy can increase the number of spam transactions to guarantee their early inclusion in the batch, and hence, it can lead to a waste of block space. On the other hand, in the FCFS approach, any transaction that enters the queue first is processed first. As a result, the network latency would be a critical issue. More specifically, it would not be fair for users with high network latency and far from the sequencer’s node as their transactions will arrive in the queue later than the others. It seems the issues mentioned will still not be resolved using decentralized sequencing with the FCFS ordering policy. Finally, to the best of my knowledge, the FCFS itself cannot prevent censoring transactions as a malicious sequencer can still prevent a transaction to include in a batch. (Arbitrum/Optimism uses some force transaction inclusion mechanisms to bypass the sequencer).

The previous work in this field done in Flashbots is [4]. The focus of this research is on defining potential MEVs over interconnected blockchains, which were mentioned as cross-domain MEVs. Different situations of the topic have been well-defined and parameterized. The paper also has been specialized in extracting MEV through arbitrage, which is the most common way of getting MEV according to [explore.flashbots](https://explore.flashbots.net/). Moreover, the sequencer collusion in different domains is discussed. Here we are trying to investigate MEV challenges specific to rollups which are mostly related to the sequencers, and also trying to ask new questions during this research.

## Plan and Deliverables

The focus of this research is studying MEV over rollups as the most prominent approach among layer-2 solutions. Here are some of the main questions related to the objectives:

-   What are the different transaction ordering strategies in terms of using a set of permissioned sequencer nodes in rollups?
-   Can rollup nodes frontrun transactions received from users and exploit their proximity to sequencers to gain optimal transaction ordering (in terms of using a form of decentralized sequencing)? 
-   What are the second-order effects of implementing fair-ordering protocols (as a solution to reduce MEV)?
-   What are the solutions to prevent sequencers or disincentivize them to censor transactions or to leak transaction contents (from their private mempool)?  

## References

1. [Validating Bridges as a Scaling Solution for Blockchains](https://eprint.iacr.org/2021/1589.pdf)
2. [MEV and Me](https://research.paradigm.xyz/MEV)
3. [The Sequencer and Censorship Resistance](https://developer.arbitrum.io/sequencer)
4. [Unity Is Strength: A Formalization Of Cross-Domain MEV](https://arxiv.org/abs/2112.01472)
