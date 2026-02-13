---
id: <leave blank -- will be assigned by reviewers>
title: Sybil Resistance in Inclusion List Mechanisms: FOCIL and AUCIL
team: Abhimanyu Nag (MITACS Fellow, University of Alberta) [lead], Sarisht Wadhwa (Duke University) [advisor]
created: 2026-01-26
---

# Sybil Resistance in Inclusion List Mechanisms: FOCIL and AUCIL

## Background and Problem Statement

Inclusion lists (ILs) [4] are emerging as a critical censorship resistance primitive for Ethereum under proposer-builder separation (PBS) [3]. Two design paradigms have been developed: **FOCIL** [1], which relies on consensus enforcement with fixed per-slot participants and no explicit pricing, and **AUCIL** [2], which relies on economic incentives with strategic participation and explicit price formation. With FOCIL (EIP-7805) proposed to headline the forthcoming Hegota upgrade [5], the robustness of IL designs is an immediate concern. Crucially, neither paradigm is fully Sybil-proof or bribery-proof.

FOCIL is resistant to Sybils at the identity layer where its 1-out-of-\(k\) honesty assumption and random committee sampling make full committee capture statistically impractical (e.g. for \(k=16\) and adversarial stake fraction \(\alpha=0.3\), single-slot capture probability \(\approx 0.3^16 \approx 4 \times 10^{-9}\)) [17]. The vulnerability is economic. Stouka et al. [6] design transaction fee mechanisms (TFMs) for FOCIL and show that unconditional inclusion lists can significantly increase the minimum bribe needed to censor a transaction but only if the block producer’s strategy space excludes adding fake transactions to the mempool. When fake transaction strategies are included, the cost of bribing under conditional and unconditional lists becomes similar, because injecting fake transactions that are later invalidated is the cheapest deviation for omitting a transaction from an inclusion list (Section 7, [6]). Moreover, the censorship cost bounds in [6] are equilibrium-dependent: there is no single fee split that maximizes resistance for all transactions, and users do not pay committee fees in equilibrium unless someone else does. Thus FOCIL is Sybil proof by trust guarantees but not bribery proof as a TFM design problem.

AUCIL [2] by Wadhwa et al. addresses these gaps by explicitly pricing inclusion through an auction and aligning incentives: Phase I produces a correlated equilibrium among includers that coordinates transaction coverage, and Phase II aggregates individual inclusion lists via an auction that rewards contributors. This yields a hard censorship cost floor equal to the block reward \(R\) and does not rely on altruism. However, AUCIL does not analyze false-name bidding [14] under adversarial identity creation. In Phase I, adversarial identities can submit correlated signals that bias the intended correlated equilibrium. in Phase II, the auction is vulnerable to false-name bidding (efficient auction designs including VCG are generically not false-name-proof [14]). So AUCIL is economically robust by design but has an open Sybil/false-name problem.

No existing analysis combines Sybil attacks with the full strategy space identified in [6]. We study how Sybil resistance manifests differently across these two paradigms and what design patterns yield robust guarantees under identity elasticity. This aligns with the Flashbots research agenda on **Mechanism Design under Sybils** [8]. Building on TFM literature [19,20], our central research questions are:

1. How does the choice between FOCIL and AUCIL shape the mechanism’s vulnerability to Sybil attacks, and what are the implications for PBS TFM design?
2. What are the fundamental economic trade-offs between these FOCIL and AUCIL under identity elasticity — where does each break, and why?
3. What design patterns across both paradigms provide robust Sybil resistance? And what might be optimal for Ethereum's future?

## Approach

We model both paradigms as instances of a common abstraction: *capacity-constrained allocation mechanisms for transaction inclusion*. Sybils correspond to **false-name deviations** that perturb the mechanism’s participant set and can change equilibrium allocations and effective prices. Our working definition of Sybil resistance is **stake-neutrality**: for fixed total stake \(S\), an operator’s expected payoff, marginal inclusion probability, and induced equilibrium price impact is minimal when stake is split across \(B\) identities.

