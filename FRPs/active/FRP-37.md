---
id: 37
title: Efficacy of Commitment Devices (CDs) in Multi-Agent Games Involving Large Language Model (LLM) Agents
team: Feng Yan, Jason Hu, Will Jiang
created: 2023-9-03
status: active
---

# Efficacy of Commitment Devices (CDs) in Multi-Agent Games Involving Large Language Model (LLM) Agents

## Motivation and Problem Statement
TLDR: Commitment Device might be the most important opportunity for blockchain adoption in an AI-dominant world.

General-purpose AI models like large language models has created AI agents: intelligent entities that can interact with the real world and make more independent decisions. In a world of increasing AI adoption, it’s inevitable that we will soon see AI agents interact with each other on behalf of their owner in all kinds of scenarios with real-life stakes. Thus, it is important to design mechanisms to achieve efficient negotiation & maximize social welfare that come from these interactions.

Commitment Devices are proved to work in improving outcomes in multi-agent games, and they are widely used in real life, for humans (e.g. laws, regulations, etc). There are also concrete evidence that commitment devices can improve final outcome in multi-agent systems based on reinforced learning (RL). However, there is yet any work to explore how can CD be used to improve the interaction between multiple LLM agents, which will like achieve mass adoption due to its wide applicability and relative ease of implementation (no need to re-train RL model).

Commitment Device should also be naturally based on the blockchain. Tokens align incentives on uncertain, contingent payoffs. Smart contracts can make the issuance of CD trustless, and the permissionlessness and transparency reduce information asymmetry among different agents. [Liao 2023]

## Plan and deliverables
1. Literature review on commitment devices, existing RL research on repetitive games, and prompting techniques.
   
2. Design and conduct experiments to quantitatively assess the performance of LLM agents with and without commitment devices. \
  This research will concentrate on the following game types (categorized by complexity):
      * Classic static and simultaneous-move games: Prisoner’s Dilemma (PD), Public Goods
      * Dynamic and sequential games: Harvest, Cleanup
      * Asymmetric information games: Simple Bargaining
      * Putting one of the above games on-chain to test on LLM agent's ability in comprehending and creating smart contracts (in solidity).
   
3. Characterize the efficacy of prompt-injection attacks and ways of mitigation when other agents are not controlled by LLM but are strategic agents capable of adversarial/exploitative behavior.
   
4. Optional: implement a commitment device framework on SUAVE
   
The ultimate deliverables will be a research paper elucidating the findings and a concise blog post providing explanatory insights.

The outcomes stemming from this study possess the potential to exert substantial influence on SUAVE's mechanism design and the formulation of intents.
    

## References
1. Get It in Writing: Formal Contracts Mitigate Social Dilemmas in Multi-Agent RL https://arxiv.org/pdf/2208.10469.pdf
2. GPT Bargaining https://github.com/FranxYao/GPT-Bargaining
3. Playing repeated games with Large Language Models https://arxiv.org/pdf/2305.16867.pdf
4. Training Socially Aligned Language Models in Simulated Human Society https://arxiv.org/abs/2305.16960
5. CredibleCommitments.WTF https://hackmd.io/@sxysun/ccdwtf
6. Voyager: An Open-Ended Embodied Agent with Large Language Models https://voyager.minedojo.org/
7. Future of Decentralization, AI, and Computing Summit https://youtu.be/J5OmmgAdNg8?t=25867
8. Training Socially Aligned Language Models in Simulated Human Society https://arxiv.org/abs/2305.16960
9. Playing repeated games with Large Language Models  https://arxiv.org/abs/2305.16867
10. Universal and Transferable Adversarial Attacks on Aligned Language Models https://arxiv.org/pdf/2307.15043.pdf
11. Large Language Models as Optimizers https://github.com/Moocember/Optimization-by-PROmpting
