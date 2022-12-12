---
id: 26
title: Credible Commitments via Open Games 
team: 20squares
created: 2022-12-07
status: active
---

# Credible Commitments via Open Games

We aim to use compositional game theory to study credible commitments scenarios by drafting a series of simple models. Our goal is to explore previously unknown types of MEV, and how MEV estimation varies depending on the beliefs of the players involved in the game.

## Background and Problem Statement

Credible commitments are known to change the equilibria of games. For instance, credibly committing strategies can veer the Nash equilibrium of a game such as prisoner dilemma to its paretian optimum.

In the case of a **coordinator** existing, namely a player able to order credible commitments submitted by other players, this feature can be abused: Players coming in first can extort other players, and as such one dominant strategy becomes bribing the coordinator to frontrun other players.

This kind of problems is interesting because it allows us to explore and pinpoint new potential kinds of MEV.

At 20squares we have software for **compositional game theory**, which allows for fast prototypation of game-theoretic models, simulations and analysis.

We plan to use open games to model some simple games that are related to credible commitments and in general bayesian beliefs about other players. From analyzing these games we hope to be able to find interesting and/or new connotations of the concept of MEV.

## Plan and Deliverables

We will start by simply modelling the 'prisoner dilemma with commitments' that we hightlighted in the previous section. It will will be a simple three player game - Alice, Bob, Coordinator.

Then, we will abstract from prisoner dilemma to something more complicated. Utilizing Automatic Market Maker models we already developed independently, we will recast the previous game as follows:
- Again, there will be three players: Alice, Bob and Coordinator
- There will also be an AMM 
- Instead of sending their swap requests to the AMM directly, Alice and Bob will send them to Coordinator, together with an (optional) payment, representing the usual `transfer(coinbase, x)`.
- Coordinator must decide the order in which these swaps have to be sent to the AMM. Coordinator takes the payments as a reward.

This effectively models a situation where Alice and Bob compete to frontrun each other. We again expect that frontrunning is a dominant strategy.

In this second example the main question we aim to answer is the following: *Given that every player has beliefs about the other players involved in the game, how do such beliefs influence the maximal extractable value of the game?*

To do this, we will switch to a Bayesian setting, where Alice and Bob have some priors about each other: these may involve the amount of tokens swapped and/or the amount of fee the other player plans to send to Coordinator. We aim to analyze how these priors influence MEV estimates for Alice and Bob.

We plan to deliver:
- Models of both games;
- Analysis of both games, hopefully consisting of some equilibrium strategies and other conceptually interesting observations;
- Documentation about what the models do, how to run and test them, and how to intepret the corresponding analytics.

Depending on how resource intensive this turns out to be, and how much time we will still have available, we may entertain the possibility of scaling these models to a higher number of players. Alternatively, this can be considered a possible direction of future work.

## References

[Credible commitments slides by Xin, easy](https://docs.google.com/presentation/d/1BhPNVYzIVkpiQ9dKUqBhPYY7z04tchmlcfhwf5FaWvw/edit#slide=id.g1a0413d509c_0_0)

[Credible commitments slides by Xin, less easy](https://docs.google.com/presentation/d/1on6OpmjEuFQ5HQOx6b6JjWzUHZx5pBoWbxVJyKAFS_c/edit#slide=id.g179bd040f01_0_15)

[MEV as a cooperative game, by Xin](https://docs.google.com/presentation/d/1_qDn-S9xHC-FTcxVsE9hV7kTw3WOSNUR9kL2i_4UFuc/edit#slide=id.g187ff1cf8c1_0_319)

[Open games main repo](github.com/cyberCat-Institute)

[Open games initial paper](https://arxiv.org/abs/1603.04641)

[A simple model in Compositional Game Theory](github.com/20squares/ftx/)

[An introductory video on the techniques we want to use](https://www.youtube.com/watch?v=Xzv54dZQZaw)
