---
id:
title: MEV Value Chains Across L2 Sequencing Designs
team: Ruizhe Jia (Stanford MS&E, Lead), Shihao Yu (SMU)
created: 2026-01-16
---

# MEV Value Chains Across L2 Sequencing Designs

Layer 2 rollups have become the dominant venue for DeFi activity, yet they operate under fundamentally different sequencing designs. We argue that block speed creates a spectrum of market structures: at one extreme, very fast blocks produce first-come-first-serve (FCFS) racing where arbitrageurs compete through latency; at the other extreme, slow blocks allow priority gas auctions (PGA) where sequencers extract rents through fee competition; in between, hybrid mechanisms like Timeboost blend both dynamics. Each point on this spectrum creates a different MEV value chain—determining how surplus flows among sequencers, searchers, liquidity providers, and retail traders.

We propose a combined theoretical and empirical study of how block speed and sequencing rules shape MEV distribution. Our core hypothesis is that block time determines where a chain sits on the FCFS-to-PGA spectrum. Very fast blocks (approaching continuous time) converge to the Budish (2015) world: winner-take-all speed competition, arms race investment in latency, and sophisticated LPs racing to withdraw liquidity before being adversely selected. Very slow blocks produce the opposite: price divergence accumulates between blocks, LPs cannot adjust intra-block, and arbitrageurs bid away their profits to sequencers through priority fees. The "Goldilocks zone"—if it exists—balances these forces: blocks fast enough to limit adverse selection, but slow enough to avoid wasteful speed competition.

Our methodology combines theory with a natural experiment. On the theory side, we model the strategic interaction between LPs and arbitrageurs under different block speeds. When a price discrepancy emerges, LPs want to "pull" their liquidity before being adversely selected, while arbitrageurs race to "snipe" the stale quotes. We derive how the probability of successful LP escape, equilibrium priority fees, and sequencer revenue all vary with block time τ. The model generates sharp predictions: as τ decreases, priority fees collapse toward zero (contests become rare); as τ increases, sequencer revenue rises but LP participation falls.

On the empirical side, Base's recent upgrade to Flashblocks provides a clean quasi-experiment. In July 2025, Base reduced block times from 2 seconds to 200 milliseconds—a 10x speed increase on the same chain, with the same participants and pools. This shift moves Base dramatically along the speed spectrum, from a regime where priority bidding matters to one approaching pure FCFS. We can measure how this transition affects arbitrage frequency, priority fee distributions, LP losses, and sequencer revenue—while using Optimism (which maintained its PGA design throughout) as a control for broader market trends.

Our study has limitations. The model abstracts from some complexity: multiple competing pools, cross-chain arbitrage, and builder centralization. Empirically, classifying addresses as "arbitrageurs" versus "LPs" versus "retail" requires heuristics that may misclassify some participants. We will document our methodology and test robustness.

The implications are practical. Results will help L2 designers understand the welfare consequences of block time choices and inform decisions about where to position their chains on the speed spectrum. For Flashbots, this work illuminates how MEV dynamics vary across the rollup ecosystem—showing that sequencing design, not just block production, shapes who captures value.

## Background and Problem Statement

Block speed creates a spectrum of market structures:

- **Very fast (τ → 0):** Pure FCFS. Speed determines priority. Arbitrageurs invest in latency infrastructure. Fast LPs can escape adverse selection; slow LPs cannot. Sequencer revenue from priority fees approaches zero.
- **Very slow (large τ):** PGA dominates. Price divergence accumulates between blocks. All LPs face adverse selection. Arbitrageurs bid away profits to sequencers through priority auctions.
- **Intermediate:** Hybrid dynamics. Some speed competition, some fee bidding. Mechanisms like Timeboost explicitly blend both.

Current L2 designs span this spectrum:

- **Base:** FCFS with 200ms Flashblocks (upgraded from 2s in July 2025)—now at the fast end of the spectrum.
- **Arbitrum:** Transitioning to Timeboost—a hybrid mechanism with express lane auctions.
- **Optimism/Polygon:** PGA similar to L1—closer to the slow end of the spectrum.

**Research questions:**
1. How does block speed determine where a chain sits on the FCFS-to-PGA spectrum?
2. What are the welfare consequences at different points on this spectrum?
3. What does Base's 2s → 200ms transition reveal empirically?

**Alignment with Flashbots research focus:** This project directly targets transaction ordering mechanisms and MEV extraction/distribution across rollups (cross-domain MEV).



## Plan and Deliverables

Time commitment: ~6 weeks full-time equivalent (or part-time over a longer period).
All work (intermediate notes, code, and write-ups) will be shared publicly throughout.

**Phase 1 (Week 1): Setup + measurement design**
- Finalize chain/pool selection and measurement definitions (priority fees, arbitrage events, LP losses, sequencer revenue)
- Build reproducible data pipeline and classification heuristics with robustness checks

**Phase 2 (Weeks 2-3): Theory**
- Model LP–arbitrageur game with block time τ as key parameter
- Derive predictions for how priority fees, LP escape probability, and sequencer revenue vary with τ

**Phase 3 (Weeks 4-5): Empirics**
- Base Flashblocks natural experiment: collect pre/post data (2s → 200ms)
- Compare against Optimism as a control to isolate speed effects from market-wide changes
- Test theory predictions; run sensitivity checks for address classification and pool selection

**Phase 4 (Week 6): Synthesis + dissemination**
- Consolidate results into a concise narrative for designers and researchers
- Prepare public artifacts and draft the blog post / preprint

**Deliverables:**
1. Research paper (theory + empirics)
2. Blog post for the Flashbots forum summarizing the findings
3. Public replication repository (code + instructions) under a permissive license
4. Presentation at a Flashbots community workshop/event (or a recorded talk if scheduling requires)

## References

- Budish, Cramton, & Shim (2015). The high-frequency trading arms race. *QJE*.
- Daian et al. (2020). Flash Boys 2.0. *IEEE S&P*.
- Flashbots (2025). Flashblocks Deep Dive. *Base Blog*.
- Arbitrum Foundation (2024). Timeboost. *Arbitrum Docs*.
