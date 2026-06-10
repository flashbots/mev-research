# FRP-XX — Defending Passive LPs Against Same-Block JIT MEV via a Self-Sustaining Hook

**Title:** Defending Passive LPs Against Same-Block JIT MEV via a Self-Sustaining Uniswap v4 Hook
**Team:** voltgzer0 (solo, lead) — solidity / EVM security / v4 hooks
**Created:** 2026-06-10
**Contact:** voltmattty77@gmail.com · x.com/voltgzer0 · t.me/voltgzer0
**Repository:** github.com/voltgzer0/jit-shield (open source, MIT)
**Live deployment:** 0xca2f96f95c9E7a2109ecbD64bf80F7Cf77d86ac8 (Sepolia, verified)

---

## Executive Summary

Just-In-Time (JIT) liquidity is one of the largest persistent value leaks for passive liquidity providers in concentrated-liquidity AMMs. Researchers estimate $50–200M per year extracted from Uniswap v3 passive LPs by searchers who add a tight-range position in the same block as a target swap, capture ~80% of the swap fee, and remove the position in the same block. Uniswap v4 inherits this structural exposure unless a hook actively counters it.

This proposal frames the JIT defence problem as an **economic-defense problem solvable inside a single hook**, demonstrates a working solution (JITShield), and presents an evaluation methodology measurable directly against historic mainnet JIT transactions.

**Hypothesis.** A hook that (i) detects same-block adds via state on the previous swap's block, (ii) charges a surge fee on the next swap when a flagged position exits during a lock window, and (iii) redistributes the surge premium to honest passive LPs while retaining a small protocol cut, removes the JIT searcher's positive expected value — without taxing honest swappers or LPs.

**Methodology.** Three threads: (a) on-chain reference implementation as a v4 hook with end-to-end Foundry test coverage; (b) closed-form economic analysis comparing pre-/post-hook expected value for the JIT searcher; (c) replay-and-measure evaluation against the top-N historic mainnet JIT transactions, computing per-tx what LPs would have kept and what the protocol would have earned had JITShield been live.

**Method limitations.** The detection heuristic uses same-block correlation, which is a sufficient condition for one common JIT pattern but not a necessary condition for all JIT-shaped extraction. A range-width signal (tight-position correlation) is identified as a follow-up to reduce false-positive flagging of legitimate narrow-range refills. The protocol cut is currently implemented on exact-input swaps only.

**Implications.** A self-sustaining MEV-defence hook fundable from the value it recovers is a public-goods primitive that the broader v4 ecosystem can adopt without coordination, without an off-chain keeper, and without modifying core protocol consensus. It establishes a template (detect → surge → carve via `BeforeSwapDelta` → settle via `PoolManager.take`) reusable for adjacent defences (sandwich resistance, LVR mitigation).

---

## Background and Problem Statement

### Motivation

Concentrated liquidity reduced the capital efficiency cost of providing on-chain liquidity but created a new attack surface: searchers with cheap inventory can supply tight-range liquidity *only when it is profitable*, capturing a large share of the LP fee on any single swap and exiting immediately. Passive LPs — who commit capital for hours, days, or longer — collect proportionally less than their committed capital deserves.

Public estimates of v3 JIT extraction range $50–200M / year. v4's hook layer is the first venue where this can be defended *inside the protocol* without modifying core consensus, by changing the fee-and-redistribution economics of a single pool.

The defence problem has two technical requirements that are usually presented in tension with each other:

1. **Detect JIT cheaply and accurately.** The detection must run on every `addLiquidity` and every swap, cannot rely on an off-chain oracle, and must produce few false positives that would tax honest LPs.
2. **Capture value without burdening the swapper.** The surge must be paid by JIT searchers (directly or via their replacement flow), not by everyday traders, and the protocol's sustainability fee must not touch the base LP fee.

### Research questions

- **Q1.** Is *same-block* the right detection axis for JIT? What is the precision/recall trade-off versus richer signals (tick-range width, position-size relative to pool TVL, recent-history priors)?
- **Q2.** What is the JIT searcher's best response under a surge-and-time-lock mechanism? Specifically: can the searcher amortize the surge across multiple swaps, route around it via concurrent pools, or shift to single-block multi-pool patterns?
- **Q3.** What is the **historical** counter-factual value — i.e., for the top-N JIT transactions observed on mainnet in the past 30 days, what fraction would JITShield have shielded, how much would have stayed with passive LPs, and how much would have accrued to the protocol?
- **Q4.** How does the mechanism interact with adjacent v4 hooks (e.g. Bunni's rehypothecation, Angstrom's bundle-level defence)? Are they composable into a unified pool-level defence stack?

### Related work and current state

A reference implementation, **JITShield**, is open-sourced under MIT at `github.com/voltgzer0/jit-shield`. It is deployed and verified on Sepolia at `0xca2f96f95c9E7a2109ecbD64bf80F7Cf77d86ac8`. A single atomic transaction (`0x2ee624d8…a1d1f`) executed the full scenario end-to-end on chain: primer swap → same-block JIT add → same-block JIT remove → final shielded swap. The protocol fee accrual on chain matched the closed-form formula `input × surgeBips × protocolBips / 1e10` to the wei.

