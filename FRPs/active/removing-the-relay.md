---
id: <leave blank -- will be assigned by reviewers>
title: Removing the Relay in PBS
team: Guru-Vamsi Policharla
created: 2024-12-17
---

# Removing the Relay in PBS

## Background and Problem Statement
Provide motivation and background for the proposal, and clearly state the research questions it aims to tackle. Link to related or dependent Research Question(s) on the Flashbots Research Roadmap, and reference relevant Github Issues in this repository.

Recent results have shown that certain classes of relations admit *concretely efficient* witness encryption schemes that give rise to novel threshold encryption schemes: [GKPW24](https://eprint.iacr.org/2024/263), [CGPP24](https://eprint.iacr.org/2024/669), and [CGPW24](https://eprint.iacr.org/2024/1516). One very interesting application of [GKPW24](https://eprint.iacr.org/2024/263) is in removing the trusted relay in Proposer Builder Separation as outlined in our [blogpost](https://www.paradigm.xyz/2024/10/removing-the-relays).

Virtually all instantiations of PBS rely on a trusted intermediary party (relays) to provide necessary integrity and privacy guarantees to builders and proposers. Recently, we outlined a cryptographic approach to remove the relay in PBS (https://www.paradigm.xyz/2024/10/removing-the-relays). At a high level, block builders “witness encrypt” their block to the following statement: 

> My block can be decrypted iff $t$ out of $n$ validators sign the block with BLS signatures 

where the secret key to decrypt the block is the signatures themselves. Effectively, we bind privacy of the block to confirmation of inclusion. Thus, block builders can simply broadcast their encrypted block over a p2p network and the proposer can choose the highest paying block.

To guarantee that a proposer will be paid, one can use various approaches:
- Escrow mechanisms similar to the optimistic relay version of MEV-Boost (https://github.com/flashbots/mev-boost-relay/pull/380)
- The first transaction pays the proposer and left unencrypted
- Attaching TEE proofs of execution as proposed in TEE Boost (https://collective.flashbots.net/t/tee-boost/3741)
- Attaching proofs of correct execution via ZKVMs (quite expensive but maybe acceptable for rare instances where a massive MEV opportunity presents itself but the builder doesn’t have enough initial collateral for escrow and we don’t trust TEEs)

Importantly, this approach has advantages over previously explored solutions such as commit-and-reveal schemes. First and foremost, the builder no longer needs to send a second message as attestations on the block are themselves the key for decryption. Moreover, the threshold for decryption can be chosen dynamically at the time of encryption which allows a builder to reduce the threshold for decryption (if necessary when nodes are down and blocks are not receiving sufficient signatures).

## Plan and Deliverables
The goal of this research proposal is to:
1. Prototype, document, and open source the above scheme. The above approach can also be used in combination with other proposals such as BuilderNet/TEE Boost and will serve as a valuable starting point for extensions to encrypted mempools. It would be great to get feedback from the flashbots team here on the preferred starting point for this prototype.
2. It will also require careful modifications to the consensus and execution clients. For instance, attestation now needs to happen on encrypted blocks and therefore encrypted but invalid blocks may receive attestations. Note that this is not “free” as we can modify the protocol to mark the slot as empty and hence proposers lose out on their rewards. But slashing and fork choice rules need to be updated to take this into account, i.e. validators should not be penalized for attesting to an invalid but encrypted block as this is no fault of theirs. We will clearly document the above changes to enable the broader community to analyze, and identify any issues that the changes may pose.
3. Finally, the prototype will allow us to run valuable network experiments such as a) estimating any additional latency introduced on the critical path, and b) provide evidence for positive effects such as incentivizing builder decentralization.

## References
- Silent Threshold Encryption: [GKPW24](https://eprint.iacr.org/2024/263)
- How to Remove the Relay: [blogpost](https://www.paradigm.xyz/2024/10/removing-the-relays)
- Open Source implementation of Silent Threshold Encryption: [github repo](https://github.com/guruvamsi-policharla/silent-threshold-encryption)