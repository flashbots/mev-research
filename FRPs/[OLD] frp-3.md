# FRP-3: On-chain vs Off-chain

**Fellow:** 
</br> **Contributors:** 
</br> **Status:** 
</br> **Type:** 
</br> **Updated:** *18.09.2020*

**Summary:** 
</br> A survey of the logic bots are doing on-chain that doesn't have to do with direct execution. Such logic (eg. bot checks) doesn't necessarily need to exist on-chain.

**Motivation:**
</br> The findings of this FRP will inform the design of the transaction bundle of our sealed-bid auction mechanism for MEV extraction in terms of ordering and what can be brought off-chain. 
Additionally, by potentially bringing more bot logic off-chain we hope to alleviate network congestion and lower the amount of wasted blockspace.

**Proposed deliverable:**
</br> 
* Survey of the logic bots are doing on-chain that includes how much of it can be moved off-chain
* Enumerate order types
* Formalize trade-off between on-chain / off-chain arb computation
  * Is there any computation we should move off-chain (into bundle processing/switching)?	

**Proposed Approach:**
</br> 

**Resources:**

