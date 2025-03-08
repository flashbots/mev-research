---
id: <leave blank -- will be assigned by reviewers>
title: Arbitrage Detection in Prediction Markets
team: Oriol Saguillo, Vahid Ghafouri, Lucianna Kiffer, and Guillermo Suarez-Tangil (IMDEA Networks Institute)
created: <date created on, in yyyy-mm-dd format>
---

# Markets Arbitrage in Prediction Market

## Background and Problem Statement
Prediction markets [1] have gained significant traction over the past year, largely driven by interest in the United States elections. This surge in attention has led to the emergence of new prediction market protocols across various blockchain networks, with Polygon and Polymarket [2] being among the most prominent.

Due to the decentralized nature of market creation, sophisticated traders have begun viewing prediction markets as opportunities for arbitrage, under the assumption that these markets operate independently. However, in reality, they are often interrelated. For example, a market predicting whether Kamala Harris or Donald Trump will win the U.S. presidential election is inherently correlated with a market forecasting whether the Democratic or Republican party will secure victory.

The absence of automated tools for detecting correlations between markets can prevent users from making informed bets, potentially exposing them to arbitrage and unfavorable positions. Addressing this issue becomes increasingly urgent as more liquidity flows into prediction markets--one of the key challenges highlighted in [3]. 

These markets present a unique challenge in arbitrage detection as events are described in plain text and their correlation requires real-world knowledge. The latest advancements in NLP techniques [4], particularly in Transformer-based encoder (e.g. BERT) and generative (e.g. LLMs) models [5], present a promising opportunity for developing automated and granular analyses of semantic relationships [6]. We propose to use such techniques to automate arbitrage opportunity detection across markets, and analyze if and how these opportunities have been exploited. 

## Plan and Deliverables

The steps of the study will be following:

- Generate a dataset containing open and finished markets, initially using Polymarket as a use case. We note the proposed approach is generic for any prediction market platform.
- Utilize state-of-the-art text encoding models (e.g. all-mpnet-base-v2 [7]) as the input of clustering techniques (such as HDBSCAN [8] or dendrogram-based methods [9]) and semantic search techniques to group potentially related markets (e.g., those related to the U.S. presidential election).
- Apply LLMs, empowered by RAG [10], to the grouped/clustered markets for granularly identifying and describing potential tautologies between the markets within a cluster.
- Verify arbitrage detection methodology with simulated values for existing markets.
- Analyze markets where arbitrage was exploited using historical order book prices, quantifying the potential profits and key players.

The results of the study will be presented in an academic paper and short blog post summarizing the key findings. Our code and data will be made public. Depending on the research findings, we will attempt to contact Polymarket to propose adding this tool to their related markets tab to help inform users of potential arbitrage risks.

## References
[1] https://www.aeaweb.org/articles?id=10.1257/0895330041371321

[2] https://polymarket.com/

[3] https://jeremywhittaker.com/index.php/2024/08/30/exploiting-arbitrage-betting-against-nate-silver-for-a-54-yield/

[4] https://arxiv.org/abs/1706.03762

[5] https://arxiv.org/abs/2005.14165

[6] https://aclanthology.org/2024.emnlp-main.1171/

[7] https://www.sbert.net/docs/sentence_transformer/pretrained_models.html

[8] https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html

[9] https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html

[10] https://arxiv.org/abs/2005.11401