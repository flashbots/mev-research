---
id: <leave blank -- will be assigned by reviewers>
title: Incentive-Compatible Encrypted Mempools
team: Nicolas Alhaddad (Boston University) and Alireza Kavousi (University College London)
created: 2025-10-21
---

# Flashbots Research Proposal

The notion of encrypted mempool has seen much attention in recent years due to the various issues caused by transparency of the blockchain, particularity the vulnerability to Maximal Extractable Value (MEV), where attackers can front-run, back-run, and reorder transactions as soon as they appear[^1]. Estimates put cumulative MEV on Ethereum in the billions of dollars since 2020, underscoring the need for privacy at the mempool layer[^2]. An Encrypted mempool refers to a type of blockchain mempool where pending transactions exist in an encrypted form so that no one can read them before execution. By hiding transaction content until execution time, it mitigates MEV by tackling the information asymmetry between users and attackers.

Most proposed encrypted mempool designs rely on variants of the commit–reveal paradigm, where the commit phase establishes agreement on ciphertexts, and the reveal phase discloses either the plaintexts or the corresponding decryption keys. However, this raises the critical question: who holds the decryption key? Typically, a trusted entity or a committee of parties is entrusted with this key, releasing it only during the reveal phase. Crucially, these parties are economically incentivized to learn or leak the decryption key prematurely (i.e. before the commitment phase ends) since doing so can yield substantial MEV profits. Moreover, such violations are difficult to detect because the parties can plausibly deny having influenced the ciphertext ordering.

It remains an open problem to construct an encrypted mempool that is incentive-compatible and is resistant to such premature decryption and ordering attacks without relying on trusted committees or unverifiable ex post penalties. In this project, we formalize the notion of incentive-compatible encrypted mempools and aim to design a scheme that satisfies this property while remaining scalable, trustless, and suitable for practical deployment.

## Background and Problem Statement

Due to their practical efficiency and trust model, committee-based encrypted mempools have been of interest both in practice[^3] and in academic literature[^4]. In principle, these approaches rely on a trusted committee to generate an encryption key and decrypt the committed batch of transactions. This design introduces a structural backdoor: rational insiders can collude and have a natural incentive to learn transactions before they are committed even without leaving on-chain public traces[^5]. Recent accountability mechanisms (e.g. slashing, snitching, audits) attempt to deter collusion with ex post penalties[^6], but they presume calibrated costs and reliable detection. These assumptions are fragile on-chain and can often be overwhelmed by MEV profits.

In this project we explore the following research question: Can we build an encrypted mempool that is plausibly incentive-compatible without relying on trusted committees or unverifiable ex post penalties?

We study this problem by formalizing the notion of an incentive-compatible encrypted mempool. Intuitively, this notion implies that an encrypted mempool is incentive-compatible if the probability of premature decryption (learning the trapdoor before the designated reveal phase) is negligible in the security parameter. We then try to construct an encrypted mempool satisfying this definition, with the core insight of replacing economic deterrence with computational hardness: decryption becomes feasible only after the block is irrevocably committed. This closes the committee backdoor and yields incentive-compatible privacy, where honest participation is the best strategy and early revelation is infeasible without completing the prescribed work. The use of computational puzzles for encrypted mempools was previously proposed by Doweck and Eyal[^7], but their design faces major limitations that affect their practicality[^8]. We address these issues and further extend the design to satisfy properties required for practical and large-scale blockchain deployment, including permissionless participation (with no trust anchor or fixed committee), batch decryption with amortized communication, non-interactivity from both user and decryptor sides, guaranteed decryption of all on-chain ciphertexts, and the absence of any trusted setup. Achieving all these properties simultaneously while preserving incentive-compatibility is the central challenge of this work.

## Plan and Deliverables

We seek the following objectives in this project:

- Proposing a formal modeling for incentive-compatible encrypted mempools in the presence of rational actors.
- Proposing efficient and scalable encrypted mempool schemes that satisfy the incentive-compatibility property.
- Analyzing the security of our proposed schemes and exploring possible extensions/optimizations. 
- Conducting empirical analysis and providing proof of concept.

The expected milestones are as follows:

- Formal modeling and protocol design
- Security analysis of the protocols and optimizations/extensions
- Writing down the research paper

The final object is to deliver an academic research paper and associated proof of concept. Also, we will produce blog post for Flashbots forum and present our findings at its community events.


## References

[^1]: Daian, Philip, et al. "Flash boys 2.0: Frontrunning in decentralized exchanges, miner extractable value, and consensus instability." 2020 IEEE symposium on security and privacy (SP). IEEE, 2020.

[^2]: https://blog.shutter.network/industry-leaders-propose-ethereums-first-threshold-encrypted-mempool/

[^3]: Dziembowski, Stefan, Sebastian Faust, and Jannik Luhn. "Shutter network: Private transactions from threshold cryptography." Cryptology ePrint Archive (2024).

[^4]: Choudhuri, Arka Rai, et al. "Practical mempool privacy via one-time setup batched threshold encryption." 34th USENIX Security Symposium (USENIX Security 25). 2025.

[^5]: Rondelet, Antoine, and Quintus Kilbourn. "Mempool Privacy: An Economic Perspective." arXiv preprint arXiv:2307.10878 (2023).


[^6]: Boneh, Dan, Aditi Partap, and Lior Rotem. "Accountability for misbehavior in threshold decryption via threshold traitor tracing." Annual International Cryptology Conference. Cham: Springer Nature Switzerland, 2024.

[^7]: Doweck, Yael, and Ittay Eyal. "Multi-party timed commitments." arXiv preprint arXiv:2005.04883 (2020).

[^8]: Stearn, James. "‘Cryptographic approaches to complete mempool privacy." Flashbots Res., Cayman Islands, Tech. Rep. FRP-18 (2022).
