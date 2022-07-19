---
id: 
title: Embracing MEV in protocol design
team: borked
created: 2022-07-18
---

## Background and Problem Statement
This FRP will propose and investigate a DEX protocol where searchers are the only liquidity providers.

The MEV ecosystem -- searchers, Flashbots, miners, etc. -- is robust and capable of adding value off-chain in ways that are impossible on-chain. For example, searchers may view the mempool, process high-volume public market data, or perform complex calculations. As such, it makes sense to consider the MEV ecosystem as a resource to be utilized by any new protocol.

Two challenges for the protocol designer, then, are to devise ways to incentivize MEV activity that benefits the protocol while minimizing the opportunity for MEV attacks. For example, AAVE's liquidation mechanism and Uniswap's capital-free arbitrage are MEV activities that improve protocol health. Several DEXes implement mechanisms for reducing MEV attacks (see references below).

We'll present and discuss ways to use Flashbots' dark transaction ordering (bundles) and searchers' off-chain processing capabilities to (w.r.t. AMMs):

- reduce impermanent loss
- increase capital efficiency
- mitigate smart contract risk
- lower effective spreads
- reduce the size and frequency of price dislocations

while still minimizing MEV attacks.


## Plan and Deliverables

### Deliverables
We'll produce a paper containing:
- MEV background
 - MEV ecosystem actors and infrastructure
 - searchers' capabilities
 - helpful and harmful DEX-related MEV activity
- Short survey of related efforts
 - designs that move order matching off-chain
 - MEV attack-prevention mechanisms
- DEX protocol
 - design goals
 - description of mechanisms
 - "perturbation"-style reasoning about design ("What if we changed X, what would break?")
 - comparison to AMMs (impermanent loss, capital efficiency, etc.)

Also, the key ideas of the protocol will be implemented in a smart contract to help validate their feasibility.

The deliverables could serve as a reference or inspiration for protocol designers interested in finding ways to benefit from Flashbots and the MEV ecosystem more generally.

### Timeline
We anticipate three months to completion of the project. Full drafts of the design and code should be completed in the first month.


## References

- MEV incentivization
 - [AAVE liquidation](https://docs.aave.com/developers/guides/liquidations)
 - [Uniswap capital-free arbitrage](https://docs.uniswap.org/protocol/V2/concepts/core-concepts/flash-swaps)
- MEV attack protection
 - [CoWSwap](https://cowswap.exchange)
 - [mistX](https://blog.alchemist.wtf/alchemist-mistx-a-new-path-forward-6434984d013)
 - [ArcherSwap](https://medium.com/archer-dao/introducing-archer-swap-e13fe521d5d0)
 - [HashFlow](https://docs.hashflow.com/hashflow/)
- Utilization of off-chain processing
 - [SLOB proposal](https://jumpcrypto.com/searcher-limit-order-book/)
 - [0x exchange](https://www.0x.org/pdfs/0x_white_paper.pdf)
