---
id: <leave blank -- will be assigned by reviewers>
title: Empirical Study of Transaction Revert and MEV on L2s
team: Daniel Marzec, Fahim Ahmed
created: 2025-02-06
---

# Transaction Revert and MEV on L2s

As Ethereum rollups gain adoption, the dynamics of Maximum Extractable Value (MEV) on Layer-2 (L2) blockchains are evolving, creating new challenges and opportunities for arbitrageurs, liquidators, and sequencers. While L2 mempools are often encrypted and operate on a first-come, first-served basis, low gas fees make mempool spamming an attractive MEV extraction strategy.
In this research, we analyze the effectiveness of spam-based MEV strategies using empirical data from major rollups and DeFi protocols. Additionally, we evaluate how these strategies can be optimized with revert protection mechanisms.

## Background and Problem Statement
The evolution of MEV extraction has undergone significant transformations, beginning with Ethereum’s early days. The introduction of MEV Boost mechanisms, followed by Proposer-Builder Separation (PBS), transformed how MEV was captured on Ethereum, and now, with the rise of rollups, Layer-2 (L2) blockchains, history appears to be repeating itself.

Rollups are gaining traction, reshaping transaction execution and settlement dynamics. However, MEV remains an inherent challenge, leading to what is often described as the MEV trilemma—where avoiding MEV extraction entirely is impossible.

The Dencun upgrade resulted in a significant reduction in gas fees on L2 and a surge in the transaction revert rate, indicating the ongoing evolution of MEV strategies. Although initially, blob transactions were relatively inexpensive, their rising costs could pose new challenges for rollup scalability and MEV extraction strategies.

Looking ahead, major developments such as Unichain with the proposed sequencer-builder separation, MEV tax, and revert protection mechanisms could introduce new paradigms for MEV extraction on L2s.

This research explores these developments and analyzes the reverted transactions on L2s with the goal of attributing them to MEV extraction strategies. In particular, the research questions are:
1) How do reverted transactions correlate with different MEV strategies/taxonomies, such as atomic and non-atomic arbitrage, liquidations, and other forms of extraction? What patterns can be identified in user behavior related to reverted transactions?
2) What is the scale of spam-based MEV extraction on Ethereum rollups, based on empirical analysis of reverted transactions? How does spam-based MEV profitability compare across different L2 solutions and DeFi protocols?
3) What impact can revert protection mechanisms have on these MEV strategies, rollup economics, and Ethereum in relation to blob pricing?
   
## Plan and Deliverables
This study analyzes reverted transaction data from major EVM-compatible rollups, such as Arbitrum, Optimism, Base, ZKsync and recently launched Unichain. The dataset is sourced from blockchain archive nodes (via Dune, Nansen, Alchemy, Allium or similar platform) from the Dencun upgrade (March 2023) until today. For the executed transaction, event logs of Uniswap V2, V3, V4, or other DeFi protocols are parsed to retrieve the DeFi transaction details. Binance (with 1s data granularity) is used as a source of off-chain market prices and acts as a benchmark CEX.

The major challenge of this research is the fact that DeFi smart contracts do not register event logs of failed transactions. Thus, the failed transactions must be matched to subsequent successful ones. When a transaction succeeds, event logs from Uniswap, Aave, or other DeFi protocols can be parsed, allowing for the extraction of exact transaction parameters and the calculation of the profitability of the executed MEV strategy.

The process follows these steps:
1) Identify all reverted transactions and group them by sender and destination address.
2) Determine the most frequently used destination addresses, such as Uniswap pools and Aave pools.
3) Identify the primary senders of these transactions.
4) Locate successful transactions originating from the same senders within the relevant DeFi pools and extract the corresponding event logs (as event logs are not available for reverted transactions).
5) Assess the profitability of the identified strategy, determining whether the transactions are linked to MEV extraction.

Timeline:
- Month 1: Data gathering, event log parsing, and matching
- Month 2: Detailed analysis across DeFi liquidity pools on L2s and estimation of spam-based MEV profitability
- Month 1-2: Paper writing and synthesizing findings

Delivaratbles:
- An open-source Python project that explores reverted transactions on EVM L2s and maps them to MEV strategies.
- An academic paper to be submitted to one of the peer-reviewed conferences (e.g., AFT, FC).
- A short article published in the HackMD research publication.
- A presentation given at one of the community events.

## References
- Adams, H., Toda, M., Karys, A., Wan, X., Gretzke, D., Zhong, E., Wong, Z., Marzec, D., Miller, R., Hasu, & Floersch, K., & Robinson, D. (2024). Unichain Whitepaper. https://docs.unichain.org/whitepaper.pdf
- Zhu, B. Z., Wan, X., Moallemi, C. C., Robinson, D., & Bachu, B. (2024). Quantifying the Value of Revert Protection. arXiv. https://arxiv.org/abs/2410.19106
- Flaashbots Post (2024). It’s time to talk about L2 MEV. https://collective.flashbots.net/t/it-s-time-to-talk-about-l2-mev/3593/1
- Flashbots Dune Dashboard. Multichain Transaction Reverts. https://dune.com/flashbots/multichain-transaction-reverts
