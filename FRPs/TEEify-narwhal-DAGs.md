---
id: <leave blank -- will be assigned by reviewers>
title: Accelerating Narwhal DAGs with TEEs
team: Jialin Li, Tianyang Tao (NUS), Abhimanyu Rawat (Advaita Labs), Shashank Motepalli (UoT), and Jonathan Heiss (TUBerlin)
created: 2025-02-11
---

# Accelerating Narwhal DAGs with TEEs

## Background and Problem Statement

Blockchains have evolved significantly, currently key focus has been on improving throughput, as it directly impacts user experience, with performance determined by consensus algorithms and underlying hardware. However, the growing reliance on centralized entities like cloud providers threatens decentralization, introducing risks such as censorship and control. Directed Acyclic Graph (DAG)-based blockchains [1], such as those using Narwhal and Tusk, have innovated by decoupling transaction dissemination from consensus ordering, enabling parallel block finalization and significantly boosting throughput. Despite this, communication overhead from verifying honest nodes remains a scalability bottleneck.

Trusted Execution Environments (TEEs) offer a promising solution by providing cryptographic guarantees for execution integrity, reducing communication and verification costs. Recent research [2] by Motepalli, Livshits, and others proposes "TEEifying" [3] Narwhal mempool-based protocols like Bullshark, Tusk, and Mysticeti, demonstrating how TEEs can optimize performance and scalability. However, no empirical work has yet explored TEE integration with Narwhal mempool and X consensus protocols.

This research aims to investigate how TEEs can enhance the performance of DAG-based protocols, focusing on both basic (e.g., Bullshark) and advanced (e.g., Mysticeti, Shoal++) implementations. By leveraging TEEs, we can establish a network of validator nodes with reduced communication overhead, enabling shared sequencing scenarios and improving throughput. Additionally, TEEs offer data confidentiality, which could influence strategies around Miner Extractable Value (MEV) [4].

The goal of this study is to provide foundational insights [5] into the integration of TEEs with Narwhal-based protocols, demonstrating their potential to enhance throughput and reduce latency. This research will pave the way for future protocols to consider TEEs as an essential component in designing scalable and efficient consensus mechanisms.

## Plan and Deliverables

### 1. Analyze Narwhal Mempool Performance  
**Objective:** Identify bottlenecks in transaction dissemination, batch creation, and certification.  
**Deliverable:** Report with quantitative metrics on communication and computational overheads.  

### 2. Evaluate Narwhal-Based Consensus Protocols  
**Objective:** Assess protocols like Bullshark, Tusk, and Mysticeti for performance trade-offs.  
**Deliverable:** Technical document with flow diagrams and optimization insights.  

### 3. Propose and Simulate Enhancements  
**Objective:** Develop and test hypotheses for improving Narwhal’s efficiency.  
**Deliverable:** Proposed optimizations with performance projections.  

### 4. Design TEE Integration  
**Objective:** Integrate TEEs to reduce overhead in batch certification and transaction ordering.  
**Deliverable:** Architectural proposal with expected performance and security benefits.  

### 5. Validate and Publish Findings  
**Objective:** Prototype TEE-enhanced Narwhal, conduct experiments, and summarize results.  
**Deliverable:** Empirical benchmarks and a publishable research paper.  

## References
* [1] SoK: DAG-based Blockchain Systems: https://dl.acm.org/doi/abs/10.1145/3576899 
* [2] Rorqual: Speeding up Narwhal with TEEs: https://arxiv.org/pdf/2408.14099 
* [3] ETH++: A roadmap to (real) decentralization in a world of centralized power:  https://www.youtube.com/watch?v=ivuV-H3UUtA 
* [4] Unichain: https://docs.unichain.org/whitepaper.pdf
* [5] Flashbots report: System requirements, existing and new solutions, and their efficiency: https://www.commonprefix.com/static/clients/flashbots/flashbots_report.pdf
