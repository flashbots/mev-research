
---
id: <leave blank -- will be assigned by reviewers>

title: Mitigating Timing Games with Right Incentives - Game Theory for Efficient Consensus
 
team: Rasheed (IIIT Hyderabad), Parth Desai (IIIT Hyderabad), Sujit Gujar (IIIT Hyderabad)

created: 2025-10-15

---

# FRP: Mitigating Timing Games with the Right Incentives – Game Theory for Efficient Consensus

**Maximal Extractable Value (MEV)** refers to the profit obtainable by reordering, including, or excluding transactions within a block [1]. MEV has become a critical factor in Ethereum’s transaction ecosystem, as miners (and post-Merge, validators) can manipulate transaction ordering for financial gain. A fast (low-latency) proposer may delay block proposals to capture higher rewards from transactions that would otherwise appear in the next block. Such strategies are known as **timing games** [4]. While profitable for fast proposers, timing games reduce fairness and decentralization, increase the risk of missed blocks, and degrade overall network efficiency. This FRP studies timing games and proposes game-theoretic solutions that require minimal protocol changes while effectively mitigating the problem.

----------

## Background and Problem Statement

### Background

Traders and bots often exploit MEV using front-running, back-running, or sandwich attacks, particularly in DeFi environments [2,3]. Block propagation latency is inherent in distributed blockchains, and PoS protocols allow a timing buffer for blocks to propagate. Low-latency proposers may exploit this by delaying block release by a few seconds, capturing transactions meant for subsequent blocks.

Timing games effectively steal MEV from future proposers, reduce attestation time, increase missed slots, and pressure decentralization, favoring validators with superior network connectivity. Honest proposers may leave the system, making timing games a serious threat to fairness and decentralization.

Ethereum currently operates in **epochs** of 32 slots, each lasting 12 seconds. Validators are pseudorandomly chosen to validate each block. A _proposer_ publishes a block, while _attestors_ validate it. Each slot is subdivided into three phases: block propagation, attestation aggregation, and aggregated attestation propagation.

_Builders_ assemble transactions into blocks and bid for inclusion with the proposer, who selects the highest bid. This is called **proposer-builder separation (PBS)**. Ethereum implements PBS via **MEV-Boost**, which uses trusted relays as intermediaries between builders and proposers [6]. Relays aggregate blocks, validate them, and forward the highest bids. Currently, 90% of Ethereum blocks are published via relays [13,14].

----------

### Problem Statement

The current incentive design encourages timing games. Searchers submit profitable bundles to builders, who compete by constructing higher-revenue blocks. Proposers are incentivized to delay block publication for higher bids.

Attestors, however, are only incentivized to attest to blocks promptly and cannot distinguish between network delays and strategic delays. Since proposers face no penalties for timing games, preventing such behavior is difficult.

----------

### Related Work

**Timing Games and Their Impact**  
Timing games are profitable for proposers and increase missed blocks due to limited attestation time, contributing to centralization [4,5].

**Proposer Score Boost and Honest Reorgs**  
Ethereum introduced Proposer Score Boost [7] and Honest Reorgs [8] to incentivize on-time publishing. The former gives proposers a temporary fork-choice boost, and the latter allows honest proposers to reorg blocks with low attestation weight. However, proposers may still strategically delay publishing to meet minimum vote thresholds, so reorgs continue [12].

**Relay Enforcement**  
Relays could enforce honest block timing [9], e.g., by rejecting late bids. But restrictive relays may prompt creation of new, less-restrictive relays. Competitive pressures limit enforcement, and relays’ alignment with network fairness is not guaranteed.

**Monitoring and Penalties**  
Proposals include tracking block release consistency and penalizing missed slots [9]. Both approaches have limitations: detecting timing games is difficult, and penalties may punish honest proposers who miss slots naturally.

----------

## Plan and Deliverables

Proposers have strong control over slot outcomes and little incentive to propose promptly. We aim to:

1.  Analyze timing games and design incentive schemes that discourage delays. Proposer utility should decrease over time.
    
2.  Model the proposed solution using game-theoretic analysis to ensure on-time block publication is optimal.
    
3.  Validate the approach via simulation and theoretical analysis.
    
4.  Publish a blog post discussing minimal protocol changes and trade-offs.
    
5.  Publish a research article.
    
6.  Release all code publicly on GitHub.
    

----------

## References

1.  Ethereum. 2024. _Maximal Extractable Value (MEV)_. [https://ethereum.org/en/developers/docs/mev/](https://ethereum.org/en/developers/docs/mev/)
    
2.  Yan Ji & James Grimmelmann. 2025. _Regulatory Implications of MEV Mitigations_. Springer, Cham, 335–363.
    
3.  Sen Yang et al. 2024. _SoK: MEV Countermeasures_. DeFi ’24, 21–30.
    
4.  Timing Games Data. [https://timing.pics/](https://timing.pics/)
    
5.  Anton Wahrstätter et al. 2023. _Time to Bribe: Measuring Block Construction Market_. arXiv:2305.16468
    
6.  Flashbots. 2024. _MEV-Boost Overview_. [https://docs.flashbots.net/flashbots-mev-boost/introduction](https://docs.flashbots.net/flashbots-mev-boost/introduction)
    
7.  L. Heimbach et al. 2023. _Ethereum’s Proposer-Builder Separation_. ACM IMC ’23, 406–420.
    
8.  Caspar Schwarz-Schilling et al. 2023. _Time is Money: Strategic Timing Games in PoS Protocols_. arXiv:2305.09032
    
9.  _Timing Games: Implications and Possible Mitigations_. [https://ethresear.ch/t/timing-games-implications-and-possible-mitigations/17612](https://ethresear.ch/t/timing-games-implications-and-possible-mitigations/17612)
    
10.  Ethereum. 2021. _Proposer LMD Score Boosting_. [https://github.com/ethereum/consensus-specs/pull/2730](https://github.com/ethereum/consensus-specs/pull/2730)
    
11.  Ethereum. 2023. _Allow Honest Validators to Reorg Late Blocks_. [https://github.com/ethereum/consensus-specs/pull/3034](https://github.com/ethereum/consensus-specs/pull/3034)
    
12.  Toni Wahrstätter. 2025. _Reorg.pics_. [https://reorg.pics/](https://reorg.pics/)
    
13.  A. Unger. 2023. _From Searchers to Proposers: User Behaviour in Ethereum PBS_
    
14.  rated. 2025. _Relay Landscape | Ethereum Mainnet_. [https://explorer.rated.network/relays?network=mainnet&timeWindow=1d](https://explorer.rated.network/relays?network=mainnet&timeWindow=1d)
    