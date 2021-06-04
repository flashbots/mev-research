---
id: 15
title: MEV in eth2 - further analysis
team: @obadiaa
created: 2021-06-04
status: pending
---

# MEV in eth2 further analysis


## Background and Problem Statement
Following our exploration of mev in eth2, we'd like to focus on a few quantitative results to do further analysis on their significance.


## Plan and Deliverables
- does MEV encourage any unwanted dynamics in eth2?
  - oligopolic dynamics, wealth inequality, gini coefficient between validators
- anlysis of pool controlling multiple contiguous slots
  - RANDAO manipulation
  - assess multi-slot MEV and potential malicious behaviour
- study consensus security/finality threats that may arise from MEV (analogs to time-bandit attacks)

## References
- https://hackmd.io/@prysmaticlabs/finality
- https://notes.ethereum.org/@barnabe/rk5ue1WF_
- https://ethresear.ch/t/rng-exploitability-analysis-assuming-pure-randao-based-main-chain/1825
