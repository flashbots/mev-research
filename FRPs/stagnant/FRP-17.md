---
id: 17
title: Bundle Clashing Analysis
team: @ezetalamona @fiiiu
created: 2021-10-27
status: stagnant 
---

# Bundle Clashing Analysis
The aim of this proposal is to continue and deepen the work done in the [Bundle Clashing Analysis](https://hackmd.io/@flashbots/Hkd8iBP8u). Bundle merging is currently running at the MEV-geth level, but no analysis about “incompatibility” of bundles has been done after this implementation. We want to expand the previous analysis with a larger dataset and separating reads from writes (read after read is not incompatible, previous work used generic "accesses").

## Background and Problem Statement
One of the most important points that we want to approach within this research is to understand the current landscape of bundles in the relay. Having bundle merging available in the current system might have incentivized a change of behavior on part of our searchers. Given the chance to extract multiple opportunities by enabling bundle merging, they might have started submitting more incompatible bundles, which require a new analysis to be done, and this is one of the hypotheses that we want to test.

Detail of questions to covered in this FRP:
* What does the current landscape of bundles look like?
* How did bundle merging impact on bundles behaviour in the relay?
* What does the intersecting segment in "contracts touched" currently look like?
* Can we find any insight on the current landscape that may help us on further algorithms developments?

## Plan and Deliverables
The plan will be to develop a data analysis based on history data for a set of random equispaced blocks, to understand where the current “incompatibility” of bundles is taking place. The base analysis, as a start point, will consist on three different categories [(mirror as previous work done in the same topic)](https://hackmd.io/@flashbots/Hkd8iBP8u).

During the project we will rethink these categories, analyze which are the most useful ones and search for new alternatives.

1. “Target tx” bundles going after the same target transaction.
2. “Contracts touched” means which addresses state would have been changed by the different bundles.
3. “Compatibility” means whether processing pairs in different order would yield the same profit to the miner.

What’s the additional contribution for this study? In comparison with previous work:
* Running the previous analysis on a new different landscape with updated data.
* Use a larger dataset (previous work only used a few blocks).
* Different approach on data visualization techniques (from a data science background perspective).
* Revisit and propose new category analysis for "clashing hierarchy".
* Deep dive analysis on contracts touched: having a better understanding of the intersecting segment.
* New findings and insights on the topic willing to be shared.

The goal of this FRP is to come up with a data analysis markdown, answering all of the above questions. We aim at delivering a blogpost (short article published in our HackMD research publication) tackling this analysis with theoretical and conceptual introduction of the topic, description of the current landscape of the problem with status and characteristics of bundles in the relay, supportive graphs, quantitative analysis and respective conclusions.

## References
* https://github.com/flashbots/bundle-clashing-analysis
* https://hackmd.io/@flashbots/Hkd8iBP8u
