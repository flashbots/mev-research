---
id: 13
title: Flashbots in eth2
team: @obadiaa @tkstankacz @jparyani @fxfactorial
created: 2021-06-04
status: pending
---

# Flashbots in eth2


## Background and Problem Statement
After an initial exploration of MEV in eth2 and the Rayonism hackathon where a spec of an eth1+eth2 MEV client was built out, several new questions have surfaced on how Flashbots would function on eth2. The aim of this FRP is to dive deeper into eth2 and into the initial PoC built during the hackathon to answer these questions, working alongside external collaborators such as different types of validator pools on test implementations.


## Plan and Deliverables
- what does the ideal mechanism look like?
  - for MEV revenue distribution
  - for MEV bundle pushing
  - for bundle merging
  - to mitigate searcher and validator collusion (and what are possible dimensions of collusions)
- is there any work to be done at the beacon client level?
  - eth2 votes stuffing optimization and how that relates to eth1 block optimization?
- how are different pools and validators set-up and how will they be running flashbots?
  - study key delegation and permissions that are shared & how that influence who has ultimate say over selection of eth1 payload
  - survey different payout methods & pool architectures
- can we encrypt txs with proposed validator's key? what are the implications of this?
  - can we use ethereum's p2p network instead of Flashbots to gossip txs?
- how does the sgx spec work in eth2?


## References
- https://github.com/flashbots/raytracing
- https://github.com/ethereum/rayonism
- https://github.com/ethereum/eth2.0-specs
