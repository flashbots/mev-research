---
id: <leave blank -- will be assigned by reviewers>
title: Designing Ethereum’s Geographical(De)Centralization Beyond the Atlantic
team: Sen Yang, Burak Öz, Fei Wu, and Fan Zhang
created: 2025-10-14
---

# Designing Ethereum’s Geographical (De)Centralization Beyond the Atlantic

## Background and Problem Statement


Ethereum's decentralization depends not only on stake distribution but also on the physical locations of validators [1]. In practice, validators tend to cluster in latency-advantaged regions such as Europe and the U.S. East Coast, gaining faster access to attestations and block propagation. This project aims to investigate how protocol design -- particularly block-building paradigms such as proposer–builder separation (PBS) and local block building -- affects validator incentives and the resulting degree of geographical centralization. Specifically, it seeks to identify which designs amplify or mitigate these latency-driven concentration dynamics.


## Plan and Deliverables

We plan to build an agent-based simulation framework, calibrated with real-world latency data [2], to reproduce Ethereum validator behavior under different protocol designs (e.g., proposer–builder separation (PBS) vs. local block building). Using this framework, we aim to analyze how various protocol designs and consensus updates, such as EIP-7782 [3], affect validator incentives and geographical distribution, thereby improving our understanding of how protocol design shapes geographical (de)centralization dynamics.

**Deliverable**:
- A paper on arXiv
- A blog post
- An open-source simulation framework

## References

- [1] Phil Daian. Decentralized crypto needs you: to be a geographical decentralization maxi. https://collective.flashbots.net/t/decentralized-crypto-needs-you-to-be-a-geographical-decentralization-maxi/1385
- [2] Google: Google looker studio dashboard: fc733b10-9744-4a72-a502-92290f608571, https://lookerstudio.google.com/reporting/fc733b10-9744-4a72-a502-92290f608571
- [3] EIP-7782: Reduce Block Latency, https://eips.ethereum.org/EIPS/eip-7782


## Outputs

The project produced a paper on arXiv, a blog post on the Flashbots Collective, and an open-source implementation.

- Designing Ethereum's Geographical (De)Centralization Beyond the Atlantic, https://arxiv.org/abs/2509.21475
- Prisoners of Geography 2.0: How Protocol Shapes Where Validators Run, https://collective.flashbots.net/t/prisoners-of-geography-2-0-how-protocol-shapes-where-validators-run/5308
- Github Repo: Geographical Decentralization Simulation, https://github.com/syang-ng/geographical-decentralization-simulation