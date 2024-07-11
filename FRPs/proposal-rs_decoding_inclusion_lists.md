-------------------------------------------------------------------------------
id: 
title: Reed-Solomon Decoding for Inclusion Lists 
team: Psycho Virtual 
created: 2024-07-14 
---

# Reed-Solomon Decoding for Inclusion Lists


Reed-Solomon (RS) codes are a fundamental tool in theoretical computer science and play a key role in modern proof systems. These codes enable information to be reliably encoded, transmitted, and decoded over noisy channels. While RS codes are well studied in the context of zero-knowledge proofs, especially in the design of STARKs, their application in distributed systems like the Ethereum Virtual Machine is less explored.

One promising application is using RS algorithms to encode attestations of public mempool transactions and employing decoding algorithms to construct highly decentralized Block Inclusion Lists from these attestations. This could significantly enhance the handling of MEV in the Ethereum ecosystem by creating more transparent and fair transaction inclusion mechanisms, reducing opportunities for frontrunning and other exploitative behaviors.

This project aims to systematically study RS encoding and decoding for building decentralized Inclusion Lists.

## Background and Problem Statement

In the current Ethereum ecosystem, block builders hold significant power in choosing which transactions to include or censor. Inclusion Lists enable block proposers to circumvent censorship by ensuring that certain transactions are forcibly included. Essentially, Inclusion Lists aim to distribute the authority of transaction inclusion away from a single block producer.

This project will research the application of two distinct RS decoding algorithms to Inclusion Lists: the Berlekamp-Welch algorithm (for unique decoding) and the Guruswami-Sudan algorithm (for list decoding).

We will focus on formalizing, studying, and implementing the critical components of the system, specifically the processes of using RS codes for attestation encoding and decoding.

## Plan and Deliverables

1. **Research Publication**:
    - Publish a research paper detailing our findings and methodologies.
    - Post a blog entry summarizing the key insights and implications for the Ethereum ecosystem.
2. **Open-Source Implementation**:
    - Develop and release an open-source implementation of the RS attestation algorithms, including both Berlekamp-Welch and Guruswami-Sudan algorithms.
    - Ensure code is well-documented and easily integratable with existing Ethereum tooling.
3. **Public Presentation**:
    - Present our findings and implementation details either internally to the FlashBots team or at an external conference.
    - Prepare supporting materials such as slides, demos, or tutorials to effectively communicate our work.

## References

1. [One-bit-per-attester inclusion lists](https://ethresear.ch/t/one-bit-per-attester-inclusion-lists/19797) 
2. [eip-4844](https://eips.ethereum.org/EIPS/eip-4844)
3. [Ethereum has blobs. Where do we go from here?](https://vitalik.eth.limo/general/2024/03/28/blobs.html)
4. [Inclusion Lists](https://ethereum-magicians.org/t/eip-7547-inclusion-lists/17474)
5. [Inclusion Lists Gist](https://gist.github.com/michaelneuder/dfe5699cb245bc99fbc718031c773008)
6. [No free lunch – a new inclusion list design](https://ethresear.ch/t/no-free-lunch-a-new-inclusion-list-design/16389)
7. [Anonymous Inclusion Lists](https://ethresear.ch/t/anonymous-inclusion-lists-anon-ils/19627)
8. [Inclusion List Specs](https://notes.ethereum.org/@mikeneuder/il-spec-overview)
9. [List decoding of error-correcting codes]( https://www.cs.cmu.edu/~venkatg/pubs/papers/frozen.pdf)
10. [Algorithmic results in list decoding](https://www.cs.cmu.edu/~venkatg/pubs/papers/listdecoding-NOW.pdf)
11. [A summary on the FRI low degree test](https://eprint.iacr.org/2022/1216.pdf)
