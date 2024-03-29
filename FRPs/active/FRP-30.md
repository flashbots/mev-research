---
id: 30
title: Quantifying Shareable MEV
team: Fan Zhang (Yale), Sen Yang (Yale), Xinyuan Sun (Flashbots)
created: 2023-03-23
status: active
---

# Quantifying Shareable MEV

Sharing MEV profits with users is an important goal of MEV mitigation, and various approaches have been proposed, including [BackRunMe](https://docs.bloxroute.com/introduction/backrunme) and [MEV-Share](https://collective.flashbots.net/t/mev-share-programmably-private-orderflow-to-share-mev-with-users/1264). However, the question of how to design an effective and fair MEV sharing scheme (MSS) remains a challenge. In collaboration with Xinyuan, this project aims to conduct a systematic study of MSS, providing a theoretical foundation for MSS and validating different MSSes using blockchain data.

## Background and Problem Statement

While the Shapley Value has been proposed as a possible solution, there has yet to be a comprehensive study of MSS. This project will address this gap by formalizing the MSS problem and systematically analyzing proposed solutions. We will use blockchain data, including on-chain data and potentially mempool data, to quantitatively compare different MSSes, determine the potential amount of MEV "kickback" they could generate, and identify areas for optimization.

## Plan and Deliverables

This project builds on an ongoing collaboration with Xinyuan and will produce a formal treatment of the MSS problem, an empirical study that quantifies the performance of different MSSes using blockchain data, and recommendations for improvements. The findings will be published in an academic paper.

## References

- [Shapley Value of MEV](https://hackmd.io/@sxysun/shapley) by sxysun.
