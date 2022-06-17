---
id: <leave blank -- will be assigned by reviewers>
title: The Dark Forest of Arbitrum
team: Waylon Jepsen, Evan Kim, and Estelle Sterret.
created: 2022-06-17
---

# Dark Forest of Arbitrum

This project aims to lay the groundwork for the theoretical formalization of MEV-related phenomena on the Arbitrum network. We will formalize the Fee Mechanism and evaluate the cost of censorship. Given some block space, how much does it cost to use all block space, allowing none for anyone else? Furthermore, we will formalize the transaction ordering mechanism and what economic incentives are relevant as this is critical to all MEV activity. Additionally, we will analyze the bridge mechanisms. There is a seven-day lock period for the ETH Mainnet-Arbitrum official bridge. This seven-day period allows anyone to contest a `fraud-proof.` If a fraud-proof is challenged successfully, the validator that submitted it will get slashed, rewarding the challenger. A successful challenge will not revert the whole block but just the single transaction. We will examine these impacts on time to finality and protocols that are market-making the bridge for a more liquid bridging period. Is there an analogy between the lock-up period and the futures? What multi-chain arbitrage results from this?

## Background and Problem Statement
  
The rules of the MEV game are well explored on the Ethereum Main-net. We aim to explore and formalize the rules of the MEV game of the layer two network of Arbitrum. 

## Plan and Deliverables
  
- We will complete a paper that will be made publically availible. We aim to submit the paper to the [Defi-Security](https://defi.security/)
  
Within the context of the Arbitrum network we will:
  
- Identify and formalize fee structures and transaction sequencers
- Derive closed-form equations for the cost of censorship from fee structures
- Attempt to identify dominant MEV strategies used the in the wild by examing public mempool and transaction history
- Examine multi-block Arbitrage phenomena in the contexts of varrying block times between main-net and arbitrum
- Evaluate the cost of oracle manipulation from Chainlink Price feeds and TWAP oracles

## References
- [Flash Boys 2.0](https://arxiv.org/abs/1904.05234)
- [Replicating Monotonic Payoffs Without Oracles](https://arxiv.org/abs/2111.13740)
- [An analysis of Uniswap markets](https://arxiv.org/abs/1911.03380)
- [Clockwork finance: Automated analysis of economic security in smart contracts](https://eprint.iacr.org/2021/1147.pdf)
- [An Empirical Study of Frontrunning on the Ethereum Blockchain](https://arxiv.org/abs/2102.03347)
