---
id: 48
title: Removing the Relay in PBS
team: Guru-Vamsi Policharla
created: 2024-12-17
status: active
---

# Removing the Relay in PBS

## Background and Problem Statement
Recent results have shown that certain classes of relations admit *concretely efficient* witness encryption schemes that give rise to novel threshold encryption schemes: [GKPW24](https://eprint.iacr.org/2024/263), [CGPP24](https://eprint.iacr.org/2024/669), and [CGPW24](https://eprint.iacr.org/2024/1516). One very interesting application of [GKPW24](https://eprint.iacr.org/2024/263) is in removing the trusted relay in Proposer Builder Separation as outlined in our [blogpost](https://www.paradigm.xyz/2024/10/removing-the-relays).

Virtually all instantiations of PBS crucially rely on a trusted intermediary party (relays) to provide necessary integrity and privacy guarantees to builders and proposers. In more detail, the relay in PBS guarantees:

1. **Privacy for Builders:** The relay ensures that proposers do not learn any information about the block contents until they proposing this this block. Importantly, this prevents them from stealing the MEV found by the builder.
2. **Safety for Proposers:** The relay also executes all blocks sent by builders to confirm that the block is valid and to compute the additional value that the proposer will receive should they propose this block.

Recently, we outlined a cryptographic approach to remove the centralized relay in PBS (https://www.paradigm.xyz/2024/10/removing-the-relays). We summarize the approach below.


**Privacy for Builders:** The most challenging aspect of removing the relay lies in designing a mechanism that preserves privacy of bids up until one of them is actually chosen (as the next block). To realize this, we leverage the witness encryption scheme[^1] from [GKPW24](https://eprint.iacr.org/2024/263).

At a high level, block builders “witness encrypt” their block to the following statement: 

> My block can be decrypted iff $t$ out of $n$ validators sign the block with BLS signatures 

where the statement consists of the $n$ public keys, and the witness (secret key) to decrypt the block is signatures from some subset of $t$ validators. This allows us to effectively bind privacy of the block to confirmation of inclusion on chain. Thus, block builders can simply broadcast their encrypted block over a p2p network and the proposer can choose the highest paying block. We emphasize here that this component of the solution is applicable to PBS in general.


**Safety for Proposers:** It is reasonably easy to handle the latter requirement even without a centralized party. We outline various approaches, tailored to existing approaches in PBS:
- To improve throughput and reduce latency, an [*optimistic*](https://github.com/michaelneuder/optimistic-relay-documentation/blob/main/towards-epbs.md) version of MEV-Boost relay was [implemented](https://github.com/flashbots/mev-boost-relay/pull/380). Essentially, they implement an escrow mechanism where builders put up collateral when submitting a bid and the proposer gets paid irrespective of whether the block is valid. We can use a similar mechanism to ensure proposers get paid, even if builders propose invalid blocks.
- Attaching TEE proofs of execution as proposed in TEE Boost (https://collective.flashbots.net/t/tee-boost/3741). This approach also extends to BuilderNet as blocks are built inside TEEs and can come with execution proofs.
- Attaching proofs of correct execution via ZKVMs (quite expensive but maybe acceptable for rare instances where a massive MEV opportunity presents itself but the builder doesn’t have enough initial collateral for escrow and we don’t trust TEEs).

Importantly, this approach has advantages over previously explored solutions such as commit-and-reveal schemes. First and foremost, the builder no longer needs to send a second message as attestations on the block are themselves the key for decryption. Moreover, the threshold for decryption can be chosen dynamically at the time of encryption which allows a builder to reduce the threshold for decryption (if necessary when nodes are down and blocks are not receiving sufficient signatures).

However, the approach will require careful modifications to the consensus and execution clients. For instance, attestation now needs to happen on encrypted blocks and therefore encrypted but invalid blocks may receive attestations. Note that this is not “free” as we can modify the protocol to mark the slot as empty and hence proposers lose out on their rewards. But slashing and fork choice rules need to be updated to take this into account, i.e. validators should not be penalized for attesting to an invalid but encrypted block as this is no fault of theirs. 

At the moment, we do not have a full picture of the required changes. We expect additional changes beyond the ones mentioned above. A good starting point for the PoS protocol can be found [here](https://eth2book.info). 
We will clearly document the above changes in the form of a markdown document to enable the broader community to analyze, and identify any issues that the changes may pose.

## Plan and Deliverables
The end goal is to have an ethereum test-net which implements the above scheme. Although the core cryptographic protocol of Silent Threshold Encryption has been implemented, it needs to be integrated into a full fledged system. This is the main deliverable of this FRP. It will involve the following steps:

* First all validators need to publish "hints" -- which are additional material that is computed as a function of their secret key and a powers-of-tau CRS. These "hints" are placed in a PKI.
* Builders have access to this PKI and can download the public keys and hints of all validators. They then compute the "aggregated public key" for each slot and encrypt their bid to this public key. Note that the threshold can be chosen at the time of encryption.
* The proposer will choose the highest paying block and propose it to the network. For the prototype, we will assume there is *some mechanism* to ensure the proposer gets paid. We will not be explicitly implementing it as it is not the main focus of the FRP. 
* Finally, once sufficiently many attesations have been received anyone can decrypt the block.

The above prototype will serve as *template* that can be combined with various instantiations of PBS such as BuilderNet/TEE Boost. This will only affect how the proposer gets paid -- which can be instantiated in a flexible manner. It would be great to get feedback from the flashbots team here on the preferred starting point for this prototype with these goals in mind.

A full fledged test-net should be a good starting point to run network experiments to estimate any additional latency introduced on the critical path. We will be able to provide some preliminary benchmarking results.
Designing and running more extensive experiments would allow us provide evidence for positive effects such as incentivizing builder decentralization. However, we expect this to require quite a bit of work -- a separate research project in itself. Carrying this out may be a good idea for an FRP in the future.

## References
- Silent Threshold Encryption: [GKPW24](https://eprint.iacr.org/2024/263)
- How to Remove the Relay: [blogpost](https://www.paradigm.xyz/2024/10/removing-the-relays)
- Open Source implementation of Silent Threshold Encryption: [github repo](https://github.com/guruvamsi-policharla/silent-threshold-encryption)

[^1]: Consider an NP relation $\mathcal{R} \subset \{0,1\}^* \times \{0,1\}^*$. (Extractable) Witness encryption allows a user to encrypt a message to an NP statement $x$ such that the ciphertext can be decrypted if and only if you know a valid witness $w$ such that $(x,w) \in \mathcal{R}$.
