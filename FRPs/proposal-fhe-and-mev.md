---
id: 
title: Evaluating MEV Resistance of FHE-Protected AMMs
team: MigaLabs
created: 2025-12-23 
---
# Evaluating MEV Resistance of FHE-Protected AMMs

## 1. Introduction

Decentralised Finance (DeFi) relies heavily on Automated Market Makers (AMMs) for on-chain token exchange. However, AMMs remain vulnerable to Miner/Maximal Extractable Value (MEV) attacks, particularly frontrunning and backrunning strategies that exploit users' pending transactions in public mempools. These attacks degrade user experience by increasing slippage, creating unstable execution conditions, and enabling extractive arbitrage that costs users millions of dollars annually.

Recent proposals from Flashbots and other MEV researchers suggest using Fully Homomorphic Encryption (FHE) to protect the contents of pending transactions. FHE hides critical information—such as trade direction, amount, and slippage—from mempool observers, making classical frontrunning orders significantly more difficult to execute. However, even under FHE, backrunning opportunities remain: once a transaction is executed inside the block builder's environment, the resulting AMM state (updated reserves and implied prices) becomes visible to the builder, potentially enabling post-trade arbitrage.

This proposal aims to rigorously quantify how much MEV extraction remains possible under FHE and to characterise the strategies an economically rational attacker would use in probabilistic settings where only the post-trade AMM state is visible. This research combines empirical analysis of blockchain data with formal Markov Decision Process (MDP) modelling.

## 2. Background and Problem Statement

### 2.1 MEV and AMMs

Automated Market Makers (e.g., Uniswap v2/v3, Curve) maintain token reserves following deterministic functions. User trades modify reserves, changing the implied exchange rate. MEV attackers—searchers, builders, or validators—exploit these predictable state transitions for profit.

The most common attacks types are:

- **Frontrunning**: Attacker inserts a trade before the victim to benefit from the price impact.
- **Backrunning**: Attacker arbitrages after the victim's trade restores the AMM price to global market levels.
- **Sandwich**: A combination of the above two.

### 2.2 FHE for Mempool Privacy

Fully Homomorphic Encryption provides a cryptographic method for encrypting transaction contents while allowing certain computations on the encrypted data. Flashbots has proposed architectures where:

- Transactions enter the mempool encrypted.
- The block builder decrypts them inside a secure environment.
- Only the post-execution state becomes public.

This eliminates pre-trade visibility for attackers (mitigating frontrunning) but does not hide post-trade AMM reserves (leaving backrunning partially viable). We argue that frontrun attacks remain feasible in a probabilistic setting.

### 2.3 MDPs in Blockchain Adversarial Modeling

MDPs have been previously used to model economic attacks (e.g., RANDAO manipulation) [1]. In these settings, each state corresponds to observable blockchain parameters; actions correspond to the choice of attack parameters; and the Bellman optimality equation provides the attacker's optimal strategy over time. The MDP framework is well-suited to model probabilistic MEV extraction when attackers face uncertainty about encrypted user trades.

## 3. Motivation

FHE is a promising building block for private transaction execution, but its MEV implications remain unclear. While researchers frequently claim that FHE "removes frontrunning," the residual MEV from backrunning remains unknown and may still constitute a substantial extractive vector.

Critical questions remain unanswered:

- How much of today's MEV would persist in an FHE-based execution model?
- Which types of trades, pools, or market conditions remain vulnerable?
- What probabilistic strategies can attackers still apply when only post-trade information is available?
- Can we design AMM-level or protocol-level defenses that eliminate these residual backruns?

Answering these requires both (1) empirical reconstruction of historical MEV opportunities and (2) theoretical modelling of optimal attacker behavior under uncertainty.

This collaboration leverages the complementary strengths of MigaLabs (empirical blockchain data analysis) and Bence Ladoczki (formal MDP modeling) to produce the first quantitative and strategic analysis of MEV in encrypted transaction environments.

## 4. Plan and Deliverables

The project consists of two major components, each performed by a different entity.

### 4.1 Empirical Reconstruction and Simulation (Conducted by MigaLabs)

MigaLabs leads all data-driven and simulation tasks.

#### 4.1.1 Historical Data Collection

- Collect a full year of blockchain blocks.
- Extract all transactions interacting with major AMMs (e.g., Uniswap v2/v3, Curve, Balancer).
- Build a structured dataset including block number, tx index, calldata, gas data, and decoded swap parameters.

#### 4.1.2 AMM State Reconstruction

Using archive-node access or local EVM replay:

- Reconstruct pre-trade and post-trade AMM reserves for each swap.
- Capture implied prices, slippage, and liquidity conditions.
- Reconstruct cross-DEX prices to detect historical arbitrage opportunities.

This ensures that the actual AMM state at each moment is accurately known, enabling counterfactual simulation.

#### 4.1.3 FHE-Based Replay of Blocks

Simulate a counterfactual world in which:

- Transactions retain their execution effects,
- But pre-trade information is hidden (as under FHE).

For each trade:

- Assume builders cannot see trade details before execution.
- After execution, compute what backrunning arbitrage opportunities would arise based on post-trade state.

#### 4.1.4 Residual MEV Analysis

Compute:

- Arbitrage magnitude after each user trade,
- Total residual backrunning MEV per block / day / pool,
- Distribution of opportunity sizes over tokens, pool types, and volatility regimes.

