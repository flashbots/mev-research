---
id: <leave blank -- will be assigned by reviewers>
title: Evaluating Censorship Risk in MEV-Protected RPCs
team: pop_eax
created: 2025-07-11
---

# Evaluating Censorship Risk in MEV-Protected RPCs: Are We Undermining Ethereum's Censorship Resistant Mechanisms?

Recently, we have seen a rise of MEV protection services such as Flashbots Protect and MEVBlocker which has significantly altered how users submit transactions.
At the current growth rates, Most ethereum transactions may soon go through mev protected RPCs, this may introduce an unintended consequence: centralization of transaction submission, potentially undermining Ethereum’s censorship-resistant properties.

## Background and Problem Statement

Flashbots has made successful progress toward maintaining decentralization and censorship resistance at the block building layer through solutions like BuilderNet and open-source infrastructure.[1] However, a critical concern remains at the RPC layer
where users first submit transactions to Ethereum.
While RPC centralization isn't entirely new to Ethereum, the problem is more prevalent in the MEV context for several reasons such as a limited set of providers, non-self hostable solutions and systematic forcing since users are driven
by financial necessity out of the public mempool.


Unlike traditional RPC infrastructure where users can choose from many providers or run their own nodes, MEV protection services appear to rely on a handful of providers.
This creates a systemic push, concentrating transaction flow and raising several concerns:
- **DNS Domain Attack**: Sophisticated attackers could compromise the DNS registry of the rpc and perform a man-in-the-middle attack by either intercepting the traffic for surveillance or selectively censoring users.[6]
- **Regulatory Pressure**: The nature of the centralized service presents a much clearer target for regulatory pressure.
- **Single Point of Failure**: A service outage could lead to a denial of service of the whole ethereum network  (the impact that could be similar to the infura outage previously).[4]

Flashbots documentation for MEV-Protect doesn't include alternative options beyond a single centralized RPC endpoint, suggesting limited awareness of the sovereignty trade-offs users are making.

### Research Questions:
  1. How has the adoption of MEV protection services impacted the overall censorship resistance mechanisms of Ethereum?
  2. What type of threats and attack vectors are introduced by the MEV protection services ?
  3. Is it technically feasible to create self-hosted solutions?

By exploring these questions, this research aims to evaluate current infrastructure, and propose concrete paths toward more censorship resistant transaction submission mechanisms.


## Plan and Deliverables
- Current State Analysis
- Threat Modeling.
- Vulnerability Assessment.
- Technical analysis of Flashbots Protect architecture and self-hosting feasibility.
- Technical specification for self-hostable MEV protection infrastructure.
- Design of sybil-resistant anonymous RPC architecture leveraging POW mechanisms.
- Prototype development of key components

The results will be presented by a formal peer reviewed paper and a blog post.
## References
1. https://boost.flashbots.net/
2. https://docs.flashbots.net/flashbots-protect/overview
3. https://arxiv.org/abs/2305.01038
4. https://arxiv.org/abs/2305.03718
5. https://decrypt.co/98457/metamask-ethereum-apps-down-infura-outage
6. https://www.bleepingcomputer.com/news/security/raidforums-hacking-forum-seized-by-police-owner-arrested/#:~:text=Members%20become%20suspicious%20in%20February
