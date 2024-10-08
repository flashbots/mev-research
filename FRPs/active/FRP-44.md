| id | title | team | created | status |
| --- | --- | --- | --- | --- |
| 44 | Mechanisms of Blockchain-based Dark Pools | Muhammad Yusuf | 2024-7-29 | active |

# **Background and Problem Statement**

Dark pools have been an essential component of traditional finance since the early 90s, providing venues for trading large blocks of securities away from the public eye. As of 2022, the U.S. Securities and Exchange Commission (SEC) had registered 60 dark pools. These Traditional dark pools are run by trusted operators such as exchanges, like the NYSE or NASDAQ; some are broker-dealer-operated, like MS Pool by Morgan Stanley and SigmaX by Goldman Sachs; and some are independently operated, like Liquidnet or MatchNow.

While dark pools offer the advantage of privacy and minimizing market impact for large trades, they are not without controversy. The very operators trusted to run these pools have, on numerous occasions, been found guilty of abusing their privileged positions. Misconduct has included trading against their users, leading to a cumulative $340 million in fines imposed by the SEC for various infractions. These attacks have been continual despite of regulatory actions because the Profit from Corruption is far greater than the cost of corruption.

Blockchain-based dark pools, on the other hand, aim to abstract the need for trust in a single operator. Leveraging Privacy-Enhancing Technologies (PETs) such as Zero-Knowledge Proofs (ZK), Multi-Party Computation (MPC), Trusted Execution Environments (TEE), and Fully Homomorphic Encryption (FHE), these dark pools aim to ensure both pre-execution and post-execution privacy.

This study aims to uncover the following dark pool designs.

