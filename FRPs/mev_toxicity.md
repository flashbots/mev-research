---
id: <leave blank -- will be assigned by reviewers>
title: On the qualification of MEV toxicity
team: @IlluvatarEru, @0xpanoramix
created: 2022-10-18
---

# On the toxicity classification of MEV

Is all MEV toxic?<br>
How do we define toxic vs non-toxic MEV? <br>
Can we detect toxic MEV and eventually quantify it?<br>
Can we monitor it? <br>
These are questions asked by many but where answers are hard to give.
In this research, building on [[1]](https://writings.flashbots.net/research/quantifying-rev) we aim to come up with a detailled taxonomy of MEV transactions, from simple backrun arbitrages to sandwiches and liquidations.
We also aim to proposing a framework with definite formulas to quantify profit from MEV transactions and incurred losses for the targeted users.
This should allow further discussions on the topic of MEV toxicity while giving people a way to monitor and analyze it further.<br>

Who has never dreamt of seeing a breakdown of toxic vs non-toxic mev on the [Flashbots Explore Dashboard](https://explore.flashbots.net/)?<br>
We aim at improving `mev-inspect-py` by adding a flow classification into "toxic" and "non-toxic" categories.


## Background and Problem Statement

While everyone is discussing the toxicity of MEV, we don't have data to quantify this toxicity. Both MEV ecosystem agents and the general crypto public want to know more about this. While [[2]](https://info.zeromev.org/index.html) is giving some data about the recent blocks, we cannot see the toxicity up to date and the methodology and the code are not open source. We aim at delivering an open source, improved version of `mev-inspect-py` that the Flashbot team will be able to integrate into their explorer, backed by a serious work of qualification and quantification of MEV toxicity.

## Plan and Deliverables
Describe the planned approach to the problem, including potential time allocations and partitioning into phases. List the artifacts or intended deliverables of the proposal.

Plan:
- Definition of precise formulas to qualify and quantify MEV transactions toxicity
- Fork of `mev-inspect-py` to add a qualification feature of toxic vs non-toxic MEV

Deliverables:
- Research paper
- Code of the forked `mev-inspect-py` with classification capacity

## References
- [[1] Quantifying Realized Extractable Value by Alejo Salles](https://writings.flashbots.net/research/quantifying-rev)
- [[2] Zero MEV by pmcgoohan](https://info.zeromev.org/index.html)