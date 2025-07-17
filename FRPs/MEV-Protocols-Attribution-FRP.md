| id                                             | title                                                                   | team                                                                          | created    |
| ---------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------- |
| <leave blank -- will be assigned by reviewers> | MEV Attribution to Protocols via Opportunity Transaction Tracing        | MEV-X | 2025-07-17 |

# **MEV Attribution to Protocols via Opportunity Transaction Tracing**

## **Summary**

This proposal presents a methodology and study aimed at attributing atomic arbitrage MEV (AA MEV) to the protocols that generate it. Specifically, we focus on identifying opportunity transactions (OppTx) - user-originated interactions that create short-term arbitrage windows - and quantifying the resulting MEV extracted from them.  

We apply a simulation-based technique: for each detected arbitrage transaction, we locate its corresponding OppTx by simulating swaps in adjacent transactions using a binary search over the block’s timeline. Once the OppTx is found, we attribute it to the protocol responsible for triggering the price shift, using call context and semantic classification of contract interactions. This allows us to compute how much arbitrage value is attributable to each protocol - both in total and normalized by that protocol’s aggregate transaction activity.

Our study will focus on Polygon, Arbitrum, and Base networks, and will produce a detailed MEV attribution map across major DeFi protocols. In doing so, we introduce a framework compatible with any EVM-based chain. This dataset will provide protocol developers, infrastructure researchers, and governance stakeholders with the first structured quantification of how DeFi designs generate MEV at the point of interaction - a currently missing piece in ecosystem-wide MEV understanding.

## **Background and Problem Statement**

