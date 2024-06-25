---
id: 
title: MEV Optimal Bidding and Fair Distribution via Shapley Value
team: Dr. Sujit Gujar, Yash Chaurasia, Rasheed, Parth Desai
created: 2024-06-25
---

#  MEV Optimal Bidding and Fair Distribution via Shapley Value

MEV (Maximal Extractable Value) represents a significant pool of potential profits within the blockchain ecosystem. We aim to critically evaluate whether the current auction design is equitable for all participants. We hypothesize that the existing system may be unfair to vertically integrated builder-searchers, which we refer to as *builders*. To investigate this, we will delve into the strategic bidding approaches employed by builders. Additionally, we'll explore alternative, potentially fairer, and more innovative solutions for distributing MEV amongst all parties engaged in these auctions.

## Background and Problem Statement
Builders compete in two sequential interconnected auctions; they compete for transactions in *Order Flow Auctions* (OFAs) and for a block in *block auctions* (BA) with proposers [9]. Naturally, competing in two auctions reduces the integrated builders' utility as they end up sharing their profits with OFA providers and proposers. If a builder wins OFA(s) but loses BA, it incurs negative utility. To avoid losing in BA, such builders bid more aggressively in BA, thus reducing their profit margins. Winning in OFA is equally essential as private order flows provide more MEV opportunities, forcing builders to bid aggressively in OFAs. While proposers and OFA providers play an important role in the ecosystem, they retain most of the MEV extracted by builders [10].

Our preliminary analysis shows that bidding truthfully in both auctions may result in either negative utility to builders or builders only retaining a small fraction of the MEV extracted.
To this end, we aim to propose optimal bidding strategies for builders for the current auction mechanism. 

We also look for alternative mechanisms to the current auctions to distribute the extracted MEV among all the stakeholders - proposers, builders, and OFA providers. One such mechanism is using the Shapley Value to distribute MEV fairly among the stakeholders. Shapley Value is the only mechanism that satisfies the four properties of Efficiency, Symmetry, Linearity, and Null player. Computing Shapley Value is computationally intensive (exponential time algorithms). However, in some cases, one can reduce the computation to polynomial time.



## Plan and Deliverables
1. We plan to model the auction mechanism as a game with coupled auctions. We aim to find the optimal bidding strategies as equilibrium in both auctions, modeled as a two-stage game using the Markov Decision Process (MDP).

2. We plan to propose a coalition game over the current mechanism with the proposer, builder, and OFA provider and define a characteristic function. We strongly believe the nature of the MEV game is such that we can design an algorithm to compute the Shapley Value of nodes efficiently.

Our team has expertise in publishing in Game Theory, Multi-Agents, Blockchain, and AI forums (conferences such as AAMAS, IJCAI, AAAI, etc). Our team has computed equilibrium bidding strategies across multiple applications, e.g., Civic Crowdfunding [1-4], auctions [5,6], etc. We also have expertise in Blockchain [7,8]. We recently wrote a review survey on MEV Ecosystem Evolution [9].


### Deliverables:
- Multiple research publications.
- Blogs explaining the proposed mechanism and analyses performed.
- Open source the experiment data and code on GitHub.
- Support the integration of the proposed mechanism with existing frameworks (if any).


## References
1. [Civic Crowdfunding for Agents with Negative Valuations and Agents with Asymmetric Beliefs](https://arxiv.org/abs/1905.11324)
2. [Combinatorial Civic Crowdfunding with Budgeted Agents: Welfare Optimality at Equilibrium and Optimal Deviation](https://arxiv.org/abs/2211.13941)
3. [REFORM: Reputation Based Fair and Temporal Reward Framework for Crowdsourcing](https://arxiv.org/abs/2112.10659)
4. [Learning Equilibrium Contributions in Multi-project Civic Crowdfunding](https://dl.acm.org/doi/10.1145/3486622.3493918)
5. [Multi-unit Double auctions: Equilibrium Analysis and Bidding Strategy using DDPG in Smart-grids](https://arxiv.org/abs/2201.10127)
6. [Bidding in Smart Grid PDAs: Theory, Analysis and Strategy](https://www.arxiv.org/abs/1911.08260)
7. [PUPoW: A framework for designing blockchains with practically-useful-proof-of-work \& vanitycoin](https://arxiv.org/abs/2210.06738)
8. [FASTEN: Fair and Secure Distributed Voting Using Smart Contracts](https://arxiv.org/abs/2102.10594)
9. [MEV Ecosystem Evolution From Ethereum 1.0](https://arxiv.org/abs/2406.13585)
10. [Contingent Fees in Order Flow Auctions](https://arxiv.org/abs/2304.04981)
