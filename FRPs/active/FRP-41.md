---
id: 41
title: Stackelberg Attacks and Miner-Extractable Value (MEV)
team: SSODelta 
created: 2022-10-11
status: active
---

# Stackelberg Attacks and Miner-Extractable Value (MEV)
## Background and Problem Statement

Smart contracts have the potential to alter the expected outcomes of known games. There are two defining properties that precipitate these altered equilibria. First, smart contracts allow players to commit to strategies irrevocably; contracts can self-execute the players’ strategies and, once set in motion, the players cannot meddle in their own strategy.  Second, smart contracts can condition on the content of other contracts.  This means that a player can not only condition on the actions another player executes, but on the content of their strategy, which is visible in those players’ smart contracts.  These two nuances taken together have the potential to change the equilibrium of a game.  In particular, the commitment to contracts induces a meta-game before the actual execution of the game actions in question, making for a more complicated and sometimes decidedly different game.  We note that the advantage always lies with the player with the first contract.

In our papers [2-3], we show that the transaction fee mechanism of most major blockchains (including EIP-1559) are amenable to these attacks. In [2], we considered a model where the users of the blockchain are given the capacity to deploy smart contracts, and showed that this enables the users to spontaneously collude against the miner, who loses most of their revenue as a result. However, this model neglects the fact that the miner essentially has full control over the transactions put on the block. This implies that the miner *de facto* has the first contract move, and thus the first mover advantage will be enjoyed by the miner and not some user.  

In particular, the contracts that constitute the attack must themselves be deployed on a blockchain and a savvy miner would block their deployment. The miner’s first mover advantage on one chain could be undermined by relocating the contracts that constitute the attack on to a different blockchain  Thus, we want to introduce two blockchains in order to model both the need for a second blockchain for the commitments as well as a second token for MEV arbitrage. The motivation for this is twofold: one, we wish to allow for trading of tokens to model the situation where the miner frontruns a good trade made by one of the users. However, this could also be modeled using a DEX-based model on a single chain. The other reason is to allow for agents other than the miner to potentially deploy contacts. 

We believe these second blockchain commitments would not be enough to counter the miner’s power and would in fact allow the miner to extract more value. This would constitute an inversion of the model we propose in [2].  Beyond countering the attack in [2], we suspect our model will show that, under these model conditions, miners will so completely extract the users’ utility that the blockchain will become effectively useless.  Expounding on our research of these attacks will further illuminate the underlying complexity of games on the blockchain and emphasize the care needed in designing good transaction fee mechanisms.

## Plan and Deliverables
* Give a simple formal model of MEV 
  * One that uses a DEX to model miner frontrunning.
  * One that has multiple different blockchains to prevent the miner blocking the commitment     
    * Model commitment devices as a [lattice](https://en.wikipedia.org/wiki/Lattice_(order))
* Analyze the models for possible Stackelberg attacks.
  * We conjecture that with perfect information, the miner can extract all value from the users.
  * Study collaboration in mining pools. 
  * Study competition among miners themselves.
  * Try different utility distributions (uniform, Pareto, exponential)
* Consider possible mitigations to Stackelberg attacks.
* Summarize the results as a research paper and possibly pursue publication. 
* Create community facing blog posts and/or presentations. 

## References
* [1] Model for Games with Smart Contracts: https://arxiv.org/pdf/2107.04393.pdf 
* [2] Stackelberg Attacks on Auctions: https://arxiv.org/pdf/2305.02178.pdf 
* [3] Stackelberg Attacks in General:  https://arxiv.org/pdf/2305.04373.pdf 
* [4] Related Model of MEV: https://arxiv.org/pdf/2208.13464.pdf
* [5] Censorship in On-Chain Auctions: https://arxiv.org/abs/2301.13321 
