---
id: 37
title: Automated mechanism design using generative AI 
team: Gil Litvin (Technion), Nadav Rubinstein (Technion), Shlomi Gibly (BGU) Xinyuan Sun (Flashbots)
created: 2023-08-27
status: active
---

# Automated Mechanism Design Using Generative AI 

# Intro

We aim to use AI to eliminate suboptimal outcomes when trading through AMMs and DEXs by generating personalized smart contracts that enable traders to coordinate and trade with each other directly. Our goal is to utilize a dynamic AI algorithm that effectively locates relevant buyers and sellers, and recommends the optimal transactions.  We achieve this by analyzing on-chain blocks and modeling user behavior. 

## Background and Problem Statement

The use of a simple Automated Market Maker (AMM) protocol like uniswap has gained popularity for this purpose. However, there are certain limitations that users encounter, leading to suboptimal outcomes. One such limitation is the inability of users to coordinate with each other directly on the platform. This lack of coordination hampers the effectiveness and efficiency of trading activities. To address this issue, researchers and developers are continuously exploring innovative solutions to enhance the user experience and optimize trading outcomes.

For DEX that are based on AMM mechanisms, traders have to pay the fee to market makers. The anticipated revenue derived from the trades, aimed at selling your items to maximize your financial gain, is crucial to determine the most profitable outcome.Price slippage is an inevitable result of how transactions work. Excessively high slippage over a long period of time not only results in suboptimal outcomes for traders, but also may result in false fluctuations in price and inflate trading volume, making it an overestimation of the actual market demand.

The approach can be used to find close approximations to optimal designs from auction theory where they are known, to aid with the discovery of new optimal designs, and to scale up computational approaches to optimal, DSIC auction design.

## Plan and Deliverables

The proposed experiment aims to investigate the efficacy of dynamic algorithms for understanding and optimizing trading mechanisms. Specifically automated mechanism design. 

This research proposes to explore the possibilities of utilizing AI as a means to learn and eliminate inefficiencies and maximize trading outcomes. Based on previous data, we will use AI models to generate mechanisms that predict user intents to connect them p2p, in batch or in ring trading method. 

The study focuses on users' intentions, expressed as numerical values assessing various items. The results produce two number sets: one showing who receives an item; the other demonstrating the division of payment responsibilities.
 
the intents of users will be randomly generated and the AI's performance in optimizing the mechanism will be assessed. The primary metric for evaluation will be users' welfare.

The base model of the system is a transformer using pytorch.The system finds the optimal smart contract to satisfy the trading needs of predicted traders' intents. 
The smart contract would facilitate trade and will consist of the following parameters

Sell Token: the address of the token that is sold
Buy Token: the address of the token that is bought
Third token(only in ring trade): the address of the token that is exchanged
Sell Amount: the amount of sellToken that is sold in wei
Buy Amount: the amount of buyToken that is bought in wei
Receivers: the address that will receive the proceedings of the trade
Seller address: the address that will send the proceedings of the trade


## References

- [Optimal Auctions Through
Deep Learning](https://parkes.seas.harvard.edu/files/parkes/files/dutting_cacm21.pdf) by  Paul Dütting. 
