---
id: 
title: Exploring MEV Opportunities and mitigation strategies in Permissionless CDP Protocols
team: Mihail Kirov
created: 2024-12-28
---

# Exploring MEV Opportunities and mitigation strategies in Permissionless CDP Protocols

## Abstract  
Collateralized Debt Position (CDP) protocols, such as Liquity V2, are built to be fully permissionless, allowing anyone to participate as a borrower, supplier, or liquidator. This permissionless design introduces unique challenges and opportunities related to **Maximal Extractable Value (MEV)**, especially in liquidation events. This research explores the dynamics of public MEV opportunities within such protocols and evaluates potential modifications, such as Fully Homomorphic Encryption (FHE) and secondary liquidator auction markets, to mitigate vulnerabilities and improve fairness.

---

## Research Questions  
This research aims to address the following key questions:
1. **Liquidator Protection**: How can independent liquidators protect their liquidation opportunities from being front-run or invalidated in the MEV pipeline?  
2. **Borrower Safeguards**: How can borrowers protect themselves from malicious liquidators exploiting MEV opportunities?  
3. **State of Liquidator Auctions**: What is the current efficiency of liquidator auction mechanisms? How can liquidators increase the probability of their transactions succeeding in the presence of MEV?  
4. **Secondary Liquidator Markets**: Could a secondary market where liquidators bid for the right to liquidate a Trove improve fairness, profitability, or efficiency?

---

## Methodology  

### 1. Protocol and MEV Analysis  
- Conduct an in-depth exploration of the mechanics of Liquity V2, focusing on Trove liquidation opportunities.  
- Analyze the profitability of liquidation strategies under current MEV conditions.  

### 2. On-Chain Transaction Analysis  
- Use Testnet transaction data to study the behavior of liquidators and MEV bots.  
- Identify patterns, inefficiencies, and opportunities in liquidation transactions.  

### 3. Simulation of Auction Markets  
- Model a secondary liquidator auction market where liquidators bid for the right to execute liquidations.  
- Measure the impact of this market on profitability and security for both borrowers and liquidators.  

### 4. Evaluation of FHE Integration  
- Investigate the feasibility of integrating FHE into a Liquity V2 fork to secure sensitive liquidation computations.  
- Assess the implications for liquidators, borrowers, and protocol scalability.  

---

## Potential Implications  

### 1. Secondary Liquidator Markets  
- A structured auction market for liquidators could create a more competitive and secure environment, reducing the risks of frontrunning and increasing transparency.  
- Enhanced profit predictability and fairness for liquidators.  

### 2. Borrower Protections  
- FHE could provide borrowers with privacy-preserving safeguards against exploitative liquidators while maintaining protocol efficiency.  
- Improved borrower confidence in participating in CDP protocols.  

### 3. Protocol Evolution  
- Insights into MEV dynamics could guide protocol-level changes to improve fairness and reduce exploitability without sacrificing decentralization.  

### 4. Liquidation Pipeline Efficiency  
- Understanding the MEV pipeline’s impact on liquidations could lead to recommendations for optimizing liquidator strategies, improving the overall health of the ecosystem.  

---

## Limitations  

1. **Complexity of FHE**  
- Integrating FHE into permissionless protocols may introduce significant computational overhead and complexity, impacting scalability.  

2. **Simulation Constraints**  
- Simulated results for secondary liquidator markets may not fully reflect real-world behavior due to unpredictable MEV bot activity.  

3. **On-Chain Data Scope**  
- Analysis is limited to available data and may not capture off-chain strategies or private relays used by liquidators.  

---

## Background and Problem Statement

Collateralized Debt Position (CDP) protocols, such as Liquity V2, are central to the decentralized finance (DeFi) ecosystem. Their permissionless design allows anyone to participate as borrowers, suppliers, or liquidators. However, this permissionless nature creates a fertile ground for **Maximal Extractable Value (MEV)** exploitation, particularly in liquidation events where competition among liquidators can lead to inefficiencies, front-running, and loss of value for protocol participants.

MEV has become a critical area of research in DeFi due to its potential to both enhance and harm the ecosystem. While liquidators benefit from MEV by executing profitable liquidation transactions, this often comes at the expense of borrowers and overall protocol efficiency. For example:
- Borrowers face exploitative liquidations due lack of safeguards. Their positions can get maliciously liquidated (even if it is at a loss).
- Liquidators themselves face competition from MEV bots, which can invalidate their transactions or extract value unfairly.  
- Protocols are exposed to inefficiencies, as liquidation processes prioritize competition over fairness or transparency.

This proposal is motivated by the need to address these challenges in permissionless CDP protocols, exploring solutions that make liquidations more efficient, fair, and secure while maintaining decentralization. **Innovations such as secondary liquidator markets, Fully Homomorphic Encryption (FHE), and optimized auction mechanisms** could reduce MEV-related inefficiencies and improve user experience across the board.

## Plan and Deliverables
### Plan  
The research will be divided into three key phases to systematically address the problem and ensure actionable insights:  

#### Phase 1: Exploration and Problem Analysis (1-2 Months)  
- Conduct an in-depth review of the mechanics of permissionless CDP protocols like Liquity V2, with a focus on MEV-related trends and behaviors.  
- Perform on-chain analysis of liquidation events to identify inefficiencies, frontrunning risks, and potential vulnerabilities in the current MEV pipeline.  
- Develop a clear understanding of liquidator auction mechanisms and their limitations.  

#### Phase 2: Prototyping and Simulation (2-3 Months)  
- Model potential solutions such as secondary liquidator markets and explore their impact on profitability and efficiency.  
- Investigate the feasibility of using Fully Homomorphic Encryption (FHE) for secure computation in liquidations.  
- Simulate proposed mechanisms using testnet data to evaluate performance under realistic conditions.  

#### Phase 3: Synthesis and Community Engagement (1 Month)  
- Compile findings into a comprehensive report detailing key trends, inefficiencies, and improvement opportunities.  
- Share the results with the research and developer communities to spark discussions and gather feedback.  
- Present insights at relevant community events or conferences to promote broader adoption of the recommendations.  

---

### Deliverables

1. **Comprehensive Report**  
   - A detailed document summarizing the research findings, including:  
     - Key trends in MEV extraction within permissionless CDP protocols.  
     - Identified inefficiencies in current liquidator mechanisms.  
     - Opportunities for improvement
   - The report will include actionable recommendations for protocol designers, developers, and stakeholders to mitigate MEV-related risks and optimize liquidations.

2. **Publication and Community Presentation**  
   - The exploration will be published on **HackMD** and shared publicly to engage the broader research and developer communities.  
   - Findings will be presented at a **Flashbots community event** or a relevant DeFi/MEV-focused conference (if invited), with the goal of fostering discussions and collaboration.  
   - Supporting materials, such as presentation slides and visual data insights, will be provided for clarity and impact.

### Time Allocations  
| **Phase**                     | **Duration**    | **Activities**                                                                 |
|--------------------------------|-----------------|--------------------------------------------------------------------------------|
| Exploration and Problem Analysis | 1-2 months      | Protocol study, on-chain data analysis, and MEV trend identification.          |
| Prototyping and Simulation       | 2-3 months      | Develop and test secondary liquidator market models and FHE feasibility studies.|
| Synthesis and Community Engagement| 1 month         | Report creation, community sharing, and event presentations.                   |

## References

1. [Flashbots Protect](https://docs.flashbots.net/flashbots-protect/overview)  
2. [Liquity V2](https://docs.liquity.org/)  

