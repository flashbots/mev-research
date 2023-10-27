---
id: <leave blank -- will be assigned by reviewers>
title: Design space for SUAVE applications in decentralized finance (DeFi)
team: Can Kisagun
created: 2023-10-05
---

# Design space for SUAVE applications in decentralized finance (DeFi)

Introduction of SUAVE as a blockchain that acts as a private mempool for Ethereum, offers an interesting design space for smart contract design, especially around DeFi / Decentralized Exchange (DEX) applications that can benefit from complex settlement logic and full or partial privacy. 

The goal of this FRP is to survey the potential application space in DeFi that can be enabled by privacy preserving smart contracts of SUAVE, identify improvement opportunities and efficiency gains for existing DeFi protocol that already have users and also explore whether that creates trade-offs with SUAVE’s intended purpose.

My current hypothesis is that while DeFi has been groundbreaking for retail users, it still lacks the sophistication to fully meet the demands and needs of institutional crypto traders. SUAVE enables certain properties such as pre-order privacy, potential increased post-order anonymity, private margin information, cheap order placement and cancellations (block based) that can finally make the ecosystem ready for more sophisticated players to enter. 

My methodology will be:

1) research trading products that will benefit from full or partial privacy of orders or any other information (margin positions), assess their applicability to DeFi

2) Research how existing DeFi products can be improved by full or partially private information

3) talk to industry players (potential users) to understand whether these products enabled by SUAVE in practice solve their needs and provide a gap analysis (target is institutional traders / trading desks etc.)

At the end of this FRP, I will be able to share a report / presentation on improvements SUAVE can offer to DeFi space and how ready the market currently is. I also plan to create a gap analysis to identify improvement areas that need to be addressed to supercharge DeFi as more tokenized real world assets (RWAs) are being introduced, growing the size of addressable DeFi market.

## Background and Problem Statement
DeFi is clearly the most valuable use-case that we currently have on public blockchains. However, DeFi still mostly targets retail users and lack the sophistication needed by larger institutional traders. We believe some of these gaps can be addressed with privacy features and intent based execution SUAVE enables on Ethereum.

It’s a significant inefficiency that crypto assets are easier, cheaper and more profitable to trade on centralized exchanges or trading desks where traders bear the risk of single point of failure (FTX - Alameda) or counter party risk (OTC trades still work on a counterparty trust model).

Furthermore, with the increasing adoption of tokenized RWAs, we can expect more assets / value and more sophisticated players to come to the DeFi ecosystem. The infrastructure we have at the moment is not enough to onboard this new wave of value creation.

SUAVE not only provides value in terms of returning MEV back to users but also creates a new design space for DEXs: SUAVE’s pre-execution privacy properties and ability to cheaply post / cancel orders provide significant benefits to institutional traders who will be instrumental for the growth of  DeFi. 

In traditional finance, there are certain trading products that are built primarily on full or partial information privacy. Order execution in markets with low liquidity and large block trades benefit significantly pre-order privacy. Some trading products enabled by this model is dark pools, OTC trading and auction based price determination. 

Limit Order book (LOB) based trading has been the dominant for of trading assets in traditional finance. Limitations due transactions fees and order cancellation latency has prevented LOB based trading to gain traction on Ethereum. Instead AMMs like Uniswap dominate the decentralize exchange (DEX) design space. With the emergence of L2, we are seeing experimentations with LOB DEXs. However that comes at the cost of liquidity fragmentation. We believe using Ethereum as the settlement layer will enable access to liquidity which is essential for the DeFi ecosystem.

This FRP will explore:

- What are novel DeFi primitives that can be enabled by private smart contracts on SUAVE?
    - Dark pools
    - Large block OTC trades
    - Treasury auctions
- What are existing DeFi tools that can be improved by private smart contracts on SUAVE (i.e. margin trading)?
- What are the requirements for institutional DeFi adoption and the path forward?
- What are the implications of a growing DeFi settlement ecosystem on the initial design parameters and intent of SUAVE?

## Plan and Deliverables
The goal is to create a blog post (potentially a research paper) with the summary of the findings of the FRP and present the findings either internally to Flashbot or in conferences. In this research process, I plan to focus on the following issues:

- Define a set of trading products enabled specifically by the pre-order privacy and partial privacy and assess their relevance to a growing DeFi ecosystem
- Thoroughly analyze and prioritize 2-3 of these trading products based on their relevance to DeFi, interview potential users and create a detailed stakeholder analysis to identify system / design requirements for SUAVE based smart contracts to attract DeFi usage
- Explore potential bottlenecks this approach can impose on MEV SUAVE design, which is primarily built to address MEV attacks.

In addition to sharing findings of this research with the MEV community, this FRP also aims to shed light on the design space for SUAVE based trading products, encourage further discussions and building in this space.

The FRP is expected to be completed in 2 months

## Future work
The goal of this FRP is to pave the way for a trading application ecosystem on SUAVE to flourish and allow Ethereum to be the settlement layer for a growing DeFi ecosystem that encompasses not only crypto assets, but also tokenized RWAs. This FRP can become the foundation on which trading products on SUAVE are being built.

## References
- https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8418612
- https://jumpcrypto.com/writing/searcher-limit-order-book/
- https://www.investopedia.com/terms/d/dark-pool.asp
- https://www.coindesk.com/business/2023/06/16/crypto-traders-flock-to-otc-markets-as-exchange-liquidity-dries-up-amid-regulatory-clampdown/
- https://www.schwab.com/stocks/understand-stocks/otc-stock#:~:text=in%20OTCs%20securities%3F-,What%20are%20OTC%20securities%3F,listed%20on%20a%20national%20exchange.
- https://www.investopedia.com/terms/i/icebergorder.asp

## Background
Can Kisagun is the co-founder and former Chief Product Officer of Enigma / Secret Network. During this time, Can explored different use-cases for privacy preserving smart contract Enigma / Secret Network built, including the design space for exchanges with pre-order and post-order privacy.
