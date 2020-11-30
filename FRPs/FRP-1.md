# FRP-1: How can we build a "good" auction mechanism for validator priority "bribes"? 

## FRP-1-1: Taxonomy of MEV Extraction Strategies (NECESSARY (?) FOR FRP-1-1)
* enumerate and classify MEV extraction strategies
* how many are currently covered by MEV inspect/frontrun.me?
* *relates to evaluation MEV inspect in FRP-1-2*


## FRP-1-2: Measure PGAs, other MEV extraction strategies, define and concretize measurement infrastructure (reliability and assumptions on data)
* Use current inspect tools to find PGA's and meaure:
* current gas cost of a single arbitrage (average) taking part in PGAs --> expect this to be a long tail distribution --> try to determine the entire distribution of bots being used --> validate long tail from measurement **FIRST**
* For each extraction opportunity how many bots are showing up? (which ones are easier to find and whether some relatioship can be determined based on the profitability of these opportunities) 
* General: evaluate assumption whether we are seeing lower/upper bounds with MEV inspect or something else entirely --> validate MEV inspect opportunities (*there is an issue in MEV inspect of arbitrage found when there isn't any*) --> **IMPORTANT: evaluate what assumptions an be made from MEV inspect** --> perhaps manual validation? (i think we have enough people involved to put them to work) --> **bring with Phil and stephane**
* in what way is MEV inspect different from frontrun.me? --> cross validation with MEV inspect
* ???

## FRP-1-3: Layer 1 vs Layer 2 tx ordering auctions
* TBD: discussion with Karl Floersch regarding MEV auctions in layer 2 (rollup, etc...)
* **TODO: update after meeting with Karl**

## FRP-1-4: "Good" should apply to different types of actors (bidders, miners, external projects that are impacted by it)
* Define "good" for each of the actors involved in the auction --> for some if may mean gas cost/failure rate, for other may mean negative externalities of MEV extraction, (what about for miners, what do they care about here --> auction can be run preferrably several blocks before the block being bid for 

## FRP-1-5: Finding solutions to objective functions delivered from FRP-1-3
*  be computationally efficient and optimal strategies should should be computabel re:bidding on permutations and other NP-hard results --> for NP-hard results are there heuristic functions that approximate good/strong strategies)




## Questions for clarification
* DEFINE: How to exhibit spikes? Delays?
* 


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
* How much gas is currentlt spent in PGAs (including failed bids) and can we design an auction mechanism that's cheaper?
* Is it easier to mitigate the negative externalities of MEV extraction in Layer 2 or Layer 1? Why? What about for more cost effective?
* Auctioneers can simply reject bids that don't fit its policy of "good" MEV extraction. Is there a better strategy or better auction that can prevent gas waste? Can the auction take into account utility of the auctioneer to select the winning MEV extraction?
* 
* FRP-X:

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
</br> Data collection and analysis of Ethereum data using Flashbots monitoring infrastructure in order to 1) quantify the negative externalities caused by current techniques used for MEV-extraction and 2) quantify the related current trading bot activity on Ethereum.
</br> Bottom-up approach of mechanical inspection of the Ethereum blockchain. This inspection is executed with simple scripts that scan Ethereum call and trace data. This essentially provides us with a lower bound estimate that becomes more accurate as the mechanical inspection efforts become more fleshed out. 