The implementation has 12/12 tests passing (unit + Forge integration against a real `PoolManager` + mainnet-fork economics), zero actionable Slither findings, and a published self-audit with severity-classified findings. It is past the prototype stage but pre-external-audit.

### Why now / why Flashbots

Flashbots' research focus on the **socioeconomic structure of MEV**, on **defence mechanisms accessible to ordinary actors**, and on **public-goods MEV infrastructure** all align with the project: JITShield is a permissionless, MIT-licensed hook funded by the value it recovers, not by extracting from honest activity. The replay-and-measure evaluation is exactly the kind of empirical claim Flashbots research is positioned to validate and amplify.

---

## Plan and Deliverables

12-week plan, three phases. Phase budgets in weeks of full-time-equivalent solo work.

### Phase 1 — Mechanism hardening (weeks 1–4)

Production-grade fixes to the open security items in JITShield's published self-audit:

- Two-step ownership transfer (OZ Ownable2Step semantics)
- Owner-toggleable pause covering `beforeAddLiquidity` and `beforeSwap`
- Tick-range-width JIT signal, configurable per pool, to reduce false positives on legitimate narrow-range refills
- Exact-output protocol-fee cut path (currently exact-input only) using deferred settlement
- Slither in CI, gated PR merges, expanded fuzzing

Deliverables: PR series merged on `main`, test suite at parity (12+ → 20+ green), self-audit document updated to clear the HIGH and the MEDIUM-1..4 findings.

### Phase 2 — Replay-and-measure evaluation (weeks 5–8)

Empirical Q3 answer.

- Build a `forge` script that, given a mainnet block range, identifies JIT-shaped transactions (one block, one address, add → swap → remove, narrow range)
- For each identified transaction, fork the mainnet state at that block and replay the same call sequence against a JITShield-protected pool (mock currencies + the historic swap volume scaled to the protected pool's depth)
- Compute per-tx: searcher P&L (delta), LP receipts under both regimes, protocol fee accrued
- Publish dataset and aggregate statistics as a public Mirror.xyz blog post and as machine-readable JSON in the repo

Deliverables: dataset (≥100 historic mainnet JIT transactions), replay scripts (reusable for any v4 hook defence), public writeup with the headline numbers.

### Phase 3 — Composability study and presentation (weeks 9–12)

Q4 answer and community deliverable.

- Compose JITShield with one adjacent defence hook (Bunni-style rehypothecation OR Angstrom-style bundle defence — pick the one with more accessible reference) in a single pool, verify on a mainnet fork, measure combined extraction reduction
- Open-source the composition pattern and write up the result
- Present at the next Flashbots community event (research call, podcast, or in-person if a relevant event lands in the window)

Deliverables: composition repo + writeup, Flashbots presentation, final research blog post or Arxiv-style document summarising Phase 1–3.

### Public artefacts

- Code: `github.com/voltgzer0/jit-shield` (kept open, MIT)
- Replay dataset: `github.com/voltgzer0/jit-shield/tree/main/datasets/mainnet-jit-replay`
- Writeups: Mirror.xyz + Flashbots Forum (FRP discussion category if reactivated, otherwise Research subcategory)

### Funding requested

Total: **$15,000** (standard FRP grant size).

Use of funds:
- 12 weeks of focused solo research at $1k/week effective rate
- Replay-and-measure infrastructure (RPC, dataset storage): $1,500
- Travel / talk if Flashbots community event lands in window: ≤ $1,500
- Remainder: open-source maintenance, audit prep

If accepted, payment to be paid in USDC or ETH per Flashbots standard.

---

## References

- JITShield repository, source and self-audit: https://github.com/voltgzer0/jit-shield
- JITShield landing with verified Sepolia links and reproducible cast-call proof: https://voltgzer0.github.io/jit-shield
- Verified hook on Sepolia Etherscan: https://sepolia.etherscan.io/address/0xca2f96f95c9E7a2109ecbD64bf80F7Cf77d86ac8#code
- End-to-end atomic JIT scenario tx: https://sepolia.etherscan.io/tx/0x2ee624d85aa911c9a7d54a975266b77f7cb8a75810d312c963b791e8f35a1d1f
- Self-audit document with severity-classified findings: https://github.com/voltgzer0/jit-shield/blob/main/SECURITY.md
- Uniswap v4 PoolManager and IHooks reference: https://docs.uniswap.org/contracts/v4
- Doppler / Whetstone — liquidity-bootstrapping MEV-reduction hook (related funded work, complementary phase): https://www.uniswapfoundation.org/grants
- Flashbots MEV research repository: https://github.com/flashbots/mev-research
- Flashbots writings on MEV defence and public-goods infrastructure: https://writings.flashbots.net
