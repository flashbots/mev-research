---
id: 38
title: Approximating Optimal MEV extraction on Ethereum using Reinforcement Learning
team: mevrbevr
created: 2021-02-28
paper: <paper the proposal is related to (1, 2, ...)>
---

# Approximating Optimal MEV extraction on Ethereum using Reinforcement Learning

Here is a formal definition of what we mean by Optimal MEV: https://hackmd.io/EEbisqgATlW4eLKOIcsEYg?view (using HackMD becasue it renders LaTeX).

In english: the optimal block producer is such that it will exract more than or equal MEV than any other block producer, for any possible chain state and mempool combination.

I want to see what happens when you try to use reinforcement learning to approximate such a block producer. Here is a rough idea:
- State space is S x B x M, where S it the current Ethereum state, B is a list of transaction currently proposed for the block, M is the txs remaning in mempool
- Action space is M | P, where M is the remaing mempool txs and P is personal txs (miner originated txs), that are valid in current state
- The simulation step applies the tx output by the agent to the Ethereum state, appends it to B, and removes it from M if it originates there. If block has reached the block gas limit, the "round" ends.
- The reward is computed as the difference in total value of all the assets owned by the miner (could do it on tx level, or block level - as a delayed reward, probably want to try both and see).

If S is represented as a giant HashMap<uint256, HashMap<uint256, uint256>> and each transaction as a real Eth transaction with destination and payload given as bytes, and the simulation runs the actual EVM, I don't think the agent can learn anything useful (yet...). 

Thus it is important that we simplify the state/action space by modeling the appropriate subset of Ethereum state that is most relevant to MEV extraction. This mostly involves the largest DeFi protocols. On the last MEV roast, there was a presentation called: Extractable Value: Clockwork Finance - A Mechanized Framework for Economic Security in Smart Contracts. In that talk there was mention of modeling the DeFi ecosystem in the K-framework. It would be interesting to look into reusing that ecosystem model as the simulation environment for the RL agent.

## Plan and Deliverables

We want to start small and see where we can get:
- First only model a single Uniswap pair, and see if we can learn "the sandwich".
- I want to build machines in my image, so next we could negate the reward function and see if we can learn the reverse sandwich: the buy high, sell low bot.
- Next we could add multiple Uni pairs and see if we can learn arbing between them
- Add another AMM and see if we can arb between them
- In this fashion we can continue adding DeFi protocols to our environment and see what the agent can learn
- It would be really cool if we could replicate the neccessary conditions for one of the DeFi exploits in our model, and try to learn that...

## References
Reference current relevant literature or past work pertaining to the research question(s) at stake.
