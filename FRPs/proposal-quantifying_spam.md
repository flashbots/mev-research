---
id: <leave blank -- will be assigned by reviewers>
title: Quantifying and Analyzing Spam Across Ethereum's Ecosystem
team: Christof Ferreira Torres (INESC-ID / Instituto Superior Técnico (IST), University of Lisbon), Vabuk Pahari (MPI-SWS), Johnnatan Messias (MPI-SWS)
created: 2026-02-20
---

# Quantifying and Analyzing Spam Across Ethereum's Ecosystem

Recent works [1][2][3] have documented a significant increase in spam transactions, particularly on L2 networks. This trend is largely attributed to low transaction fees and the absence of effective filtering mechanisms, such as the bundling solutions enabled by private mempools on Ethereum. The prevailing view is that the majority of spam originates from MEV-related activities, including speculative arbitrage. This project aims to provide a comprehensive analysis of spam across the Ethereum ecosystem by proposing a general definition of spam and systematically categorizing and quantifying its various forms.

## Background and Problem Statement

MEV (Maximal Extractable Value) extraction is widespread across blockchain systems at both L1 and L2, but its dynamics differ significantly across layers. On L1s such as Ethereum, a public mempool enables MEV to be captured within the same block in which opportunities arise. In contrast, L2s (e.g., rollups) lack public mempools, making MEV opportunities visible only after block commitment and thus exploitable only in subsequent blocks.

Recently, Speculative MEV has emerged as a method to enable same-block MEV extraction without a public mempool. This approach relies on flooding the network with transactions that blindly attempt to capture potential MEV opportunities, profiting only in expectation over many attempts. While previously uneconomical, sharply reduced transaction fees, particularly on L2s after the Dencun upgrade, have made speculative strategies viable.

However, speculative MEV is considered highly inefficient. Most transactions fail because no MEV opportunity exists, yet they consume block space, computation, and storage, exacerbating congestion and Data Availability (DA) pressures while crowding out legitimate user activity.

Prior work [1][2][3] studies Speculative MEV primarily through the lens of arbitrage and relies on coarse heuristics to identify spam. For example, [1] classifies transactions as spam that simply issue multiple DEX price queries but transfer no tokens, an oversimplification that solely focuses on arbitrage related logic. More broadly, existing definitions conflate spam with failed arbitrage.

This work aims to propose a more general and formal definition of spam beyond speculative arbitrage and introduces a scalable methodology to quantify spam over long historical periods. We systematically analyze the types and prevalence of spam across major EVM chains, such as Ethereum, Arbitrum, Optimism, and Base, to assess whether speculative arbitrage is indeed the dominant source of blockchain spam or whether other sources exist.

## Plan and Deliverables

This project proposes a novel method for detecting spam in blockchain systems and integrates it with existing public datasets to enable a large-scale empirical analysis of Ethereum mainnet and major L2 rollups, including Arbitrum, Optimism, and Base.

The core idea is to define spam from a computational perspective by formalizing what constitutes a meaningful state transition in the context of blockchain transactions. We define a meaningful state change as any change that updates an account’s storage or modifies an account balance beyond simple transaction fee transfers. Based on this definition, we replay historical blocks by removing a single transaction and re-executing the block without it. If the resulting execution produces exactly the same meaningful state changes as the original block, we conclude that the removed transaction did not contribute in a meaningful way and therefore classify it as spam.

Building on this definition, we will develop an efficient methodology to perform this replay-based analysis at scale. This will enable a comprehensive empirical study that quantifies and compares spam activity across networks. We will then conduct in-depth analyses to uncover the mechanisms, behavioral patterns, and negative externalities associated with spam, and evaluate whether speculative arbitrage is the primary driver of spam in contemporary blockchain ecosystems. The results will be synthesized into a comprehensive research article.

Planned deliverables include:
- An open-source GitHub repository containing measurement scripts, curated datasets, and analytical tools
- An academic paper submitted to a peer-reviewed conference
- A shorter, accessible article published on Medium or the Flashbots website

## References
- [1] Robert Miller. (2025). MEV and the Limits of Scaling. https://writings.flashbots.net/mev-and-the-limits-of-scaling
- [2] Krzysztof Gogol, Manvir Schneider, and Claudio Tessone. (2025). When Priority Fails:
Revert-Based MEV on Fast-Finality Rollups. https://arxiv.org/pdf/2506.01462
- [3] Ozan Solmaz, Lioba Heimbach, Yann Vonlanthen, and Roger Wattenhofer. (2025). Optimistic MEV in Ethereum Layer 2s: Why Blockspace Is Always in Demand. arXiv. https://arxiv.org/pdf/2506.14768
