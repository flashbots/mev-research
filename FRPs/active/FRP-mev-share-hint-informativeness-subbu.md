---
id: <leave blank>
title: How Informative Are MEV-Share Hints? Searcher Route Choice, Blind Bidding, and Retained Surplus on Flashbots Surfaces
team: Vishal Subbu (Lead)
created: 2026-03-27
---

## Summary

56.5% of 6,843 observed MEV-Share hint events reclassified as DEX- or aggregator-related after selector decoding, versus 0.9% under a naive surface parse. This suggests that the MEV-Share stream is substantially more strategy-relevant than it first appears and motivates a study of how searchers should route and price opportunities under heterogeneous information conditions.

MEV-Share exposes selectively revealed orderflow via hinted transactions, creating a decision problem for searchers: whether to route an opportunity through MEV-Share or private builder paths. This decision depends on three linked factors: hint informativeness, information leakage, and bid competitiveness. Preliminary observations from operator discussions suggest that refund-related settings may reduce competitiveness, introduce silent discard conditions when refund costs are not covered, and are treated as trusted or permissioned rather than guaranteed. At the same time, searchers emphasize that the primary source of edge lies in correctly estimating bid floors rather than relying on rebates.

Based on initial instrumentation, I hypothesize that aggregator-routed flow represents the largest underserved opportunity class on MEV-Share: extractable, but requiring strategy adaptation beyond standard AMM simulation. In contrast, ERC-20 transfer flow is expected to be structurally poor for MEV-Share routing regardless of hint richness. I further expect that refund friction is most relevant for mid-sized opportunities where refund transaction costs materially affect competitiveness.

This proposal studies how hint quality affects route choice, bid setting, and retained surplus. The methodology combines passive event stream instrumentation, selector decoding, opportunity classification, and comparative analysis of route-specific execution outcomes. The results aim to provide a framework for searcher-side decision-making and evaluate whether improved information quality reduces blind bidding behavior that contributes to blockspace inefficiency.

## Background and Problem Statement

Flashbots research has explored MEV market structure, orderflow auctions (FRP-20), and contingent fee mechanics (FRP-28), but less attention has been given to the searcher-side workflow problem: how to act under partial information and route-dependent tradeoffs.

MEV-Share introduces a new execution surface where searchers receive hinted transactions with varying levels of disclosure. This creates a fundamental question:

- When is MEV-Share routing preferable to private routing?
- How should bids be adjusted based on hint quality and leakage risk?
- How do refund mechanics affect competitiveness and execution outcomes?

Initial instrumentation suggests that the MEV-Share stream is far more strategy-relevant than a naive parse implies. Across 6,843 events:

- 54.6% classified as aggregator-routed flow
- 31.1% as ERC-20 transfer flow
- 7.5% true non-DEX residual
- 56.5% total DEX / aggregator-related flow after reclassification

This reclassification was performed by decoding function selectors and combining them with known contract-address mappings and calldata-pattern heuristics.

These findings suggest that a large portion of the stream contains actionable opportunities, but their usability depends on information richness and routing strategy.

This problem also connects to Flashbots' broader research agenda on scaling. Flashbots has argued that blind speculative search contributes significantly to blockspace waste. If better interpretation of MEV-Share hints allows searchers to reduce blind bidding and improve route selection, this could impact overall network efficiency.

A draft of this proposal has been posted for community feedback on the Flashbots forum and was featured in The MEV Letter #131.

## Research Questions

1. How informative are MEV-Share hints across different opportunity classes?
2. For which opportunity classes does MEV-Share routing improve retained surplus relative to private routing?
3. How should searchers adjust bid / max-floor logic as hint richness and leakage risk vary?
4. When do refund-related settings meaningfully impact competitiveness or induce discard risk?

## Hypothesis

- Aggregator-routed flow represents the largest underserved opportunity class on MEV-Share, requiring strategy adaptation beyond standard AMM simulation.
- ERC-20 transfer flow is structurally poor for MEV-Share routing regardless of hint richness.
- Refund friction has the greatest impact on mid-sized opportunities where refund costs meaningfully affect execution competitiveness.

## Plan and Deliverables

### Phase 1 (Weeks 1–2): Instrumentation and Data Collection
- Collect MEV-Share event stream data
- Store raw hinted events
- Extract hint richness features and metadata

### Phase 2 (Weeks 2–4): Classification and Taxonomy
- Decode function selectors
- Map known contract addresses
- Build opportunity classification system:
  - aggregator-routed flow
  - ERC-20 transfer flow
  - direct swaps
  - NFT / bridge / safe / sequencer
  - unknown classes

### Phase 3 (Weeks 4–6): Comparative Analysis
- Analyze hint richness vs opportunity class
- Estimate route-attractiveness proxies
- Evaluate simulation feasibility by class
- Identify leakage-sensitive vs leakage-tolerant classes

### Phase 4 (Weeks 6–8): Execution Quality Analysis
- Compare MEV-Share vs private routing where feasible
- Analyze refund-on vs refund-off configurations
- Compare heuristic bidding vs modeled bidding
- Estimate expected vs realized retained surplus

### Deliverables
- Public dataset and reproducible methodology
- Research post on Flashbots forum or arXiv
- Presentation at a Flashbots or community event
- Open-source instrumentation and analysis codebase

## References

- FRP-20: An Initial Approach to Order Flow Auction Design
- FRP-28: Contingent Fees in MEV Supply Chains
- Flashbots MEV-Share documentation
- Flashbots research writings on MEV and scaling
- Flashbots forum discussions on MEV-Share and searcher workflows
- 4byte.directory selector database
