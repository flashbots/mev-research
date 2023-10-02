---
id: <leave blank -- will be assigned by reviewers>
title: Sustain Relay Services 
team: 0xRWA
created: 2023-10-01
---

# FRP-Sustain-Relay-Services

With the latest departure of key relay operators and the latest research demonstrating that relays are not living up to expectations, the role of Relay in the MEV ecosystem and the sustainability of relays are in question.

We believe that relays can play a critical role in the MEV ecosystem, with value-added relay services even after ePBS, possibly integrated with SUAVE. This research proposal aims to investigate current relay economics, propose a viable economic design based on the MEV marketplace dynamics to sustain relay operations, mitigate centralization and censorship risks, and complement ePBS/SUAVE through innovative value-added relay services in the future. 

## Background and Problem Statement

Blocknative, a provider of tools for transactions on the Ethereum blockchain, [posted](https://twitter.com/blocknative/status/1706685103286485364) on 9/27/2023 that it is exiting services related to its MEV-Boost Relay. This leaves only four main relays, according to [Relayscan.io](https://www.relayscan.io/), increasing the centralization and censorship risks. 

Blocknative's CEO, Matt Cutler, said that the business of running a relay and block-building services represents "a lot of work" and "a lot of expertise, a lot of engineering, and not a lot of economic incentive for someone in our position as a credibly neutral player."

In the current PBS setup post the Merge, relays are mostly funded by public good initiatives, compared to profitable business models of searchers, block builders, and proposers. This is unlikely to be sustainable in order to continue playing critical mediator roles in the PBS auction marketplace. Blocknative's exit from the relay business just last week is a good example.        

On top of that, this ETH Zurich research paper, published on 9/24/2023, [Ethereum’s Proposer-Builder Separation: Promises and Realities](https://arxiv.org/pdf/2305.19037.pdf), claims that "Our findings reveal that although PBS grants validators the opportunity to access optimized and competitive blocks, it tends to stimulate censorship rather than reduce it. Additionally, we demonstrate that relays do not consistently uphold their commitments and may prove unreliable. Specifically, proposers do not always receive the complete promised value, and the censorship or filtering capabilities pledged by relays exhibit significant gaps."

Given the above problems, findings, and failing relay business, we are motivated to propose research to tackle some research questions such as: 

1. What could be a viable economic design to incentivize relays for sustainable relay operations as a business?
2. How can the centralization/censorship risks in relay services be mitigated?
3. What value-added services can relays provide to survive upcoming ePBS and integrate with SUAVE?


## Plan and Deliverables
Here's a proposed multi-phased approach with deliverables:

1. Phase 1: Research relay operators, including Blocknative, a previous relay operator in the business, to gain a better understanding of relay economics.
2. Phase 2: Propose a viable economic design to sustain relay operations, attract competition, and mitigate risks of centralization and censorship.
3. Phase 3: Propose relay services in payment verification, cancellation, privacy, etc., complimenting ePBS / SUAVE with innovative value-added relay services. 

We plan to deliver by end of 2023 / early 2024.  

## References
[Ethereum’s Proposer-Builder Separation: Promises and Realities](https://arxiv.org/pdf/2305.19037.pdf)

[Blocknative to Suspend MEV-Boost Relay After Economics Fail to ‘Materialize’](https://www.coindesk.com/tech/2023/09/26/blocknative-to-suspend-mev-boost-relay-after-economics-fail-to-materialize/)

[Relays in a post-ePBS world](https://ethresear.ch/t/relays-in-a-post-epbs-world/16278)

[The Future of MEV is SUAVE](https://writings.flashbots.net/the-future-of-mev-is-suave/)
