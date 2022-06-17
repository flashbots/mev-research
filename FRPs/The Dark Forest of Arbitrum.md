---
id: <leave blank -- will be assigned by reviewers>
title: The Dark Forest of Arbitrum
team: Waylon Jepsen, Evan Kim, and Estelle Sterret.
created: 2022-06-17
---

# Dark Forest of Arbitrum
  
We will extend MEV theory by formalizing aspects of cross-domain MEV between Arbitrum One and Ethereum. We will evaluate potential MEV security threats by analyzing consensus properties, fee mechanism, and computation cost for Arbitrum One. We will also analyze Arbitrum One's plan to decentralize the sequencer by utilizing Chainlinks Decentralized Oracle Network (DON) and Fair Sequencing Service (FSS) Framework and what this implies for widely known MEV strategies such as arbitrage, sandwiching, and liquidations. We aim to show how MEV evolves on Layer 2 and provide mathematical formalizations supported by quantitative data analysis.
  

## Background and Problem Statement
  
This research paper aims to provide mathematical formulations to analyze cross-domain MEV between Ethereum and Arbitrum. Given the different mechanics and increased computational resources available on Aribtrum One, how will MEV evolve on Arbitrum One and between Arbitrum One and Ethereum? Are there MEV exploitable security vulnerabilities in this new landscape? How will MEV further develop as Arbitrum One continues to mature and decentralizes the sequencer via Chainlinks DON and FSS framework?

## Plan and Deliverables
  
We plan on completing the paper and submitting to [Defi-Security](https://defi.security/). Deliverables include the following:

- Mathematically formalize fee structures, cost of censorship, and transaction sequencers in context of cross domain MEV
- Chainlink price feeds secure collateral between multiple blockchains including Arbitrum One and Ethereum. Formalize this form of cross domain liquidation MEV
- Analyze mainnet block producer economic incentive to manipulate/censor Arbitrum One blocks and formalize Arbitrum One block production profitability
- Evaluate MEV opportunities with respect to Layer 2 price feeds (Chainlink Price feeds, TWAP oracles, and reserve spot price). How does faster asset pricing on Layer 2 affect MEV on Arbitrum One? Does a faster Layer 2 (and conversly cheaper gas fees) imply more arbitrage and thus more liqudity connectivity? 
- Evaluate MEV opportunities with respect to the official Aribtrum Bridge and more faster mechanisms such as Chainlink Proof of Reserve
- Identify dominant MEV strategies formalized earlier by quantitative data analysis on historical data
  

  

## References
- [Flash Boys 2.0](https://arxiv.org/abs/1904.05234)
- [Unity is Strength: A Formalization of Cross-Domain Maximal Extractable Value](https://arxiv.org/abs/2112.01472)
- [Clockwork finance: Automated analysis of economic security in smart contracts](https://eprint.iacr.org/2021/1147.pdf)
- [Replicating Monotonic Payoffs Without Oracles](https://arxiv.org/abs/2111.13740)
- [An analysis of Uniswap markets](https://arxiv.org/abs/1911.03380)
- [High-Frequency Trading on Decentralized On-Chain Exchanges](https://arxiv.org/abs/2009.14021)
- [The Blockchain Oracle Problem in Decentralized Finance—A Multivocal Approach](https://www.mdpi.com/2076-3417/11/16/7572)
- [TWAP Oracle Attacks: Easier Done than Said?](https://eprint.iacr.org/2022/445.pdf)
- [An Empirical Study of Frontrunning on the Ethereum Blockchain](https://arxiv.org/abs/2102.03347)
- [Quantifying Blockchain Extractable Value: How Dark is the Forest?](https://arxiv.org/abs/2101.05511)
- [Chainlink 2.0: Next Steps in the Evolution of Decentralized Oracle Networks](https://research.chain.link/whitepaper-v2.pdf)
- [Order-Fair Consensus in the Permissionless Setting](https://eprint.iacr.org/2021/139)
- [Building Scalable Decentralized Payment Systems](https://arxiv.org/abs/1904.06441)
