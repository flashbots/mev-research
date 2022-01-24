---
id: <leave blank -- will be assigned by reviewers>
title: Auction decison using AI
team: @avibrahms
created: <date created on, in yyyy-mm-dd format>
---

# Auction decison using deep learning approach

The goal of this FRP is to improve the auction mechanism using deep learning. Recent breakthroughs in auction mechanisms have been achieve through deep learning and the purpose of this research is to extensively survey the deep learning approaches to auction mechanisms in general. Devise at least one mechanism applicable to Flashbots auctions, implement and test the viability of such a solution, and compare the results to Flashbots current first-price sealed-bid auction mechanism as well as the classical mempool auction mechanism. 

## Background and Problem Statement
While the current auction mechanism is satisfying miners as well as for searchers, it has some limitations:
  * searchers still have to compete on a traditional auction fashion for bundles inclusion.
  * Relays need to compute a full simulation to calculate bundle fees and this is ressource intensive.
  * miners may benefit from a higher fee reward while searchers could further optimize their cost

## Plan and Deliverables
Describe the planned approach to the problem, including potential time allocations and partitioning into phases. List the artifacts or intended deliverables of the proposal.

## References
https://ieeexplore.ieee.org/document/9120521
  
https://cacm.acm.org/magazines/2021/8/254315-optimal-auctions-through-deep-learning/fulltext
