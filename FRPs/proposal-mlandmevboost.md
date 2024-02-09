---
id: 
title: Machine Learning and MEV-boost Auctions
team: <team that will carry out the proposal, with a designated lead>
created: <date created on, in yyyy-mm-dd format>
---

# What Can Machine Learning Tell Us About MEV-boost Auctions?

We argue that bidding strategies during MEV-boost Auctions can be inferred using reverse engineering. 
We build SVM (support vector machine)[1] models using the public available data provided by PBS relays. To make the picture more comprehensive, we experiment with data from sources other than the relays (market conditions, NFT events, etc.).

Our plan is to identify the most relevant variables during an MEV-boost auction and infer bid values from different builders. We classify builders into categories just as in [2], but we intend to complement [2] with real-life data and investigate how realistic is the classification of [2] (naive, adaptive, last-minute and bluff). Finally we build a tool that can predict the evolution of an MEV-boost auction using on-the-fly data from PBS relays. 

Limitations: without actually carrying out this plan, we are unable to tell the degree of accuracy of our method.

## Background and Problem Statement

Relays in the context of PBS (proposer builder separation) are responsible for the orchestration of MEV-boost auctions. Block builders battle for inclusion and they calculate their bids based on how much perceived MEV value is in the block under consideration. Bids can be queried from public relays, and the time evolution of the bids from different builders is public information. Our preliminary measurement results showed that only a handful of builders vie for inclusion on the public relays (not more than 40 on Aestus for example). Clearly, no one can determine their perceived MEV, as profitable block building strategies are kept secret. But still, our conjecture is that bidding strategies can be predicted using machine learning. Also, no rational bot bids more than the maximum expected MEV of the given block, which implies that bidding strategies must be in correlation with the block building strategies. 

Notwithstanding the fact that, in 2024, over 90% of Ethereum blocks are constructed with MEV-Boost, there is a notable scarcity of literature discussing bidding strategies and auction design. This work seeks to provide a comprehensive explanation of these concepts, catering to both researchers and practitioners in the blockchain field. Our objective is to demystify the inner workings of MEV-Boost auctions, making them more understandable for a wider audience.


## Plan and Deliverables


- Data collection from public PBS relays (Aestus, Agnostic Gnosis, Eden Network, Flashbots, Manifold, etc) [2 month]

- Determining important features [1 week]

- SVM model building [1 month]

- Model evaluation, accuracy assessment, model improvement, fine-tuning parameters [3 weeks]

- Proposal for improved accuracy [1 week]

- Research paper [2 weeks]

- Open-source code on GitHub with documentation [1 week]


## References

[1] Tang, L., & Yan, X. (2009). Support vector machine with adaptive parameters in financial time series forecasting. IEEE Transactions on Neural Networks, 20(5), 771-784.
[2] Wu, F., Thiery, T., Leonardos, S., & Ventre, C. (2023). Strategic Bidding Wars in On-chain Auctions. arXiv preprint arXiv:2312.14510 [cs.GT].
