# MEV-Research

## Flashbots Research Process
Flashbots Research is an open, transparent and iterative collective creation process taking inspiration from both academic and applied research, and modelled upon Ethereum Improvement Proposal (EIP) process. Anyone can contribute to Flashbots Research through opening or answering a Github issue in this repo, and/or writing a Flashbots Research Proposal (FRP) by proposing to answer a Research Question specified in the [Flashbots Research Roadmap (WIP)](research_roadmap.md), and/or create a pull request to revise a particular FRP. 
![Flashbots Research Process Diagram](/assets/Flashbots_ResearchProcess.png)
 
#### Flashbots Research Proposals (FRPs)
FRPs stands for Flashbots Research Proposal. It is a markdown document describing the approach to answering a core Research Question specified on the [Flashbots Research Roadmap (WIP)](research_roadmap.md). Similar to a research proposal for academic writing, it entails introducing what the research proposes to do and/or prove. It should incorporate systematic breakdown of the research question. It will also give an in-depth account of the methodologies, approaches or theories that will be used to support the hypothesis within the project, including a review of the relevant literature.
Please review [FRP-0](/FRPs/FRP-0.md) for the process of creating an FRP, and [FRP-1](/FRPs/FRP-1.md) as an example FRP.
If there exists a Research Question you deem important that is not currently on the Flashbots Research Roadmap, we invite you to open an Issue in this repository and propose your specific Research Question for consideration. FRP editors will review and update the Flashbots Research Roadmap periodically. 

#### Issues
If you would like to raise a new Research Question to be incorporated into the Flashbots Research Roadmap, or you are a (prospective) MEV Fellow who would like to breakdown a particular Research Question into addressable sub questions to seek community contributions, we invite you to open an Issue in this repository and link it to the relevant FRP Draft.
</br> An Issue will be closed by FRP editors if the newly proposed Research Question has been reviewed and acted upon, or a FRP has been completed, or the Issue is no longer relevant.

