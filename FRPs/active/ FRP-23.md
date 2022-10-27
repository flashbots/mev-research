---
id: 23
title: Welfare, AMMs and MEV
team: @nikete @BrunoMazorra @sxysun1
created: 2022-10-18
status: active
---

# Welfare, AMMs and MEV

## Background and Problem Statement

Automated Market Makers, in particular those structured around CFMMs, create a substantial part of all MEV.

Under specific models of utilty funcitons, stochasticity, and AMM structure some welfare analysis of a AMM is posible. For LMSR and related AMMs over bianry assets, this is done in  [Interpreting prediction markets: a stochastic approach](https://proceedings.neurips.cc/paper/2012/hash/41a60377ba920919939d83326ebee5a1-Abstract.html) and the related literature.

The goal of this FRP is to study a simple model of how a CFMM can provide welfare. To do this, first establish the ideal case where all trades can happen simultaneoulsy at the walrassian equilibrium (WE) prices and allocations. Given this benchmark WE utiility, then the study of how much of that utility can be recovered in the sequential case by a given CFMM, is closely related to the concentration of measure of a suitably defined random variable that expresses liquidity being provided and utiltiy being obtained by each sequential trader.


## Plan and Deliverables

Analize  a pure endowments economy, a baseline case with a stochastic endowments Walrasian Equilibrium and compare it with agetns sequentially interacting with a CFMM AMM. 

Consider the welfare properties of CFMM AMMs, the MEV that can be extracted and the welfare losses caused by it's extraction. 

Deliverables: a blog post with a summary of the findings and design directions, a colaborative research paper.



## References

- [Interpreting prediction markets: a stochastic approach](https://proceedings.neurips.cc/paper/2012/hash/41a60377ba920919939d83326ebee5a1-Abstract.html)
- [Flashboys 2.0.](https://arxiv.org/pdf/1904.05234.pdf)
 
