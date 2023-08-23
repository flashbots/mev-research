---
id: "<>"
title: "<Redistributing MEV as Universal Basic Income: Design and Implementation Strategies>"
team: "<Circles UBI team>"
created: "<date created on 2023-08-23>"
---


# Redistributing MEV as Universal Basic Income: Design and Implementation Strategies

This project proposes an approach to repurpose the impact of Maximal Extractable Value (MEV) in the De-Fi ecosystem by designing a redistribution mechanism that supports tokenized universal basic income (UBI). UBI is intended as a periodic payment unconditionally delivered to all on an individual basis, without means-test or work requirement. The Circles UBI system adopts smart contracts to deliver tokenized UBI to over 5.000 users. By integrating an MEV redistribution mechanism with Circles, it will effectively address the MEV problem while positively impacting society by supporting local economies and communities. This proposal is the first to address the MEV problem in intent-centric architectures (Anoma), providing knowledge-creation opportunities for the Flashbots community. Two versions of the redistribution mechanism will be released and carefully evaluated: a Proof-of-Concept compatible with the Ethereum blockchain, and  a prototype tailored for the Anoma protocol stack. State-of-the-art software engineering methodologies will be used to address usability, complexity, and scalability issues of the proposed system.



## Background
Decentralized Finance (DeFi), built on blockchain technologies, replaces traditional financial intermediaries with decentralized applications (DApps) for peer-to-peer transactions, lending, and borrowing (Zhang and Jacobsen, 2018; Schär, 2021). Despite this paradigm shift, empirical studies (Kusmierz and Overko 2021; Zhao et al., 2022) indicate a centralization of power, marked by the concentration of tokenized assets, including cryptocurrencies and governance tokens, in a few hands.

A major threat to the integrity and fairness of the blockchain and De-Fi ecosystems relates to Maximum Extractable Value attacks (Bartoletti and Zunnino, 2022), which allow privileged actors to unduly extract value from the blockchain operation by virtue of their privilege position.
Such attacks manifest in the political economy of blockchains when participants with the ordering power (i.e. block proposer, which can be validators, or miners in Proof-of-Work contexts), deliberately manipulate the order of transactions or select specific transactions to maximize their own profit. 

Such attacks manifest in the political economy of blockchains when participants with the ordering power (i.e. block proposer, which can be validators, or miners in Proof-of-Work contexts), deliberately manipulate the order of transactions or select specific transactions to maximize their own profit. 

Recent research efforts allow us to model and quantify the Maximal Extractable Value (MEV) and its composition (Salles, 2021) in blockchain-based systems. 

These attacks pose a significant concern for the security and integrity of the entire De-Fi ecosystem, and the promise of decentralisation brought forth by blockchain technology. Some examples of attacks include frontruns and backruns (Flashbots, 2020). 
Empirical measurements indicate that Ethereum is frequently targeted by such manipulations, resulting in substantial implications for both individual users and the blockchain network (Flashbots, 2020). Several approaches to mitigate MEV have been advanced.  The Cow (Coincidence of Wants)[^1], for instance, searches and matches for inverse trades (i.e. the coincidences of wants). This reduces the arbitrage opportunity window for external actors to perform MEV attacks. Other solutions, by contrast, such as the  MEV-share protocol by Flashbots, address the problem from a different angle. Rather than focusing on reducing the arbitrage opportunity window, the MEV-Share protocol allows all involved stakeholders to benefit from the potential profits arising from transaction reordering operation. In this protocol users directly submit these transactions to the MEV-Share Node, which segregates user transactions from the general mempool, thus reducing exposure to adversarial actors. The MEV-Share Node also notifies searchers about user transactions, so that they can create strategically bundled transactions, designed to extract MEV. Each bundle includes a payment, calculated based on the anticipated profit from successfully executing the contained transactions. These bundles are communicated directly to block proposers, who, then, form blocks with such transaction sets, prioritizing the most lucrative. Once a bundle is successfully integrated into a block, the searcher realizes the profit. Part of the profit is redistributed to the original transacting parties.

## Problem Statement
While the technologies discussed above are valuable to enhance transparency of the overall De-Fi ecosystem, we propose an approach to more radically address the inequality problem by leveraging the MEV to fund unconditional basic income (UBI) to users within any given blockchain network. Given the inevitability of MEV within the current blockchain political economy, we aim to adopt a model that takes the structure of MEV as a starting point in order to find ways of redistributing value. We name this approach **Maximal Redistributable Value** (MRV).

