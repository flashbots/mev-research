---
id: <leave blank -- will be assigned by reviewers>
title: MEV on Rollups
team: @saharAP 
created: 2022-09-18
---

# MEV on Rollups
## Background and Problem Statement

MEV in L2 protocols is one of the research areas offered by Flashbots. Given the rise of different L2 solutions and the migration of many Defi projects to these networks, this topic will be of interest to many researchers. As a result, MEV opportunities that are mostly related to Defi projects could also move to these L2 protocols.

L2 solutions have come to the world based on the idea of having scalable networks with minimum gas cost. Previous solutions had data availability issues. After that, other protocols were proposed that solved the data availability problem but had some trust assumptions which undermined the validity of the data placed on the mainnet. The ultimate L2 proposed solutions so far are rollups which are trustless bridges in which they validate every bunch of transactions before publishing on the L1 network. Rollups are divided into two main categories based on their validation method: optimistic rollups and zero-knowledge base rollups. L2 solutions have different roles in their systems: sequencer, executor, aggregator, and challenger [1]. Also, transaction ordering and execution can be separated in rollup protocols but in practice, they can be gathered in a single node; however, the role of the sequencers themselves in ordering and censoring transactions can cause potential MEVs [2].

The previous work in this field is [3]. The focus of this research is on defining potential MEVs over interconnected blockchains, which were mentioned as cross-domain MEVs. Different situations of the topic have been well defined and parameterized. The paper also has been specialized in extracting MEV through arbitrage, which is the most common way of getting MEV according to [explore.flashbots](https://explore.flashbots.net/). Moreover, the sequencer collusion in different domains is discussed. At the end of the paper, the authors asked some open questions that we are trying to investigate, and also trying to ask new questions during this research.

## Plan and Deliverables

The focus of this research is studying MEV over rollups as the most prominent approach among layer-2 solutions. The first step is to recognize potential MEVs on rollup protocols and figure out different approaches that current protocols use, and do the implementation of them if needed. The second step would be investigating potential MEVs on cross-rollup communications. Here are some of the main questions related to the objectives:

-	What are the potential MEVs that could happen on rollups?
-	What have the existing rollup protocols done to control transaction ordering and to have a censorship-resistant protocol?
-	What’s the role of transaction finality in increasing or reducing MEV?
-	What are the other types of MEV other than arbitrage that could happen on the L2 networks?
-	What are the MEV potentials on cross-rollup and L1-rollup communications?

## References

1. [Validating Bridges as a Scaling Solution for Blockchains](https://eprint.iacr.org/2021/1589.pdf)
2. [MEV and Me](https://research.paradigm.xyz/MEV)
3. [Unity Is Strength: A Formalization Of Cross-Domain MEV](https://arxiv.org/abs/2112.01472)
