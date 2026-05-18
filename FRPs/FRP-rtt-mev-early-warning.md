# FRP-XX: Network-Layer RTT as a Pre-MEV Signal: Empirical Evidence and Predictive Framework

**Status:** Draft  
**Authors:** Alexander Kent (Phoenix Zero)  
**Created:** 2026-05-19  

---

## Summary

We propose a research investigation into whether network-layer round-trip time (RTT) latency, measured at the sequencer level, constitutes a reliable leading indicator of MEV activity on L2 networks — specifically Base, Arbitrum, Optimism, and ZKSync Era.

**Hypothesis:** A measurable and reproducible RTT spike at the sequencer level precedes on-chain MEV activity (as measured by revert ratio and blob base fee) by 27–180 seconds, providing an actionable pre-MEV signal window.

**Empirical basis:** On May 17, 2026 at 23:29:43 UTC, our Phoenix Zero oracle detected a Base sequencer RTT increase from 52ms to 739ms (P99, 1-minute window). The on-chain revert ratio crossed 50% at 23:30:10 UTC — 27 seconds later. Peak revert ratio reached 61.36% at 23:39:35 UTC. This constitutes one documented, timestamped incident. This research aims to generalize this finding across a 90-day dataset.

**Methodology:** Correlate 90 days of continuous RTT measurements (2-second probe interval, `eth_blockNumber` calls, 4 chains) against on-chain revert ratio, blob base fee, and MEV bundle density from Flashbots MEV-Boost data. Quantify lead time distribution and false positive rate.

**Limitations:** Single oracle node (NYC region); measurement captures propagation latency only, not mempool state; RTT spikes may have non-MEV causes (CDN routing, validator maintenance).

**Implications:** If confirmed, RTT-based pre-MEV signals could enable DeFi protocols to implement automated circuit breakers, MEV-protected transaction routing, and risk-adjusted pricing — all triggered before on-chain evidence is available.

---

## Motivation and Background

MEV detection today is reactive: revert ratios, bundle data, and gas spikes are observable only after MEV activity has begun. The window between MEV bot activation and on-chain confirmation represents an unexploited signal layer.

Network-layer RTT to sequencer endpoints reflects the load on sequencer infrastructure during block production. During MEV storms, block builders submit competing bundles, increasing sequencer processing load and observable latency before transactions are finalized on-chain.

Prior work has focused on mempool-level signals (Flashbots MEV-Share, SUAVE) and on-chain data (revert ratio analysis). No published research examines raw sequencer RTT as a leading indicator.

**Research questions:**
1. Does sequencer RTT reliably lead on-chain MEV metrics, and by how much?
2. What RTT velocity threshold (rate of change) optimally separates MEV onset from noise?
3. Do cross-chain RTT correlations exist? (ZKSync P99 spike → Base congestion, +2–5 min)
4. What is the false positive rate at actionable thresholds?

---

## Relation to Flashbots Research Roadmap

This proposal relates to:
- **MEV supply chain measurement** — quantifying pre-block-production signals
- **L2 MEV characterization** — understanding MEV dynamics on Base, Arbitrum, OP
- **MEV mitigation** — enabling protocol-level defenses triggered before on-chain confirmation

---

## Planned Approach

### Phase 1 — Data Collection and Baseline (Weeks 1–3)
- Export 90-day RTT dataset from Phoenix Zero feed.jsonl (2-second resolution, 4 chains)
- Align with Flashbots MEV-Boost bundle data and Dune on-chain revert ratio timeseries
- Establish per-chain RTT baseline distributions and identify candidate MEV events

### Phase 2 — Correlation Analysis (Weeks 4–6)
- Compute cross-correlation between RTT P99 and revert ratio with time-lag sweep (0–300s)
- Identify optimal RTT velocity threshold (gas_velocity metric: Δgas_pressure over 90s)
- Test ZKSync→Base cross-chain lag hypothesis on all documented MEV events in dataset

### Phase 3 — Predictive Model Validation (Weeks 7–9)
- Build lightweight classifier: RTT spike + velocity → MEV onset probability
- Measure precision/recall against held-out MEV events
- Quantify false positive rate and actionable threshold

### Phase 4 — Publication (Weeks 10–12)
- Research post to Flashbots Collective forum
- Open-source the RTT correlation analysis code
- Dataset excerpt published for reproducibility

---

## Deliverables

1. Research post on Flashbots Collective: *"RTT as Pre-MEV Signal: 90-Day Empirical Study"*
2. Open-source Python analysis notebook (RTT correlation, threshold optimization)
3. Documented false positive analysis across 4 L2 chains
4. Quantified lead-time distribution (P10/P50/P90 across all detected MEV events)

---

## Team

**Alexander Kent** — founder of Phoenix Zero RTT Oracle. Built and operates continuous L2 sequencer monitoring infrastructure since 2025. Responsible for May 17, 2026 MEV incident detection (27-second lead time, documented). 

Infrastructure: DO NYC1, Python, `eth_blockNumber` probes, 2s resolution, 90-day JSONL feed.

Contact: aleksandrkent64@gmail.com

---

## References

- Phoenix Zero live dashboard: https://phoenix-zero.vercel.app
- Public API: https://rtt.phoenix-ai.work/api/public-feed
- May 17 incident: Base P99 52ms→739ms at 23:29:43 UTC, revert ratio >50% at 23:30:10 UTC
- Flashbots MEV-Boost: https://docs.flashbots.net
- Flashbots Research Topics: https://github.com/flashbots/mev-research/blob/main/topics.md
