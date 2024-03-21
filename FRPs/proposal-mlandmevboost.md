---
id: 
title: Efficient Design Principles for MEV-Boost Auctions
team: Bence Ladoczki
created: 2024-03-21
---

# A neural-network-based approach to the PBS landscape

RegretNet is a neural network architecture that can generate DSIC (dominant-strategy incentive-compatible, e.g. every agent maximizes utility by bidding honestly, regardless of the other agents’ bids), IR (individually rational) auction models. Our goal is to use different bid profiles from MEV-boost auctions and with the design of efficient auctions relying on RegretNet compare the characteristics of the two models. More specifically, we use the Adam optimizer for training[2] and we train the model in different MEV-boost auction settings with known valuation distributions. As a baseline, we consider settings involving selling to one agent (e.g. 1 builder wins the auction on a certain relay) where revenue-maximizing solutions are known and evalute the trained model by making comparision to the analytical solution. 

Limitations: It is known that as the number of participants increases, it becomes more and more difficult (computationally for sure) to both maximize revenue and obey the regret constraints. We perform experiments in this direction as well and report on our results.

## Background and Problem Statement

Designing revenue-maximizing auctions while ensuring strong incentive guarantees is a fundamental problem in economic theory.

A seminal work by Dütting et al.[1] on RegretNet laid down the cornerstones of a neural network-based architecture that can be utilized to design efficient auction mechanisms. The core idea behind RegretNet is that within a Bayesian auction, one knows the valuation distributions from which samples can be drawn and the allocation and payment rules can be inferred from neural networks, with a learning objective designed to maximize revenue while enforcing strategyproofness.

More specifically, the allocation and payment functions are represented by neural networks with a set of learned weights. The allocation networks end with a softmax layer, to ensure that the allocation is a valid categorical distribution. The payment network ends with a sigmoid layer, outputing a value - the final payment.

The training data for RegretNet is a dataset of bid profiles sampled from the valuation distribution. These are used for training by standard gradient descent methods. The goal is to maximize the payments drawn from truthful bids, subject to strategyproofness. For example, maximizing expected payment can be done by simply maximizing the mean payment over training samples. In this work, unlike prior works using synthetic bids, we collect data from PBS relays and build realistic auction models.


## Plan and Deliverables


- Data collection from public PBS relays (Aestus, Agnostic Gnosis, Eden Network, Flashbots, Manifold, etc) [2 month]

- Evaluating the applicability of RegretNet as is [1 week]

- Neural network building [1 month]

- Model evaluation, accuracy assessment, model improvement, fine-tuning parameters [3 weeks]

- Proposal for improved accuracy [1 week]

- Research paper [2 weeks]

- Open-source code on GitHub with documentation [1 week]


## References

[1] P. Dütting, Z. Feng, H. Narasimhan, D. Parkes and S. Srivatsa Ravindranath. 2019. Optimal auctions through deep learning. International Conference on Machine Learning. 1706–1715.

[2] Kingma, D. P., & Ba, J. (2015). Adam: A Method for Stochastic Optimization. In 3rd International Conference for Learning Representations, San Diego.

