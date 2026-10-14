---
id: 
title: Zero-Storage Intra-Block Dynamic Fee Adaptation for LVR Elimination across Fast-Block L2 Sequencing Regimes
team: Volkan Dağlı (ITouch Systems Research Group, Lead), Zerrin Dağlı, Dağhan Dağlı
created: 2026-10-15
---

# Zero-Storage Intra-Block Dynamic Fee Adaptation for LVR Elimination across Fast-Block L2 Sequencing Regimes

Automated Market Makers (AMMs) suffer persistent structural value leakage to informed arbitrageurs and sandwich searchers—formally quantified as Loss-Versus-Rebalancing (LVR). While dynamic fee hooks have been proposed to internalize LVR by scaling swap fees during volatile regimes, existing designs suffer from a fundamental architectural flaw we term the *Oracle Latency and State-Lockout Paradox*. Cross-block volatility oracles react too late to prevent atomic intra-block extraction, whereas stateful intra-Pool hooks that elevate fees across multiple subsequent blocks introduce a severe *Multi-Block Griefing (Routing Blackout)* vulnerability: an attacker can execute a low-cost "dust" perturbation trade to trigger the multi-block fee lock, causing aggregator routers to divert organic retail volume to competing venues.

We propose a theoretical, formally verified, and empirical study of **Zero-Storage Intra-Block Dynamic Fee Adaptation** via procedural boundary dynamics (**Werracle**). Our core hypothesis is that an AMM reflex hook can suppress toxic LVR and atomic sandwich extraction without inducing routing blackouts if and only if: (1) fee adaptation is strictly *intra-block and memoryless* across blocks (zero persistent `SSTORE` state lockouts), and (2) swap flow toxicity is classified in $\mathcal{O}(1)$ execution time using non-linear phase-space boundary dynamics rather than 1D scalar price displacement. By encoding the non-linear decision boundary into a compact 24-byte coordinate seed $\Theta = (c_x, c_y, \text{zoom})$ packed inside a single 32-byte slot (`bytes32`) and evaluating a 12-point sparse multi-scale harmonic tripod over $\mathbb{Z}/9\mathbb{Z}$ in $\mathbb{Q}_{16.16}$ fixed-point arithmetic, our implementation (`WerracleFeeHook.sol`) executes purely in EVM stack registers at **21,438–22,557 gas** with **0 `SSTORE` writes**.

Our methodology combines three pillars:
1. **Formal Machine Verification (Lean 4):** Using Lean 4 (v4.34.1, Mathlib4), we prove universal halting ($\le 9$ steps per point, 108 global arithmetic cycles), strict fee bounds ($500 \le \text{Fee} \le 5000$ bps), intermediate overflow freedom, and a worst-case gas ceiling ($\le 24,000$ gas) with zero unproven axioms (`sorry`).
2. **Adversarial Gauntlet Simulation:** On a 40-core Dual Intel Xeon testbed, we simulate 30,000 swaps across ETH/USDC, WBTC/USDC, and UNI/ETH pools under benign retail flow, MEV sandwich bundles, flash-loan drains, and dust-griefing attacks, benchmarking against existing stateful dynamic fee hooks.
3. **L2 Sequencing & SUAVE Integration Analysis:** Extending the FCFS-to-PGA spectrum studied in FRP-56, we analyze how zero-storage intra-block fee reflexes interact with sub-second L2 Flashblocks (e.g., Base 200ms, Unichain) and Flashbots SUAVE / MEV-Share orderflow auctions.

Our approach has clear limitations. First, calibrating the 24-byte coordinate seed $\Theta$ requires offline Pareto optimization against historical tick distributions for each asset class (e.g., correlated stable pairs vs. volatile tail assets). Second, an intra-block hook observes local pool state perturbations rather than external CEX orderbooks directly; while it penalizes large informed price-moving arbitrage and atomic sandwiches, small-size latency arbitrage within the normal fee band remains bounded by the baseline fee tier. Third, while 22,557 gas costs `< $0.0005` on L2 rollups, it represents a non-trivial fixed overhead for tiny retail swaps on Ethereum L1.

The practical implications for the Flashbots ecosystem are substantial: providing L2 rollup designers, Unichain/Base liquidity providers, and SUAVE application builders with a machine-verified, zero-storage primitive that captures LVR surplus atomically while preserving 100% routing liveness for benign orderflow.

## Background and Problem Statement

