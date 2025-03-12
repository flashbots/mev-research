---
id: <leave blank -- will be assigned by reviewers>
title: Priority order flow
team: Shtuka Research (team lead: Andrew W. Macpherson)
created: 2025-03-12
---

# Priority order flow

We propose to mount an empirical study of payments between block builders and other closely affiliated entities with a goal of revealing the extent to which builder net revenue is driven by forwarded order flow. We hypothesise that these payments — examples of which are easily found — represent rebates for a relatively undocumented form of order flow sharing that we dub *priority* order flow, where a builder forwards its private order flow to another builder with an effective discount on its fee bid.

Understanding the extent and significance of these flows is of special importance in analysing the PBS market because it  qualifies the extent to which builder success truly depends on *exclusive* as opposed to *shared* or *forwarded* flow, and correspondingly has implications on customer acquisition cost,  barriers to entry, and hence concentration vectors in PBS markets.

## Background and Problem Statement
In the celebrated study of Oz et. al (2024), order flow is classified into *public*, which has been observed in a public mempool, and *exclusive*, which ultimately appears in a block without ever entering the public mempool. But is this exclusive OF really exclusive? We argue that a better term for this so-called "exclusive" flow is rather *private*, since we don't actually know from the data whether that flow was shared privately with just one or with multiple builders. 

One of the most discussed "back-room deals" in Ethereum block building is the integration between the Banana Gun Telegram bot and Titan Builder; yet Yang et al. (2024) showed that this flow is multiplexed (muxed) to other builders in some cases. Similarly, given Flashbots Builder's limited market share, Flashbots Protect must be muxing a large fraction of its flow to multiple builders to achieve its reported transaction landing rate;[^landing] indeed, this is an explicit promise of "fast" mode.[^fast] These observations notwithstanding, since calls to builder APIs are (by design) private, it is generally not straightforward to detect muxing or forwarding behaviour.

[^landing]: https://dune.com/flashbots/flashbots-protect
[^fast]: https://docs.flashbots.net/flashbots-protect/quick-start#faster-transactions



So far, the research community has made limited use of statistical modelling techniques to make inferences about private flows. This project aims to change that: we propose to combine public data about PBS bids, payments between builders and from builders to proposers, and general market data to make deductions about the value of exclusive and shared flows and how important these are to the players' business models.

This project forms part of the Shtuka Research 2025 research programme on order flow: https://shtuka.io/orderflow

## Plan and Deliverables

By inspecting the publicly known addresses of the major builders using data platforms such as Arkham Intel, it is easy to find examples of payments from builder A to builder B in a block built by builder A. We will explore and gather a dataset of value transfers from the builder of a block.

We hypothesise that with the exception of the single payment to the proposer matching the winning bid of the PBS auction, an ETH value transfer originating from the builder of each block is a rebate for a bundle sent with a positive `refundPercent` field in the RPC call.[^refundPercent] These flows are observable and, in many cases, their recipients have community labels. It is not hard to find examples using platforms like Arkham Intel (see below).

[^refundPercent]:  See for example https://docs.titanbuilder.xyz/api/eth_sendbundle

What is not directly observable (except for a single dataset available for a limited time period from the Ultrasound Relay) is the revenue associated with blocks that did not win the PBS auction. However, bids in the PBS auction can be collected from the Relay API. For simplicity, we hypothesise that non-winning bids approximately reflect the value of non-winning blocks, that is, we assume non-winning bids are not shaded. This is in line with the simplifying assumption that builders follow the dominant strategy in an English auction, which is to continue raising the bid until the current top bid exceeds their value for the item.

Starting from the general questions:

* Are payments between builders higher when the winning block value or builder net revenue is higher?
* Are rebates to a (non-winning) builder higher when that builder's bids are higher?

we will develop a statistical model and perform regression analysis to relate observed payment and PBS bid flows with hidden variables such as value of non-winning blocks and exclusive versus muxed OF value.

Milestones:

* Build graphical model of builder fee and forwarding fee flows
* Collect data on block values, PBS bids, and other factors identified as explanatory.
* Carry out a regression analysis to find out how much of builder revenue and profit is driven by multiplexed or forwarded, as opposed to exclusive, OF.

Deliverables:

* Technical report with model details and commentary (prepared with LaTeX)
* Python notebook[s]
* Flashbots forum post

## References

### Selected observations

* We can see frequent payments from beaverbuild to Titan builder of the order of around 0.002 ETH (~$4) in blocks constructed by beaverbuild.
  https://intel.arkm.com/explorer/entity/beaverbuild

* Similarly, many payments from Titan to an entity labelled as SCP MEV bot deployer, again at around 0.002 ETH.
  https://intel.arkm.com/explorer/address/0xC6093Fd9cc143F9f058938868b2df2daF9A91d28

  One of the largest ones we could find had a block reward of 0.662 ETH, with 0.372 paid to proposer, an unusually small fraction. This block saw 0.0675 paid to SCP, comprising over 20% of pre-rebate net revenue.

### Bibliography

* Öz, B., Sui, D., Thiery, T., & Matthes, F. (2024). Who Wins Ethereum Block Building Auctions and Why? In R. Böhme & L. Kiffer (Eds.), *6th Conference on Advances in Financial Technologies (AFT 2024)* (Vol. 316, p. 22:1-22:25). Schloss Dagstuhl – Leibniz-Zentrum für Informatik. https://doi.org/10.4230/LIPIcs.AFT.2024.22
* Yang, S., Nayak, K., & Zhang, F. (2024). *Decentralization of Ethereum’s Builder Market* (No. arXiv:2405.01329). arXiv. https://doi.org/10.48550/arXiv.2405.01329
* Thiery, Thomas. (2023, August 10). *Empirical analysis of Builders’ Behavioral Profiles (BBPs)*. Ethereum Research. https://ethresear.ch/t/empirical-analysis-of-builders-behavioral-profiles-bbps/16327
