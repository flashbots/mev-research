---
id: 53
title: Empirical Analysis of CEX-DEX Arbitrage PnL with Bounded Liquidity
team: Fei Wu
created: 2025-07-15
status: active
---

# FRP: Empirical Analysis of CEX-DEX Arbitrage PnL with Bounded Liquidity

Existing empirical studies typically overestimate the profit and loss (PnL) of CEX-DEX arbitrageurs by using markouts calculated with CEX mid price. Building upon our recent work, this proposed research plans to conduct an empirical analysis to have a better estimation of the realized PnL of CEX-DEX arbitrageurs and the profitability of integrated searcher-builders by accounting for the cost of liquidity.

## Background and Problem Statement
This proposal is developed based on the “Arbitrage with bounded liquidity” topic in the Flashbots Research Problem Database and a very recent work we have achieved under the The Latest in DeFi Research (TLDR) fellowship program.

In our recent empirical work [1], by checking the markouts calculated with the CEX mid price around the slot time for all historical CEX-DEX trades for each searcher (identified from on-chain data using heuristics), we can empirically observe that markouts typically reach their highest point before they start to drop. In other words, we know when each searcher’s information advantage (alpha signal) typically maximizes before their profit is eroded by market impact, including the impact of their own hedge trade. And assuming that the searcher starts to hedge at this time point, markouts calculated with mid price provide an upper-bound estimation of arbitrage revenue and searcher PnL.

The problem with this methodology is that this (over)estimation does not account for the liquidity of the tokens and ignores the cost of hedge execution, i.e., slippage or price impact.

## Plan and Deliverables
Several ways come to my mind for now to approach this question. The plan is to explore all these approaches and compare the results to ensure that the results are robust.

1. Instead of using the mid price, we can use the implementation volume-weighted average price (VWAP). This would assume that the searcher hedges their position instantly, sweeping the CEX orderbook and experiencing the maximum slippage. By doing this, we should get a lower-bound estimation of arbitrage revenue and searcher PnL. By incorporating this lower-bound estimation with the prior upper-bound estimation, we have a better understanding of the value range of searcher PnL compared to having only upper-bound overestimation.
2. Aside from mid price or VWAP, we can also try to use time-weighted average price (TWAP) during the hedge window. TWAP should provide a more accurate estimation of the actual average execution price by accounting for part of the price impact (i.e., permanent price impact) incurred during the hedge window. Note that using TWAP does not capture the full price impact since we are essentially assuming that the hedge is executed in infinitely small slices such that these small slices do not incur any slippage (i.e., temporary price impact).
    
    To know TWAP, we need to know the hedge window. For low-liquid token pairs, this is easy to be derived from empirical observations in our prior work [1]. However, for high-liquid token pairs, we cannot directly derive from empirical observations. A possible solution could be to apply the Almgren‑Chriss model with some assumptions of searchers’ risk-aversion and calibrate it against empirical data to derive plausible bounds or a distribution for the hedge window.
    
3. We can also try to develop a hedge cost model and calibrate it against empirical data. This has been covered by [2], where the author modeled the hedge cost as quadratic (i.e., linear marginal cost) for low-liquid token pairs, which is also mentioned in the Almgren–Chriss model. For high-liquid token pairs, a simple and effective model could be that the hedge cost is linear to the trade size, i.e., the marginal cost is constant.
4. From our earlier discussion with top CEX-DEX searchers, we were informed that the arbitrage opportunity is highly competitive among searchers recently, and the bid they put for that opportunity (i.e., coinbase transfer alongside the transaction) is very close to 100% of their expected arbitrage revenue. Our empirical work [1] validated this by showing that, the margin SCP and Wintermute keep at their searcher level and not transferred to their builder is only 10-15%. Note that 10-15% is still an overestimation since the hedge cost is not considered. This can be translated into: the difference between the best markout and their bid value is essentially their estimation of the hedge cost based on their model. We can then reverse engineer and calibrate the above hedge cost models with this data, or apply regressions to fit a hedge cost model for each token pair and apply it to other searchers. 

With these approaches above, we should have deeper insights into CEX-DEX searchers’ realized PnL and integrated searcher-builder profitability.

**Deliverable**: A paper or a post on Flashbots Collective presenting the analyses and results

## References
[1] Fei Wu, Danning Sui, Thomas Thiery, Mallesh Pai. “Measuring CEX-DEX Extracted Value and Searcher Profitability: The Darkest of the MEV Dark Forest”. https://arxiv.org/abs/2507.13023. Accepted by AFT 2025.

[2] Christoph Schlegel. "Arbitrage with bounded Liquidity." *arXiv preprint arXiv:2507.02027* (2025). https://collective.flashbots.net/t/arbitrage-with-bounded-liquidity/5064
