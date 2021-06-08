# Flashbots Research Areas

At Flashbots, we perform research along several lines related to MEV, its extraction, and other related topics. The following is a live list of the research topics that are ongoing or under consideration.

## Auction Design
At the core of Flashbots is an auction via which the prioritization of bundles takes place. Performing this auction off-chain allows for a more efficient MEV-extracting process, avoiding chain bloat and increasing gas prices. Having a good auction mechanism is key to Flashbots' mission. Many research questions are centered around this problem, like what should we specifically require of the auction mechanism, how the notion of "good" applies to the different actors in the system, which requirements can be satisfied by a good choice of the pricing formula and which require additional setup like cryptoeconomic incentives, etc. For a given set of mechanisms, analytic or numerical analyses should be performed to study their properties. As part of the research efforts, new questions will arise that will help us shape the auction at the core of Flashbots' infrastructure.

## Cryptographic Privacy
Flashbots Alpha does not provide privacy guarantees to the searchers, meaning miners could inspect their bundles to steal profit opportunities. Ensuring searcher privacy is however a key milestone in our roadmap. We are building a secure enclave (SGX) based solution for this, but are also performing research to ultimately do away with trusted hardware. Cryptographic methods like commit-reveal schemes, zero-knowledge proofs, or threshold encryption might help us build a fully private auction. 

## Cryptoeconomic Privacy
Aside from purely cryptographic solutions, another approach to ensuring auction privacy might come from properly aligning incentives. Designing a protocol where actors bond stakes which can get slashed upon misbehavior is one potential alternative up for further exploration.

## MEV in ETH 2
Ethereum is beginning its move to Proof of Stake, which will substantially modify the landscape of MEV extraction. It will soon no longer be miners who have exclusive transaction ordering rights, but instead validators will be in charge of picking and ordering transactions for inclusion. This will introduce several differences to how MEV extraction takes place. Knowing which validator will propose a block ahead of time, to name one change, might substantially modify the MEV landscape. Work is already underway to identify how these changes will affect the Flashbots system, to be ready to adapt once The Merge takes place.

## EIP-1559
Even sooner than Ethereum 2, a substantial modification to miner rewards will take place with EIP-1159, scheduled for the London hard fork set to occur in July. After this change, miners are expected to collect most of their revenue from block rewards as well as MEV extraction, with much less coming from transaction fees in the for of "miner tips". While the Flashbots system might continue operating without change, further investigation is needed to make sure the changes introduced by this EIP are gracefully accommodated by our system.

## MEV in L2
Another major development that is taking place in Ethereum these days is L2 solutions, where computation is delegated to off-chain systems which only log minimal data on chain which can be used to prevent fraudulent execution. These systems typically introduce transaction "sequencers" which get to decide the order of the transactions to be exectuted in the L2. We are currently exploring how MEV extraction in L2 systems will evolve, and how can Flashbots contribute to making it more efficient and fair.

## MEV Taxonomy
In a recent [research post](https://hackmd.io/@flashbots/quantifying-REV), we introduced nomenclature for a consistent quantification of Realized Extractable Value, taking into account the different actors in the system. This framework, however, doesn't consider the different sources of MEV, like liquidations, arbitrage, etc. In order to provide a complete picture of the MEV extraction landscape like we strive to do with our [MEV explorer](https://explore.flashbots.net/), it would be useful to build and maintain a taxonomy of the different MEV opportunities as they are exploited in the wild. Some of this work is already encoded in the inspectors underlying the explorer dashboard, but still lacking a more theoretical approach.

## Account Abstraction
It has been [pointed out](https://github.com/flashbots/pm/issues/24) that Flashbots could be used to achieve account abstraction, where transactions are initiated not by EOAs but by contracts. This idea is already being implemented by projects like [Tornado Cash](https://twitter.com/TornadoCash/status/1387067161542283265?s=20), it would be useful to understand the full potential and limitations of such an approach in order to assess whether Flashbots should build dedicated infrastructure aimed at this specific use case. 

## Protocol Design
While Flashbots' main focus is making MEV extraction more efficient to minimize negative network externalities, it has been widely pointed out that protocols and Dapps can do a much better job in preventing MEV in the first place. It would be interesting to understand to what extent common patterns in protocol design can be applied to minimize the amount of MEV available in the system.

## Search Optimization
Flashbots core provides an efficient communication channel between searchers and miners, but it is searchers who are in charge of finding the best MEV extraction opportunities. As part of our mission to democratize MEV extraction, we are interested in exploring the question of search optimization, where different approaches to systematically identifying MEV opportunities can be considered.

## Flashbots as Critical Infrastructure
Flashbots source code is now run by more than half the mining hashrate of Ethereum, making it a piece of critical infrastructure of the Ethereum network. More research is required around the implications of this, and on how can we guarantee a thoroughly secure and reliable operation. 
