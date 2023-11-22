---
id: 37
title: Automated Mechanism Design Using Generative AI in CFMM 
team: Gil Litvin (Technion), Nadav Rubinstein (Technion), Shlomi Gibly (BGU) Xinyuan Sun (Flashbots)
created: 2023-08-27
status: active
---

# Automated Mechanism Design Using Generative AI in CFMM 

## Intro

Could AI be used to propose contracts on user behalf to implement better coordination? In this proposal, we address the challenge of cooperative behaviors in selfish agents in multi-agent reinforcement learning (MARL) by proposing the use of contracting. We present a novel approach to see if agents can successfully coordinate on trading assets in a better way. Our objective is to utilize Artificial Intelligence (AI) techniques to find more efficient and optimized trading routes by enabling users to contract each other to mitigate potential losses incurred when choosing suboptimal routes.

## Background and Problem Statement

The DeFi space has witnessed the proliferation of automated market-making protocols, including CFMMs like Uniswap. While these protocols have democratized trading, they suffer from limitations that often lead to suboptimal outcomes for users. One such limitation is the lack of direct user coordination within these platforms, resulting in less effective and efficient trading activities.

In the context of CFMM trading, users often encounter scenarios where they must pay fees to market makers. Sandwich attacks have been analyzed for specific types of automated market makers. They involve strategically placing trades to exploit price movements and maximize profits at the expense of the user's trade execution price. The revenue derived from these trades directly affects their financial gains. Additionally, price slippage is a common occurrence due to transaction mechanics. Excessive slippage can lead to suboptimal trading outcomes, false price fluctuations, and inflated trading volumes.

## Plan and Deliverables - Framing the problem with AI

To address these challenges, we propose reframing the problem as an AI-enhanced asset coordination challenge within CFMM trading. We envision AI to empower users to contract each other to minimize losses associated with less favourable trading routes. We align with the spirit of Multi-Agent Reinforcement Learning (MARL), where users are modelled as reinforcement learning agents in an environment that tests if asset coordination leads to better routing of transactions for traders.

Each agent's objective is to maximize the output tokens they receive for their input tokens. Agents interact with a CFMM smart contract, and AI techniques are applied to facilitate the creation of contracts that enhance coordination, potentially leading to better trading routes and improved trading outcomes.

## Training of Multi-Agent Reinforcement Learning (MARL) Agents

To investigate the efficacy of AI in enhancing asset coordination within Constant Function Market Maker (CFMM) trading, we will employ Multi-Agent Reinforcement Learning (MARL) techniques. This section outlines the training setup and experimentation options we plan to explore, each of which will be tested across a range of scenarios.

### Training Options

1. Different Initial Token Holdings vs. Same Initial Token Holdings:
- In this setup, we will explore two variations:
-- Agents start with different initial token holdings.
-- Agents start with the same initial token holdings.
- These variations aim to assess the impact of agents' initial conditions on their ability to coordinate effectively.

2. Randomly Chosen Contract Suggestion vs. All Agents Suggest Contracts:
- We will test two scenarios:
-- In each round, one agent will be randomly chosen to suggest a contract.
-- In each round, all agents will suggest contracts.
- This experimentation will help us understand how contract suggestion dynamics affect coordination.

3. Limit on the Number of Participants in a Contract:
- To manage computational complexity, we will set a limit of three participants per contract.
- This constraint allows us to explore coordination patterns without overwhelming computational demands.

### Agent Objectives

Agents in the MARL framework will aim to maximize the number of tokens while considering different priorities for token types. Specifically:

- Agents will have randomly assigned priorities, with some prioritizing the first token and others the second token more.
- These priorities will reflect agents' individual economic strategies and will be drawn randomly.

### Expected Outcomes
Through this training setup, we anticipate observing intriguing patterns of asset coordination and agent behaviour, including:
- The emergence of coordination among agents with similar priorities.
- The formation of groups or clusters of agents with aligned economic strategies.
- Variations in coordination strategies based on the initial token holdings of agents.
- Insights into whether agents with similar economics tend to coordinate more effectively.

### Data Collection and Analysis
During training, we will collect data on agent actions, rewards, and coordination patterns. We will analyse this data to gain insights into the effectiveness of AI-driven contract proposals in optimizing trading outcomes.
In summary, our training setup for MARL agents will allow us to explore various scenarios and dynamics related to asset coordination. By systematically examining these options and their combinations, we aim to uncover valuable insights into how AI can enhance coordination among users in decentralized finance environments.
