| id                                             | title                                                                  | team                                                                          | created    |
| ---------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------- |
| <leave blank -- will be assigned by reviewers> | Extracting Atomic Arbitrage MEV on L2: A Multi-Chain Measurement Study | MEV-X — a research-driven group focused on on-chain MEV analysis and modeling | 2025-05-27 |

# **Extracting Atomic Arbitrage MEV on L2: A Multi-Chain Measurement Study**

## **Summary**

This proposal outlines a plan to conduct a rigorous measurement study of atomic arbitrage MEV (AA MEV) across multiple Layer 2 Ethereum networks: Polygon, Arbitrum, and Base. Our objective is to extract and quantify atomic arbitrage activity using on-chain data, classify execution strategies, and evaluate the impact of protocol architecture and infrastructure (e.g., auction systems, sequencer models) on MEV dynamics.

The study will use a proven, production-grade analysis framework developed by our team at MEV-X. This framework includes pipeline modules for data ingestion, swap-level decoding, multi-hop arbitrage classification, and profitability analysis. In our prior work, this methodology was applied to Polygon over 23 million blocks, producing the most detailed empirical dataset on AA MEV to date on Polygon. We intend to extend the framework to Arbitrum and Base, incorporating additional protocols such as Curve, Uniswap V4, AAVE, and PMMs.

The expected outcomes include a dataset of atomic arbitrage on the three networks, a detailed analysis of MEV dynamics across ecosystems,and a scientific paper to be presented at an academic conference and submitted for peer-reviewed publication. Results will contribute to a clearer understanding of MEV in L2 and support future research and mitigation tooling.

## **Background and Problem Statement**

MEV-X is a research-driven project that has been actively working on MEV protection, extraction, and analysis. Our experience in identifying, modeling, and implementing MEV strategies has provided us with a deep understanding of how inefficient transaction ordering creates value extraction opportunities. Having built this foundation, we are now uniquely positioned - and highly motivated - to conduct a comprehensive market analysis of MEV activity across Polygon, Arbitrum, and Base.