This generates a quantitative "lower bound" on the MEV that would survive under FHE.

The results of this empirical study serve as inputs for the theoretical modeling conducted by Bence Ladoczki.

### 4.2 MDP Modeling of Probabilistic Backrunning

Bence Ladoczki will lead the formal modelling and policy analysis by constructing and solving a Markov decision process for sandwich trading in weighted automated market makers, using empirically motivated distributions for user order sizes and slippage tolerance.

The work will evaluate optimal arbitrage policies under varying pool weights and liquidity conditions, and will quantify associated liquidity provider fee revenue, user transaction costs, and risk-sensitive performance metrics.

The analysis will be supported by extensive simulation and visualisation, including parameter-sweep studies and policy heatmaps, to enable systematic comparison of protocol design choices.

Inventory dynamics will be explicitly modelled through penalty functions on residual positions, allowing the framework to capture balance-sheet constraints and inventory risk faced by strategic traders.

#### 4.2.1 Constructing an MDP for Backrunning Under Uncertainty

Define:

- **States**: AMM pre-trade and post-trade distributions, price-path distributions, mempool conditions, and market indicators.
- **Actions**: Probabilistic choices of backrun trade size and timing, constrained by capital and gas limits.
- **Transition Probabilities**: Derived from the empirical distribution of trade impacts and liquidity conditions obtained from MigaLabs' dataset.
- **Rewards**: Expected backrun profit (arb size minus gas costs).

#### 4.2.2 Solving for Optimal Strategies

Apply:

- Bellman equations,
- Value iteration or policy iteration,
- Approximate dynamic programming (if the state space is large).

Derive:

- Optimal attacker policy under FHE constraints,
- Expected long-run MEV extraction per state or market condition.

#### 4.2.3 Designing New Defense Mechanisms

Using insights from the optimal policies, Bence Ladoczki will design and analyze:

- AMM mechanisms that obscure or smooth the post-trade state,
- Randomization or batching mechanisms that reduce arb sharpness,
- Protocol-level mitigations for builder-level asymmetric information.

These designs will then be sent back to MigaLabs for empirical evaluation.

### 4.3 Joint Evaluation and Integration

Both entities collaborate to:

- Re-run simulations with modified AMM designs,
- Measure how much MEV reduction occurs,
- Produce a unified analysis combining empirical and theoretical results.

## 5. Expected Outcomes

- A quantitative understanding of residual MEV under FHE.
- The first MDP-based model of probabilistic backrunning with encrypted transactions.
- A catalogue of residual vulnerabilities in current AMM designs.
- Proposed defenses tested in simulation.
- Joint publications and presentations outlining the findings.

## The Team

**Bence Ladoczki**: He is a researcher working at the intersection of blockchain systems, distributed networks, and applied machine learning. His work focuses on the security, scalability, and economic mechanisms of decentralized systems, particularly Ethereum, MEV, randomness, and cross-chain protocols. In parallel, he has contributed to high-performance scientific computing and quantum chemistry methods, as well as machine learning applications in multimedia and video streaming. Overall, his research combines theoretical modeling with empirical analysis to address real-world challenges in complex computational systems. Recently he published a paper on the manipulability of the distributed randomness generator of the beacon chain and analysed the problem using MDPs [1].

**Dr. Leonardo Bautista-Gomez**: Dr. Leonardo Bautista-Gomez is the founder and leader of MigaLabs. He is also a Core Researcher for Ethereum. He has been collaborating with the Ethereum Foundation for over seven years, receiving multiple research grants from the EF and other institutions. He has over a decade of research experience in supercomputers, deep learning, and blockchain technology. He has published more than 50 scientific articles [2, 3, 4]. He has received multiple international academic awards, including the IEEE TCSC Award for Excellence in Scalable Computing and the ACM/IEEE George Michael Memorial High Performance Computing Fellowship. He did his Ph.D. at the Tokyo Institute of Technology and his Master's at the Pierre & Marie Curie University Paris 6.


**References**

[1] Ábel Nagy, János Tapolcai, István András Seres, and Bence Ladóczki. 2025. Forking the RANDAO: Manipulating Ethereum's Distributed Randomness Beacon. In *Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security (CCS '25)*. Association for Computing Machinery, New York, NY, USA, 873–887. https://doi.org/10.1145/3719027.3744852

[2] Mikel Cortes-Goicoechea, Tarun Mohandas-Daryanani, Jose Luis Muñoz-Tapia, and Leonardo Bautista-Gomez. 2023. Autopsy of Ethereum's Post-Merge Reward System. In *2023 IEEE International Conference on Blockchain and Cryptocurrency (ICBC)*. IEEE, 1–9. https://doi.org/10.1109/icbc56567.2023.10174942

[3] Mikel Cortes-Goicoechea, Tarun Mohandas-Daryanani, Jose Luis Muñoz-Tapia, and Leonardo Bautista-Gomez. 2025. The impact of connectivity and software in Ethereum validator performance. *Cluster Computing* 28, 366. https://doi.org/10.1007/s10586-025-05153-y

[4] Simon Brown and Leonardo Bautista-Gomez. 2024. Exploring Correlation Patterns in the Ethereum Validator Network. *arXiv preprint* arXiv:2404.02164. https://arxiv.org/abs/2404.02164



