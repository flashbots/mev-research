---
id: 27
title: Auction Simulations under PBS
team: 20squares
created: 2022-12-09
status: active
---

# Auction Simulations under PBS

We aim to use compositional game theory to model the current auction mechanismm in the Proposer-Builder Separation paradigm. We aim to then run analyses on our model and, depending on the concrete outcomes, to suggest alternative auction mechanisms that may improve welfare and other desiderata.

## Background and Problem Statement

Under the proposer-builder-separation paradigm, the auction mechanisms which determine the allocation of transactions are key for the overall performance of the system.

It is important to understand how the current format and possible alternative auction designs affect the different actors' payoffs (validators, builders). In particular, it is critical to understand whether single builders might be able to establish themselves as a dominant player thereby posing a risk for the overall protocol.

This also requires to model the individual differences in information different builders might have access to (such as exclusive order flow) and how such informational advantages might interact with bidding behavior and possible centralization effects.

Once we have developed a basic model of the environment, we want to answer the following questions: What effect do different auction formats have on the different participants in the block auction and how might such formats contribute to avoiding an entrenching and thus ultimately centralization of few players.

## Plan and Deliverables

We will develop a model of the auction environment based on compositional game theory. Compositional game theory is based on a novel mathematical framework and comes equipped with an implementation that supports the modelling processes. A key advantage of this approach is its compositionality: game theoretic models can be developed in a divide-and-conquer fashion.

Compositionality is particularly useful for the problem at hand as we can approach the modelling of the auction setting in PBS in a modular way. The model we provide here can be easily extended or be reused in a different setting.

### Phases

Our approach has three phases:

1. Develop an adequate model of the current auction market. We will be focusing on the auction between builders and validators and a repeated interaction in that market.

2. Analyze the current auction market. What can we say w.r.t. equilibrium bidding strategies? What properties do these strategies exhibit? Is there a threat of centralization?

3. Depending on the results under 2, we will propose alternative auction designs and compare their performance.

### Deliverables

We will provide an open games model, i.e. a computational representation of the auction setup and the relevant agents, that features the key elements and, what is key, can be easily extended in the future. In addition, we will provide outputs of the analysis and the different auction designs we investigated. The analysis will be fully replicable and should be easy to reuse.

## References
[Flashbots Auction Overview](https://docs.flashbots.net/flashbots-auction/overview)
[Flashbots MEV-Boost](https://boost.flashbots.net/)
[Builder API](https://ethereum.github.io/builder-specs/)
[PBS](https://ethresear.ch/t/proposer-block-builder-separation-friendly-fee-market-designs/9725)
[Open games main repo](github.com/cyberCat-Institute)
[Open games initial paper](https://arxiv.org/abs/1603.04641)
[A simple model in Compositional Game Theory](github.com/20squares/ftx/)
[An introductory video on the techniques we want to use](https://www.youtube.com/watch?v=Xzv54dZQZaw)
