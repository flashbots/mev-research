---
id: 12
title: MEV in l2 & sidechains exploration
team: @obadiaa @fxfactorial
created: 2021-06-04
status: pending
---

# MEV in l2 & sidechains exploration


## Background and Problem Statement
As Ethereum's layer 1 becomes increasingly used, many applications are looking to move to outer layers of Ethereum in order to operate more efficiently (high tx throughput, lower tx fees). Each of these layers have different tx ordering rules from layer 1, different consensus mechanisms and different entities executing the ordering. Intuitively, it seems a lot of existing MEV transaction flow could move to these layers and makes MEV on such layers worth studying in further detail.

In addition, a key property of Ethereum today widely used by most applications in DeFi is atomic composability: the ability to compose smart contracts together and execute multi-contract interactions atomically in a single transaction. However, atomic cross-layer composability does not seem to be achievable. In the case of DeFi, this implies potentially significant liquidity fragmentation which should be a large source of MEV. However, the mechanics of how it will be captured, and how layers will interact with each other is not clear at the moment.

This initial FRP is an exploration of these themes to start wrapping our heads around the multi-chain multi-layered world.


## Plan and Deliverables
Since this is a rather large topic, we will prioritize l2s and sidechains with existing adoption and will limit work on the ones that are still actively changing their technology significantly.

Some of the questions we plan to cover include:
- what does the liquidity landscape look like once l2s are adopted?
  - survey of cross-chain l2s solutions (Optics, Hop, Connext, Exfil)
  - survey of different protocol architectures (cross-L2 liquidity pools vs isolated ones)
  - assessing the impact of liquidity fragmentation (instances of protocols in different places, different L2 tokens)
- what does the content of eth1 blocks look like when l2s are adopted?
- what are potential scenarios for how adoption of l2s will progress?
- is transaction ordering across l2s useful? how would it work?
  - build a prototype?
- are there new forms of MEV enabled by L2s?
  - pockets enabled by low tx high tps
- compare and contrast how this problem resembles cross-shard composability
- study probabilistic MEV & risk-scoring/weighting in an asynchronous world of l2s and shards, across different concepts of finality and ordering

We aim at delivering a blogpost that covers these key points as well as relevant prototypes.


## References
- https://ethresear.ch/t/cross-rollup-dex-with-smart-contracts-only-on-the-destination-side/8778
- https://twitter.com/gakonst/status/1311342880146042881
- https://docs.celo.org/celo-codebase/protocol/optics#optical-channels-for-cross-chain-communication
- https://twitter.com/ConnextNetwork/status/1363933825802248194
- https://ethresear.ch/t/cross-shard-defi-composability/6268
- https://hop.exchange/whitepaper.pdf
- https://twitter.com/matchaxyz/status/1400483371067723780?s=21
- https://github.com/perpetual-protocol/perp-arbitrageur
- https://medium.com/starkware/caspian-an-l2-powered-amm-f20e93b5421
