---
id: 22
title: Quantifying the Impact of Frontrunning and Randomness on UX
team: @awmacpherson
created: 2022-09-24
status: active
---

# Background and problem statement

## Background

Perhaps the most notorious monsters of Ethereum's dark forest are the frontrunners.[^frontrun] A *frontrun* on a pending transaction $t$ occurs when another agent with knowledge of $t$ extracts value by arranging for some other transaction to be executed before $t$, often to the detriment of the owner of $t$. This is possible not only because of network latency effects, but because transactions are not necessarily executed in the order they are received by a validator.

A related scenario in legacy finance is *stale quote sniping* in which, following a shift in an underlying market, a market maker's quote is taken at an unfavourable price before they are able to cancel it.[^budish] The MM's ability to avoid this execution path depends on how quickly it is able to get an order cancellation executed.

Both situations have similar features: a user calls a function on a shared database where, due to a *latency* — in real time (seconds) or chain time (gas) — other transactions or changes in external signals may occur between call and execution. If the call is visible to other agents during this delay, these events may be the result of adversarial actions. The user cannot be sure about the *machine state* in which their call will be executed, and hence the utility they will derive from the execution.

Much has been proposed to combat frontrunning: enforced "fair" transaction ordering,[^fair-ordering] pre-execution privacy layers,[^private-mempool] off-chain order books.[^0x] In the context of HFT in TradFi markets, attention has been directed to scheduling innovations like speed bumps[^speed-bump] and batch auctions of various frequencies.[^budish] Such designs aim to prevent or discourage a particular behaviour seen as harmful.

How can protocol or application designers choose between this panoply of solutions? While some ad hoc comparisons on empirical or theoretical grounds have appeared, there lacks a systematic method to evaluate solutions. What is missing is a **quantitative** framework for comparing the effects of execution latency on users in different contexts. 

## Problem statement

Suppose given the following data:

- A *function* $\mathcal{A}:\mathcal{I}\times\Theta \rightarrow \Theta$ of a *user input* $i\in\mathcal{I}$ and a *machine state* $x\in\Theta$. 
- A *utility function* $u:\Theta\rightarrow\mathbb{R}$ over state.
- A random $[0,\infty]$-valued variable $T$ called the *latency*.
- A random $\Theta$-valued process $\\{X_t\\}_{t\in [0,\infty)}$ called the *history*.

From these data we construct a *random function* $\tilde\{\mathcal\{A\}\}\_\{X,T\}(i)$ that accepts input $i$, waits a random amount of time $t\sim T$ and then executes $\mathcal\{A\}$ on $i$ and the random input $X_t$. Caller utility $U_{\mathcal{A},X,T}(i) = u\circ \tilde{\mathcal{A}}\_{X,T}(i)$ is then also a random function: the outcome of a randomly stopped stochastic process. The properties of this random function — e.g. expectation, variance — can be viewed as quantitative measures of the UX — utility, risk — of the function $\mathcal{A}$.

This leads us to the following questions:

1. Which properties of $U_{\mathcal{A},X,T}$ are interesting from a UX perspective? 
2. Which properties of $\mathcal{A}$, $X$, and $T$ correspond to which properties of $U_{A,X,T}$? How can application designers influence them?
3. How do existing financial applications shape up when evaluated against this list of properties? Can we design new applications with chosen sets of properties?

This project falls under the **protocol design** research topic. Since these models will touch on different scheduling algorithms, there may be interaction with [FRP-21](https://github.com/flashbots/mev-research/blob/main/FRPs/active/FRP-21.md).

# Plan and deliverables

## Plan

- Exhibit simple statistical models for utility of some functions from core DeFi applications, drawing components (for example price models) wherever possible from existing literature:

  - AMM (swap).
  - LOB (create order, cancel order, settle).
  - Overcollateralized lending (deposit, withdraw, borrow, repay, liquidate).
  - Any type of "one-time opportunity" such as an NFT mint.

- Derive formulas for elementary properties (moments, range) of utility distributions of these models.

- Evaluate models in the context of:

  - values of $T$ corresponding to three different scheduler algorithms (FIFO, batch, scheduled execution);
  - public and private execution (affecting the set of possible adversarial actions)

- Adjust general framework so as to admit all examples under consideration. Clarify any further structure that becomes apparent from the study.

## Deliverables

- A formal research article targeting publication in a mainstream academic journal or conference proceedings in the areas of DeFi, [crypto]economics, security, or market microstructure.
- Presentation at international conferences.
- Blog post aimed at a non-technical DeFi audience.

# References

[^frontrun]: https://medium.com/@danrobinson/ethereum-is-a-dark-forest-ecc5f0505dff
[^budish]: https://academic.oup.com/qje/article/130/4/1547/1916146
[^fair-ordering]: https://eprint.iacr.org/2020/269
[^private-mempool]: https://medium.com/flashbots/announcing-flashbots-protect-9e039e9f0aa3
[^0x]: https://www.0x.org/pdfs/0x_white_paper.pdf
[^speed-bump]: https://exchange.iex.io/about/speed-bump/
