---
id: 43
title: Can Sandwich Attacks Benefit Their Victims?
team: @benber86
created: 2024-03-28
status: active
---

# Can Sandwich Attacks Benefit their Victims?

Sandwich attacks have caused millions of dollars of losses to unsuspecting traders and an equivalent amount of revenue to attackers. They are commonly perceived either as nefarious and akin to theft, or at most, a form of arbitrage, yet one that lacks the typical arbitrage benefit of correcting price discrepancies between markets. Yet, on rare occasions, some sandwich attacks do seem to generate better results for their victims when, in periods of high volatility, they give their victims faster execution and thus a better price.

## Background and Problem Statement

Sandwich attacks[^1] -- in which an attacker targets a victim's swap by frontrunning it to manipulate the price before backrunning it to generate a profit -- are one of the most common form of MEV on Ethereum. Sandwiches generate over $1 million in daily revenue.[^2]. Because the revenue comes directly from the difference between the victim's original execution price and their specified lowest acceptable price (slippage), any revenue from sandwiches means an equivalent loss for the trader. Since sandwich attacks first made their appearance[^3] over 5 years ago, they have been extensively studied[^4][^5][^6][^7] and several mitigation methods have been put forward. 

Most of the research on sandwiches is concerned with ways to eliminate them as they are seen as a largely nefarious activity and a "conceptual flaw"[^7] of decentralized exchanges using an automated market maker design. A survey[^6] on users' perception of sandwich attack found that individual traders perceive sandwich attacks as malicious or at best an acceptable form of arbitrage -- but one that does correct price asymmetries. Some traders also identify a benefit to sandwich attacks in that they can teach users a valuable lesson about slippage as well as foster innovation and the creation of new mitigation mechanisms. However, few would argue that sandwiches can be financially beneficial to the victims.

Yet one can easily find multiple examples of on-chain sandwiches where, by getting sandwiched, the victim seemingly gets a better price as their transaction benefits from faster inclusion. This is more commonly observable during periods of high volatility where a large number swaps on the same pool and in the same direction happens within a short timeframe and often within the same blocks. By being executed upstream from all the subsequent trades as part of a sandwich, the victim's transaction benefits from a more favorable price than they would have received had it been in a later position. This can translate into a financially positive outcome for the victim if the higher price allows the transaction to be executed when it might otherwise have reverted for failing to meet the specified slippage threshold, leaving the user holding an asset that continues to depreciate (in the case of a rapid sell event). 

One might, however, argue that the gains are illusory as the same or a better outcome could have been achieved if the victim had set more optimal gas settings. We intend to further explore the efficiency of sandwiches loss as a fee for an external gas optimisation and the relationship between slippage and gas settings.

## Plan and Deliverables

### Plan
- Start with a data collection phase where we use heuristics to detect such profitable sandwiches on one major DEX at first.
- Based on analysis of the different examples collected, outline the main mechanisms by which sandwiches can result in apparent positive outcomes for the victim and draw up a typology.
- Formalize and model the different case encountered, accounting for gas costs, DEX fees, AMM models and slippage settings to more precisely outline the conditions and the definitions of profitability under which sandwiches can be profitable for the victim.
- Enhance our detection algorithm and expand it to other DEXes.
- Quantify the volume and prevalence of these sandwiches on Ethereum mainnet.

### Deliverables
- Datasets of profitable sandwich transactions, including metadata and classification from our typology and optimal gas settings that would have ameliorated the risk of being sandwiched in these transactions.
- In-depth blog article presenting our methodology, analysis and key findings.


[^1]: L. Zhou, K. Qin, C. F. Torres, D. V. Le, and A. Gervais, "High-frequency trading on decentralized on-chain exchanges," in _42nd IEEE Symposium on Security and Privacy_, SP 2021, San Francisco, CA, USA, 24-27 May 2021. IEEE, 2021, pp. 428–445. [https://doi.org/10.1109/SP40001.2021.00027](https://doi.org/10.1109/SP40001.2021.00027)
[^2]: https://eigenphi.io/mev/ethereum/dailyReport
[^3]: https://medium.com/@Prestwich/mev-c417d9a5eb3d
[^4]: Guillermo Angeris, Alex Evans, and Tarun Chitra. 2021. "A Note on Bundle Profit Maximization". [https://angeris.github.io/papers/flashbots-mev.pdf](https://angeris.github.io/papers/flashbots-mev.pdf)
[^5]: Canidio, Andrea and Fritsch, Robin, 2024. "Arbitrageurs' profits, LVR, and sandwich attacks: batch trading as an AMM design response", Papers, arXiv.org. [https://arxiv.org/abs/2307.02074](https://arxiv.org/abs/2307.02074)
[^6]: Ye Wang, Patrick Zuest, Yaxing Yao, Zhicong Lu, and Roger Wattenhofer. 2022. "Impact and User Perception of Sandwich Attacks in the DeFi Ecosystem. In Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems" (CHI '22). Association for Computing Machinery, New York, NY, USA, Article 591, 1–15. [https://doi.org/10.1145/3491102.3517585](https://doi.org/10.1145/3491102.3517585)

[^7]: Andreas Park, 2023. "The Conceptual Flaws of Decentralized Automated Market Making," _Management Science, INFORMS_, vol. 69(11), pages 6731-6751, November. [https://ideas.repec.org/a/inm/ormnsc/v69y2023i11p6731-6751.html](https://ideas.repec.org/a/inm/ormnsc/v69y2023i11p6731-6751.html)
