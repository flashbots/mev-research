---
id: 13
title: Flashbots in eth2
team: @obadiaa @tkstankacz @taarushv
created: 2021-06-04
status: in progress
---

# Flashbots in eth2


## Background and Problem Statement
After an initial exploration of MEV in eth2 and the Rayonism hackathon where a spec of an eth1+eth2 MEV client was built out, several new questions have surfaced on how Flashbots will function on eth2. The aim of this FRP is to dive deeper into eth2 and into the initial PoC built during the hackathon to answer these questions, working alongside external collaborators such as different types of validators/validator pools.

As explained in the initial post [MEV in eth2 - early exploration](https://hackmd.io/@flashbots/mev-in-eth2), MEV is more important in eth2 given its significant boost to validator rewards and its amplifying effect on the inequality between validators. For that reason, we need to make sure MEV extraction is democratized in eth2 by ensuring it benefits validators of all sizes and doesn't lead to foreseeable negative externalities.


## Plan and Deliverables

The main deliverable of this FRP is to produce one, or multiple specs, of Flashbots in eth2 as well get a deep understanding of the validator landscape. The FRP will answers questions such as:

- what does the ideal mechanism look like?
  - for MEV revenue distribution
  - for MEV bundle pushing
  - for bundle merging
  - to mitigate searcher and validator collusion (and what are possible dimensions of collusions)

- is there any work to do at the beacon client level?
  - eth2 votes stuffing optimization and how that relates to eth1 block optimization?
  - vouch, attestant's tool for client diversity that picks between beacon blocks proposed by different beacon clients
  - should mev be integrated in a single eth1+beacon client process or be at the eth1 client level?

- can we encrypt txs with proposed validator's key? what are the implications of this?
  - can we use ethereum's p2p network instead of Flashbots to gossip txs?
  - is there anything that can upstreamed into Ethereum?

- how are different pools and validators set-up and how will they be running flashbots?
  - study key delegation and permissions that are shared & how that influence who has ultimate say over selection of eth1 payload
  - survey different payout methods & pool architectures
  - secret shared validator pools


## References
- https://github.com/flashbots/raytracing
- https://github.com/ethereum/rayonism
- https://github.com/ethereum/eth2.0-specs
- https://twitter.com/jcksie/status/1384154639596101632?s=21
- https://github.com/ethereum/eth2.0-specs/pull/2454
- https://github.com/attestantio/vouch
- https://github.com/ethereum/eth2.0-specs/pull/2454
