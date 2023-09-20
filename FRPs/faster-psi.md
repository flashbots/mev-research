---
id: <leave blank -- will be assigned by reviewers>
title: Fast Private Set Intersection
team: lichu@semiotic.ai, gokay@semiotic.ai, severiano@semiotic.ai (leader), sam@semiotic.ai, 
created: 2023-08-16
---

# Even Faster Private Set Intersection

## Background and Problem Statement

Privacy-preserving set intersection (PSI) lets two parties find the intersection of their respective sets where neither party can infer elements in the other party's set that are not in the intersection. This has multiple use cases in standard computing, such as a secure database join, cheater detection algorithms in online games, and human genome testing. A secure and fast PSI algorithm would also be useful in the blockchain context, for example for comparing access lists ([EIP-2930](https://eips.ethereum.org/EIPS/eip-2930)) and as a primitive to enable private auctions.

The most obvious solution to the PSI problem is the hashing solution: Alice hashes all the elements in her set and sends them to Bob. Bob hashes all the elements in his set and compares them to Alice’s. Even though this is extremely fast and involves little communication, it can leak privacy of Alice’s inputs if the space is small. Alice could simply hash all the elements in the space and compare them to the elements in Bob’s hashed set!

On the other hand, most existing PSI implementations rely on a third-party server ("server-aided protocols"). While these protocols are secure if the three parties are disconnected, they are completely insecure if the server colludes with one of the actors. One of our team members, Gokay, improved these methods while working at Samsung Research for private location sharing (Saldamli & Chow, 2022).

To remove the reliance a third-party server, we propose to use fully homomorphic encryption (FHE) to perform PSI in a completely trustless manner. In addition, we seek to improve upon state-of-the-art FHE PSI algorithms by building an algorithm that uses fixed-depth circuits, which allows for comparing sets of unlimited size without a large performance impact. This would serve as a strong cryptographic primitive that could be used across multiple subdomains within blockchains.

We base our research and implementation on Chang et. al.'s ["Fast Private Set Intersection from Homomorphic Encryption"](https://dl.acm.org/doi/10.1145/3133956.3134061). Their protocol uses circuits whose depth is the size of the smallest set being compared. We will implement their protocol and add optimizations that fix the circuit depth to some value D. These optimizations consist roughly of splitting one of the sets into multiple subsets of size D, and running the original protocol multiple times against each of those subsets. We hypothesize that the execution time will be approximately the same, but having a fixed depth will allow larger sets to be used without sacrificing security.

## Plan and Deliverables

1. Write down details of our optimizations.
2. Implement original protocol using Microsoft SEAL, the most widely used FHE library both in the academia and in the industry.
3. Implement optimizations.
4. Benchmark and compare both protocols.

Note that our implementation will use a Node wrapper library of Microsoft SEAL, making it possible to run the algorithm even from the browser!

## References

-   A. Narayanan, N. Thiagarajan, M. Lakhani, M. Hamburg, and D. Boneh, Location privacy via private proximity testing, In proceedings of NDSS 2011.
-   S. Kamara, P. Mohassel, M. Raykova, and S. Sadeghian. Scaling private set intersection to billion-element sets. In Financial Cryptography and Data Security (FC’14) , LNCS. Springer, 2014.
-   G. Saldamli, R. Chow. "Fast Private Set Intersection", Preprint 2022
-   Hao Chen, Kim Laine, and Peter Rindal. 2017. Fast Private Set Intersection from Homomorphic Encryption. In Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security (CCS '17). Association for Computing Machinery, New York, NY, USA, 1243–1255.