To establish proposer welfare, we choose to adopt a General Equilibrium (GE) [9] (because inclusion fees, block rewards, and mempool congestion jointly determine equilibrium prices and bribery costs) with three concrete outputs: 

 1. Welfare decomposition across transaction submitters, includers, proposers/builders, and committee members, for both FOCIL under [6]’s TFMs and AUCIL

 2. Equilibrium prices and how identity creation perturbs them — for FOCIL this includes the block producer’s fake-transaction strategy, for AUCIL the effect of false-name bidding on Phase-II outcomes 

 3. Strategyproofness-in-the-large [11] for AUCIL, yielding computable bounds on manipulation gain in large markets.

We treat committee size \(k\) as a design variable (even for FOCIL since k = 16 is still a placeholder and needs more research): for target tolerances \((\epsilon,\delta)\), we bound a deviation-gain (regret) term \(R(k,N,B)\) and a price-distortion term \(\Delta p(k,N,B)\), where \(N\) is market scale and \(B\) is the attacker’s identity budget, and recommend the smallest \(k\) such that \(R \le \epsilon\) and \(\Delta p \le \delta\). We model the attacker as a single economic operator with a hidden type \(\theta\) (censorship value, coordination capacity, identity cost) and compute comparative statics as \(B\) increases, we evaluate under both thin-tailed and fat-tailed attacker-size assumptions [13,14].

For **FOCIL**, we formalize and extend [6]’s full strategy space (including fake-transaction injection) in the presence of Sybils and derive how [6]’s censorship cost bounds degrade with identity budget \(B\), bribery attack by Sybil participants and identify design knobs (committee size \(k\), fee-split rules, reward/penalty normalization). Our main approach is to test FOCIL's TFM in the presence of Sybils as a fraction of the IL committee and their ability to bribe honest members given attacker budget. We think of this as a hybrid Sybil-bribery attack where the budget needed to conduct a bribery attack lowers given greater fraction of attacker participation in the committee.

For **AUCIL**, we model the two-phase structure, extend the deviation space to false-name participation (one agent controlling multiple identities with coordinated Phase-I signals), analyze Phase II under false-name bidding, and evaluate mitigations such as minmax problem aggregation constraints and caps on marginal contribution. By analyzing both paradigms with standardized metrics, we extract general design principles: which Sybil resistance properties depend on enforcement (consensus vs economic), which on participation structure (fixed vs strategic), and which are universal. The goal is concrete recommendations for FOCIL and AUCIL and design-space guidance for future IL proposals (e.g. Relay ILs [15], Rainbow Incentives and FOCILR [18]).

## Plan and Deliverables

The project is organized in four phases totalling to approximately ~5-6 months total.

### 1. Formalize IL Abstraction and FOCIL Baseline
**Objective:** Establish a unified IL allocation model and Sybil threat model, and characterize FOCIL’s censorship cost bounds under the full strategy space in [6].
**Approach:** Define the capacity-constrained allocation abstraction and Sybil threat model (stake splitting, coordinated identity control, fake transaction injection as in [6]). Analyze FOCIL’s censorship cost bounds under [6]’s Double and Single TFMs, characterize how they degrade under hybrid attack of identity splitting and bribery wealth and evaluate especially when it is cheap for the block producer to add fake transactions to the mempool. Establish measurable metrics (e.g. minimum censorship cost, capture probability, welfare loss under partial capture) and evaluate the current TFM proposal as per [6].
**Time:** 1-1.5 months

### 2. Formalize False-Name Deviations in AUCIL
**Objective:** Model false-name attacks in AUCIL’s two-phase structure and propose false-name-robust aggregation rules.
**Approach:** Formalize false-name deviations in Phase I (correlated signals biasing the correlated equilibrium) and Phase II (false-name bidding in the aggregation auction). Analyze how adversarial identity creation breaks Phase-I equilibria and propagates to Phase-II outcomes. Identify which aggregation rules fail under identity splitting, propose and compare mitigations (e.g. stake-normalized or minmax aggregation, caps on marginal contribution). Establish the same measurable metrics for the auction-based paradigm.
**Time:** 1-1.5 month

