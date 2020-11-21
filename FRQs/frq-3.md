# FRQ-3: How Can We Leverage Existing Auction Literature?

**Fellow:** @sbaks0820
</br> **Contributors:** 
</br> **Status:** In Progress
</br> **Updated:** 18.11.2020

**Summary:** 
</br> A survey of ad auctions, other priority auctions games and computational game theory papers.
This is a survey of existing auction techniques and the beginning of a longer process of developing mempool auction theory.
We anticipate a lot of the existing literature can be disqualified given the assumptions they make, for example in the auctions
where there is no-collusion assumption from the auctioneer.

**Related research questions:**
* FRQ-1: How can we build a 'good' auction mechanism for validator priority 'bribes'? [link]
* FRQ-2: What does a formal mathematical definition of a 'good' auction mechanism for validatory priority 'bribes' look like? [link]

**Related issues**
* Survey of ad auctions/other priority bidding games. Known pathologies / design trade-offs
* Discuss trade-off of first vs second price auction, continuous vs discrete auctions
* Develop early thoughts around mempool auction theory
* In the current POC version, the bundle auction favors small bundles. What is the full impact othis design? 


**Resources:**
* https://arxiv.org/pdf/1901.06830.pdf
* https://arxiv.org/pdf/1610.03013.pdf
* http://wnzhang.net/share/rtb-papers/repeat-auction.pdf
* http://dosamobile.com/wp-content/uploads/2017/08/TwoAlternatives.pdf
* https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf (Chapter 11 on Combinatorial Auctions)
* Here is the POC version of the bundle auction: Flashbots miners select the most valuable bundle per unit of gas used and place it at the beginning of the list of transactions included in a block at the given blockheight. Miners determine the value of a bundle based on the following equation where the change in block.coinbase balance represents a direct transfer of ETH through a smart contract.
![Alt Text](https://user-images.githubusercontent.com/15959632/99228128-7c883b00-27ec-11eb-8b95-3896b21e0b08.png)


-----
**Proposed Approach:**
</br> It might be helpful to try to enumerate the assumptions that we can make for bidders in our context. 
Things such as budget constraints, participation in repeated games. I arrived at this paper from another RTB paper I was reading: http://wnzhang.net/share/rtb-papers/repeat-auction.pdf. 
It introduces this idea of Fluid Mean Field Equilibrium, which is a computationally feasible alternative to Bayesian equilibrium, for repeated auctions. 
It also makes some specific assumptions about bidders valuing each auction equally and their budget constraints. It think it could be promising direction.
