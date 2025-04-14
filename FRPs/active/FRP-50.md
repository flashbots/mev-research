---
id: 50
title: Accelerating Narwhal DAGs with TEEs
team: Jialin Li, Tianyang Tao (NUS), Abhimanyu Rawat (Advaita Labs), Shashank Motepalli (UoT), and Jonathan Heiss (TUBerlin)
created: 2025-02-11
status: active
---

# Accelerating Narwhal DAGs with TEEs

## Background and Problem Statement

Blockchains have evolved significantly, currently key focus has been on improving throughput, as it directly impacts user experience, with performance determined by consensus algorithms and underlying hardware. However, the growing reliance on centralized entities like cloud providers threatens decentralization, introducing risks such as censorship and control. Directed Acyclic Graph (DAG)-based blockchains [1], such as those using Narwhal and Tusk, have innovated by decoupling transaction dissemination from consensus ordering, enabling parallel block finalization and significantly boosting throughput. Despite this, communication overhead from verifying honest nodes remains a scalability bottleneck.

Trusted Execution Environments (TEEs) offer a promising solution by providing cryptographic guarantees for execution integrity, reducing communication and verification costs. Recent research [2] by Motepalli, Livshits, and others proposes "TEEifying" [3] Narwhal mempool-based protocols like Bullshark, Tusk, and Mysticeti, demonstrating how TEEs can optimize performance and scalability. However, no empirical work has yet explored TEE integration with Narwhal mempool and X consensus protocols.

