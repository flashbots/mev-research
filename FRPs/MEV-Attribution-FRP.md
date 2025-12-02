| id                                             | title                                                                  | team                                                                          | created    |
| ---------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------- |
| <leave blank -- will be assigned by reviewers> | MEV Attribution Framework | Andrei Seoev, Yury Yanovich, Ksenia Kurinova, Anastasiia Smirnova, Aleksei Smirnov, Alisa Kalacheva | 2025-12-02 |

# MEV Attribution Framework

## Background and Problem Statement

The extraction of Maximal Extractable Value (MEV), which refers to profit gained by strategically adding, removing, or reordering transactions in a block, has become a permanent and defining feature of decentralized finance (DeFi) [1]. The ecosystem is often described as a "dark forest" where any profitable transaction visible in the public mempool is quickly discovered and exploited.

While significant research and infrastructure development (e.g., MEV-Boost, MEV-Share) has focused on quantifying total MEV volume and mitigating its negative externalities, a fundamental problem remains largely unaddressed: **MEV Attribution**.

When an arbitrageur extracts profit, who or what created the opportunity?  
The current state of the art relies on simplistic, binary heuristics. These methods are insufficient because they:

- **Fail to Quantify Contribution:** They cannot determine how much a specific transaction contributed to the final profit.
- **Ignore Complex Interactions:** They break down in the presence of multiple, interdependent opportunity and arbitrage transactions within a single block.
- **Overlook the Initial State:** They do not cleanly separate profit arising from pre-existing blockchain state disbalances from profit created by transactions within the block.

This lack of a rigorous attribution model hinders progress in several critical areas:

- **Fairness and Accountability:** It is currently impossible to determine which users and protocols are the primary “sources” of MEV.
- **MEV Supply Chain Analysis:** We cannot properly model the economic flow of value from “producers” of disbalance to “consumers” (arbitrageurs).
- **Advanced MEV Strategies:** Searchers cannot systematically decompose arbitrage opportunities into contributing components.

Our research aims to solve this by formalizing MEV attribution as a problem of **fair value distribution in a cooperative system**, drawing on concepts from game theory.  
The results will support more transparent benchmarking of protocol design and more informed discussion about mitigation, fairness, and infrastructure evolution across DeFi.

---

## Our Idea: A Shapley Value-Based Attribution Model

We propose a novel framework for MEV attribution that moves beyond heuristics to a mathematically rigorous model. We conceptualize a block as a cooperative game where:

- **Players:** The set of transactions in a block preceding an Atomic Arbitrage (AA) transaction, plus the initial blockchain state.
- **Value Function:** The profit of the AA transaction, a function of state changes induced by a coalition (subset) of preceding transactions.
- **Goal:** To fairly allocate the total arbitrage value among protocols based on their inferred contribution.

The core of our method is the Shapley value, a cooperative game theory concept known for its fairness properties (efficiency, symmetry, linearity, null player).

To make this tractable and theoretically sound, we will deliver four key components:

### 1. Formal Attribution Model
Define the cooperative game for a given AA transaction, specifying the player set and profit function \(V(S)\) for every subset \(S\). Explicitly account for pool fees (τ) and network costs (β) as friction.

### 2. Criterion for Minimal Sufficient Transaction Sets
The combinatorial explosion of subsets is a primary challenge. We will define a practical criterion that restricts the player set to transactions interacting with pools relevant to the AA.

### 3. Algorithm for Effective Search Path Reduction
Computing Shapley values requires simulating AA profit across many orderings. We design an algorithm leveraging liquidity pool structure and the constant-product formula to prune “fail paths.”

### 4. Analysis Framework and Numerical Insights
We will implement the model, the transaction set criterion, and the pruning algorithm in a framework suitable for examining MEV attribution on EVM-compatible chains. Initial analysis will focus on Ethereum and Polygon.


---

## Deliverables

This project will produce:

1. **Research Paper:** Comprehensive description of the model, algorithms, and empirical results.
2. **Attribution Framework Implementation:** Internal implementation used to conduct the analysis and generate results.

3. **Public Dissemination:** A summary blog post explaining findings to a broader audience.

The proposed research is planned for a 12 week timeline. Empirical evaluation will focus on Polygon and Ethereum, while the attribution framework and software implementation will remain applicable to any EVM-compatible network.

---

## Team Background

Our team has a unique blend of theoretical and practical expertise in MEV and blockchain economics, as evidenced by our publication record.


- Proven MEV Research Capability: Our prior work "The Bidding Games: Reinforcement Learning for MEV Extraction on Polygon Blockchain" [3] and "Unpacking Maximum Extractable Value on Polygon: A Study on Atomic Arbitrage" [4] demonstrates deep hands-on experience in identifying, classifying, and analyzing MEV transactions.

- Deep DeFi and Modeling Expertise: Our research on concentrated liquidity market makers [5] and DeFi risk assessment [6] provides the necessary foundation for accurately modeling the behavior of complex AMMs and the financial interactions within blocks.

- Strong Data Analysis and Blockchain Forensics: Our experience with Bitcoin transaction graph analysis [7] ensures we can handle the large-scale data processing and forensic analysis required to dissect blockchain blocks effectively.

We are uniquely positioned to execute this research, bridging the gap between abstract game theory and the messy reality of on-chain data.

---

## References

[1] Philip Daian, Steven Goldfeder, Tyler Kell,  Yunqi Li, Xueyuan Zhao, Iddo Bentov, Lorenz Breidenbach, Ari Juels. “Flash boys 2.0: Frontrunning in decentralized exchanges, miner extractable value, and consensus instability.” In 2020 IEEE symposium on security and privacy (SP) (pp. 910-927). IEEE. (2020).

[2] Torres, C. F., Camino, R., & State, R. (2021). Frontrunner jones and the raiders of the dark forest: An empirical study of frontrunning on the ethereum blockchain. Proceedings of the 30th USENIX Security Symposium. 

[3] **Andrei Seoev**, Leonid Gremyachikh, **Anastasiia Smirnova**, Yash Madhwal, **Alisa Kalacheva**, Dmitry Belousov, Ilia Zubov, **Aleksei Smirnov**, Denis Fedyanin, Vladimir Gorgadze, **Yury Yanovich** "The Bidding Games: Reinforcement Learning for MEV Extraction on Polygon Blockchain." arXiv preprint arXiv:2510.14642 (2025). 

[4] Daniil Vostrikov, Yash Madhwal, **Andrey Seoev**, **Anastasiia Smirnova**, **Yury Yanovich**, **Alexey Smirnov**, Vladimir Gorgadze. "Unpacking Maximum Extractable Value on Polygon: A Study on Atomic Arbitrage." IEEE ICBC (2025). 

[5] Urusov, A., Berezovskiy, R., & **Yanovich, Y**. "Backtesting framework for concentrated liquidity market makers on Uniswap V3." Blockchain: Research and Applications (2025). 

[6] Melnikov, I., Lebedeva, I., Petrov, A., **Yanovich, Y.** "DeFi Risk Assessment: MakerDAO Loan Portfolio Case." Blockchain: Research and Applications (2024). 

[7] Larionov, N., **Yanovich, Y.** "Bitcoin Shared Send Transactions Untangling in Numbers." IEEE Access (2023).
