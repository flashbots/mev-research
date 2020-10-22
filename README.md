# **Mission Statement [WIP DRAFT]**

This document may be used to:
* Onboard community members and give them context on who we are
* Share with the wider community in case of a leak before we go public 
* Align our thoughts in a concise and rigorous way which will be helpful in a lot of discussions we will be having

Structure:
* Context
* Flashbots
* Purpose
* Values
* Future of the organization
* Who
* Resources



---




## Context
Miner extractable value (MEV) is the name for the upper bound of the value block producers can extract by doing one or several of these 3 actions: censoring an external transaction, inserting their own transaction or ordering transactions within the block they are producing. While miners are best positioned to extract this value, it is typically extracted less efficiently (given gast costs) by DeFi traders and mempool snipers through priority gas auctions and backrunning strategies. There are several concerns with MEV extractions:

* MEV extraction by miners is a significant risk to consensus stability.

In systems with high enough MEV, the profit available from optimizing for MEV extraction can subsidize forking attacks of two different forms. The first is an undercutting attack that forks a block with significant MEV. The second is a time-bandit attack that forks the blockchain retroactively based on past MEV. 

* The competition for MEV extraction can lead to the development of information asymmetry at the infrastructure level.

The sophistication of trading strategies will naturally lead traders to collude with miners in order to secure the ultimate guarantee of transaction priority. Such off-chain bilateral miner-trader deals would endanger Ethereum’s perception as a fair transparent technological layer and would bring us away from the values Ethereum and DeFi were built on: open, permissionless and transparent technology infrastructure.

- Systematic MEV-extractive behavior can destroy valuable ecosystems built on top of Ethereum such as DeFi

MEV extraction can negatively impact the experience of users on Ethereum-based applications, for instance by consistently offering more slippage to Uniswap users. In addition, such behavior would lead to a lack of confidence in transaction settlement and could entice users and developers to go to more welcoming platforms.  

These concerns are not new and were pointed out more than a year ago in Flashboys 2.0 where the term MEV was coined. However, they have become more pressing today on Ethereum as DeFi’s explosive growth over the last few months has resulted in an abundance of profitable structural arbitrage trading opportunities (i.e. MEV). As a consequence:
* the money a miner can make from MEV is now significantly higher than the transaction fees a miner gets. Miners are now becoming economically incentivized to extract MEV. 
* Miners have started exploring DeFi and are becoming more aware of the profitable transactions they are including in blocks. 
* Several projects are focusing on MEV such as KeeperDAO, B Protocol and Phantom pool, accelerating different visions of Ethereum’s future.

Enter Flashbots..




## FlashBots
Flashbots is a block producer architecture that optimizes for MEV extraction in a fair, profitable, and efficient manner through a permissionless and privacy-preserving block space auction mechanism. We aim to align the incentives of traders, miners and developers and to ensure that any application built on top of Ethereum that creates value doesn’t cause significant consensus instability. We believe what we are building is applicable to Eth2.0, a multitude of Layer 2 solutions and other Layer 1 blockchains.

## Purpose
We would like to avoid what we see as existential threats for Ethereum listed above. 
We would also like Flashbots to enable several positive externalities including the alleviation of network congestion, a fairer value distribution that is accretive to Ethereum’s security, the acceleration of the transition to meta-transactions and smart contract wallets, the spark of a new way of designing Dapps with less surface for MEV extraction and the generation of community discussions around MEV. 

## Our Values
Ethical research and development
Dual-engine power from research and engineering
Sustainability
Simplicity in mind
Community involvement

## Future of the organization
Over the next few months, we will be releasing research and open-source the code of our proof of concept. We see this first phase as exploratory and a way for us to answer technical, economic and ethical feasibility questions related to the technology we are building. We believe the piece of infrastructure we are building is a public good and are treating it as such.
Over the longer term, should these questions of the exploratory phase be answered positively, we would like this organization to be dedicated to the many open research questions around this problem and are open to profit-seeking opportunities that will arise as long as they are sustainable, non value-destructive and let us compete on an even playing field with others. We envision a potential value capture mechanism that would redistribute that value to maintaining public infrastructure and subsidizing high quality essential research.

## Origin & Who
Flashbots started as a community effort and is the result of the work of many individuals who have chosen to lend their time and expertise to this important problem. 


## Resources