### 3. Computer Simulations
**Objective:** Compare both paradigms under the same metrics and attacker model, extract design principles, stress-test with simulations.
**Approach:** Evaluate FOCIL and AUCIL side by side on the established metrics. Identify conditions under which identity splitting weakens each paradigm’s guarantees. Extract general design principles (what depends on enforcement mechanism, what on participation structure, what is universal). Run simulations under different Bayesian priors (worst-case and fat-tailed attacker scenarios) of attacker budget to validate and stress-test the theoretical bounds.
**Time:** 1-1.5 month

### 4. Research Paper and Formalization
**Objective:** Produce the research paper and Lean 4 formalization of key results.
**Approach:** Write the full research paper with formal results and a design-implications section for protocol engineers. Formalize in Lean 4 the core model, definitions, and selected key lemmas and theorems for reproducibility and verification. Prepare scripts/notebooks for parameter sweeps and stress tests.
**Time:** 1-1.5 month

## Final Deliverables

- **Research paper** with formal results and a design-implications section covering: (i) how FOCIL and AUCIL resist Sybil attacks differently, with attention to the economic attack paths in [6] (ii) general design principles for Sybil-robust IL mechanisms (iii) parameter recommendations for committee sizing under Sybil risk (iv) failure modes to avoid in future IL designs (e.g. Relay ILs [15]). We hope to aim Ethereum Technical Conferences and Academic Conferences like AFT, MARBLE and ACM to publish our paper.
- **Open-source artifacts:** Lean 4 code for key lemmas and theorems and scripts/notebooks for parameter sweeps and stress tests.

## References

- [1] [EIP-7805: Fork-choice enforced Inclusion Lists (FOCIL)](https://eips.ethereum.org/EIPS/eip-7805)
- [2] [AUCIL: An Inclusion List Design for Rational Parties](https://eprint.iacr.org/2025/194)
- [3] [Proposer Builder Separation Roadmap](https://ethereum.org/roadmap/pbs/)
- [4] [Inclusion Lists: EIP-7547](https://ethereum-magicians.org/t/eip-7547-inclusion-lists/17474)
- [5] [Hegotá Headliner Proposal: FOCIL, EIP-7805](https://ethereum-magicians.org/t/hegota-headliner-proposal-focil-eip-7805/27604)
- [6] [Multiple Proposer Transaction Fee Mechanism Design: Robust Incentives Against Censorship and Bribery](https://arxiv.org/pdf/2505.13751)
- [7] [The Sybil Attacks and Defenses: A Survey](https://arxiv.org/pdf/1312.6349)
- [8] [Flashbots Problem Database: Mechanism Design with Sybils](https://flashbots.notion.site/Mechanism-Design-with-Sybils-21f6b4a0d876816da1bbe1dc3204878c)
- [9] [General Equilibrium Theory](https://en.wikipedia.org/wiki/General_equilibrium_theory)
- [10] [Strategyproofness](https://en.wikipedia.org/wiki/Strategyproofness)
- [11] [Strategyproofness-in-the-large (Azevedo–Budish)](https://eduardomazevedo.github.io/papers/azevedo-budish-spl-wp.pdf)
- [12] [On Sybil Proofness in Competitive Combinatorial Exchanges](https://www.arxiv.org/abs/2512.10203)
- [13] [The Cost of Sybils, Credible Commitments, and False-Name Proof Mechanisms](https://arxiv.org/abs/2301.12813)
- [14] [The effect of false-name bids in combinatorial auctions (Yokoo et al.)](https://www.sciencedirect.com/science/article/abs/pii/S0899825603000459)
- [15] [Relay Inclusion Lists](https://ethresear.ch/t/relay-inclusion-lists/22218)
- [16] [Lean 4 Prover](https://github.com/leanprover/lean4)
- [17] [Fox, Pai, Resnick: Censorship Resistance in On-chain Auctions](https://arxiv.org/abs/2301.13321)
- [18] [Rainbow roles & incentives: ABPS + FOCILR + AS](https://ethresear.ch/t/rainbow-roles-incentives-abps-focilr-as/21826)
- [19] [Roughgarden: Transaction Fee Mechanism Design](https://arxiv.org/abs/2106.01340)
- [20] [Gafni et al.: A Small Collusion is All You Need](https://arxiv.org/abs/2510.05986v2)
