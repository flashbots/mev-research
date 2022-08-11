---
id: <leave blank -- will be assigned by reviewers>
title: <Improvig Commit-Reveal Scheme and Proposer Builder Separation (PBS) for Better MEV Resistance>
team: <Dr.Jiahua Xu, Jieliang Yin, Yebo Feng, Zhangxiang Hu>
created: <2022-07-26>
---

# Research Grant Proposal - Improving Commit-Reveal Scheme and Proposer Builder Separation (PBS) for Better MEV Resistance
 
 There are different kinds of Maximum Extractable Value (MEV) on DeFi like arbitrage, front-running, and sandwich attack, and one kind of MEV is that miners can arbitrarily view, censor, and reorder users' transactions before putting them on chain to earn extra profits from them at the expanse of users' interests.
 
 Such kind of MEV is detrimental to users and to protect users from such MEV, different privacy-preserving techniques have been proposed to hide the details of users' transactions like the commit-reveal scheme, which allows users to submit an encrypted transaction to the chain, and reveal the content later only after it is confirmed with immutability. Compared with other full privacy-preserving techniques like zero-knowledge proof, it doesn't provide so strong privacy protection but is already enough for protecting users' transactions from MEV at lower cost and better efficiency, which is more practical and economical for most users.
 
 However, the current commit-reveal scheme still has unsolved problems for practical and widespread use. For each transaction, commit-reveal requires users to submit twice on chain including one encrypted and one revealed, which is not so efficient and reliable. For a better commit-reveal scheme, we design a new commit-reveal scheme with improved Proposer Builder Separation (PBS) that optimizes the whole on-chain process. Proposers reach consensus together on the encrypted transactions users commit first, then decrypt and reveal them for the builder to verify, execute and append on chain. With corresponding technical evaluation and economic analysis, we will prove that it will resist MEV better and benefit users, proposers, and builders.



## Background and Problem Statement
 
 Some malicious MEV previews users' transactions in advance and then censors and reorders them like front-running and sandwich attacks. To prevent such MEV, different solutions have been proposed including PBS and privacy-preserving techniques. Based PoS consensus used by Ethereum 2.0, miners working on PoW will be replaced by validators, and PBS separates validators into builders constructing new blocks and proposers, especially accepting and putting new blocks on chain. In this way, MEV profits could be shared with builders, and proposers can transfer the workload of sophisticated block construction and MEV execution while maintaining the stability and decentralization of blockchain consensus.
 
 However, PBS does not prevent malicious MEV from users' transactions. To protect the transactions of users from MEV, privacy-preserving techniques like cryptography and zero-knowledge proof can make the details of transactions fully private except for users themselves, so builders and proposers have no chance to know the transaction content to launch MEV attacks on them.
 
 However, the additional cost and delay caused by many privacy-persevering MEV resistance techniques are too high to be used in reality. Achieving full privacy-preserving like the zero-knowledge proof is too costly and inefficient, and there is no need to make transactions fully private for MEV resistance. Also, full privacy-preserving will inevitably compromise usability and transparency to some degree, which is not so applicable in practice like meeting requirements of the financial regulation. Full privacy also doesn't work in many DeFi applications like AMM, which needs to reveal the latest public states timely for usability and transparency. Other proposed solutions either need centralized third-party or strong security assumptions, which are not reliable and realistic under many situations.

  

## Plan and Deliverables
 
 To address the issues above, in our research, on the one hand, we will look into different kinds of privacy-preserving techniques like commit-reveal and optimize them to enhance their usability, efficiency, and reliability. On the other hand, by improving PBS and combining it with optimized privacy-preserving techniques, we make PBS MEV resistible, and improved PBS can better implement optimized privacy-preserving techniques.
 
 In our commit-reveal design, users send encrypted transactions to proposers. Based on the improved PBS, proposers will first accept and reach consensus on them. They can't do any MEV attacks because the content of transactions is hidden. After proposers confirm which transactions will be put on chain, those transactions can be revealed and sent to the builder for validation and execution. Knowing the details of transactions after being revealed, builders can process them at lower cost and better efficiency, but they can't extract MEV because their order and content have already been determined by proposers during the commit phase. In this way, users could be protected from MEV attacks when proposers commit their transactions first for consensus, and maintain transparency and usability when builders reveal their transactions to process and put them on chain.
 
 By improving and combining PBS and commit-reveal, our solution aims at enabling usable, efficient, and reliable on-chain service that protects users' interests from MEV and regulates proposers and builders without privileges. To the best of our knowledge, our work is the first to:

 * improve PBS including applying commit-reveal technique into PBS to make PBS MEV resistible.
 
 * improve commit-reveal technique with improved PBS for better MEV resistance in usability, efficiency, transparency, and reliability.
 
 * optimize the on-chain process to balance the relationship among users, proposers, and builders and avoid anyone having privileges for maximizing their  self-interests but harmful to others within the blockchain.
 
  * design the incentive mechanism to make our solution benefit every participant on blockchain including users, proposers, and builders.

 Our timeline, budget, and deliverables could be:
 
  * August 2022: Design the privacy-preserving and cryptography techniques including the commit-reveal scheme for better usability, efficiency, and transparency than existing MEV mitigation strategies.
 
  * September 2022: Improve the PBS scheme and combine it with privacy-preserving techniques to make it MEV resistible.
 
  * October 2022: Design the corresponding fee mechanism to benefit users, miners (or validators), and MEV extractors. We will prove that although no MEV attack exists, a better trading experience will bring more transactions, so they can still earn more than now.
 
  * November 2022: Develop the demo for our technical design and invite all users in the community to test, evaluate, and contribute to it.
 
  * December 2022: Write the research report explaining our design in detail and submit it along with the demo code and testing result as deliverables.
 
 The amount of the grant is highly flexible and negotiable. After getting the grant, the whole research process will be fully open in the community and everyone in the community is welcome to join and contribute to our research. They can also make all kinds of contributions besides research like development, testing, feedback, and promotion. The given grant will be used to reward all contributors in the community to reward their valuable contributions.
  
 
 
## Team Members
 Supervisor Dr.Jiahua Xu: Dr. Jiahua Xu (https://jiahua-xu.com) is a Research Project Manager at University College London Centre for Blockchain Technologies, UK. Her research interests lie primarily in blockchain economics, behavioral finance, and risk management.
  
 Jieliang Yin: Jieliang Yin is a graduate student studying at Carnegie Mellon University proposing this research project. He is interested in blockchain research and design and had several blockchain research and design experiences
  
 Yebo Feng: Yebo Feng is a Ph.D. candidate in the Department of Computer and Information Science at the University of Oregon (UO), where he conducts his research in the Center for Cyber Security and Privacy. His research interests include network security, anomaly detection, DDoS defense, and distributed system security. He is the recipient of the Best Paper Award of 2019 IEEE CNS, Gurdeep Pall Graduate Student Fellowship of UO, and Ripple Research Fellowship. He has served as the reviewer of IEEE TDSC, ACM TKDD, and IEEE JSAC. He was also on the program committees of several international conferences, such as CYBER, SECURWARE, and B2C.
 
 
 We welcome more people to join and contribute to our research and will give them corresponding returns!
 
