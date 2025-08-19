# Summary  

Blockchain transactions today suffer from a **time-of-check to time-of-use (TOCTOU) gap**: the moment between when a user signs a transaction and when it is executed on-chain. In this gap, transaction outcomes may diverge due to malicious reordering, market conditions, or smart contract manipulation.  

This gap enables both **malicious MEV** (e.g., front-running, sandwiches) and emerging scams such as **transaction simulation spoofing**, where users are misled into signing a transaction which final outcome differs from what they previewed. As financial institutions begin adopting Ethereum, regulators increasingly highlight the need for execution guarantees before large-scale adoption can occur.

# Summary  

Blockchain transactions today suffer from a **time-of-check to time-of-use (TOCTOU) gap**: the moment between when a user signs a transaction and when it is executed on-chain. In this gap, transaction outcomes may diverge due to malicious reordering, market conditions, or smart contract manipulation.  

This gap enables both **malicious MEV** (e.g., front-running, sandwiches) and emerging scams such as **transaction simulation spoofing**, where users are misled into signing a transaction whose final outcome differs from what they previewed. As financial institutions begin adopting Ethereum, regulators increasingly highlight the need for execution guarantees before large-scale adoption can occur.  

We propose **transaction contractualization**: only including a transaction if its execution at block-building time matches the simulation previously accepted by the user. This enforces execution fidelity, reliably eliminating malicious MEV by design. Crucially, it does so without introducing centralization, subjective heuristics, or opaque trust assumptions, preserving Ethereum’s ethos of transparency, decentralization, and permissionlessness in the block-building pipeline.

---

# Background and Problem Statement  

Currently, there is no effective solution to malicious MEV that avoids undermining Ethereum’s core values of transparency, decentralization, and permissionlessness. If the block-building pipeline becomes centralized, opaque, and based only on trust, Ethereum’s foundational principles are compromised.  

The proposals most often discussed share recurring limitations:  

- **Centralization of trust.** Encrypted mempools (e.g., Shutter) require key-management committees, creating new points of failure. Private relays and RPCs (e.g., Flashbots Protect) concentrate order flow into a few operators who must be trusted not to misbehave.  
- **Problems of detection and subjectivity.** Private relays rely on heuristic filters to detect sandwiches, but increasingly sophisticated strategies (e.g., Jared’s proxy-contract bots with off-chain calldata) make detection unscalable.  
- **Erosion of efficiency and permissionlessness.** Encrypted mempools add decryption delays and cryptographic overhead, slowing block building while still requiring trusted operators. Keeping transactions hidden until after consensus would require major changes to how consensus works and would prevent real-time market optimization.  

Meanwhile, new attack vectors such as **transaction simulation spoofing** show that malicious MEV cannot be captured by heuristics alone. The problem is structural: the TOCTOU gap allows outcomes to diverge between simulation and execution. This undermines user trust and increasingly blocks institutional adoption, where financial regulation expects **execution fidelity**: what a client signs must be exactly what is executed.  

Wallets already warn that the simulations they display are not enforceable, since they are run in safe environments without block building or MEV. For users, however, it is damaging to trust when the actual outcome differs completely from what was shown in the simulation.  

---

## Proposed Approach: Transaction Contractualization via User Intent  

Users already rely on transaction simulation in their wallets. The simulation outcome represents the user’s expectation of what the transaction will produce at that moment.  

Our approach encodes this simulation outcome as part of the signed intent. When block builders assemble a block, they re-simulate transactions in final order before block proposal:  

- If the execution matches the user-signed simulation → the transaction is included.  
- If it does not match → the transaction is dropped.  

This mechanism enforces **transaction contractualization** between the blockchain and its users: transactions are only validated if they continue to reflect the user’s declared intent.  

By doing so, the system reliably prevents **Mafia EV** and attacks such as **transaction simulation spoofing**. For example, if a block searcher attempts a sandwich attack, the front-running transaction will alter the user’s outcome. During the in-block simulation, our comparison algorithm will detect this discrepancy and drop the victim’s transaction (or invalidate the entire bundle).  

