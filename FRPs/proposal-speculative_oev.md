---
id: <leave blank -- will be assigned by reviewers>
title: An Analysis on Speculative Oracle Extractable Value
team: Hasret Ozan Sevim (International School of Advanced Studies (University of Camerino) / Catholic University of Sacred Heart), Christof Ferreira Torres (INESC-ID / Instituo Superior Técnico (IST), University of Lisbon)
created: 2026-02-20
---

# An Analysis on Speculative Oracle Extractable Value

Previous work [1][2][3] has examined Oracle Extractable Value (OEV) primarily from a theoretical and non-speculative perspective. In contrast, this project seeks to advance the understanding of OEV through an empirical analysis of historical liquidation events and oracle price updates, with a particular focus on how oracle update latencies may enable or influence speculative OEV extraction strategies.

## Background and Problem Statement

OEV is a subset of Maximal Extractable Value (MEV) that focuses on value extraction enabled by on-chain signals provided by oracles. A prominent example of OEV is liquidations: lending protocols rely on oracle price feeds to determine whether collateral values have fallen below required thresholds and whether loans should be opened for liquidation.

Chainlink is currently the most widely used price oracle provider and is heavily integrated into on-chain lending protocols such as Aave. With the emergence of optimistic or speculative arbitrage [4], a natural question arises: how can speculative MEV extraction strategies be applied in the context of OEV, and liquidations in particular?

Chainlink operates Decentralized Oracle Networks (DONs), which consist of multiple nodes that independently collect price data from various sources and reach consensus to aggregate and publish a unified market price on-chain. Lending protocols then use these prices to assess collateral values and trigger liquidations when necessary. Many of the underlying price sources originate from common centralized exchanges (CEXs), which are blockchain-independent. However, these prices must be propagated to multiple blockchains, each with different latency characteristics.

This raises the question of whether latency differences across chains can be exploited for MEV extraction. The goal of this project is to collect historical liquidation data and oracle price updates and analyze whether systematic patterns or deterministic cross-chain latencies exist that could be leveraged to perform speculative MEV strategies, such as liquidation-based arbitrage.

## Plan and Deliverables

We begin by collecting historical liquidation data across four major blockchain networks: Ethereum, Arbitrum, Optimism, and Base. To do so, we will leverage and adapt existing data collection and analysis scripts developed by Ferreira Torres et al. [5], extending them where necessary to support multi-chain analysis and to ensure consistent data extraction across networks. This dataset will include detailed information on liquidation events such as timestamps, transaction ordering, affected assets, and liquidation volumes.

In a second step, we will associate these historical liquidation events with corresponding oracle price data. Specifically, we will collect historical price feed updates emitted on each of the four chains and link them to liquidation triggers. This will allow us to analyze how oracle-reported price changes propagate across chains and how they correlate with observed liquidation activity.

Building on this combined dataset, we will compute and analyze cross-chain latency differences in oracle price updates. Our goal is to study whether these latencies exhibit deterministic behavior or recurring patterns across chains. Identifying such patterns would make it possible to predict oracle update timing and assess whether these delays can be exploited to extract speculative OEV, particularly through liquidation-based strategies.

To keep the scope of the project focused and tractable, we restrict our analysis to liquidation events emitted by the Aave protocol and price updates emitted by Chainlink. These choices are well justified, as Aave and Chainlink currently represent the largest lending protocol and the most widely used decentralized price oracle, respectively, across all chains considered in this study.

The primary deliverables of this project will be a research paper detailing our methodology, data analysis, and results, as well as an accompanying blog post that summarizes the key findings and their implications for a broader technical audience. 

## References

[1] Greene, J., Shahid, A., Benligiray, B. and Vänttinen, H., Oracle Extractable Value (OEV) through Order Flow Auctions.

[2] Finkbeiner, C. and Almashaqbeh, G., 2025. SoK: Blockchain Oracles Between Theory and Practice. Cryptology ePrint Archive.

[3] Humphry, R., Avramovic, P., Acevedo, F., Alkhair, S. and Gervais, A., 2024. Review of Maximal Extractable Value & Blockchain Oracles. Technical report, Financial Conduct Authority.

[4] Solmaz, O., Heimbach, L., Vonlanthen, Y. and Wattenhofer, R., 2025. Optimistic MEV in Ethereum Layer 2s: Why Blockspace Is Always in Demand. arXiv preprint arXiv:2506.14768.

[5] Ferreira Torres, C., Mamuti, A., Weintraub, B., Nita-Rotaru, C. and Shinde, S., 2024, December. Rolling in the shadows: Analyzing the extraction of mev across layer-2 rollups. In Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security (pp. 2591-2605).
