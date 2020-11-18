# FRP-2: Negative Externalities and Bot Metrics Around MEV

**Fellow:** Alejo Salles
</br> **Contributors:** @bogatyy, @andrei-anisimov, @austin-williams, @gakonst
</br> **Status:** In Progress
</br> **Type:** Data collection & analysis
</br> **Updated:** 18.11.2020

**Simple summary:** 
</br> Data collection and analysis of Ethereum data using Flashbots monitoring infrastructure in order to 1) quantify the negative externalities caused by current techniques used for MEV-extraction and 2) quantify the related current trading bot activity on Ethereum.

**Motivation:**
</br> Flashbots is building an open, transparent sealed-bid block space auction mechanism for communicating transaction order preference in order to mitigate the negative externalities of current MEV extraction techniques. In order to better understand whether the Flashbot spec would improve the state of the network, it is important to first have a strong grasp of the current network impact of MEV extraction.

**Proposed deliverable:**
* Graph of gas wasted over time
* Percent of blockspace wasted over time
* Breakdown various protocols by gas/arb usage
* Gas/arb usage vs. MEV profits
* Upwards pressure on gas price?
* Competition: # of bots per opportunity
* From bot perspective: wasted efficiency for each bot (how often failing / burning gas vs succeeding)
* Gas wasted conditioned on various events? e.g. certain auctions / rebases
* How to exhibit spikes? Delays?
* Backrunning / types of arbitrage? Breakdown by category?
* Breakdown of arbs by protocol across all arbs
* Validation against other dashboards? e.g. this one 
* Breadth of analysis: What % of these are covered by inspectors?

**Proposed Approach:**
</br> Bottom-up approach of mechanical inspection of the Ethereum blockchain. This inspection is executed with simple scripts that scan Ethereum call and trace data. This essentially provides us with a lower bound estimate that becomes more accurate as the mechanical inspection efforts become more fleshed out.

**Resources:**
* https://github.com/pdaian/flashboys2/tree/master/go-ethereum