To pursue this goal, we address two main gaps in the current body of knowledge on MEV and existing tools. Firstly, we aim to formalize the design of a decentralized MEV redistribution mechanism based on collective governance. Furthermore, we will develop, and test the protocol in a real-world context.

The MRV system will leverage the existing network of the Circles UBI community currency system, which currently distributes tokenized unconditional basic income (UBI) to over 5.000 users (Avanzo et al., 2023). UBI is defined by BIEN as a “periodic cash payment unconditionally delivered to all on an individual basis, without means-test or work requirement”. Testing the approach on the Circles UB network will enable us to model and study the impact of the redistribution of digital assets as a policy on the real economy of local urban communities.

Users currently receive UBI based on personal currencies (CRC tokens), distributed via smart contracts to Circles users. These are backed by goods and services produced by local businesses accepting CRCs as medium of exchange. In this context, the MEV redistribution of digital assets such as Ether, DAI or any one token would serve to incentivize users to use CRCs as medium of payment, hence facilitating the expansion of the network.  Every user could convert their CRCs for stablecoins or other kinds of tokens (which are convertible for national currency) backed by the value of MEV being redistributed. 
This would have a much stronger impact on the local economy compared to an airdrop of stablecoins or other kinds of tokens due to the local multiplier effect community currencies generate (Criscione et al., 2022). Most importantly, backing CRC with MEV funds would enable the expansion of the economic network, hence increasing the sustainability of the UBI. This would in its turn facilitate the circulation of CRC and prevent deadlocks and gridlocks in the payment system, which recent studies show to be structural to the bootstrapping phase of community currency systems (Criscione et al., 2022). 

To achieve this goal, we will develop a smart-contract based redistribution mechanism Proof-of-Concept integrated with the current version of the system. Moreover, since the Circles UBI will transition from a traditional DApp architecture to a privacy-preserving intent-centric one, the Circles Entropy system, whose design is outlined in (Dashyan et al., 2023), further challenges are faced, and new knowledge-creation opportunities unfold. These are related to the study of MEV redistribution in a novel privacy-preserving architecture, similar to recent efforts by Flashbots' SUAVE.

The vast majority of approaches to prevent or reduce the damage of EV attacks, focus on the most widely adopted smart-contract based blockchain protocols, such as Ethereum. None of these, to the best of our knowledge, focuses on declarative or intent centric architectures and protocols, even though the concept can be generalized to a wider class of distributed systems relying on arbitrary ordering. 

This project will, therefore, also cast light on how to redistribute MEV in the Anoma protocol stack (Goes et al., 2021). Anoma, on which Circles Entropy will be based, aims to provide an anonymous decentralized system on which declarative smart contracts are executed privately through the matching of intents. These, rather than relying on complete state transitions (i.e. transactions), adopt partial state transitions, defined as intents (Goes et al., 2021). 
Circles Entropy is a technology for preserving privacy in trust and credit relations among the users of the system. Its architecture consists of the following components: a P2P gossip network spreading anonymous intents, and a solver network that performs cryptographic computations to match user intents with the appropriate solution. When an intent is solved, the transaction is settled. This final step involves the settlement layer for transaction validation. In this system, users can send tokens to each other only if they belong to the same web-of-trust. Conversely from the current implementation of Circles UBI, in Circles Entropy, the Web-of-Trust provides strong privacy guarantees, meaning that the users have the view exclusively of their own local connections, but no actor has a view of the complete graph and paths among actors. 

In this context, EV attacks can be performed by reordering intents, rather than transactions. Solvers can be paid in a variety of different tokens they accept in order to look for possible intent matching (Ether, Ensos, etc). Given the novelty of this system and architecture, it is essential to study and correctly handle potential EV attacks and to extend MEV existing formal models to address the specificities of this type of architecture. Redistribution of MEV shall take place to incentivize users to use Circles Entropy, as outlined above for the current version of the system.
In the following section, we outline the research questions we aim to address and highlight their relevance to the Flashbots interests.

In the following sub-section, we outline the research questions we aim to address and highlight their relevance to the Flashbots interests.

### Research Questions
This project proposal aims to respond to the following general research question: *How to develop a UBI-oriented MEV redistribution mechanism?*
In order to achieve a manageable complexity during the project and to create a separation of concerns, we deduce a set of sub-research questions, listed below:

- RQ1: What are the formal models and  metrics to quantify MEV and REV in intent-centric architectures?

- RQ2: What is the architectural design of the system enabling the redistribution of the MEV as UBI (for EVM and intent centric architectures)?

- RQ3: how are the different components and interfaces for the MEV-UBI redistribution system implemented?

To respond to the general RQ, we'll expand the existing metrics and moodels of MEV focused on blockchain-based architectures (Salles, 2021; Bartoletti and Zunnino, 2022) to encompass intent-centric architectures' specificities (RQ1). We'll, then, provide a mdoel for UBI-oriented redistribution mechanisms (RQ2), and implement two artifacts: a PoC compatible with the current architecture of the Circles UBI system, and a prototype to be integrated with the Circles Entropy system (RQ3). 

This project scope intersects the Flashbots research interests in several respects. Firstly, the proposed generalized MEV redistribution protocol design is platform agnostic, and, therefore, its implementation can integrate with the current version of the MEV-share protocol in the Ethereum network. Given the challenging and ambitious scope of the project, the research grant will finance only part of the expenses focusing particularly on the research questions. The cost of technical implementation will be covered by the Circles Coop, leveraging on its resources and network (Plan and Deliverables).

Most importantly, these RQs match the long-term goal to expand the reach of MEV-share, and other Flashbots technologies such as Suave to diverse architecture types. 

Both research threads connect in particular to the Protocol Design research area, but have relevant long-term implications for areas including Cryptographic Privacy and Search Optimization, given the need to design a MEV redistribution protocol in an architecture with specific privacy constraints. 

## Plan and Deliverables
The project will develop in one year time, and will proceed in parallel with the design and development of the Circles Entropy system. By virtue of the synergy with this project, the researchers hired with the funds granted will collaborate with the Circles Coop team, including developers and researchers specialized in distributed systems, mathematics and cryptography. Each of the two phases will be 6-months long. Furthermore, this project will be the running case of a PhD thesis in computer science, whose defense is foreseen by the beginning of 2025.

**Phase 1 (M1-M6):** The first phase will produce a deliverable consisting in the following contributions:
- A set of metrics to quantify the MEV and relative components for intent-centric architectures;
- A set of heuristics for the search of intents maximizing the Extractable Value in intent-centric architectures;
- A formal model of MEV in intent-centric architectures;

This phase will produce a conference paper responding to RQ1. At the beginning of this phase (first two weeks of the project development), a detailed budget allocation plan will be produced. This will allow the Circles Coop eG to establish roles and responsibilities within the Circles UBI team, and allocate the resources to support its members or hire new researchers to work on the project. 

Circles Coop eG will leverage on the existing team experience, the several research collaborations with universities, (i.e. University of Torino, University of Freiburg, Basic Income Earth Network) and collaborations with other companies (i.e. Anoma, Informal Systems and others) to produce highly qualified research, while respecting the budget constraints. This phase of the project will especially leverage collaborations with Anoma, contributing  knowledge and labor to the realization of the Circles Entropy project.


**Phase 2 (M7-M12):** The following research phase will respond to the RQs 2 and 3. This will produce a journal paper focused on the remaining research questions, and a deliverable report including the outputs outlined below:

- High level definition of the MRV redistribution protocol;
- System model integrating the proposed MRV redistribution mechanism;
- Implementation of the proof-of-concept MRV for the Ethereum network / Gnosis Chain and the current Circles UBI architecture;
- Implementation of the MRV based on the Circles Entropy intent-centric architecture;
- Validation of the proposed system model through simulations;
- Evaluation of the proposed approach through testing;
The EVM-compatible PoC will provide further insights for the subsequent implementation in the intent-centric architecture (Circles Entropy), which will be conducted in the last months of Phase 2.
## Methodology
In order to deal with the issues concerning scalability, complexity and usability of the proposed system, we will adopt the Trusted DApp Modeling (also known  as DAOM) framework (Udokwu et al., 2021). This consists of a software engineering method developed by the researchers at the Lappeenranta University of Technology to support DApp development. T-DM is an agent-oriented methodology (Sterling and Taveter, 2009) that enables developers to distinguish between on-chain and off-chain elements of the system in the early stages of the design process. 
This method will support the modeling stage by virtue of the following diagram types:
- **T-DM Requirement diagrams**: useful in the initial stages of the development to outline functional requirements of the system, non functional requirements and stakeholders involved.
- **T-DM Component diagrams**: will be generated by virtue of the heuristic mappings described in (Udokwu et al., 2021). These enable the translation  of the goal model into an architectural model of the system. These include ad-hoc notation showing which components and subcomponents that perform on-chain functions in the system.
- **T-DM Sequence diagrams**: these are based on standard UML sequence diagrams, and include additional syntax displaying the number of actions performed on-chain and off-chain. This allows developers to take account of gas costs in the early stages of the development process.

