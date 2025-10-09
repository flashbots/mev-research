---
id: <leave blank -- will be assigned by reviewers>
title: Decentralized Proposer-as-a-Service (DPaaS)
team: Ittai Abraham, Matthew Lentz (Lead), Chenyang Liu, and Kartik Nayak
created: 2025-10-04
---

# Decentralized Proposer-as-a-Service (DPaaS)

## Background and Problem Statement

The current Proposer-Builder Separation (PBS) design and implementations (e.g., MEV-Boost [1]) rely heavily on a “relay” entity that acts as an intermediary between builders and proposers. Relays are centralized, in terms of both the number of implementations and deployments (currently dominated by four) as well as an individual relay’s position between a set of builders and a proposer. Relays are employed to provide a number of beneficial security properties to both builders and proposers, including: confidentiality for non-winning blocks, validation of all blocks from builders, and availability of the winning block.

**Problem**: Currently, both proposers and builders place significant inherent trust in the correctness of relays, and relays serve as single points of failure in the ecosystem.

**Related Work**: There have been several prior explorations to address this problem. TEE-Boost [2] leverages Trusted Execution Environments (TEEs) for builders to provide attestations to proposers that prove validity of the block (e.g., includes transaction to pay the proposer) while maintaining block confidentiality; however, supporting strong block availability guarantees requires an additional solution (e.g., a trusted third party). The proposal by Policharla et al. [3, 4] combines threshold encryption with TEE-Boost to provide data availability; however, this requires modifications to the consensus protocol (impacting deployability) and the threshold decryption for validators is not directly compatible with the dynamic availability goal in Ethereum.

**Our Idea**: Decentralized Proposer-as-a-Service (DPaaS). We argue it is useful to consider decentralization at a small scale across multiple TEEs, which we term “proposer entities” (PEs),  to avoid any single point of failure (e.g., as a result of a TEE compromise) and achieve strong defense in depth. Principals who wish to become validators in Ethereum can enroll as a validator through a DPaaS instance, which will act on behalf of the validator. By default, DPaaS takes on all roles for the validator (full-offload); however, we plan to allow for flexibility in enabling the validator to still manage some aspects themselves, such as running the auction, while still providing strong guarantees (light-offload). We plan to leverage cryptographic approaches to enable such decentralization across multiple PEs while appearing as a single entity to the rest of the Ethereum network (i.e., validators), allowing us to avoid any changes to the Ethereum consensus protocol.

Naturally, this decentralization comes with its own challenges that we will need to address in our work. First, we need to develop approaches to support all of the traditional properties and features afforded by relays while considering a strong threat model in which some PEs may fail (e.g., compromised by an adversary). Additionally, there are many system performance constraints and goals to meet with respect to slot times and auction interactions (e.g., updates of current winning bids) which we need to meet.

## Plan and Deliverables

**Plan**:
- Develop the design for DPaaS, including protocols between builders and the DPaaS system
- Write down the protocol specification and corresponding security analysis
- Implement the design for DPaaS, which includes development of several software bases that execute inside of TEEs for builders and PEs
- Evaluate our prototype implementation in terms of the performance (e.g., auction update latency, scalability)

**Deliverables**:
- Software Prototype Implementation (e.g., TEE software) which includes support for: 1) both AMD SEV-SNP and Intel TDX TEEs, and 2) light- and full-offload variants
- Academic Paper

## References

- [1] https://github.com/flashbots/mev-boost
- [2] https://collective.flashbots.net/t/tee-boost/3741
- [3] https://www.paradigm.xyz/2024/10/removing-the-relays
- [4] https://github.com/flashbots/mev-research/blob/main/FRPs/active/FRP-48.md
