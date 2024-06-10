---
id: <leave blank -- will be assigned by reviewers>
title: <Incentive-Aligned Proposer Builder Separation Model>
team: <Babu Pilla, (team TBC)>
created: <2014-06-10>
---

# Incentive-Aligned Proposer Builder Separation Model

The PBS model seems to be a promising solution to addressing MEV exploitation. The aim is to foster good MEV, which is essential for a healthy ecosystem, and avoid bad MEV, which exploits the power of being in the position of ordering transactions. However, the same old principal-agent problem applies between the proposer and builder. As such, a weaker point is the assumption of trust between participants and the incentive model.

We propose designing an incentive schema where builders and proposers act in their best interests, naturally protecting customers (users). Let us assume the builder is a customer (user)-facing entity; then they should be incentivised to serve the users, for example, by minimizing MEV extraction. Our preliminary work identifies an incentive scheme that motivates the builder to offer better rates for users in return for a reward if the builder provides a lower slippage. We want to expand this research with some experiments and incorporate the latest developments.

## Background and Problem Statement

While the primary intent of the PBS model is to protect against transaction censorship attacks and restructure the economics of MEV. However, this model engenders a competitive marketplace among its participants with a risk of centralisation with a limited number of participants. In the PBS model, block building and proposing are distinct operations open to any participants with the necessary resources. Ideally, there should not be any dependency between builders and proposers. There needs to be a balance where builders are motivated to create blocks that are profitable to users, and proposers are incentivised to choose blocks that are best for the network. Nonetheless, the current PBS architecture involves varying trust assumptions among builders, proposers, and relayers. While separating block building from validation is advantageous, the associated incentive scheme is currently underdeveloped due to these trust assumptions. The research question is: How can we minimise the trust assumptions among different participants in the PBS model?

## Plan and Deliverables

Conduct a literature review on the latest developments in the PBS and MEV space. Seek feedback on the proposed model's practicality. Develop a testing model to evaluate certain properties of the proposed scheme. Finally, publish a journal paper.

Funding will be helpful to get students to work on the implementation and testing.

## References
Previse work.
- [Blockchain MEV minimisation solution with price guarantee reward](https://hackmd.io/@sxysun/shapley).
