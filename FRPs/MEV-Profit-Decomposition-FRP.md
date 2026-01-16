| id                                             | title                                                                  | team                                                                          | created    |
| ---------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------- |
| <leave blank -- will be assigned by reviewers> | On-Chain MEV Profit Decomposition via Sequential Attribution | Andrei Seoev, Yury Yanovich, Ksenia Kurinova, Anastasiia Smirnova, Aleksei Smirnov, Alisa Kalacheva | 2026-01-16 |

### Background and Problem Statement
The extraction of Maximal Extractable Value (MEV) is a permanent and defining feature of decentralized finance (DeFi) [1]. While significant research has focused on quantifying total MEV volume and mitigating its negative externalities, a fundamental analytical problem remains **unaddressed**: determining the precise on-chain origin of arbitrage profit.

When an arbitrage transaction extracts profit, we cannot currently answer:
> *Which specific prior transactions created this profit opportunity, and what was each one’s quantitative contribution?*

Current methods rely on simplistic, binary heuristics that are insufficient because they:

1.  **Fail to Quantify Contribution:** Cannot determine *how much* a specific transaction contributed to the final profit.
2.  **Ignore Complex Interactions:** Break down when multiple transactions collectively create an arbitrage opportunity.
3.  **Overlook the Initial State:** Cannot separate profit arising from pre-existing blockchain state disbalances from profit created by transactions within the block.

This analytical gap hinders progress in critical areas:
*   **Protocol Design & Fee Mechanisms:** Developers cannot measure which protocols generate MEV opportunities, making optimal fee structure design impossible.
*   **MEV Supply Chain Analysis:** We cannot trace the economic flow of value from "producers" of disbalance to "consumers" (arbitrageurs).
*   **Strategic Development:** Searchers cannot systematically decompose complex opportunities for more sophisticated strategy design.

**Crucially, this problem is distinct from builder-searcher payment allocation.** Mechanisms like the Flashbots refund rule distribute a builder's profit among searchers but do not address the fundamental question of *how individual on-chain arbitrage profits originate from prior on-chain activity.*

This type of attribution is a prerequisite for reasoning about future MEV mitigation mechanisms. Without a clear understanding of which on-chain actions generate arbitrage profit and in what proportions, it becomes difficult to design principled auction rules, incentive mechanisms, or protocol-level interventions that target the source of MEV instead of its downstream effects.



### Our Idea: Sequential Profit Attribution via Shapley Values
We propose a novel framework for **on-chain MEV profit decomposition** that moves beyond heuristics to mathematically rigorous analysis. We conceptualize the block as a **temporally-ordered cooperative game** where:

*   **Players:** The initial blockchain state plus all transactions preceding an Atomic Arbitrage (AA) transaction in block order.
*   **Value Function:** The profit of the AA transaction when executed after different subsets of preceding transactions.
*   **Goal:** To fairly allocate the AA's total profit among these players based on their marginal contributions to creating the disbalance.

The core of our method is the **Shapley value**, a solution concept from cooperative game theory that ensures mathematically fair attribution based on each player's average marginal contribution across all possible transaction sequences.

**Our approach focuses exclusively on on-chain analysis:** we decompose the profit of individual arbitrage transactions into contributions from prior transactions, respecting the blockchain's linear execution order. This differs fundamentally from auction-based attribution mechanisms that allocate builder revenue among bidding searchers.

To make this analysis both theoretically sound and computationally feasible, we will deliver:

1.  **A Formal Sequential Attribution Model:** Defining the precise cooperative game for any AA transaction, specifying how profit varies with different subsets of preceding transactions, explicitly accounting for pool fees and network costs.
2.  **A Criterion for Minimal Sufficient Transaction Sets:** Establishing a practical criterion to limit analysis to only those transactions that interact with pools relevant to the AA, dramatically reducing computational complexity while preserving attribution accuracy.
3.  **An Algorithm for Efficient Marginal Contribution Calculation:** Developing an algorithm that leverages the structure of liquidity pools to prune unprofitable transaction sequences early in simulation, enabling practical computation of Shapley values.
4.  **Empirical Analysis of MEV Generation Patterns:** Applying our methodology to real blockchain data (focusing on Ethereum and Polygon) to provide the first quantitative analysis of how arbitrage profit decomposes across prior transactions and initial state.

### Deliverables
This project will produce two concrete outputs for the Flashbots community and broader research ecosystem:

*   **Research Paper:** A comprehensive academic paper detailing the sequential attribution model, the computational criterion and algorithm, and empirical findings from our analysis of real blockchain data.
*   **Public Dissemination:** Presentation of findings through a summary blog post to make the insights accessible to a broader audience.

The proposed research is planned for a 12-week timeline. Empirical evaluation will focus on Polygon and Ethereum, while the attribution framework will remain applicable to any EVM-compatible network.

### Team Background
Our team possesses a unique blend of theoretical and practical expertise in MEV and blockchain economics:

*   **Proven MEV Research Capability:** Prior work on atomic arbitrage classification [4] and RL-based MEV extraction [3] demonstrates hands-on experience in identifying and analyzing MEV transactions at scale.
*   **Deep DeFi and Modeling Expertise:** Research on concentrated liquidity market makers [5] and DeFi risk assessment [6] provides the foundation for accurately modeling complex AMM behaviors.
*   **Strong Data Analysis and Blockchain Forensics:** Experience with transaction graph analysis [7] ensures we can handle the large-scale data processing required for this research.

We are uniquely positioned to execute this research, bridging game-theoretic foundations with practical on-chain analytics.

### References
[1] Daian, P., et al. "Flash boys 2.0: Frontrunning in decentralized exchanges, miner extractable value, and consensus instability." *2020 IEEE Symposium on Security and Privacy (SP)*. IEEE, 2020.

[2] Torres, C. F., Camino, R., & State, R. "Frontrunner jones and the raiders of the dark forest: An empirical study of frontrunning on the ethereum blockchain." *30th USENIX Security Symposium*, 2021.

[3] Seoev, A., et al. "The Bidding Games: Reinforcement Learning for MEV Extraction on Polygon Blockchain." *arXiv preprint arXiv:2510.14642* (2025).

[4] Vostrikov, D., et al. "Unpacking Maximum Extractable Value on Polygon: A Study on Atomic Arbitrage." *IEEE ICBC* (2025).

[5] Urusov, A., Berezovskiy, R., & Yanovich, Y. "Backtesting framework for concentrated liquidity market makers on Uniswap V3." *Blockchain: Research and Applications* (2025).

[6] Melnikov, I., et al. "DeFi Risk Assessment: MakerDAO Loan Portfolio Case." *Blockchain: Research and Applications* (2024).

[7] Larionov, N., Yanovich, Y. "Bitcoin Shared Send Transactions Untangling in Numbers." IEEE Access (2023).


