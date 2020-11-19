# FRP-2: Negative Externalities and Bot Metrics Around MEV

**Fellow:** @fiiiu
</br> **Contributors:** @bogatyy, @andrei-anisimov, @austin-williams, @gakonst
</br> **Status:** In Progress
</br> **Type:** Data collection & analysis
</br> **Updated:** 18.11.2020

**Summary:** 
</br> Data collection and analysis of Ethereum data using Flashbots monitoring infrastructure in order to 1) quantify the negative externalities caused by current techniques used for MEV-extraction and 2) quantify the related current trading bot activity on Ethereum.

**Motivation:**
</br> Flashbots is building an open, transparent sealed-bid block space auction mechanism for communicating transaction order preference in order to mitigate the negative externalities of current MEV extraction techniques. In order to better understand whether the Flashbot spec would improve the state of the network, it is important to first have a strong grasp of the current network impact of MEV extraction.

**Proposed deliverable:**
</br> **Gas metrics**
* Graph of gas wasted over time
* Breakdown various protocols by gas/arb usage
* Gas/arb usage vs. MEV profits
* Upwards pressure on gas price?

**Bot metrics**
* Competition: # of bots per opportunity
* From bot perspective: wasted efficiency for each bot (how often failing / burning gas vs succeeding)
* Gas wasted conditioned on various events? e.g. certain auctions / rebases
* How to exhibit spikes? Delays?
* Backrunning / types of arbitrage? Breakdown by category?
* Breakdown of arbs by protocol across all arbs
* Validation against other dashboards? e.g. [this one](https://explore.duneanalytics.com/public/dashboards/FFFpCKoE41bvFpESiyjUIBJfEMt4GoMFwcidNcAh)
* Breadth of analysis: What % of these are covered by inspectors?

**Network metrics**
* Percent of blockspace wasted over time 
* What is the overhead of a single arb / PGA transaction?
* What is the overhead for a miner? What is the overhead for a full node? How do we measure waste?
* What happens to the p2p network / full nodes with much more priority auctions?
* How many (arb) txs broadcast first time in a block?
* How much worse is this in a stateless world? Or other proof-required-for-tx schemes?
* How many deletions? How many messages came in we already saw (duplication)?
* How spammy are various bots compared to other users? How much more duplication?


**Proposed Approach:**
</br> Bottom-up approach of mechanical inspection of the Ethereum blockchain. This inspection is executed with simple scripts that scan Ethereum call and trace data. This essentially provides us with a lower bound estimate that becomes more accurate as the mechanical inspection efforts become more fleshed out.

**Resources:**
* https://github.com/pdaian/flashboys2/tree/master/go-ethereum