Over the course of our work, we have executed over 300,000 successful MEV transactions on the Polygon network, gaining deep operational insight into real-world arbitrage mechanics. Building on this practical foundation, we conducted a comprehensive empirical study of atomic arbitrage MEV on Polygon, covering 22 months of on-chain data and more than 23 million blocks. The analysis showed that atomic arbitrage accounts for over $12 million in extracted MEV, representing approximately 1% of the chain’s total TVL. We identified a growing adoption of structured inclusion mechanisms, which - despite handling fewer transactions - enabled more efficient value capture and reduced network congestion. The study has been accepted for presentation at IEEE ICBC 2025 in Pisa, and a public summary is available [here](https://medium.com/@MEV-X/mev-trends-on-polygon-a-study-of-atomic-arbitrage-5ad569b0b550).

While Polygon served as a valuable initial testbed - it represents only one point in the broader Layer 2 design space. To develop a more complete understanding of how sequencer architecture, transaction ordering policies, and network-level infrastructure impact MEV dynamics, we aim to apply our methodology to Arbitrum and Base: two economically significant L2s that rely on centralized sequencers and first-come-first-served transaction ordering, without public mempools or formalized inclusion markets.

This study is designed to answer a set of foundational questions about the nature and structure of atomic arbitrage MEV across major Layer 2 networks. Specifically, we aim to:

- Quantify the volume, distribution, and economic impact of atomic arbitrage MEV on Polygon, Arbitrum, and Base using fully on-chain data.
- Assess how network architecture - particularly differences in sequencer models, mempool visibility, and inclusion mechanisms - influences MEV extraction strategies and outcomes.
- Compare the structure, latency, and profitability of arbitrage transactions across ecosystems with and without structured transaction ordering systems.
- Characterize searcher behavior and execution dynamics in the absence of public prioritization or auction-based mechanisms.
- Validate and adapt our existing methodology to new network environments and additional protocol standards such as Uniswap V4, Curve, AAVE, and PMMs.

By addressing these questions, the study will contribute to a deeper empirical understanding of how protocol design affects MEV behavior and help inform both theoretical modeling and future infrastructure development.

## **Plan and Deliverables**

The proposed research will be structured into three main phases, over approximately 12–14 weeks, depending on network trace access and infrastructure availability. Our goal is to extend the methodology previously applied to Polygon and produce comparable metrics for Arbitrum and Base.

### **Phase 1 – Infrastructure Extension and Protocol Coverage (Weeks 1–4)**

- Adapt our Polygon analysis pipeline to support Arbitrum and Base, including network-specific block parsing and pricing sources.
- Implement protocol-specific decoding modules for additional DeFi systems, including:
    - **Curve**,
    - **Uniswap V4**,
    - **AAVE v3**,
    - **PMM-based DEXs**.
- Validate swap decoding logic and multi-hop path extraction for each network.

### **Phase 2 – Arbitrage Identification and Classification (Weeks 5–9)**

- Apply our previously developed **heuristic criterion** to identify atomic arbitrage (AA) transactions:
    - Multi-swap structure (≥2 swaps),
    - Non-negative net asset delta,
    - Positive net profit after fees.
- Compute weekly aggregates and descriptive statistics, including:
    - **Total MEV extracted** (in native token and USD),
    - **Transaction count**, **searcher count**, and distribution of profitability,
    - **Per-transaction MEV statistics**: mean, median, min, max, and key percentiles,
    - **Swap count per transaction** (mean, median, distribution),
- For networks or periods where auction-based mechanisms are observed, optionally measure:
    - **Bid-based MEV share**, if applicable (e.g., through identifiable protocols with structured inclusion logic).
- Categorize strategy patterns (e.g., high-frequency low-value spam vs. infrequent high-precision arbitrage) based on behavioral clustering.
- For chains with centralized sequencers (e.g., Arbitrum and Base), we have observed that some arbitrage transactions occur in the next block (top-of-block), while others are backrun. Since there is no public mempool, we hypothesize that these transactions are routed through private RPC nodes that forward them as bundles to the sequencer. We aim to estimate the volume and frequency of such transactions to better understand private orderflow dynamics and searcher access patterns

### **Phase 3 – Comparative Analysis and Synthesis (Weeks 10–14)**

- Produce a chain-by-chain comparative study with:
    - Differences in MEV capture structure,
    - Observable impact of infrastructure,
- Measure relative latency and transaction density when feasible, based on known opportunity triggers and response timings.
- Analyze variance across protocols and time periods, identifying trends and saturation indicators.

### **Deliverables**

**Academic Paper and Conference Presentation**

We will prepare a formal research paper summarizing our methodology and findings across Polygon, Arbitrum, and Base. The paper will be submitted to a peer-reviewed venue (e.g., IEEE ICBC, FC) and presented at an academic conference.

**Public AA MEV Analysis Report**

A clear and accessible report will be published, covering:

- Overview of atomic arbitrage activity on the three networks
- Classification of execution patterns
- Extracted MEV metrics
- Observations on how network architecture influences MEV strategies

This report will be shared openly for use by researchers, developers, and the wider community.

**Community Summary and Presentation**

We will present our key findings in a short talk or article aimed at a general audience, with the goal of improving MEV visibility and understanding in the L2 ecosystem.

## **References**

1. **MEV-X.** *MEV Trends on Polygon: A Study of Atomic Arbitrage.*
    
    Medium blog post, 2025 (accepted at IEEE ICBC 2025).
    
    An empirical study focusing on atomic arbitrage MEV trends on Polygon, providing detailed analysis of MEV dynamics and extraction patterns.
    
   [https://medium.com/@MEV-X/mev-trends-on-polygon-a-study-of-atomic-arbitrage-5ad569b0b550](https://medium.com/@MEV-X/mev-trends-on-polygon-a-study-of-atomic-arbitrage-5ad569b0b550)
    
2. **Bagourd, Arthur, et al.** *Quantifying MEV on Layer 2 Networks.*
    
    arXiv preprint, September 2023.
    
    Quantitative analysis of MEV extracted on Layer 2 networks including Polygon, Arbitrum, and Optimism, leveraging adapted Flashbots mev-inspect tooling.
    
   [https://arxiv.org/abs/2309.00629](https://arxiv.org/abs/2309.00629)
    
3. **Gogol, Krzysztof, et al.** *Layer-2 Arbitrage: An Empirical Analysis of Swap Dynamics and Price Disparities on Rollups.*
    
    arXiv preprint, June 2024.
    
    Empirical investigation of swap behavior and arbitrage opportunities across Ethereum rollups (Arbitrum, Base, Optimism, zkSync), introducing metrics such as Maximal Arbitrage Value (MAV) and Liquidity Volume Ratio (LVR).
    
    [https://arxiv.org/abs/2406.02172](https://arxiv.org/abs/2406.02172)
    
4. **0x70562F91075eea0f87728733b4bbe00F7e779788.** *Deciphering L2 MEV: Sequencer Workflow & MEV Data Analysis.*
    
    Mirror.xyz blog post, 2024.
    
    Technical breakdown of Layer 2 sequencer operations and MEV extraction, discussing FCFS ordering, spam-based vs auction-based MEV strategies, and data analysis challenges.
    
    [https://mirror.xyz/0x70562F91075eea0f87728733b4bbe00F7e779788/QYpLM5ZJdSUKgaz6F8twtBFkHqwDnGTbQFAa55dr5so](https://mirror.xyz/0x70562F91075eea0f87728733b4bbe00F7e779788/QYpLM5ZJdSUKgaz6F8twtBFkHqwDnGTbQFAa55dr5so)
    
5. **Flashbots.** *Flashbots Auction Overview.*
    
    Official Flashbots documentation, 2021–2024.
    
    Overview of the Flashbots private sealed-bid auction mechanism designed to mitigate negative externalities of MEV extraction, relevant for understanding MEV ordering and latency considerations.
    
    [https://docs.flashbots.net/flashbots-auction/overview](https://docs.flashbots.net/flashbots-auction/overview)
    
6. **Flashbots Collective.** *FRP-24: On the Quantification of MEV on L2s.*
    
    Flashbots Research Proposal, 2023.
    
    Research proposal focused on measuring MEV on Layer 2 networks, discussing methodological challenges and classification frameworks.
    
   [https://collective.flashbots.net/t/frp-24-quantifying-mev-on-l2s/450](https://collective.flashbots.net/t/frp-24-quantifying-mev-on-l2s/450)
    
7. **Flashbots Collective.** *FRP-25: Quantifying Fairness Granularity for First-Come-First-Serve (FCFS) Chains.*
    
    Flashbots Research Proposal, 2024.
    
    Study on the impact of FCFS sequencer models on transaction ordering fairness and spam attack vectors in Layer 2 chains.
    
    [https://collective.flashbots.net/t/frp-25-quantifying-fairness-granularity-for-first-come-first-serve-fcfs-chains/1615](https://collective.flashbots.net/t/frp-25-quantifying-fairness-granularity-for-first-come-first-serve-fcfs-chains/1615)
    
8. **Flashbots Collective.** *FRP-29: Research on MEV in L2 Blockchains.*

	Flashbots Research Proposal, 2024.

	Comprehensive overview of MEV research in Layer 2 blockchains, including sequencer decentralization and MEV extraction mechanisms.

	[https://collective.flashbots.net/t/frp-29-research-on-mev-in-l2-blockchains/1617](https://collective.flashbots.net/t/frp-29-research-on-mev-in-l2-blockchains/1617)