Liquidity providers in constant function market makers (CFMMs) face an asymmetric adverse selection game against searchers with superior price and ordering privileges (Milionis et al., 2022; Schlegel & Kilbourn, 2025; Schlegel, 2025). In the current Uniswap v4 hook ecosystem, attempts to mitigate LVR via dynamic fees fall into two paradigms, both of which exhibit structural vulnerabilities documented in our preliminary 10,000-swap ($10M TVL) adversarial benchmark:

1. **The Multi-Block Griefing / Routing Blackout Vulnerability (Stateful Cooldown Hooks):**
   Hooks that persist elevated fees in EVM storage (`SSTORE`) for $k \ge 3$ blocks following a volatility spike are vulnerable to cheap denial-of-service griefing. In our simulation, 100 intentional dust push trades ($10–$50) repeatedly triggered the 3-block fee lockout, causing smart order routers (Uniswap Routing API, 1inch) to route **$269.6M** in legitimate retail volume to competing DEXs—a **96.5% collapse in net LP fee revenue** ($123.8k vs. $3.5M baseline).
2. **The Linear Displacement False-Positive Dilemma (1D Scalar Hooks):**
   Hooks that scale fees purely as a linear or quadratic function of scalar price displacement $|P_{\text{swap}} - P_{\text{ref}}|$ cannot distinguish between predatory MEV extraction and benign institutional rebalancing. In our benchmark, 1D scalar hooks penalized **100.0% of legitimate whale trades ($100k–$500k)** with maximum fees, whereas phase-space boundary evaluation reduced whale false positives to **10.8%** while absorbing **42.22% to 120.0% (compensatory surplus)** of toxic MEV extraction.

| Metric (10,000-Swap Adversarial Gauntlet, $10M TVL) | Stateful Cooldown Hook | 1D Scalar Displacement Hook | **Werracle (Intra-Block Zero-Storage OED)** |
| :--- | :---: | :---: | :---: |
| **Volume Diverted to Competitors (DoS Loss)** | $269.6 Million | $0.0 | **$0.0 (Zero Routing Blackout)** |
| **Whale Rebalancing False-Positive Rate** | 81.9% | 100.0% | **10.8% (89.2% Clean Flow Preserved)** |
| **Execution Gas Overhead per Swap** | 34,820 gas (`2 SSTORE`) | 31,450 gas (`1 SSTORE`) | **21,438 – 22,557 gas (`0 SSTORE`)** |
| **Shock-Accelerated Early Escape Gas** | N/A | N/A | **28% Gas Drop During Active Attack** |
| **Machine-Checked Formal Proof** | None | None | **Lean 4 (40 Theorems, 0 `sorry`)** |

**Research Questions:**
1. **Intra-Block LVR Capture vs. Block Time ($\tau$):** How does an atomic, zero-storage non-linear fee reflex alter the LVR extraction equilibrium across slow PGA chains (Ethereum L1) versus fast Flashblock / FCFS rollups (Base 200ms, Unichain), directly extending the framework of **FRP-56** (*MEV Value Chains Across L2 Sequencing Designs*) and Schlegel (2025) (*The LVR Gap for Random Block Times*)?
2. **Shock-Accelerated Escape Dynamics:** Under extreme flash-loan and sandwich perturbations, our $\mathbb{Z}/9\mathbb{Z}$ modular recurrence diverges to the escape horizon at $n \in \{1, 3\}$ rather than $n = 9$, reducing execution gas by up to 28% during active attacks. How can this *inverse gas-toxicity curve* be weaponized to make toxic probing strictly unprofitable under **Öz & Wu (2026)** (*To Wait or To Probe: Arbitrage Competition on High-Throughput Blockchains*)?
3. **SUAVE & MEV-Share Composability:** How can off-chain seed calibration and differentially private orderflow hints on **SUAVE / MEV-Share** pair with on-chain 24-byte seed updates to create self-calibrating LVR-resistant pools without leaking LP strategy parameters?

## Plan and Deliverables

**Time Commitment & Budget:** 12 weeks (3 months) full-time equivalent across our research and formal verification group. (Aligned with our $50,000 Flashbots Research Grant breakdown: Milestone 1: $15k, Milestone 2: $20k, Milestone 3: $15k; all research artifacts, code, proofs, and datasets remain 100% open-source public goods regardless of grant hiatus status).

