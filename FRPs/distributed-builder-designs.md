---
id: 
title: Early Exploration on Distributed Block Builder Designs
team: HashCloak
created: 2023-08-08
---

# Early Exploration on Distributed Block Builder Designs
We formally define distributed block building in the permisionless setting, where a number of block builders may collaborate to construct a block, and explore a variety of possible designs. We look at how distributed block builders fare competitively against their centralized counterparts. Given the permissionless setting that our model assume, we also touch on security and incentive compatibility of such designs in the face of mutually distrusting (and possibly adversarial) block builders.

## Background and Problem Statement
MEV and PBS tends towards builder centralization, where a small cartel of builders control what transactions make it into a block. This threatens Ethereum’s goals of credible neutrality and decentralization, given transaction censorship is way cheaper in a PBS regime. Additionally, a handful of builders having control over block production presents a liveness risk to the Ethereum network. This motivates the need for distributed (and decentralized) block builders.

## Plan and Deliverables
We explore possible designs for how a block builder could be trustlessly distributed among *n* mutually distrusting builders (who may or may not also be MEV searchers). The adversarial setting of this problem also requires special attention to the privacy, security, and incentive compatibility of such block builder schemes. We define a minimum set of requirements for a distributed block builder to be secure and incentive compatible.

Following that, we answer whether any practical constructions of such distributed block builders satisfy these requirements and can remain competitive against existing centralized builders.

Concretely, this paper:
1. A literature review of MEV and PBS (MEV-Boost and ePBS) architectures
5. Defines desiderata for distributed block builders protocols
6. Identifies the constraints our desiderata place on decentralized builder protocols and argue whether distributed builders can be competitive against centralized builders.
7. Formulates possible incentives for builders to collaborate to build blocks and centralize builder order flow in one decentralized protocol. This would formally validate SUAVE's raison d'être.
8. Proposes concrete designs for distributed block builder protocols that fulfill our desired criteria (security, privacy, incentive compatibility). We could also answer if SUAVE's current proposed design satisfies this.

Namely, some of these desiderata look like:
- bundle and transaction privacy (to prevent mev-stealing)
- low-latency (block building is highly time sensitive)
- geographic decentralization
- feasibility of distributed block building post-danksharding

We plan to produce a research paper and a shorter blogpost with a summary of our results.

## References
1. [FRP-10: Distributed Blockbuilding networks via secure knapsack auctions](https://collective.flashbots.net/t/frp-10-distributed-blockbuilding-networks-via-secure-knapsack-auctions/1955) by Mikerah Quintyne-Collins
2. [Distributed Block Building](https://github.com/flashbots/mev-boost/issues/139) by Alex Stokes
3. [Decentralizing the Builder Role](https://joncharbonneau.substack.com/p/decentralizing-the-builder-role) by Jon Charbonneau
4. [Game-Theoretic Model for MEV-Boost Auctions (MMA)](https://ethresear.ch/t/game-theoretic-model-for-mev-boost-auctions-mma/16206?utm_source=substack&utm_medium=email) by Thomas Thiery
5. [Block Builder Decentralization is coming, but maybe not so soon](https://bittokoin.substack.com/p/block-builder-decentralization-is) by BallsyAlchemist
