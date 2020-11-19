# FRP-5: Miner Guarantees Study

**Fellow:** Annica Research (?)
</br> **Contributors:** Jason, Scott, Stephane, Andrei (?)
</br> **Status:** 
</br> **Type:** 
</br> **Updated:** 18.11.2020

**Summary:** 
</br> Collecting relevant miner metrics and anticipating questions miners and mining pools considering adopting Flashbots would ask.

**Motivation:**
</br> Miners and mining pools tend to be risk-averse when it comes to changes to their infrastructure, both hardware and software. As mining operations are massive and capital intensive, every change needs to be carefully thought about since its impact can be significant.
With that in mind, it's only natural miners need convincing to run MEV-Geth, and more broadly adopt Flashbots, to get them over the mental and operational hurdle of having to change their system.
FRP-5 is a research proposal to that effect.

**Proposed deliverables:**
* Latency considerations: how low-latency can we make the system? What are unavoidable sources of latency? How to minimize latency?
* Other required resources for geth client. CPU? Network? DoS vectors?
* Theory for when miners should run client A over client B?
* Feasibility of A/B testing? What metrics matter?
* How to compare in limited trials?
* Measure miner latency: assuming both no Flashbots txs / saturation
* Measure required resources on miner side
* Measure latency penalty of minimal viable switching algorithm [critical]
* Academic definition for "strictly dominating" client in game theory?


**Proposed Approach:**
</br> 

**Resources:**
* Miner survey