In practice, this changes the financial incentives:  
- If a sandwich bundle is submitted, the victim’s transaction will be invalidated, meaning the attacker’s bribe cannot be collected or must be paid from the attacker’s own funds.  
- If the attacker’s transaction fails, the bundle becomes less profitable or is outright rejected by the validator.  

As equilibrium shifts, searchers will be incentivized to align their bundles with the same open simulation standard that block builders use. This ensures they get paid for their bundles and that block builders include their blocks.  

In other words, the financial game realigns: searchers are rewarded for respecting user intent rather than exploiting it. Malicious modifications that change a transaction’s expected outcome are penalized by design.  

---

## Limitations  

- **Monarch EV.** It increases transparency and accountability, making Monarch EV more measurable and auditable.
- **Moloch EV.** The proposal does not address Moloch EV.
- **Denial of Service.** Dropping transactions could be abused for low-cost DoS. Dropping is a user-controlled safeguard, not arbitrary censorship. Users can set acceptance criteria (like slippage to increase inclusion probability). 
- **Performance overhead.** Additional simulation and validation steps introduce slight overhead into block building, which may impact performance at scale.  
- **Auditability.** Dropped transactions are not visible on-chain. A domain-specific storage layer may be needed to record these events for traceability and accountability.  

---

## Implications  

- Reliably eliminates **Mafia EV** (malicious MEV and spoofing) in a transparent, auditable, and straightforward way.  
- Provides visibility into, though does not fully eliminate, **Monarch EV** (e.g., liquidations and builder reordering).  
- Leaves **Moloch EV** (coordination failures such as gas wars) unaddressed, but complements other solutions such as SUAVE or FOLIC.  
- Stays fully aligned with Ethereum’s ethos of transparency, decentralization, and permissionlessness, while preserving market efficiency.  

---

# Plan and Deliverables  

# Plan and Deliverables  

**Phases:**  

1. **Prototype Integration** — *1 month*  
   - Extend the modified REVM fork with intent-checking logic.  
   - Connect it to the existing open-source simulation tool.  

2. **Local Block Builder Testing** — *1 month*  
   - Deploy in a simulated block-building pipeline with realistic transaction load.  
   - Measure performance impact and block processing delay.  

3. **Data Structure Standard Research** — *1 month*  
   - Investigate and evaluate candidate data structures for encoding and comparing transaction simulations.  
   - Benchmark accuracy, efficiency, and robustness of comparison methods.  
   - Publish test results and recommend a standard format for adoption.  

4. **Evaluation & Documentation** — *1 month*  
   - Produce benchmarks, attack case studies, and design trade-offs.  
   - Document integration path for mainnet builders and SUAVE.  

**Deliverables:**  
- Modified REVM fork with intent-validation logic.  
- Integration with open-source simulation tool for end-to-end flow.  
- Performance benchmarks and evaluation report.  
- Demonstration dataset showing blocked malicious transactions.  
- Reference specification for transaction contractualization, enabling builders and SUAVE researchers to evaluate standardization paths.

---

# Previous Work and Continuation

I am an ESP Q1 grantee under the ETHRangers Program.  

This proposal builds on my earlier work investigating advanced phishing vectors such as **Transaction Simulation Spoofing**. During implementation, I realized the same approach also mitigates sandwich attacks and, more broadly, many attacks that exploit the mempool.  

A prototype was developed and successfully tested on Sepolia, showing promising results. The natural next step is to integrate this mechanism directly into the block-building pipeline.  

---

# References  

- ZenGo: *TOCTOU Attacks on Wallet Simulations* (Feb 2025) [Link](https://zengo.com/transaction-simulation-white-paper-ethereum-foundation-grant/)  
- ScamSniffer: *Transaction Simulation Spoofing — A New Threat in Web3* (Jan 2025) [Link](https://drops.scamsniffer.io/transaction-simulation-spoofing-a-new-threat-in-web3/)  
- Sun, S. *Short Note on {Monarch, Moloch, Mafia} Extractable Value* (Nov 2022) [Link](https://hackmd.io/@sxysun/short-note-ext)  
- Qin, K., Daian, P., et al. *Remeasuring the Arbitrage and Sandwich Attacks of Maximal Extractable Value in Ethereum* (May 2024) [Link](https://arxiv.org/abs/2405.17944)  
