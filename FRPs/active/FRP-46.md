---
id: 46
title: App-level MEV Capture - Lending Protocols
team: Anthias Labs - Specific team members include Charlie Ambrose, Aaron Xie, Aniruddh Yadav, Vasu Khanna
created: 2024-10-16
status: active
---

# App-level MEV Capture - Lending Protocols

## Background and Problem Statement
Apps, specifically lending protocols, provide a constant source of MEV that becomes a cost on liquidators and inevitably a missed opportunity cost on the end user of the lending protocol, both borrower and liquidity supplier. This is the case as liquidations inevitably create arbitrage opportunities in secondary markets as liquidators offload collateral inventory. What if that arbitrage value (MEV) could be re-captured by the protocol in some way? This creates better value capture for the protocol, or it could be redistributed to the liquidity providers, or it could be re-distributed to liquidators (which as a consequence allows liquidation incentives to be lower as liquidations would be theoretically cheaper, which would improve the borrower  experience). 
- Could you whitelist an in-house liquidator as first priority?
- Could you sell liquidations as orderflow to a private auction system?

Furthermore, on a related note, on-chain spot-orderbook-based decentralized exchange designs are slowly becoming clearer in the DeFi purview, especially with the rise of protocols like Hyperliquid and soon GTE on MegaETH among others. We believe that these will become popular liquidation venues for certain mature assets due to their improved price execution and capital-efficiency. But how can on-chain orderbook-based decentralized exchanges be designed in a way to avoid the toxic MEV pitfalls of traditional AMMs? From this question we can ask, how can lending protocols take advantage of these designs directly to capture liquidation value for users, making decentralized borrowing and lending more profitable and capital efficient for both borrowers and lenders? These are the key questions with which we want to frame this research: app-level liquidation MEV capture for lending protocols.

Our team at [Anthias Labs](https://anthias.xyz) cares about this research topic because it affects our partners and clients directly. For background, we are a boutique on-chain advisory firm focused on DeFi risk management and system design. We have worked on risk parameterization and / or risk monitoring with DAOs including Aave, Compound, Euler, Exactly and more. Separately, we also work directly with a few DAO ecosystems on ecosystem development. These clients include the Solana Foundation, the Uniswap Foundation, Arbitrum DAO, and Optimism Collective. 

We have helped our clients navigate asset depeggings, liquidation cascades, flash crashes, and more. This research will enable us to more effectively align the interests of the lending protocols we work with and their liquidity venues in a risk-adjusted manner. On a longer-term horizon, by aligning these interests, we can help lending protocols work with the most-optimized exchanges and avoid liquidity fragmentation. While this is not the initial goal of this research, it is another proponent for its value. The primary question now stands: how can apps, specifically lending protocols, capture MEV more effectively via processing liqudiations through on-chain orderbooks.


## Plan and Deliverables
As deliverables for this research, we plan to publish the research in a paper and share it to HackMD as well as present it at a Flashbots community event or at an upcoming conference. 

We are expecting the research process to take 6-8 weeks to complete. That timeline will be broken down somewhat like the following:
- **Weeks 1-2:** The state of on-chain orderbook exchanges: what is the state of order matching and pricing for the on-chain orderbook exchanges with the highest transactions occurring on a daily basis over the past 90 days. What are their matching algorithms and pricing mechanisms? How can these be optimized to tighten spreads and minimize any form of toxic flow? Quantitative analysis of transaction volume and frequency, average order size, bid-ask spreads.
- **Weeks 3-4:** Dive into data analysis around how liquidity flows impact profitably for MEV searchers. Primary sub-question: How can fixed liquidity terms for various on-chain orderbook exchanges be implemented, if necessary, in order to, again, minimize toxic flow, and provide a more profitable trade to the end user.
- **Weeks 5-7:** This period will encompass the bulk of the research in which we will take the previous weeks’ findings and begin to explore how lending protocols, specifically, can integrate directly with on-chain orderbook exchanges to enable app-level MEV capture that can lead to reduced liquidation incentives and better supply and borrow rates, which can increase capital efficiency and, thus, user demand for lending protocols that adopt the findings of this research. Quantitative analysis into liquidation frequency across a select variety of lending protocols, MEV bot activity, impact of MEV capture on liquidation penalties and more.
- **Week 8:** Culmination of the research process. Finalize the deliverable paper, and share with the Flashbots forum to get comments before publishing. Then begin planning the deployment process for the paper, and determine where it will be presented.
  
## References
- [Anthias Liquip Score: Measuring Liquidation Probability](https://github.com/anthias-labs/research/blob/main/Anthias%20Liquip%20Score%20Measuring%20Liquidation%20Probability.pdf)
- [Comparative Study of AMM Protocols](https://github.com/anthias-labs/research/blob/main/Liquidity%20Providers%20Taking%20Position%20of%20Volatility.pdf)
- [Illuminating Ethereum's Order Flow Landscape](https://writings.flashbots.net/illuminate-the-order-flow)
- [Order flow, auctions and centralisation II - order flow auctions](https://writings.flashbots.net/order-flow-auctions-and-centralisation-II)
- [Lissy: Experimenting with on-chain order books](https://arxiv.org/abs/2101.06291)
- [Oval by UMA](https://uma.xyz/oval)