MEV-X is a research-driven team focused on MEV extraction, classification, and empirical measurement. Over the past two years, we have executed over 400,000 MEV transactions and developed a modular infrastructure for data extraction, arbitrage classification, and transaction-level analysis. Our previous study of atomic MEV on Polygon - covering over 23 million blocks - was accepted at IEEE ICBC 2025 and summarized publicly [here](https://github.com/seoeva/MEV-X-Researches/blob/main/Unpacking_Maximum_Extractable_Value_on_Polygon-A_Study_on_Atomic_Arbitrage.pdf). 

All of our academic work is conducted in close collaboration with an experienced scientific advisor, who supervises and co-authors our research publications, including the paper accepted to IEEE ICBC 2025. His academic profile can be reviewed [here](https://scholar.google.com/citations?user=z4O6KWwAAAAJ). We are also actively engaged with the blockchain research program at MIPT (Moscow Institute of Physics and Technology), where our team contributes to applied MEV research and protocol analysis.

However, that work concentrated on the execution side of MEV: searcher strategies, inclusion methods, and network-level efficiency. What remains largely unexamined is where MEV originates - which protocols and transaction types create extractable value, and at what frequency and scale. In practice, many DeFi protocols unintentionally generate arbitrage opportunities. The protocols responsible for creating these opportunities are rarely identified, and the cumulative cost imposed on users remains unquantified.

This research aims to close that gap by introducing a reproducible framework for tracing MEV back to the protocol-level transaction that caused it, and generating per-protocol MEV attribution metrics.

## **Research Objectives**

- Formally define Opportunity Transactions (OppTx) as user-initiated economic interactions (e.g., swaps) that introduce price discrepancies subsequently captured through atomic arbitrage - either in the same block or shortly after.

- Develop a reproducible method for identifying OppTx, using binary search and simulation to determine which preceding transaction enabled a known arbitrage event.

- Attribute each OppTx to a protocol, using heuristics based on transaction structure, routing logic, and contract interaction patterns.

- Compute the following metrics per protocol:

  - Total attributed MEV (in both native token and USD terms),

  - Protocol share of all attributable MEV across the dataset.

- Produce a structured attribution dataset and a scientific publication, summarizing the findings from Polygon, Arbitrum, and Base, with applicability to other EVM-based environments.

## **Plan and Deliverables**

The proposed research will be executed over three structured phases across 12–14 weeks. The study will focus on Polygon, Arbitrum, and Base, while the methodology will remain applicable to any EVM-compatible network.

### **Phase 1 - Opportunity Transaction Identification and Attribution (Weeks 1–4)**

- Develop a standalone simulation-based module to identify Opportunity Transactions (OppTx) by performing binary search across block transaction timelines around known arbitrage events.

- Establish confidence in the identification method by verifying OppTx–AA transaction pairs in manually reviewed examples and edge cases.

- Attribute each identified OppTx to a specific protocol using heuristics based on transaction structure, routing behavior, and contract context.

- Maintain a structured record linking each identified OppTx to its originating protocol, enabling accurate aggregation of MEV attribution statistics in later phases.

### **Phase 2 - Metric Computation and Aggregation (Weeks 5–9)**

- Aggregate per-protocol MEV attribution data and compute:

  - Total MEV attributed to each protocol (in native tokens/USD),

  - Per-protocol MEV share (the proportion of total attributed AA MEV generated by each protocol, measured relative to the cumulative MEV we were able to trace to identifiable sources).

  - Normalized MEV exposure relative to protocol-level transaction activity (e.g., swap count or volume).

- Identify major sources of MEV leakage across protocols and assess distribution patterns within and between networks.

### **Phase 3 - Synthesis and Publication (Weeks 10–14)**

- Finalize per-protocol MEV attribution datasets for Polygon, Arbitrum, and Base.

- Document core findings, trends, and implications in a peer-reviewed academic paper to be submitted to a relevant research venue.

- Prepare an ecosystem-facing summary report outlining methodology, protocol-level results, and broader relevance.

- Optionally deliver a presentation or webinar summarizing the study for a general technical audience.

## **Deliverables and Impact**

This project will produce three core outputs:  

**1. Research Paper and Conference Submission**  
We will document our methodology, findings, and attribution framework in a formal academic paper. The paper will be submitted to a peer-reviewed venue focused on blockchain systems. Target venues include journals such as Blockchain: Research and Applications, Financial Innovation, and IEEE Transactions on Information Forensics and Security, as well as conferences like IEEE ICBC, IEEE ICDCS, and IEEE COINS. Final selection will depend on thematic fit and submission deadlines. 

**2. Protocol-Level MEV Attribution Results**  
We will provide aggregated results detailing the MEV attributed to major DeFi protocols across Polygon, Arbitrum, and Base. These results - expressed in both native tokens and USD - will be included in the research paper and accompanying report, enabling comparative analysis and independent interpretation without requiring access to full raw data. 
 
**3. Public Report and Summary for Ecosystem Stakeholders**  
We will produce a concise, non-technical summary of our key findings. This report will provide protocol teams, researchers, and governance participants with accessible insights into how MEV is created at the application layer - and which designs contribute most to value extraction.

## **Why This Matters**

While most MEV studies focus on who extracts value, our work addresses a neglected but critical question: where that value originates. By shifting the focus from extraction to attribution, this project introduces the first structured approach to quantifying MEV generation at the protocol level. The results will support more transparent benchmarking of protocol design and enable more informed discussion about mitigation, fairness, and infrastructure evolution across DeFi.

## **References**

**Bagourd, Arthur, et al.** *Quantifying MEV on Layer 2 Networks.*  
arXiv preprint, September 2023.  
Quantitative analysis of MEV extracted on Layer 2 networks including Polygon, Arbitrum, and Optimism, leveraging adapted Flashbots mev-inspect tooling.  
https://arxiv.org/abs/2309.00629

**Gogol, Krzysztof, et al.** *Layer-2 Arbitrage: An Empirical Analysis of Swap Dynamics and Price Disparities on Rollups.*  
arXiv preprint, June 2024.  
Empirical investigation of swap behavior and arbitrage opportunities across Ethereum rollups (Arbitrum, Base, Optimism, zkSync), introducing metrics such as Maximal Arbitrage Value (MAV) and Liquidity Volume Ratio (LVR).
https://arxiv.org/abs/2406.02172

**Flashbots Collective.** *FRP-24: On the Quantification of MEV on L2s.*  
Flashbots Research Proposal, 2023.  
Research proposal focused on measuring MEV on Layer 2 networks, discussing methodological challenges and classification frameworks.  
https://collective.flashbots.net/t/frp-24-quantifying-mev-on-l2s/450

**Flashbots Collective.** *FRP-29: Research on MEV in L2 Blockchains.*  
Flashbots Research Proposal, 2024.  
Comprehensive overview of MEV research in Layer 2 blockchains, including sequencer decentralization and MEV extraction mechanisms.  
https://collective.flashbots.net/t/frp-29-research-on-mev-in-l2-blockchains/1617