The system design will extend existing proposals discussing the design of a UBI-oriented MEV redistribution protocol (Apriori and Linares, 2023). 
In order to support the validation  process, Coloured Petri Net based simulations (Jensen, 2005) of the protocol will be generated. The proof-of-concept for the redistribution mechanism will be developed in Solidity, which makes the approach replicable for the Ethereum network. 

[^1]: [Coincidence of Wants Overview](https://docs.cow.fi/overview/coincidence-of-wants)
## References
- **Apriori (Anoma), & Ajmaq (CirclesUBI/Entropy)**. (2023). On UBI and MEV: Towards the Intentional Redistribution of Value. HackMD. Retrieved August 23, 2023, from [link](https://hackmd.io/euIFc_HOT26wSTJqkgGxHQ)
- **Avanzo, S., Criscione, T., Linares, J., & Schifanella, C.** (2023, September). Universal Basic Income in a Blockchain-Based Community Currency. In Proceedings of the 2023 ACM Conference on Information Technology for Social Good (pp. 223-232).
- **Bartoletti, M., & Zunino, R.** (2023). A theoretical basis for Blockchain Extractable Value. arXiv preprint arXiv:2302.02154.
- **Criscione, T., Guterman, E., Avanzo, S., & Linares, J.** (2022). Community currency systems: Basic income, credit clearing, and reserve-backed. Models and design principles (No. 04-2022). FRIBIS Discussion Paper Series.
- **Dashyan, D., Kulkarni, A., Linares, J., & Srikanth, K.** (2023). Circles Entropy: An Anonymous Trust and Credit System. Retrieved August 23, 2023, from [link](https://circlesentropy.github.io/blackpaper/)
- **Flashbots**. (2020). Flashbots: Frontrunning the MEV crisis. Ethresear.ch. Retrieved August 23, 2023, from [link](https://ethresear.ch/t/flashbots-frontrunning-the-mev-crisis/8251)
- **Goes, C., Sun Yin, A., & Brink, A.** (2022). Anoma: a unified architecture for full-stack decentralised applications (Pre-release). [link](https://media.githubusercontent.com/media/anoma/whitepaper/main/whitepaper.pdf)
- **Jensen, K.** (2005). An introduction to the practical use of coloured Petri Nets. In W. Reisig & G. Rozenberg (Eds.), Lectures on Petri Nets II: Applications: Advances in Petri Nets (pp. 237–292). Springer Berlin Heidelberg. [DOI](https://doi.org/10.1007/3-540-65307-4_50)
- **Kusmierz, B., & Overko, R.** (2022, August). How centralized is decentralized? Comparison of wealth distribution in coins and tokens. In 2022 IEEE International Conference on Omni-layer Intelligent Systems (COINS) (pp. 1-6). IEEE.
- **Salles, A.** (2021). Quantifying Realized Extractable Value. Flashbots. Retrieved from [link](https://hackmd.io/@flashbots/quantifying-REV)
- **Schär, F.** (2021). Decentralized finance: On blockchain-and smart contract-based financial markets. FRB of St. Louis Review.
- **Sterling, L., & Taveter, K.** (2009). The Art of Agent-Oriented Modeling. Intelligent Robotics and Autonomous Agent series.
- **Udokwu, C., Brandtner, P., Norta, A., Kormiltsyn, A., & Matulevičius, R.** (2021). Implementation and evaluation of the DAOM framework and support tool for designing blockchain decentralized applications. International Journal of Information Technology, 13, 2245-2263.
- **Zhang, K., & Jacobsen, H. A.** (2018). Towards Dependable, Scalable, and Pervasive Distributed Ledgers with Blockchains (Technical Report).
- **Zhao, X., Ai, P., Lai, F., Luo, X., & Benitez, J.** (2022). Task management in decentralized autonomous organization. Journal of Operations Management, 68(6-7), 649-674.
