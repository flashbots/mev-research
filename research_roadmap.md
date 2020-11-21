# Flashbots Research Roadmap


## Phase 1: MVP Systems Description / Ethical Structure (Nov 20 - March 21)
Phase 1 is practical/ultra-applied research akin to 'industry' R&D, in close loop with development.
We expect Flashbots developers to be heavily involved in this phase.
</br> Phase 1 has 2 research papers as a deliverable. Phil Daian will by guiding the outline, goals and high-level questions related to these papers. The outcome of Phase 1 is immediately relevant to providing MVP and communicating our intentions to the community. We expect to be able to describe the remainder of the research roadmap in-depth in our first research document under 'Future Work'.


### Paper 1: Whitepaper / proof-of-concept

**Paper style/field:** Cryptocurrency systems paper, short paper/PoC (9pgs)
</br> **Similar papers:** bloxroute, Thunderella, FlyClient
</br> **Venue:** FC22?  USENIX?

**Research question:** How can we build a "good" auction mechanism for validator priority "bribes"?
- "Good":
  - Gas efficiency for community
  	- Measure: gas saved with perfectly efficient arbs, gas currently wasted on-chain
  - Network overhead for community
  	- Measure: current arb-bot network overhead, full node bandwidth wasted
  - Prefer off-chain computation whenever possible for equivalent security
  	- Formalize trade-off between on-chain / off-chain arb computation
  		- Is there any computation we should move off-chain (into bundle processing/switching)?				
  - Efficiently express preferences of all network actors
  	- Enumerate current arb use cases, show that system covers all of them
  	- Discuss trade-offs in order type complexity vs. latency
  - Permissionless: no KYC / ad-hoc trust required in design
  	- Create security criteria for users not needing to trust miners/pools in PGA
  	- Enumerate where current design falls short, impliations of shortcomings
  - Better for miners unilaterally than vanilla Geth
  	- Measure miner latency: assuming both no Flashbots txs / saturation
  	- Measure required resources on miner side
  	- Measure latency penalty of minimal viable switching algorithm [critical]
  	- Academic definition for "strictly dominating" client in game theory?

**Research question:** How can we leverage existing auction literature?
- Survey: ad auctions / other priority bidding games.  Known pathologies / design trade-offs
- Discuss traade-off of first vs. second price auction, continuous vs. discrete auctions
- Mempool auction theory?

**Research question:** How does architecture differ across chains?  PoW/PoS/leaderless/other?
- Hypothesis: architecture is general and will allow for priority in all systems
- Measure percent of hashpower / probability of success for PoW / PoS, leaderless protocols

### Paper 2: Ethical / community charter
**Purpose**: Intended to open discussion, describe future goals, elicit community priority

**Research question:** Should we build a "good" auction mechanism for validator priority "bribes"?
- Open question: what is state-of-the-art in discussion on parasitic vs. helpful arbitrage / "MEV"
- Open question: what are market designs that synergize with Flashbots / provide benefits to users other than arbers

**Research question:** How do we minimize possible user harm of priority bribe incentives?

**Research question:** How do we minimize possible consensus harms of priority bribe incentives?

**Resarch question:** Should we allow for any MEV on the system?  Should we bound the MEV?

**Engineering question:** What kind of transparency should we allow?  Fully transparent MEV portal?
- Who leads?  Need firm commitment to develop, keep public.

### Paper 3: Clockwork Finance - Toolkit for understanding MEV [Cornell Research]
**Research question:** how do new contracts measure their own MEV?  Formally, what determines and affects MEV?
</br> **Artifacts: "MVP" tools for measuring, calculating, and reasoning about MEV.**



## Phase 2: Ethical Consideratons / Community Goals

**Paper style/field:** CS ethics / social sciences paper, short paper (10-12pgs)
</br> **Similar papers:** On the Moral Character of Cryptographic Work, Will the Market Fix the Market
</br> **Venue:** IEEE S&B?  Ledger journal?
</br> **Potential Collaborators:** Ethereum Foundation?  Community call?  Other MEV projcts?


**Research question:** How can we build fair markets for users?

**Research question:** What is fair ordering
- Support work like https://eprint.iacr.org/2020/269 with a grant?
- Implement similar systems?  Industry partnerships?  Internal definitions?


- Continue exploration mapped out by Phase 1>>Paper 2
- How can we create a robust organization to support our aims of commons infrastructure?
- Depends on MVP gaining traction

## Phase 3: Refinements and Product Implications

**Paper style/field:** CS systems / systems security
</br> **Similar papers:** ??
</br> **Venue:** ??
</br> **Potential Collaborators:** ??

Continue exploration mapped out by Phase 1>>Paper 1
Derive list of metrics to collect from deployed product
Depends on MVP gaining traction

## Phase 4: Long-Term Game Theory and Profit Distribution

**Paper style/field:** CS / econ, computational economics
</br> **Similar papers:** quadratic voting, ad auctions
</br> **Venue:** EC?
</br> **Potential Collaborators:** ??

**Research Question:** What does value capture / extraction look like in an auction-based ecosystem?  Compared to defi as a whole?

**Research Question:** How best to distribute profits?
- Incentive alignment between miners, users, defi developers, etcetc.

**Research Question:** How best to hold the auctions?


## Phase 5: ???

To be determined after MVP phase


