# FRP-6: Literature review of auction mechanism that fit in with Flashbots.


**MEV Fellow:** @sbaks0820
</br> **Status:** Draft
</br> **Updated:** 24.11.2020

### Abstract
This proposal goes hand in hand withe FRP-1: How can we build a "good" auction mechanism for validator priority "bribes"? 
Part of determining what a "good" auction should is undertsanding the current literature on auction theory as well as places where such auctions
are in use. ???

### Motivation
Flashbots is designing an open block-space auction mechanism for transaction priority to capture existing MEV. In order to understand how to design
such an auction it is crucial to understand current auction theory, current auction appications, and, *most impotantly*, their limitations. 

### Defining the Research Question

To design an auction mechanism, the first step is to define a security model for how actors behave, what their capabilities are, and whether they can collude. 
It is necessary to first define a model for how participants behave as that motivates particular design choices over others. 
Other relevant questions arising from a clear model definition:
* Do current auctions designs in practice, such as those in digital adauctions, suffice for our purposes?
* Can we leverage existing auction literature to design a "good" auction mechanism that fits with flashbots?
* Which auction mechanisms have optimal strategies that participants are able to even compute? (see Betting on Permutations)
* In the current POC version, the bundle auction favors small bundles. What is the full impact of this design?
* Do some auctions mechanisms assume non-malicious participants (gain utility by hurting other participants, dos the auction, ???)?
* Which auction mechanisms allow for collusion between participants?
* Which auctions mechanisms are efficient enough for miners to run between mining blocks?

#### Related research questions
FRP-1

### Resource List
* [This great response by Tarun Chitra on an MEV Auction proposal](https://ethresear.ch/t/mev-auction-auctioning-transaction-ordering-rights-as-a-solution-to-miner-extractable-value/6788/3)
* [digital add auctions paper](https://arxiv.org/pdf/1610.03013.pdf)
* [another real-time bidding paper](http://wnzhang.net/share/rtb-papers/repeat-auction.pdf)
* [Prior attempt at a fee market for Ethereum](https://arxiv.org/pdf/1901.06830.pdf)
* [Algorithmic Game Theory bible (especially chapter 11)](https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf)
* Here is the POC version of the bundle auction: Flashbots miners select the most valuable bundle per unit of gas used and place it at the beginning of the list of transactions included in a block at the given blockheight. Miners determine the value of a bundle based on the following equation where the change in block.coinbase balance represents a direct transfer of ETH through a smart contract.
![Alt Text](https://user-images.githubusercontent.com/15959632/99228128-7c883b00-27ec-11eb-8b95-3896b21e0b08.png)

### Proposed Deliverables
* Develop a taxonomy to make it easier to reason about auction mechanism in the cotext of the Flashbots/crypto ecosystem.
* Develop early thoughts around mempool auction theory.


### Proposed Methodology 
Read relevant papers on: auction mechanisms for ad auctions, auction mechanisms that allow collusion between participants, and theoretical combinatorial auctions mechanisms or auctions on permuatations. 
Work with FRP-1 to define what auctions mechanisms we want to consider (i.e. which are deemed to be "good") and use the developed taxonomy to narrow our search space of auction mechanisms.
Finally, consider the current Proof-of-concept implementation and the "ideal implementation" and determine whether there are significant theoretical differences in the two to warrant radically different auction designs.
If so, this is an even more interesting problem that is worth exploring and might motivate whether it's better to auction large bundles (all txs in a block) or small bundles for priority in relation to other transcations.
