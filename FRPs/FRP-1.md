# FRP-1: How can we build a "good" auction mechanism for validator priority "bribes"? 


**MEV Fellow:** @fiiiu
</br> **Contributors:** @bogatyy, @andrei-anisimov, @austin-williams, @gakonst
</br> **Status:** Draft
</br> **Updated:** 22.11.2020

### Abstract

### Motivation
</br> Flashbots is building an open, transparent sealed-bid block space auction mechanism for communicating transaction order preference in order to mitigate the negative externalities of current MEV extraction techniques. In order to better understand whether the Flashbot spec would improve the state of the network, it is important to first have a strong grasp of the current network impact of MEV extraction.

### Defining the Research Question
</br> We want to build an open, transparent sealed-bid block space auction mechanism for communicating transaction order preference in order to mitigate the negative externalities of current MEV extraction techniques. What is the most optimal design to make this mechanism efficient? Which design will have the biggest positive impact on the state of the Ethereum network? This research questions aims to tackle all these questions by surveying existing academic literature, collecting data and analyzing it and thoroughly studying design trade-offs we are considering.

**Related research questions**:
* FRQ-2: What is a formal mathematical definition for a 'good' auction mechanism for validator priority 'bribes'? [link]
* FRQ-3: How can we leverage existing auction literature? [link]

**Related issues**
* Gas efficiency for community
  * Measure: gas saved with perfectly efficient arbs, gas currently wasted on-chain
* Network overhead for community
  * Measure: current arb bot network overhead, full node bandwidth wasted
* Prefer off-chain computation whenever possible for equivalent security
  * Formalize trade-off between on-chain / off-chain arb computation
  * Is there any computation we should move off-chain (into bundle processing/switching)?
* Efficiently express preferences of all network actors
  * Enumerate current arb use cases, show that system covers all of them
  * Discuss trade-offs in order type complexity vs latency
* Permissionless: no KYC / ad-hoc trust required in design
  * Create security criteria for users not needing to trust miners/pools in PGA
  * Enumerate where current design falls short, implications of shortcomings
* Better for miners unilaterally than vanilla Geth
  * Measure miner latency: assuming both no Flashbots txs/saturation
  * Measure required resources on miner side
  * Measure latency penalty of minimal viable switching algorithm [critical]
  * Academic definition for "strictly dominating" client in game theory?
  * Negative Externalities and Bot Metrics Around MEV

### Literature Review or List of Resource
  * https://github.com/pdaian/flashboys2/tree/master/go-ethereum


### Proposed deliverables
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


**Proposed Methodology & Implementation:**
</br> Bottom-up approach of mechanical inspection of the Ethereum blockchain. This inspection is executed with simple scripts that scan Ethereum call and trace data. This essentially provides us with a lower bound estimate that becomes more accurate as the mechanical inspection efforts become more fleshed out. 
Data collection and analysis of Ethereum data using Flashbots monitoring infrastructure in order to 1) quantify the negative externalities caused by current techniques used for MEV-extraction and 2) quantify the related current trading bot activity on Ethereum.

