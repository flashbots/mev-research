---
id: <leave blank -- will be assigned by reviewers>
title: Anti-collusion mechanisms for MEV protection
team: Stefan Dziembowski (lead) and Sebastian Faust
created: 2025-09-02
---

# Flashbots Research Proposal Template

 Collusion is a fundamental challenge for any cryptographic protocol or distributed system. In blockchain environments, however, it is particularly concerning, as parties may be financially incentivized to collude and deviate from the honest execution of a protocol. Such behavior directly undermines the primary security assumption on which most cryptographic and distributed systems rely—namely, that a subset of participants act honestly. A setting where collusion is particularly critical is in the context of countermeasures against Miner Extractable Value (MEV). Here, a collusion allows the colluding parties to extract value from users, e.g., by front-running honest users’ transactions before they are finalized in a block. Colluding parties can extract value from users, for example, by front-running transactions before they are finalized in a block. Collusion in MEV contexts is a concern in two prominent approaches: the Flashbots ecosystem [2], which implements the proposer–builder separation (PBS) paradigm, and solutions employing encrypted mempools, such as the Shutter network [4]. The goal of this project is to provide a comprehensive analysis of the current state of anti-collusion mechanisms in the context of MEV protection, and to identify the most effective solutions for protecting users from MEV extraction by colluding parties

## Background and Problem Statement

 ### Collusion in MEV Protection.
 In this section, we provide more details on two popular approaches for MEV protection, namely the proposer-builder separation (PBS) paradigm and the encrypted mempools. Let us first consider the PBS paradigm used, e.g., by the Flashbots ecosystem. In PBS, the proposer is responsible for selecting the blocks to be added to the blockchain, while the builder is responsible for constructing the blocks from transactions in the mempool. Currently, these two roles are separated. This separation of roles is intended to prevent collusion between proposers and builders; however, in practice, nothing prevents a colluding builder and proposer from coordinating their actions (e.g., a proposer could always agree to select blocks from a colluding builder). Such collusion can lead to centralization of power, thus eliminating the fairness in the auction process. Another example where collusion is a problem is in solutions leveraging encrypted mempools such as the Shutter network [4]. Here, a set of so-called keypers maintains a shared secret key that is used to decrypt private transactions within the mempool. When the keypers collude, they can prematurely decrypt transactions, leading to MEV extraction, e.g., they can learn the content of the transactions before the block is finalized and front-run them.

 ### Cryptographic Countermeasures to Prevent Collusion.
 Cryptographers have proposed various countermeasures to prevent collusion in security protocols. Generally speaking, complete prevention of collusion is challenging, if not impossible, to achieve, except for some very specific scenarios that restrict the communication capabilities of the colluding parties (see, e.g., [7]). More commonly, the goal is to design protocols that deter collusion, instead of preventing it. Such approaches include: traceable secret sharing [6], secret sharing with snitching [3], deniable secret sharing [1], and the collusion deterrence protocols of [5]. Although some of these countermeasures were partly motivated by the MEV applications, we are not aware of any comprehensive study that would analyze the applicability of these countermeasures to this specific use case.


## Plan and Deliverables

The goal of this project is to (a) study the MEV countermeasures concerning how vulnerable they are to collusion, (b) provide an overview of current anti-collusion mechanisms used in cryptography and distributed systems, and (c) evaluate the applicability of the techniques from (b) to the systems from (a). The research will be carried out by Stefan Dziembowski and Sebastian Faust.

###  Deliverable.
The project will produce a comprehensive report in the form of a blog post, where we outline the results of our study. This is mainly a survey project to show the applicability of the anti-collusion mechanisms to MEV protection. In follow-up projects, we will investigate further extending the anti-collusion mechanisms to MEV protection, designing new cryptographic protocols, and analyzing their security properties.

## References

 [1] Ran Canetti, Ivan Damgard, Sebastian Kolby, Divya Ravi, and Sophia Yakoubov. “Deniable Secret Sharing”. In: IACR Cryptol. ePrint Arch. (2025). url: https://eprint.iacr.org/2025/525.

 [2] Philip Daian, Steven Goldfeder, Tyler Kell, Yunqi Li, Xueyuan Zhao, Iddo Bentov, Lorenz Breidenbach, and Ari Juels. “Flash Boys 2.0: Frontrunning in Decentralized Exchanges, Miner Extractable Value, and Consensus Instability”. In: 2020 IEEE Symposium on Security and Privacy, SP 2020, San Francisco, CA, USA, May 18-21, 2020. IEEE, 2020.

 [3] Stefan Dziembowski, Sebastian Faust, Tomasz Lizurej, and Marcin Mielniczuk. “Secret Sharing with Snitching”. In: Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security, CCS 2024, Salt Lake City, UT, USA, October 14-18, 2024. ACM, 2024.

 [4] Stefan Dziembowski, Sebastian Faust, and Jannik Luhn. “Shutter Network: Private Transactions from Threshold Cryptography”. In: IACR Cryptol. ePrint Arch. (2024). url: https://eprint.iacr.org/2024/1981.

 [5] Tiantian Gong, Aniket Kate, Hemanta K. Maji, and Hai H. Nguyen. “Disincentivize Collusion in Verifiable Secret Sharing”. In: Advances in Cryptology- EUROCRYPT 2025- 44th Annual International Conference on the Theory and Applications of Cryptographic Techniques, Madrid, Spain, May 4-8, 2025, Proceedings, Part V. Vol. 15605. Lecture Notes in Computer Science. Springer, 2025.

 [6] Vipul Goyal, Yifan Song, and Akshayaram Srinivasan. “Traceable Secret Sharing and Applications”. In: Advances in Cryptology- CRYPTO 2021 41st Annual International Cryptology Conference, CRYPTO 2021, Virtual Event, August 16-20, 2021, Proceedings, Part III. Vol. 12827. Lecture Notes in Computer Science. Springer, 2021.

 [7] Abhi Shelat. “Collusion-free protocols”. In: Proceedings of the Behavioral and Quantitative Game Theory- Conference on Future Directions, BQGT ’10, Newport Beach, California, USA, May 14-16, 2010. ACM, 2010.