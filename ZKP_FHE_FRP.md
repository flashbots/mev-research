---
id: <leave blank -- will be assigned by reviewers>
title: Zero Knowledge Proofs of FHE
team: Hadas Zeilberger and Jonathan Passerat-Palmbach
created: 2024-10-07
---

# Flashbots Research Proposal

Fully Homomorphic Encryption is useful for performing computations on encrypted data, which is great for preserving the privacy of input data. However, the person decrypting the final result has no visibility into the computation that took place. On the other hand, a SNARK enables someone to verify that a certain sequence of operations took place on some input data. But in the absence of other cryptographic methods, the output of a SNARK circuit is always visible to the verifier.

More concretely, [previous work from Flashbots](https://writings.flashbots.net/blind-arbitrage-fhe) describes how Fully Homomorphic encryption can enable arithmetic operations on ciphertexts in a simplified MEV arbitrage setting involving 3 parties: a user, a searcher and a trusted block builder. Thus, a searcher can perform comparisons and computations on encrypted transactions, so that a user's data remains private. However, if only FHE is used then the blockbuilder can only decrypt the final result, and has no insight into 1) if the transaction was correctly formed or 2) If the comparisons executed by the searcher were done correctly.

If we additionally use SNARKs, a user can now prove that the transaction is valid and the searcher can prove that it did indeed apply the agreed upon FHE program. 

On the other hand, suppose we only used SNARKs without FHE. Then, the user can prove that their transaction was processed correctly, but the transaction - which is the output of the SNARK circuit- is still visible to the verifier. Thus we require both FHE and SNARKs so that we have the ability to operate on encrypted data as well as the ability to verify that a sequence of operations is correct. 

The combination of FHE and zk-SNARKs is an important but under-explored primitive in privacy-preserving systems. In a SNARK, a prover is able to convince a verifier of the correctness of the output of some computation while keeping the input secret. However, if we want to overlay extra privacy guarantees, such as hiding the output from the verifier or the input from the prover, then the prover would need to operate on encrypted data and possibly execute the encryption within the SNARK circuit.

As SNARKs are general purpose computations, it is possible to naively encode a fully-homomorphic encryption protocol into a SNARK circuit. However, this would lead to very slow proving times. A major bottleneck is the fact that FHE is performed over Rings whereas SNARKs are defined over Finite Fields, and so non-native Ring operations have to be simulated, leading to a large constant overhead. 




## Background and Problem Statement

Prior work (ABPS24) circumvents this issue by using Lattice-Based SNARKs which are already based on a decomposition of a Ring element into a product of Finite Field elements using the Chinese Remainder Theorem. However this requires running many instances of the SNARK protocol on each element of the decomposition. 

The protocol in [VKH23], on the other hand, encodes an FHE into a SNARK by simulating the Ring operations directly into the SNARK. To optimize this step, they only do the modular reduction just before the arithmetic overflows, so that this expensive operation can be done less frequently. 

In this project, we propose to use a different approach. It turns out that any error-correcting code over a Finite Field is well-defined and has good distance properties when defined over a polynomial ring. The reasoning for this is very similar to the reason that error-correcting codes can be defined over any extension field (described in Remark 1, Page 16 of ZCF23). This means that any multilinear SNARK can be defined directly over polynomial rings. We expect this to be faster than the CRT approach because it requires just one SNARK instance per circuit instead of several. 

The goal of this project is to minimize the overhead induced by encoding ring operations in a finite-field based SNARK. This will most likely require the combination of several methods, one of which will be the technique described in the previous paragraph. As a starting point, we will analyze and benchmark the prover times of the three methods described above on mock circuits that arithmetize ring-based operations to validate that our method is faster. Next, we will find the optimal FHE parameters and implement them on SNARKs of FHE for some mock circuits. 

## Plan and Deliverables
1) Analyze and benchmark the three methods of encoding ring operations in a SNARK:  
          a. CRT encoding - 20 hours
          b. Proving each non-native operation explicitly - 7 hours
          c. Coding-based SNARKs over polynomial rings - 7 hours
2) Build a mock FHE-SNARK and benchmark it against other implementations/techniques - 10 hours
3) Finally, implement a simplified version of an FHE-SNARK for the application described in https://writings.flashbots.net/blind-arbitrage-fhe - 40 hours
**Languages**: Rust
**Frameworks/Libraries**: Arkworks or Plonky3


## References
[ABPS24] https://cic.iacr.org/p/1/1/24/pdf
[ZCF23] https://eprint.iacr.org/2023/1705.pdf
[VKH23] https://arxiv.org/pdf/2301.07041 (Verifiable FHE)
[PP24] https://writings.flashbots.net/blind-arbitrage-fhe (FHE for MEV)

