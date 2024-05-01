---
id: 
title: Efficient Design Principles for MEV-Boost Auctions
team: Bence Ladoczki
created: 2024-05-01
---

# A neural-network-based approach to the PBS landscape

The problem we are trying to solve in this work is to design an auction game which has a Nash equilibrium giving the relay the highest possible expected utility. RegretNet is a neural network architecture that can generate dominant-strategy incentive-compatible (DSIC) (every agent maximizes utility by bidding honestly, regardless of the other agents’ bids), individually rational (IR) and revenue-maximizing auction models. Our goal is to use different bid profiles from MEV-boost auctions and with the design of efficient auctions relying on RegretNet evaluate the performance (regret, utility, revenue etc.) of the current auction mechanism on PBS relays. More specifically, we use the Adam optimizer for training[2] and we train the model in different MEV-boost auction settings with known valuation distributions. As a baseline, we consider settings involving selling to one agent (e.g. 1 builder wins the auction on a certain relay) where revenue-maximizing solutions are known and evalute the trained model by making comparision to the analytical solution. 

Limitations: It is known that as the number of participants increases, it becomes more and more difficult (computationally for sure) to both maximize revenue and obey the regret constraints. We perform experiments in this direction as well and report on our results.

## Background and Problem Statement

Designing revenue-maximizing auctions while ensuring strong incentive guarantees is a fundamental problem in economic theory.

A seminal work by Dütting et al.[1] on RegretNet laid down the cornerstones of a neural network-based architecture that can be utilized to design efficient auction mechanisms. The core idea behind RegretNet is that within a Bayesian auction, one knows the valuation distributions from which samples can be drawn and the allocation and payment rules can be inferred from neural networks, with a learning objective designed to maximize revenue while enforcing strategyproofness.

More specifically, the allocation and payment functions are represented by neural networks with a set of learned weights. The allocation networks end with a softmax layer, to ensure that the allocation is a valid categorical distribution. The payment network ends with a sigmoid layer, outputing a value - the final payment.

The training data for RegretNet is a dataset of bid profiles sampled from the valuation distribution. These are used for training by standard gradient descent methods. The goal is to maximize the payments drawn from truthful bids, subject to strategyproofness. For example, maximizing expected payment can be done by simply maximizing the mean payment over training samples. In this work, unlike prior works using synthetic bids, we collect data from PBS relays and build realistic auction models.


## Plan and Deliverables


- We thoroughly review the literature on efficient auction design, including [3-8] to explore possible realizations of optimal auctions on PBS relays based on these scientific works.

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

[3] Edelman, B., Ostrovsky, M., & Schwarz, M. (2005). Internet Advertising and the Generalized Second Price Auction: Selling Billions of Dollars Worth of Keywords. National Bureau of Economic Research Working Paper Series, No. 11765. DOI: 10.3386/w11765

[4] Cramton, P. (1997), The FCC Spectrum Auctions: An Early Assessment. Journal of Economics & Management Strategy, 6: 431-495. 

[5] Leyton-Brown, K., Milgrom, P., & Segal, I. (2017). Economics and computer science of a radio spectrum reallocation. Proceedings of the National Academy of Sciences of the United States of America, 114(28), 7202–7209. 

[6] Vickrey, W. (1961). Counterspeculation, Auctions, And Competitive Sealed Tenders. Journal of Finance, 16(1), 8–37.

[7] Myerson, R. B. (1981). Optimal Auction Design. Mathematics of Operations Research, 6(1), 58–73.

[8] Daskalakis, C., Deckelbaum, A., & Tzamos, C. (2013). Mechanism design via optimal transport. In ACM Conference on Economics and Computation
