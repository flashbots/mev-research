---
id: <leave blank -- will be assigned by reviewers>
title: What we learn from failed transactions on Ethereum
team: Alireza Arjmand, Professor Majid Khabbazian, University of Alberta
created: 2023-02-09
---

# What we learn from failed transactions - Malicious pattern discovery

Imagine we are in 2040 and wonder if there were cases of censorship in 2020. We can go back on the canonical chain and analyze the blocks mined in 2020. If we find partially-empty blocks, we may suspect that there were censorship cases in 2020. This is suspicious, however, does not have a solid support as one may argue that there were perhaps not enough transactions in the mempool at the time where partially-empty blocks were mined. Unfortunately, we do not have the full picture of the 2020 mempool data in 2040 (we only know the part that were published on the blockchain). Even if a person has stored the whole mempool data in the past two decades, there is no consensus on the stored data, so we have to fully trust the person to draw a conclusion. A conclusion based on trusting an external party has no place, at least, in the scientific community. This brings us to the question of whether or not it is possible to use the public blockchain itself to make an argument in favor or against the existence of censorship. We surprisingly show that it is somewhat possible, thanks to the failed transactions!

While a small percentage of all transactions fail on Ethereum mainnet, they are included in the blocks and happen regularly. While many choose to ignore these transactions, we believe that failed transactions can help find malicious patterns such as weak censorship and PGAs. While MEV-Boost drops the failed transactions from its introduced blocks, we shift our focus to the public mempool transactions.

