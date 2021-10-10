---
id: 11
title: MEV in eth2 early exploration
team: @obadiaa @tkstankacz @fiiiu @taarushv @prysmaticlabs
created: 2021-05-28
status: finished
---

# MEV in eth2 early exploration


## Background and Problem Statement
The Merge is the long-awaited change in consensus mechanism of Ethereum from proof of work to proof of stake. PoS Ethereum, or eth2, is a major upgrade that will significantly change the flow of transaction inclusion and validation on the Ethereum chain. We propose to do an exhaustive survey of eth2, and to reason about MEV within it, including in what form it may exist, how it could be extracted, whether any negative externalities are incurred from it and who are its stakeholders.

This proposal's core limitation is the fact eth2 in production may differ from the current picture of eth2 we have available, both with respect to what The Merge will entail and with respect to future updates to Ethereum after The Merge such as the addition of sharding or stateless clients.

## Plan and Deliverables
- general survey of eth2
- assess how, and if, MEV exists in eth2
- assess how Flashbots might work in eth2
- surface deeper research questions that will be further studied following this work

We aim at delivering a blogpost that covers these key points.


## References
Reference current relevant literature or past work pertaining to the research question(s) at stake.
- https://pintail.xyz/posts/beacon-chain-validator-rewards/
- https://notes.ethereum.org/@vbuterin/B1mUf6DXO
- https://hackmd.io/@prysmaticlabs/finality
- https://ethresear.ch/t/eth1-eth2-client-relationship/7248
- https://notes.ethereum.org/@n0ble/rayonism-the-merge-spec
- https://github.com/flashbots/raytracing
- https://ethresear.ch/t/high-confidence-single-block-confirmations-in-casper-ffg/8909?u=benjaminion
- https://docs.google.com/spreadsheets/d/1FslqTnECKvi7_l4x6lbyRhNtzW9f6CVEzwDf04zprfA/edit#gid=0
