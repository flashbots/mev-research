---
id: <leave blank -- will be assigned by reviewers>
title: <Deferred Revelation Auction>
team: <saguillo2000>
created: <2024-06-21>
---

# Credible Auctions

Incentive compatibility for auctioneers has become a topic of interest to mechanism designers of auctions within digital marketplaces. The main goal of this project is to produce an open source smart contract with the Deferred Revelation Auction (DRA) over Ledger from Taruan et. al.

## Background and Problem Statement

The concept of credibility, a strong form of incentive compatibility for auctioneers, has been stated as a desired goal of auctions that range from basic transactions in blockchains and NFTs to online ad auctions. The US Department of Justice’s 2023 antitrust suit against Google effectively argues that Google’s manipulation of ad auctions from the privileged position of auctioneer caused both buyers and users harm. In a permisionless environment as it is in blockchains Tarun describes 3 main areas where this type of auction can be applied to: NFTs market, MEV and PBS. 

A PoC of this protocol can ensure later open source colaboration in order to guarantee a fair price with the assets like NFTs or other types of manipulation by the auctioneer.

## Plan and Deliverables

The plan is to start with a simple Proof of Concept written in Solidity (we can see if for Rust or other type of languages can be useful). The roadmap would be as follows:

- Diagram of the auction and the different methods to be implemented.
- Provide a first PoC with tests

## References
Credible, Optimal Auctions via Blockchains: https://eprint.iacr.org/2023/114.pdf , Tarun Chitra et. al.