#### MEV Research Fellows
An MEV Research Fellow (or MEV Fellows) is a [MEV Fellowship](https://github.com/flashbots/mev-research/blob/main/research_fellowship.md) grant recipient whose FRP has been accepted upon review and who undertakes answering the Research Questions specified in the Flashbots Research Roadmap. In addition to delivering the FRPs, the MEV fellows, who can be either a natural person or an organization, will act as co-authors of the Flashbots research papers and are responsible for collaborating with other MEV Fellows in architecting, coordinating and delivering the Flashbots research papers and presentations. 

#### MEV Research Contributors
If you are interested in contributing but do not want to commit to the responsibility of drafting and getting necessary alignment for an FRP, you can become a MEV Research Contributor (or Contributor). A Contributor is anyone who is not an MEV Fellow but contributes meaningful artifacts to FRPs that end up being included in the Flashbots research papers. Contributors can be either invited by respective MEV Fellows for particular FRP throughout its lifecycle of research, or request to join an MEV Fellow to work on a particular FRP before its review, to collaborate on a particular Research Question. 
</br> Opening/answering Github Issues in this repo or creating meaningful pull requests to draft FRPs are ways to signal interest and demonstrate qualification as a Contributor. Contributors will be recognized in the papers for their contribution.

## Flashbots Research Phase I
Phase I of [Flashbots Research Roadmap (WIP)](research_roadmap.md) is considered the proof-of-concept stage of Flashbots. It consists in practical/ultra-applied research akin to 'industry' R&D, in close loop with development. We expect Flashbots developers to be heavily involved in this phase.
</br> Phase I has 2 research papers as a deliverable, the first draft of the papers will be due at the end of January, and publication targeting Q1 2021. 
The outcome of Phase I is immediately relevant to providing technical and economic evaluation to the Flashbots Proof-of-Concept (PoC), and communicating our design and intentions to the community.

#### Phase I Timeline
The tentative timeline for Flashbots Research Phase I is as follows, subject to adjustment by FRP editors.
![Flashbots Research Phase I Timeline](/assets/Flashbots_ResearchPhaseITimeline.png)

#### Paper 1: Whitepaper / proof-of-concept
Paper style/field: Cryptocurrency systems paper, short paper/PoC (9pgs)
</br> Similar papers: bloxroute, Thunderella, FlyClient
</br> Venue: FC22? USENIX?
- **Research Question:** How can we build a "good" auction mechanism for validator priority "bribes"?
  - Related FRP: [FRP-1](/FRPs/FRP-1.md)
  - Related Issues: to be updated
- **Research Question:** How can we leverage existing auction literature?
  - Related FRP: to be updated
  - Related Issues: to be updated
- **Research Question:** How does architecture differ across PoW/PoS/leaderless?
  - Related FRP: to be updated
  - Related Issues: to be updated

#### Paper 2: Ethical / community charter
Paper style/field: CS ethics / social sciences paper, short paper (10-12pgs)
</br> Similar papers: On the Moral Character of Cryptographic Work, Will the Market Fix the Market
</br> Venue: IEEE S&B?  Ledger journal?
- **Research Question:** Should we build a "good" auction mechanism for validator priority "bribes"?
  - Related FRP: to be updated
  - Related Issues: to be updated
- **Research Question:** How do we minimize possible user harm of priority bribe incentives?
  - Related FRP: to be updated
  - Related Issues: to be updated
- **Research Question:** How do we minimize possible consensus harms of priority bribe incentives?
  - Related FRP: to be updated
  - Related Issues: to be updated
- **Research question:** Should we allow for any MEV on the system? Should we bound the MEV?
  - Related FRP: to be updated
  - Related Issues: to be updated

**Authorship**
</br> Our research efforts will output research papers that will be shaped by Research Fellows. Anyone (including entities) can be an author of these papers as long as they meet one of the criteria for authorship we follow, as described in the Association for Computing Machinery's [Criteria for Authorship](https://www.acm.org/publications/policies/authorship), with modification to recognize contribution from anonymous authors.

## MEV Research Workshop
### Purpose
</br> Research workshop is a 60-minute weekly discussion that addresses specific research questions, Flashbots Research Proposals (FRPs) and/or open questions within the scope specified in the [Flashbots Research Roadmap (WIP)](research_roadmap.md), so to set directions for resolving open issues or specific questions that arise from research-engineering coordination. Anyone can propose a topic to be discussed in the Research Workshop by opening a github issue in Flashbots' [/mev-research repo](https://github.com/flashbots/mev-research/) and/or labeling an outstanding issue "workshop", and linking it to related FRPs and github issues or research questions yet to be addressed (Example: [Issue 24](https://github.com/flashbots/mev-research/issues/24) on MEV taxonomy). Research workshop will be recorded and published after the call.

| No. |Date | Topic | Agenda | Notes | Recording |
|:---|:---|:---|---|---|:---|
1 | Nov 19 | Breaking down Research Roadmap into Research Questions | - | - | [video](https://drive.google.com/file/d/1_3ukmSFWq2qeucg00OUpOfdHQ-BOkBR1/view?usp=sharing) |
2 | Dec 3 | Flashbots Research Proposals (FRPs) and Research Processs | - | - | [video](https://drive.google.com/file/d/18aH_2kYFFw3oyohDNidID4riR-fE5sIi/view?usp=sharing) |
3 | Dec 10 | Developing an MEV Taxonomy | [Issue #24](https://github.com/flashbots/mev-research/issues/24) | to be updated | [video](https://drive.google.com/file/d/18aH_2kYFFw3oyohDNidID4riR-fE5sIi/view?usp=sharing) |

## Resources:
</br> [Flashbots Medium](https://medium.com/flashbots/frontrunning-the-mev-crisis-40629a613752)
</br> [Flashbots EthResearch post](https://ethresear.ch/t/flashbots-frontrunning-the-mev-crisis/8251)
</br> [Research Roadmap](https://github.com/flashbots/mev-research/blob/main/research_roadmap.md)
</br> [Research Fellowship](https://github.com/flashbots/mev-research/blob/main/research_fellowship.md)

## **Ship Vault**
</br> [Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges by Daian et. al.](https://arxiv.org/abs/1904.05234)

[Frontrunning in DEXs, Miner Extractable Value, and Consensus Instability by Phil Daian at IEEE Symposium on Security and Privacy](https://youtu.be/vR1v7AQ8i3k)

[How To Get Front-Run on Ethereum mainnet by Scott Bigelow](https://youtu.be/UZ-NNd6yjFM)

[High-Frequency Trading on Decentralized On-Chain Exchanges by Zhou et. al](https://arxiv.org/abs/2009.14021)

[Fair Sequencing Services: Enabling a Provably Fair DeFi Ecosystem by Juels et. al. (Chainlink)](https://blog.chain.link/chainlink-fair-sequencing-services-enabling-a-provably-fair-defi-ecosystem/)

[MEV Auction: Auctioning transaction ordering rights as a solution to Miner Extractable Value by Karl Floersch (Optimism)](https://ethresear.ch/t/mev-auction-auctioning-transaction-ordering-rights-as-a-solution-to-miner-extractable-value/6788)


[Blinder: MPC Based Scalable and Robust Anonymous Committed Broadcast by Ittai Abraham et. al.](https://eprint.iacr.org/2020/248)

[Time, clocks, and the ordering of events in a distributed system by Leslie Lamport](https://amturing.acm.org/p558-lamport.pdf)

[On The Instability Of Bitcoin Without The Block Reward by Carlsten et. al.](https://www.cs.princeton.edu/~arvindn/publications/mining_CCS.pdf)

[SoK: Transparent Dishonesty: Front-running Attacks on Blockchain by Eskandari et. al.](https://arxiv.org/pdf/1902.05164.pdf)

[MEV auctions considered harmful by Ed Felten (Offchain Labs)](https://medium.com/offchainlabs/mev-auctions-considered-harmful-fa72f61a40ea)

[Order-Fairness for Byzantine Consensus by Kelkar et. al.](https://eprint.iacr.org/2020/269)

[Tesseract: Real-Time Cryptocurrency Exchange Using Trusted Hardware by Bentov et. al](https://eprint.iacr.org/2017/1153.pdf)

[Submarine Sends by Breidenbach et. al.](https://libsubmarine.org/)

[TEX – A Securely Scalable Trustless Exchange by Khalil et. al.](https://eprint.iacr.org/2019/265.pdf)

[Spam resistant block creator selection via burn auction by Barry Whitehat](https://ethresear.ch/t/spam-resistant-block-creator-selection-via-burn-auction/5851)


## Miscellaneous Gems
[Ethereum is a Dark Forest by Dan Robinson](https://medium.com/@danrobinson/ethereum-is-a-dark-forest-ecc5f0505dff)

[Escaping the Dark Forest by Sam Sun](https://samczsun.com/escaping-the-dark-forest/)

[Dark Forest Escape Route Starkware whiteboard session video recording](https://www.crowdcast.io/e/dark-forest-escape-route)

[ETHOnline - 'Phil & Georgios Talk Miner Extractable Value'](https://youtu.be/tv0CkmcoGkM)

[IC3 Blockchain Camp 2020 - Phil Daian - "DeFi Composability - Friend or Foe?"](https://youtu.be/55o-1On5a2U)

[Gas Wars: Understanding Ethereum’s Mempool & Miner Extractable Value by Uncommon Core podcast](https://anchor.fm/uncommoncore/episodes/9-Gas-Wars-Understanding-Ethereums-Mempool--Miner-Extractable-Value-ejtp3j)

[The Alchemy of Hashpower (Part II) by Leo Zhang](https://www.aniccaresearch.tech/blog/the-alchemy-of-hashpower-part-ii)

[Exploring DeFi Trading Strategies: Arbitrage in DeFi by Alex Obadia](https://link.medium.com/Q389Yt3LH9)

[How to munch on pickles from a whale dinner by Tomasz Mierzwa](https://link.medium.com/RavyJlN9oab)

[Portion of Daily Gas Used by Backrunning Bot Contracts by Phillipe Castonguay](https://explore.duneanalytics.com/public/dashboards/FFFpCKoE41bvFpESiyjUIBJfEMt4GoMFwcidNcAh)

[Gas Gambits - Game Theory Example of Incentivized Collaboration by KeeperDAO](https://medium.com/keeperdao/gas-gambits-game-theory-example-of-incentivized-collaboration-9a42e9c9b867)

[Phantom TX: a dark pool for Ethereum transactions](http://phantomtx.com)

[Candyshop: a smart transaction batching service that extracts value by controlling transaction ordering]( https://www.notion.so/CandyShop-Quick-Overview-517b726b0e1c4f06b3fe88f0a0ee1577)

[Scrooge-McEtherface: attack tool that loots Ether from vulnerable smart contracts](https://github.com/b-mueller/scrooge-mcetherface)

[Surrogeth: Tricking frontrunners into being transaction relayers](https://ethresear.ch/t/surrogeth-tricking-frontrunners-into-being-transaction-relayers/6937)

[B.Protocol: A Decentralized Backstop Liquidity Protocol](https://medium.com/b-protocol/b-protocol-b6dd4e3bf9c0)

[Gas Now (Sparkpool): ETH Gas Price quotation system based on Pending transactions](http://www.gasnow.org)

[Blocknative Mempool Explorer](https://explorer.blocknative.com/)

[Geth Wiki](https://geth.ethereum.org/docs/)

[What diagrams exist to illustrate the Ethereum blockchain creation process?](https://ethereum.stackexchange.com/questions/2286/what-diagrams-exist-to-illustrate-the-ethereum-blockchain-creation-process)
