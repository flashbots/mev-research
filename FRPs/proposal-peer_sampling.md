---
id: <leave blank -- will be assigned by reviewers>
title: @lthibault, @aratz-lasa
team: <team that will carry out the proposal, with a designated lead>
created: 2023-08-01
---

# Gossip-Based Peer Sampling for Censorship-Resistant Bootstrapping

**Research Track:**  Flashbots as critical infrastructure

**Key Words:**  critical infrastructure, bootstrapping, peer-discovery, censorship-resistance, robustness, gossip-based protocol


<!-- Use this initial section to provide a ~500 word summary of the proposal. The summary should consist in a simple straightforward statement of what your hypothesis is, what methodology you intend to use, what limitations those methods may have, what implications your results may have. -->

## Background and Problem Statement

>The Achilles heel of the Node Discovery Protocol is the process of joining the network: while any other node may be used as an entry point, such a node must first be located through some other mechanism.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;— [The Discv5 Protocol Specification](https://github.com/ethereum/devp2p/blob/master/discv5/discv5.md#comparison-with-other-discovery-mechanisms)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bootstrapping is a weak point for peer-to-peer (P2P) networks.  Upon starting, each participating process must contact an existing member of the swarm, and this so-called "bootstrap peer" must be discovered out-of-band.  Crucially, it is extremely difficult to avoid centralization at this level, since it is impractical to distribute the full set of active peers.  Instead, nodes wishing to join the swarm will either refer to a static list of bootstrap peers, or query a federated discovery system.  In both cases, the set of nodes/servers is small when compared to the swarm, often by several orders of magnitude.

<!-- Problem: bootstrapping is a weak-point for p2p networks
  - Large networks may place heavy loads on bootstrap peers => expensive to operate
  - Bootstrap nodes can be DoSed or blacklisted
    - Partial attacks are often sufficient.  Requests become concentrated on subset of bootstrap nodes => thundering herd.
  - Disseminating new bootstrap nodes can be a challenge (esp. under adverse conditions) -->

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;One immediate problem is that a moderately-sized P2P network places a significant load on its bootstrap infrastructure.  But perhaps less obviously, this burden compounds with scale.  Indeed, the incentive to attack a P2P network increases with its popularity, so as the network increases in size, so too does its tendency to rely on an ever-shrinking set of trusted bootstrap nodes.  This point bears emphasizing:  a malicious bootstrap node can pair its target with a specially chosen set of peers that segments it away from the main network, and is thus an appealing vector for common denial-of-service (DoS), eclipse and sybil attacks.  Rational node operators should therefore prefer official services over their community-operated counterparts.   In the case of Ethereum, this amounts to a preference for bootstrap nodes operated by the Ethereum Foundation.  Thus, large networks have a tendency not only to centralize their bootstrapping infrastructure, but also to increase their operating costs.  These costs, combined with the reputational demands, conspire to raise the barrier-to-entry beyond what is achievable for most parties.  Adding to the problem, a small set of bootstrap nodes is subject to "thundering herds".  If, say, the Ethereum Foundation's bootstrap nodes were to be targeted by a DoS attack or somehow suspected of being compromised, the sudden ensuing roll-over to other bootstrap providers is likely to overload their servers.  It is worth pausing to consider both the cascading impact of attacks on bootstrap infrastructure, and the ease with which they can be performed; some are as simple as starting a rumor.

<!-- Argument:  everything gets easier when we scale down the requests to discovery services -->

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By now it should be evident that hardening against bootstrap attacks is largely a matter of reducing the number of requests that must be processed by centralized services.  Ideally, each Ethereum node—be it in the execution-layer (EL) or in the consensus-layer (CL)—would interact with a [discv5](https://github.com/ethereum/devp2p/blob/master/discv5/discv5.md) discovery service once in its entire lifetime:  on first boot.  In this ideal scenario, nodes periodically construct a bounded-size list of random peers by querying a local peer-sampling service, and persist it to a local cache.  Upon subsequent boots, the node can employ the cached peers to re-join the network, falling back on discv5 only if this fails.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;At first glance, the obvious primitive on which to build the peer-sampling service would be the Kademlia DHT, since this is at the heart of Discv5.  However, randomized DHT walks suffer from several drawbacks that make them less than ideal.  Firstly, they can be quite slow due to their use of recursive RPC calls, and while this latency is not necessarily problematic in the context of a one-off bootstrapping operation, it becomes costly when nodes must continually refresh their caches.  Moreover, recursive walks are inherently fragile, since a failure in any segment of the path will invalidate the walk.  Separately, DHTs are quite delicate, and even minor differences in implementation [can make it hard for nodes to join the network, and even lead to network fragmentation](https://github.com/ethereum/devp2p/blob/master/discv5/discv5-rationale.md#115-guard-against-kademlia-implementation-flaws).  Fragmentation is especially tricky for the Kademlia protocol for two reasons, the first of which is straightforward:  partitions quickly become permanent as `PING` RPCs fail and peers are subsequently evicted from the routing table.  The second issue is that Kademlia is very slow to merge large partitions.  Intuitively, this is because Kademlia works by skipping over large parts of the key-space, so in a situation where there are two mostly-disjoint networks, it follows that a given query is unlikely to pass through a node that is present in both.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;With these limitations in mind, our main research question is the following:  can we find a sampling algorithm that is better suited to the task of constructing and updating a cache of bootstrap peers than Kademlia?  In particular, such an algorithm should be (1) more efficient than a recursive walk, (2) robust against common attack vectors, and (3) immune to degradation and degeneration in the presence of partitions.  Moreover, the algorithm should be suitable for use in both the execution-layer and consensus-layer networks.

<!-- Provide motivation and background for the proposal, and clearly state the research questions it aims to tackle. Link to related or dependent Research Question(s) on the Flashbots Research Roadmap, and reference relevant Github Issues in this repository. -->

## Plan and Deliverables
<!-- Describe the planned approach to the problem, including potential time allocations and partitioning into phases. List the artifacts or intended deliverables of the proposal. -->

### Protocol Specification

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will build on the work of [3] to propose a gossip-based peer-sampling protocol suitable for use as a peer cache.  As detailed in the previous section, gossip is inherently more efficient and robust than recursive walks, making it suitable for continuous operation in the background.  We aim to design a protocol that extends [3] in two important ways:

1. **Partition Tolerance**.  The algorithm described by [3] aggressively pursues the eviction from cache of "stale" entries that point to defunct peers.  Under temporary network splits, however, nodes will quickly evict peers located in a different partition, which has the effect of making the partition permanent.  We pursue a strategy that retains a configurable proportion of suspected-defunct peers while also preserving key properties of the original algorithm.
2. **Prevention of Amplification Attacks**.  [3] assumes a non-byzantine environment with fail-stop errors only.  In its naive form, the algorithm allows attackers to disseminate arbitrary records in such a way as to cause a targeted peer to suffer a disproportionate burden of bootstrap requests.  We pursue a self-certifying scheme for peer records comparable to [4] that prevents attackers from forging arbitrary records, and a replacement for integer-based counters based on nested signatures that prevents attackers from manipulating the age of records.

### Analysis of Protocol

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will conduct a rigorous analysis of the protocol using analytical methods and simulations.  We will demonstrate that key properties of [3] are preserved and that properties of the novel protocol emerge in a reasonable amount of time using a reasonable amount of resources.  In particular, we will examine the undirected graph formed by the set of all peer-caches in a cluster and show

1. that the clustering coefficient decays quickly, indicating rapid convergence on a uniform distribution of peers across caches,
2. that the average path length quickly converges on a small value, indicating a well-connected graph,
3. that the average node degree quickly converges on the upper bound of the cache size, indicating that the cache fills quickly and that entries point to unique peers,
4. that stale entries are evicted in better-than-linear time; and,
5. that the desired proportion of suspected-stale entries is preserved.

### Implementation

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will provide a working implementation of the gossip-based peer-sampling protocol built on libp2p.  This implementation can be integrated into consensus-layer nodes with minimal effort.

## References
<!-- Reference current relevant literature or past work pertaining to the research question(s) at stake. -->

1. [Ethereum Discovery](https://ethereum.org/en/developers/docs/networking-layer/#discovery)
2. [Discv5 Protocol](https://github.com/ethereum/devp2p/blob/master/discv5/discv5.md)
3. Márk Jelasity, Spyros Voulgaris, Rachid Guerraoui, Anne-Marie Kermarrec, and Maarten Van Steen. [Gossip-based peer sampling.](https://inf.u-szeged.hu/~jelasity/cikkek/tocs05.pdf) ACM Transactions on Computer Systems (TOCS), 25(3):8–es, 2007.
4. David Mazières and M. Frans Kaashoek. 1998. [Escaping the evils of centralized control with self-certifying pathnames.](https://dl.acm.org/doi/abs/10.1145/319195.319213) In Proceedings of the 8th ACM SIGOPS European workshop on Support for composing distributed applications (EW 8). Association for Computing Machinery, New York, NY, USA, 118–125. https://doi.org/10.1145/319195.319213
