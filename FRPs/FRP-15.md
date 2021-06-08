---
id: 15
title: MEV in eth2 - inequality & attack vectors analysis
team: @obadiaa
created: 2021-06-04
status: pending
---

# MEV in eth2 - inequality & attack vectors analysis


## Background and Problem Statement
Following our [early exploration of mev in eth2](https://hackmd.io/@flashbots/mev-in-eth2), we've raised a few concerns we'd like to study further:
a) whether MEV amplifies and catalyzes oligopolistic dynamics in eth2
b) whether there are new vectors of attacks opened by properties of eth2 such as the change in leader selection

For a)
We'd like to look into two potential forces of inequality which map onto the actual reward process of both i) the protocol and ii) the "utility functions" of various players. For instance, pools manage to pay out mostly constant income, while solo stakers are much more at the mercy of assignment randomness. Meanwhile, larger players will necessarily over time benefit from earning more and activating new validators faster.

We'd like to use the evolutionary game theory (EGT) framework to study this more closely. We have three types of players that have very different dynamics: solo stakers, pools and exchanges. EGT specifies utility functions for each player type as well as population dynamics that govern the relative size of each population of types over time. There are possibly formal results to be found there but to start even simple simulations could be giving us clues as to how the oligopolistic dynamics mentioned in the post could play out.

For b)
Block proposers are known one epoch in advance in eth2 which may facilitate mechanisms such as deterministic multi-block MEV. There may be potential vectors of attacks opened by this possibility that warrant further study. In addition, the origin of MEV stems from the study of consensus security and we believe MEV in the context of finality should be explored further to understand if there are any analogs to time-bandit attacks in eth2.


## Plan and Deliverables
For a)
- write down a model and build out simulations based on EGT to verify whether oligopolistic dynamics would play out depending on:
  - initial conditions/initial population sizes
  - whether e.g. some types can extract MEV or not and whether there are economies of scale wrt MEV extraction (e.g. multiblock MEV)
  - system randomness

We propose to start with a simple model and to iterate on its complexity as we progress with our analysis.

For b)
- analysis of large validators controlling multiple contiguous slots
  - RANDAO manipulation
  - assess multi-block MEV and potential malicious behaviour that could arise from it (eg. oracle manipulation)
- study consensus security/finality threats that may arise from MEV (analogs to time-bandit attacks)

## References
- https://hackmd.io/@prysmaticlabs/finality
- https://notes.ethereum.org/@barnabe/rk5ue1WF_
- https://ethereum.github.io/beaconrunner/notebooks/naiveurn.html
- https://ethresear.ch/t/rng-exploitability-analysis-assuming-pure-randao-based-main-chain/1825
- https://twitter.com/tkstanczak/status/1396178139445927937?s=20
- https://twitter.com/samuelshadrach4/status/1401965712223064064?s=21