To justify the importance of the topic, we will provide a summary of our work so far in the subsequent paragraphs. We start by replaying failed transactions at the start of the three previous blocks to see if they would succeed, if they do, we tag them as a rational failed transaction. We notice that over 60 percent of failed transactions classify as rational and could have been successful if they were included in their expected position by the block builders. This can be explained by how competitive opportunity capturing is (checked MEV [[2]](notion://www.notion.so/Failed-Transactions-Flashbots-research-proposal-6c34ed7b0ed64f11991d4a5daa537d68######2.)). We also found out that these transactions paid close to 1.65M$ USD gas fee in only three weeks of analysis time.

By analyzing this data, however, we noticed that some of the transactions were aiming to be included in an earlier index or block. We consider that (1) our users are rational, (2) they decide to send a transaction based on a state on a certain block height, and (3) they will not send their transactions after the opportunity is captured. Therefore, if the inclusion of a rational failed transaction happens a couple of blocks after a position it could be successful in, considering the delay of the network [[3]](notion://www.notion.so/Failed-Transactions-Flashbots-research-proposal-6c34ed7b0ed64f11991d4a5daa537d68######3.), and the block mining time, we can use the censorship definition mentioned by Justin Drake [[1]](notion://www.notion.so/Failed-Transactions-Flashbots-research-proposal-6c34ed7b0ed64f11991d4a5daa537d68######1.), and tag that transaction as censored in case there was enough gas in a block to include the transaction.

We can also reason by analyzing failed transactions and find the instances of PGAs. We believe that this method can be complimentary with the method used by Daian et al. [[5]](notion://www.notion.so/Failed-Transactions-Flashbots-research-proposal-6c34ed7b0ed64f11991d4a5daa537d68######5.).

The novelty of our approach lies in the exclusion of mempool. Monitoring the mempool can be a simple way of finding censorships and PGAs but has proven to be a substantial task by [[5]](notion://www.notion.so/Failed-Transactions-Flashbots-research-proposal-6c34ed7b0ed64f11991d4a5daa537d68######5.) as there can be different versions of mempool based on the location of nodes in the network. However, by doing this analysis over the mainnet, where all of the data is subject to consensus, it can be a reliable method of finding malicious patterns. Some of the pros and cons in comparison with the method using a mempool are listed below:

Pros:

- It is possible to find patterns among the past transactions, while in the case of using a mempool, we need to have access to the mempool at the time of mining from a trusted party.
- The experiment is repeatable by others, where the data is accepted by the network. This can help us define a set of heuristics for censorship and PGA instances.
- There is no need to aggregate several mempools and maintain them throughout the project.
- Using only on-chain data is much faster since the mempool analysis is capped by the live monitoring of the mempool.
- Enables us to find patterns among the transactions that were sent to miners via a private channel but landed on-chain and failed.

Cons:

- Can flag the transactions that were sent late as a censorship instance and produce a false positive.
- Does not identify patterns in the private mempools that guarantee "next block or never" inclusion.
- We do not count failed backrunnings as rational transactions, however, we argue that the same method can be used to find backrunning by replaying transactions.
- We decide not to analyze successful transactions, we imagine that many of the opportunity-capturing transactions consist of checked MEV transactions that decide to fail if the opportunity is already captured. The extension of this research would be to analyze rationality via the profitability of transactions.

We have implemented a proof-of-concept where we could extract data from almost 150,000 blocks in 2022. The mentioned proof-of-concept is developed with the help of hardhat and is available here: [https://github.com/Allarious/MEVoila](https://github.com/Allarious/MEVoila)

As a part of our data we found the frequency of suspicious instances of censorship during the course of our analysis:

- Number of blocks analyzed: 148,132
- Number of transactions analyzed: 26,809,622
- Number of failed transactions: 1,050,812
- Fraction of all transactions inside flashbots blocks: 60.61%

| P | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Flashbots Blocks | 80064 | 27536 | 8991 |
| Rest of the Network | 66500 | 52700 | 17760 |

Where P is the number of blocks since the first successful run of a failed transaction at the start of a block. As an example, if a failed transaction is included in block height 100, and we could replay it successfully at index 0 of block 98, we consider block 98 censored the said transaction with P=0 and block 99 censored the transaction with P=1 and the transaction landed in block 100. The numbers are the frequency of the **suspicious censorship instances** identified considering the P of each instance. Interestingly, we see that the censorship instances from the public mempool for flashbots is higher for P = 0, and drops much lower for P > 0. Here, we can clearly see that a user sending a transaction late can be flagged as censorship, therefore, as P goes higher for a censorship instance, we can say with higher certainty that the instance was truly a case of censorship.

## Problem Statement

We need to find the answer to several questions to further continue this research:

- What is the frequency of censorships and PGAs happening on-chain?
- Is there metadata that we can leverage to enhance our method?
- How much can we optimize the code and the data output?
- What other data can we extract from the failed transactions?
- How can this method be used alongside the mempool timestamps to find malicious patterns more effectively?

## Plan and Deliverables

- We already have implemented a proof-of-concept that shows promising data, but it can be optimized to run much faster. This can help us to analyze many more blocks.
- We are planning to write an academic paper discussing our method and evaluating our data.
- We are planning to provide public endpoints where it shows if a failed transaction was censored, or the reason for a specific transaction failure (Can be used to see transaction front-runnings).
- (Bonus) It might be possible to define heuristics and analyze transactions based on their profitability and rationality instead of only looking at their status on-chain.

## References

###### 1. Justin Drake, [Censorship Résistance and PBS](https://www.youtube.com/watch?v=XZJcZ05d-Wo&feature=youtu.be), September 2022

###### 2. Alex Obadia, [Quantifying MEV: Introducing MEV-Explore v0](https://medium.com/flashbots/quantifying-mev-introducing-mev-explore-v0-5ccbee0f6d02), February 2022

###### 3. Weizhao Tang, Lucianna Kiffer, Giulia Fanti, and Ari Juels, [Strategic Latency Reduction in Blockchain Peer-to-Peer Networks](https://arxiv.org/pdf/2205.06837.pdf), 2022

###### 4. Kaihua Qin, Liyi Zhou, and Arthur Gervais, [Quantifying blockchain extractable value: How dark is the forest?](https://arxiv.org/abs/2101.05511), 2021

###### 5. P. Daian, S. Goldfeder, T. Kell, Y. Li, X. Zhao, I. Bentov, L. Breidenbach, and A. Juels, [Flash boys 2.0: Frontrunning in decentralized exchanges, miner extractable value, and consensus instability](https://arxiv.org/abs/1904.05234), 2020

###### 6. Dan Robinson, [Ethereum is a dark forest](https://www.paradigm.xyz/2020/08/ethereum-is-a-dark-forest), Aug 2020.