- [Renegade](https://renegade.fi/), with a crossing network-based design, uses a UTXO-based system and will be deployed using Arbitrum’s Orbit. It combines an ultra-ponk-based zero-knowledge proof system with an enshrined MPC.
- [Tristero](https://www.tristero.xyz/) with an orderbook-based uses an account model and a network of Intel SGX TEE nodes. It uses “salted” intents.
- Panther Protocol, an orderbook, uses a combination of a MASP and a time-based escrow contract to source liquidity externally.
- [Singularity](https://www.thesingularity.network/) with a hybrid orderbook-AMM design, also uses a UTXO based system. It relies on a network of FHE nodes and an Ultra-plonk based zero-knowledge proof system.
- [Penumbra](https://penumbra.zone/) with a CL-AMM based on a UTXO model. It uses a groth16 ZK-proof system with homomorphic Pedersen commitments.
Enclave Markets is a CEX running a cross-crossing network and a CLOB. It uses TEEs for confidential computing.
- CT+2, a DEX based on SUAVE that utilizes batch auctions and is designed to source liquidity externally.

But even blockchain-based dark pools backed by cryptography primitives need to be questioned to test their mantel of privacy. This FRP aims to question the effectiveness and resilience of today’s blockchain-based dark pool designs. Specifically,

- How "dark" are these blockchain-based dark pools? Within what level of privacy can they effectively operate?
- Can they effectively mitigate risks related to MEV, LVR, collusion, trust parties, and information asymmetry?
- Establishing foundations of dark pool design choices across different PETs, DEX designs, matching systems and sourcing liquidity
- How dark pool design choices affect latency, settlement, time & costs of privacy, and quality of pricing
- If the order flow routing off of dark pools is to settle on Ethereum, how do its privacy guarantees hold up at the block building and settling periods?
- If the order flow is routing off of L2s, can the L2’s sequencer have a peek at its order flow?
This would help evaluate their designs to see the flow of transactions, whether third parties or relayers handle them, and whether they could peek at order information depending on how PETs are used in the order cycle.
This would seek to answer whether any value could be extracted from each design and, if so, how.
Why would a dark poo settle on an L2? Latency and costs are major factors for building on an L2. Renegade, for example, is on Arbitrum One. Arbitrum currently uses FCFS, but if and when Timeboost is implemented, it will open up the L2 scene for other types of MEV as searchers are allowed to build bundles.
So, the choice of L2 or L1 influences levels of privacy, latency, and costs.

This research proposal seeks to investigate these questions, exploring whether blockchain-based dark pools can overcome the inherent challenges faced by traditional dark pools and if they are a step above.

# **Plan and Deliverables**

We plan to produce a paper and present our findings at a conference.

A few steps we plan to take as a part of our study

- Survey dark pool teams (Renegade, Tristero, Panther, Penumbra, Singularity, CT+2, & Enclave Markets). This step aims to establish the reasoning behind each dark pool's design choices and trade-offs across PETs, DEX design, matching system, settlement, etc.
- Survey dark pool users such as market makers, solvers, and liquid funds.
- Quantitative analysis of
    - latency & Settlement
    - Proof generation costs & time
    - Quality of pricing
    The above-mentioned metrics will be measured after executing orders on the mainnets and testnets of functional dark pools. Dark pool teams and their users would assist in thoroughly and realistically establishing these metrics.
    For example, latency is the duration between when an order finds a match to the builder and sequencer inclusion.
    For example, if a dark pool is using relayers, how much time does it take for the relayer nodes to process a match?
    The most liquid asset will be chosen in a particular dark pool to ensure there are no delays in execution.
    The type of PET used, and the transaction workflow will heavily influence latency. So, mapping out the execution process in great detail will be one of the core parts of this research.
    There should be a transaction explorer for each design that is live or in the testnet. This would help quantify latency. Additionally, I will work with dark pool teams to help get accurate numbers.
- Establish Desired Properties of Dark Pools
    - Pre-execution Privacy
    - Order Matching Mechanisms (Mid-point, Price Time Priority, batching, auctions)
    - Nature of Liquidity (Sourced internally or externally, through private pools or an orderbook, or through hook-like mechanisms)
    - Post-execution Privacy
    - MEV Resistance & Degree of Programmability to accommodate good MEV
    - Censorship Resistance
- Thoroughly analyze each design’s trade-offs and map out potential attack vectors, points of information asymmetry, collusion, and trust assumptions.
- Highlight points of information leakage that could lead to MEV extraction. This could be influenced by various dark pool design choices.
- Analyze levels of LVR vulnerability in AMM-based designs
- Consolidation, drafting publication

We will also hold discussions with teams building private defi and share our findings.

# **References**

[Diving Into Dark Pools by Muhammad Yusuf](https://distributedresearch.substack.com/p/diving-into-dark-pools)

[Dark Pools by Lev Livnev](https://lev.liv.nev.org.uk/darkpools/)

[Renegade Whitepaper](https://renegade.fi/whitepaper.pdf)

Singularity Whitepaper (confidential)

Tristero Whitepaper (confidential)

[Mempool Privacy: An Economic Perspective](https://arxiv.org/abs/2307.10878) by Antoine Rondelet & Quintus Kilbourne

[Pre-Execution Privacy In PBS by Quintus Kilbourne](https://collective.flashbots.net/t/pre-execution-privacy-in-pbs/2035)

[FRP-18: Cryptographic Approaches to Complete Mempool Privacy by Jbstearn](https://collective.flashbots.net/t/frp-18-cryptographic-approaches-to-complete-mempool-privacy/1210)

[The Muted Seven – 7 Things You Should Consider Re Confidential Compute](https://greenfield.xyz/2024/07/04/the-muted-seven-7-things-you-should-consider-re-confidential-compute/) by Greenfield

[FRP-40: SUAVE’s Potential in DeFi: A focus on decentralized exchanges (DEX) and auction mechanisms](https://collective.flashbots.net/t/frp-40-suave-s-potential-in-defi-a-focus-on-decentralized-exchanges-dex-and-auction-mechanisms/3204)

[Prime Match: A Privacy-Preserving Inventory Matching System](https://www.usenix.org/system/files/usenixsecurity23-polychroniadou.pdf)

[Ratel: MPC-extensions for Smart Contracts](https://eprint.iacr.org/2023/1909.pdf)