**Phase 1 (Weeks 1–4): Formal Game-Theoretic Model & Multi-Pair Seed Calibration**
- Formalize the game-theoretic equilibrium between informed CEX-DEX arbitrageurs, uninformed retail routers, and a zero-storage intra-block boundary fee hook as a function of rollup block time $\tau$ and seed tuple $\Theta = (c_x, c_y, \text{zoom})$.
- Release the open-source Uniswap v4 Hook (`WerracleFeeHook.sol`) and Foundry invariant/fuzzing testbed with pre-calibrated golden seeds for the top 10 L2 trading pairs (`ETH/USDC`, `WBTC/USDC`, `UNI/ETH`, `wstETH/ETH`, etc.).

**Phase 2 (Weeks 5–8): Empirical Replay across L2 Flashblocks & Adversarial Probing**
- Replay historical high-volatility tick data across Ethereum L1, Base (pre/post-200ms Flashblocks), and Unichain Sepolia testnet deployments.
- Quantify net LP welfare, LVR suppression ratios, router retention (zero griefing verification), and searcher probing revert costs.
- Publish the formal research paper on SUAVE-assisted confidential seed updates and intra-block LVR elimination.

**Phase 3 (Weeks 9–12): Machine-Verified Lean 4 Certificate & Public Telemetry Portal**
- Expand the machine-checked **Lean 4 (Mathlib4)** verification package covering fixed-point $\mathbb{Q}_{16.16}$ non-overflow, $\mathbb{Z}/9\mathbb{Z}$ early-escape bounds, and griefing-resistance invariants.
- Deploy an open, reproducible live telemetry and benchmarking dashboard for the Flashbots community.

**Deliverables:**
1. **Academic Research Paper & Flashbots Collective Report:** Complete theoretical and empirical manuscript + summary post on `collective.flashbots.net`.
2. **Open-Source Smart Contract & Foundry Benchmark Suite:** Production-grade zero-storage EVM contracts (`Werracle.sol`, `WerracleTripodZMod9.sol`, `WerracleFeeHook.sol`) and 30,000-swap adversarial gauntlet scripts at [`github.com/pCwOrM/werracle`](https://github.com/pCwOrM/werracle).
3. **Machine-Verified Lean 4 Proof Artifact:** Complete `lake build` formal verification suite (`formal_proofs/WerracleProof.lean`) with zero unproven axioms (`0 sorry`).
4. **Community Workshop Presentation:** Presentation of findings and live L2 hook benchmarks at a Flashbots research workshop / Roast.

## References

- Milionis, J., Moallemi, C. C., Roughgarden, T., & Zhang, A. L. (2022). Automated Market Making and Loss-Versus-Rebalancing (LVR). *arXiv:2208.06046*.
- Daian, P., Goldfeder, S., Kell, T., Li, Y., Zhao, X., Bentov, I., Breidenbach, L., & Juels, A. (2020). Flash Boys 2.0: Frontrunning in Decentralized Exchanges, Miner Extractable Value, and Consensus Instability. *IEEE Symposium on Security and Privacy (S&P)*.
- Schlegel, J. C., & Kilbourn, Q. (2025). Arbitrage with Bounded Liquidity. *arXiv:2507.02027*.
- Schlegel, J. C. (2025). The LVR Gap for Random Block Times: A Quick and Useful Approximation. *Flashbots Collective Forum*.
- Öz, B., & Wu, F. (2026). To Wait or To Probe: Arbitrage Competition on High-Throughput Blockchains. *arXiv:2606.00720*.
- Jia, R., & Yu, S. (2026). FRP-56: MEV Value Chains Across L2 Sequencing Designs. *Flashbots MEV Research*.
- Dağlı, V., Dağlı, Z., & Dağlı, D. (2026). Werracle: Sub-Cent Intra-Block AI Reflex Oracles and Flash-Loan Circuit Breakers for EVM Smart Contracts. *arXiv:2609.30719 [cs.CR, cs.AI, cs.DC]*; Zenodo DOI: `10.5281/zenodo.22942598`.
- Dağlı, V., Dağlı, Z., & Dağlı, D. (2026). Zero-Storage Procedural Neural Synthesis via Boundary Dynamics: Formal Verification in Lean 4 and Bare-Metal Gauntlet Validation. *arXiv:2609.33066 [cs.LG, cs.AI, cs.LO]*; Zenodo DOI: `10.5281/zenodo.22983889`.
- Dağlı, V., Dağlı, Z., & Dağlı, D. (2026). Orbital Error Dynamics: Self-Organized Criticality, Ephemeral Parameter Resonance, and Non-Linear Biological Ontologies in Zero-Storage Neural Synthesis. *arXiv:2609.30115*.