This research aims to investigate how TEEs can enhance the performance of DAG-based protocols, focusing on both basic (e.g., Bullshark, Tusk) and advanced (e.g., Mysticeti, Shoal++) implementations, while exploring the integration of these TEE-enhanced protocols with EVM-like execution environments. By leveraging TEEs, we can establish a network of validator nodes with reduced communication overhead, enabling shared sequencing scenarios and improving throughput, particularly when paired with a lightweight EVM-DAG implementation such as [Weld](https://github.com/MaanavKhaitan/weld) to model transaction execution and consensus bottlenecks. Additionally, TEEs offer data confidentiality, which could influence strategies around Miner Extractable Value (MEV) [4], providing insights into how secure execution impacts ordering and scalability in DAG-based systems.

We distinguish between basic DAG-based protocols, such as Bullshark and Tusk, and advanced protocols, like Mysticeti and Shoal++. Bullshark and Tusk employ regular, round-based DAG structures where validators propose blocks linked to prior rounds in a predictable, linear fashion, assuming synchronous networks with bounded delays for consensus finality; this simplicity ensures efficiency but limits adaptability to variable conditions. In contrast, advanced protocols like Mysticeti and Shoal++ enhance performance through complexity, leveraging partial synchrony with dynamic, denser DAG topologies to achieve low-latency commits and high-throughput parallel block processing, respectively. This research evaluates how TEEs can augment both categories, reducing overhead in the structured designs of Bullshark and Tusk while amplifying the scalability of advanced implementations.

The goal of this study is to provide foundational insights [5] into the integration of TEEs with Narwhal-based protocols, demonstrating their potential to enhance throughput and reduce latency, while also exploring their compatibility with EVM-like execution environments. This research will pave the way for future protocols to consider TEEs as an essential component in designing scalable and efficient consensus mechanisms.

## Plan and Deliverables

Our team—Jialin Li, Tianyang Tao (NUS & Advaita Labs), Abhimanyu Rawat (UPF & Advaita Labs), Shashank Motepalli (UoT), and Jonathan Heiss (TUBerlin)—brings complementary expertise to this project. Li, a professor at NUS and domain expert in distributed systems, specializes in BFT and DAG-based protocols; Tao and Rawat contributes strong algorithmic, cryptographic optimizations and systems knowledge; Heiss focuses on TEE implementations; Motepalli co-authored theoretical evaluations of TEEs with DAG protocols. We currently possess code for most Narwhal-based DAG implementations and preliminary mempool benchmarks, facilitating a swift start to experimentation. This 7-month plan reflects the time-intensive nature of blockchain deployment and evaluation, with phases designed for rapid, iterative progress leveraging our existing resources.


### 1. Analyze Narwhal Mempool Performance
**Objective:** Identify bottlenecks in transaction dissemination, batch creation, and certification.
**Approach**: Conduct an analytical evaluation of Narwhal’s Rust implementation, modeling transaction workloads—including those from an EVM-like execution environment—to assess baseline performance, with a focus on communication delays and computational costs.
**Time**: 1 month (April 2025)
**Details**:
- **Libraries**: Narwhal’s Rust implementation Bullshark, Tusk, Mysticeti, etc. are publicly available.
- **Methodology**: Analytical modeling of mempool dynamics.
- **Workload**: Synthetic transactions of [Mysticeti orchestrator](https://github.com/MystenLabs/mysticeti/tree/main/orchestrator), combined with EVM-like transactions generated by [Weld](https://github.com/MaanavKhaitan/weld), can be used.
- **Hardware**: Local machines for modeling, leveraging existing code.
- **Metrics**: Latency (ms), Throughput (tx/s), communication overhead (bytes), etc.
- **Deliverable:** Report with quantitative metrics on communication and computational overheads, including initial EVM compatibility insights.

### 2. Evaluate Narwhal-Based Consensus Protocols
**Objective:** Assess protocols like Bullshark, Tusk, Shoal++ and Mysticeti for performance trade-offs.
**Approach:** Perform a primarily analytical assessment of these protocols using Narwhal’s Rust library, modeling behavior under synthetic workloads to study protocol-specific optimizations (e.g., Tusk’s batching, Mysticeti’s latency reduction), supplemented by targeted empirical experiments on a small testnet (10 nodes) to validate analytical findings.
**Time:** 1-2 months
**Details**:
- **Hardware**: Cloud-based nodes (e.g., AWS EC2 instances, Phala TEE cloud nodes) for testnet.
- **Optimization Insights**: Refers to protocol-specific insights (e.g., Bullshark’s simplicity, Shoal++’s parallelism, and EVM-like execution constraints) along with theoretical latency trade-offs.
- **Deliverable:** Technical document with flow diagrams and optimization insights of each protocol’s DAG structure and performance trade-offs (e.g., latency vs. throughput).

### 3. Propose and Simulate Enhancements
**Objective:** Develop and test hypotheses for improving Narwhal’s efficiency.
**Approach**: Model enhancements (e.g., optimized batching) analytically, then simulate on the existing testnet to project gains. A concise simulation phase builds on prior results, enabled by our code access.
**Time:** 1-2 months
**Hypotheses**:
- TEEs in batch certification reduce communication overhead.
- TEE-enhanced commit rules cut latency in different synchrony models.
- **Efficacy Goals**: Increase throughput, reduce latency, and enhance scalability for different existing DAG designs.
- **Deliverable:** Proposed optimizations with performance projections.

### 4. Design TEE Integration
**Objective:** Integrate TEEs to reduce overhead in batch certification and transaction ordering.
**Approach**: Design a TEE-enhanced Narwhal architecture in Rust, implementing it with cloud-based TEE nodes (mostly Phala based TDX nodes) and testing with different protocols.
**Time:** 2 months
**Details**:
- **Protocols**: Bullshark, Tusk, Mysticeti, Shoal++ (covering basic and advanced DAGs).
- **TEEs**: Intel TDX (via Phala network), chosen for its node management and availability.
- **Focus**: Primarily consensus layer (certification, latency, ordering, etc.)
- **Deliverable:** Architectural proposal detailing TEE deployment, with expected performance and security benefits.  

### 5. Validate and Publish Findings
**Objective:** Prototype TEE-enhanced Narwhal, conduct experiments, and summarize results.
**Approach**: Deploy a TEE-enhanced testnet (TDX nodes), benchmark against baseline Narwhal across protocols, and draft a paper.
**Time:** 1-2 months
**Details**:
- **Experiments**: Compare TEE-enhanced vs. baseline performance (throughput, latency, overhead) under synthetic txs; test fault tolerance with node failures; measure TEE attestation overhead.
- **Setting vs. #1**: Follows Phase 1’s Narwhal Rust library, and metrics (throughput, latency, overhead), but uses Phala TDX nodes (not local machines) and empirical testing (not analytical modeling).
- **Deliverable:** Empirical benchmarks and a research paper encompassing the overall process.

## References
* [1] SoK: DAG-based Blockchain Systems: https://dl.acm.org/doi/abs/10.1145/3576899 
* [2] Rorqual: Speeding up Narwhal with TEEs: https://arxiv.org/pdf/2408.14099 
* [3] ETH++: A roadmap to (real) decentralization in a world of centralized power:  https://www.youtube.com/watch?v=ivuV-H3UUtA 
* [4] Unichain: https://docs.unichain.org/whitepaper.pdf
* [5] Flashbots report: System requirements, existing and new solutions, and their efficiency: https://www.commonprefix.com/static/clients/flashbots/flashbots_report.pdf
