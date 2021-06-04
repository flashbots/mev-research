---
id: 14
title: Cryptoeconomic design exploration
team: @pdaian @obadiaa 
created: 2021-06-04
status: in progress
---

# Cryptoeconomic design


## Background and Problem Statement
While Flashbots is exploring an SGX-based solution to provide complete pre-trade privacy as outlined in [this post](https://ethresear.ch/t/mev-sgx-a-sealed-bid-mev-auction-design/9677). We would like to explore in parallel if there are cryptoeconomic mechanisms that can reinforce, or substitute the hard cryptography of SGX, to achieve the same desirable result: namely a fully private way to submit tx to block proposers without having to reveal it to them until they cannot tamper with them anymore.

The aim of this research is to collect internal thoughts on the topic, write up a short strawman spec and start building more thinking, especially how it relates to eth2 and mev-sgx.


## Plan and Deliverables
- strawman proposal of a cryptoeconomic mechanism to provide flashbots functionalities
  - include all relevant tradeoffs
- think of merging design with technical specs to reinforce each other (eg. design + sgx)
- think of how eth2 fits in the picture and if there are any mechanisms we can piggy back on
  - opt-in slashing conditions?
  - any desired protocol changes?


## References
- [Cryptoeconomic relayer bonding proposal](https://hackmd.io/@flashbots/B19hth85_)
- Cryptoeconomic design whiteboard sesh recording
- [ArcherDAO Private Bundler proposal](https://hackmd.io/uTptoEtLQwOrt9sm2fc2cw)
- [DoS micro-fee and reputation proposals](https://hackmd.io/@flashbots/SJEKRgz5O)
