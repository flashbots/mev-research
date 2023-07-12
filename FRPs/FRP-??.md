# FRP-???. Do backrun auctions protect traders?

## Background and problem statement

A backrun auction is a type of order-flow auction (OFA)[^ofa] which through some mechanism associates a backrun execution to each order that arrives at a market. In an ideal world, backruns would exactly cancel out the market impact of trades, with the result that the execution price of an order does not depend on where it lands in the block; potentially a big UX win for on-chain trading venues. Such systems also enable schemes whereby the value extracted by the backrunner can be partly returned to the user (so-called "MEV rebates"), a meme which is only increasing in popularity.[^mevblocker][^backrunme]

This ideal scenario — where a backrunner's dominant strategy is to set the price to that of an external reference market with deep liquidity — is realised in the "thermodynamic limit" where there is an infinitely large pool of non-cooperating backrunners each with an infinitesimal chance to backrun a given trade. Of course, we know that in practice this is often far from reality.[^payload] This project will study how sub-ideal conditions lead to equilibria in which rational backrunners give bad pricing.

If a would-be backrunner knows he has a good chance of of securing more than one backrun in a block, then under the right conditions, setting prices unfavourable to traders has better EV than the reference price. A simple example: if there are exactly two trades in a block and backrunning is controlled by a single player (a monopoly), then that player's best strategy can be to use the backrun slot on the first transaction to frontrun the second. If the market is illiquid, this can apply even if the backrunner does not know the contents of trades in advance (for example because this information is concealed using cryptography[^secret]) and must set a single target price for the entire block. Introducing competition does not necessarily mitigate this problem: one can identify non-cooperative oligopolistic equilibria where powerful players consistently set unfavourable prices.

## Plan and deliverables

1. Precisely formulate and prove the claim made in the introduction: that in the event that each backrunning agent has a single trade horizon, their dominant strategy is to set the price to that of a liquid reference market.

2. Develop a taxonomy of backrun auctions in terms of the information and actions available to would-be backrunners once the slots have been allocated. Does the backrunner knows the number and contents of trades in the block, which trades they will backrun, or some function of these? Does the backrunner set a target price for each trade they handle or one for the whole block? 

   (The focus here is on the game given a possibly unknown allocation of backrun slots, rather than the mechanism of selection itself.)

3. Exhibit quantitative protocol-level conditions under which strategies to set prices unfavourably in the hopes of gaining favourable executions in the future are uneconomical.

The deliverables will be a paper discussing the findings and a shorter explanatory blog post aimed at a more general audience.

The results of this work have the potential to have real impact on the information-theoretic design of future trade protection and MEV rebate protocols, as well as providing novel tools for analysis of existing venues.

## References

- BackRunMe. A backrun auction by bloXroute. https://docs.bloxroute.com/introduction/backrunme
- MEV-share (Flashbots). https://docs.flashbots.net/flashbots-mev-share/overview
- OFAs by Quintus. https://collective.flashbots.net/t/order-flow-auctions-and-centralisation-ii-order-flow-auctions/284
- Blink (frontrun protection through fake transactions). https://docs.blinklabs.xyz/blink/
- FRP 22. Adversarial blockchain queues and trading on a CFMM. https://collective.flashbots.net/t/frp-22-outputs-adversarial-blockchain-queues-and-trading-on-a-cfmm/1269
- FRP 30. On MEV rebates and social welfare. https://github.com/flashbots/mev-research/blob/main/FRPs/active/FRP-30.md
- MEVBlocker. https://mevblocker.io/#faq
- Builder dominance and searcher dependence. https://frontier.tech/builder-dominance-and-searcher-dependence
- Backrunning private transactions with MPC. https://collective.flashbots.net/t/backrunning-private-transactions-using-multi-party-computation/1198
- EBV analytics. https://payload.de/data/

[^ofa]: https://collective.flashbots.net/t/order-flow-auctions-and-centralisation-ii-order-flow-auctions/284
[^mevblocker]: https://mevblocker.io/#faq
[^backrunme]: https://docs.bloxroute.com/introduction/backrunme
[^payload]: https://frontier.tech/builder-dominance-and-searcher-dependence
[^secret]: https://collective.flashbots.net/t/backrunning-private-transactions-using-multi-party-computation/1198

