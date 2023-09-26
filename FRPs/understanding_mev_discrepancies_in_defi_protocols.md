---
id: 
title: Understanding MEV Discrepancies in DeFi Protocols
team: @IlluvatarEru
created: 2023-09-26
---

# Understanding MEV Discrepancies in DeFi Protocols

&ensp; Flashbots provides a great estimate of how much total MEV has been extracted over time on the Ethereum network ([[1]](######1.)) and some snapshot data on protocol specific MEV.
However, there is no estimate of the different types of MEV by protocol, nor historical data. 
In this research proposal, we aim to build upon this foundation and delve deeper into the nuanced realm of Protocol specific extracted MEV and this by category of MEV.
By doing so, we seek to contribute to a better understanding of the evolving dynamics of MEV extraction in DeFi and offer insights that can inform future mitigation strategies and protocol design enhancements.



## Background and Problem Statement

&ensp; Are some protocols more prone to MEV than others? To which type of MEV specifically? Frontruns, backruns, sandwiches? 

These are questions asked by retail users everyday, they want to avoid toxci MEV and are looking for the safer protocols to use (though MEV is not the only factor to consider).
It would be interesting to study how MEV has impacted each of the major protocols and how it evolved over time, and this for different types of MEV transactions.
Do different protocols have different mechanisms that impact their proportion to be targeted by each MEV type?

The implications of our research are twofold. First, answering these questions can not only help users make informed decisions as to which protocol they can use or not, but also protocol developers to understand which mechanisms favor (or protect from) which type of MEV.
Second, our findings may contribute to ongoing discussions within the DeFi community about enhancing MEV mitigation strategies and improving the overall security and fairness of decentralized exchanges.

## Plan and Deliverables
We plan on following the below steps:
1. Get `mev-inspect-py` Ethereum historical data and relevant classification of MEV types
2. Find the main protocols involved over time
3. For each protocol, get quantity of sandwich/frontrun/backruns over time and associated stats (median MEV by tx or by volume for each type of MEV)
4. Explain the discrepancies obtained in step 3. if any by exploring the protocols mechanisms

### Deliverables:
1. A thread on the Flashbots forum giving updates on the research as it is being done
2. A research paper explaining the methodology and results
3. An open source software to run the analysis

## References
###### 1. [Flashbots Transparency Dashboard](https://transparency.flashbots.net/)
###### 2. [Flashbots Forum Post on the topic](https://collective.flashbots.net/t/do-we-have-mev-data-by-protocol/2464)