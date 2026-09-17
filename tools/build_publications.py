#!/usr/bin/env python3
"""
Regenerates the publications index from the canonical list below.

Run:  python3 tools/build_publications.py

Writes:
  docs/publications.json   data consumed by the site
  docs/publications.csv    same data, for spreadsheets
  publications.md          markdown table rendered on github.com

To add a publication: add a row to ROWS and re-run.
Fields: category, title, date (YYYY-MM-DD), authors, url
"""
import csv, json, datetime, pathlib

AP = "Academic Papers"
FW = "Flashbots Writings"
FC = "Flashbots Collective Forum Posts"
ER = "ethresear.ch Post"
EX = "Excalidraw"

ROWS = [
    (AP, "The Price of Decentralization in Block Building", "2026-06-01",
     "Burak Öz (Flashbots), Fei Wu (Flashbots), Luis Correia (Flashbots), Sen Yang, Bruno Mazorra (Flashbots), Stefanos Leonardos",
     "https://arxiv.org/abs/2606.01874"),
    (AP, "Timing Games: Probabilistic Backrunning and Spam", "2026-02-25",
     "Bruno Mazorra (Flashbots), Christoph Schlegel (Flashbots), Akaki Mamageishvili",
     "https://arxiv.org/abs/2602.22032"),
    (AP, "Geographical Centralization Resilience in Ethereum’s Block-Building Paradigms", "2025-09-25",
     "Sen Yang (Flashbots), Burak Öz (Flashbots), Fei Wu (Flashbots), Fan Zhang",
     "https://arxiv.org/abs/2509.21475"),
    (AP, "The CoinAlg Bind: Profitability-Fairness Tradeoffs in Collective Investment Algorithms", "2026-01-02",
     "Andrés Fábrega, James Austgen, Samuel Breckenridge, Jay Yu, Amy Zhao, Sarah Allen (Flashbots), Aditya Saraf, Ari Juels",
     "https://arxiv.org/abs/2601.00523"),
    (AP, "Attestation of Host Networking Stack for TEEs", "2025-10-14",
     "Filip Rezabek, Moe Mahhouk",
     "https://arxiv.org/abs/2510.12469"),
    (AP, "Cross-Chain Sealed-Bid Auctions Using Confidential Compute Blockchains", "2025-10-22",
     "Jonas Gebele, Timm Mutzel, Burak Öz (Flashbots), Florian Matthes",
     "https://arxiv.org/abs/2510.19491"),
    (AP, "Conditional Recall", "2025-10-24",
     "Christoph Schlegel, Xinyuan Sun",
     "https://arxiv.org/abs/2510.21904"),
    (AP, "TimeBoost: Do Ahead-of-Time Auctions Work?", "2025-11-23",
     "Akaki Mamageishvili, Christoph Schlegel (Flashbots), Ko Sunghun, Jinsuk Park, Ali Taslimi",
     "https://arxiv.org/abs/2511.18328"),
    (AP, "The Free Option Problem of ePBS", "2025-09-29",
     "Bruno Mazorra, Burak Öz, Christoph Schlegel, Fei Wu",
     "https://arxiv.org/abs/2509.24849"),
    (AP, "Arbitrage with Bounded Liquidity", "2025-07-02",
     "Christoph Schlegel, Quintus Kilbourn",
     "https://arxiv.org/abs/2507.02027"),
    (AP, "Encrypted Backruns", "2025-04-14",
     "Jonathan Passerat-Palmbach",
     "https://fc25.ifca.ai/preproceedings/238.pdf"),
    (AP, "NDAI Agreements", "2025-02-11",
     "Matthew Stephenson, Andrew Miller (Flashbots), Xyn Sun (Flashbots), Bhargav Annem, Rohan Parikh",
     "https://arxiv.org/abs/2502.07924"),
    (AP, "Cross-Chain Arbitrage: The Next Frontier of MEV in Decentralized Finance", "2025-01-28",
     "Burak Öz (Flashbots), Christof Ferreira Torres, Christoph Schlegel (Flashbots), Bruno Mazorra (Flashbots), Jonas Gebele, Filip Rezabek (Flashbots), Florian Matthes",
     "https://arxiv.org/abs/2501.17335"),
    (AP, "Liquefaction: Privately Liquefying Blockchain Assets", "2024-12-03",
     "James Austgen, Andrés Fábrega, Mahimna Kelkar, Dani Vilardell, Sarah Allen (Flashbots), Kushal Babel, Jay Yu, Ari Juels",
     "https://arxiv.org/abs/2412.02634"),
    (AP, "Who Wins Ethereum Block Building Auctions and Why?", "2024-07-18",
     "Burak Öz (Flashbots), Danning Sui (Flashbots), Thomas Thiery, Florian Matthes",
     "https://arxiv.org/abs/2407.13931"),
    (AP, "On Sybil-proof Mechanisms", "2024-07-19",
     "Minghao Pan (Flashbots), Bruno Mazorra (Flashbots), Christoph Schlegel (Flashbots), Akaki Mamageishvili",
     "https://arxiv.org/abs/2407.14485"),
    (AP, "Searcher Competition in Block Building", "2024-07-10",
     "Akaki Mamageishvili, Christoph Schlegel (Flashbots), Benny Sudakov, Danning Sui (Flashbots)",
     "https://arxiv.org/abs/2407.07474"),
    (AP, "Maximal Extractable Value in Batch Auctions", "2025-07-02",
     "Mengqian Zhang, Yuhao Li, Xinyuan Sun (Flashbots), Elynn Chen, Xi Chen",
     "https://dl.acm.org/doi/10.1145/3736252.3742581"),
    (AP, "Playing the MEV Game on a First-Come-First-Served Blockchain", "2024-01-15",
     "Burak Öz (Flashbots), Jonas Gebele, Parshant Singh, Filip Rezabek (Flashbots), Florian Matthes",
     "https://arxiv.org/abs/2401.07992"),
    (AP, "DAO Decentralization: Voting-Bloc Entropy, Bribery, and Dark DAOs", "2023-11-06",
     "James Austgen, Andrés Fábrega, Sarah Allen (Flashbots), Kushal Babel, Mahimna Kelkar, Ari Juels",
     "https://arxiv.org/abs/2311.03530"),
    (AP, "A Study of MEV Extraction Techniques on a First-Come-First-Served Blockchain", "2023-08-12",
     "Burak Öz (Flashbots), Jonas Gebele, Parshant Singh, Filip Rezabek (Flashbots), Florian Matthes",
     "https://arxiv.org/abs/2308.06513"),
    (AP, "Time Moves Faster When There is Nothing You Anticipate: The Role of Time in MEV Rewards", "2023-07-11",
     "Burak Öz (Flashbots), Benjamin Kraner, Nicolò Vallarano, Bingle Stegmann Kruger, Florian Matthes, Claudio Juan Tessone",
     "https://arxiv.org/abs/2307.05814"),
    (AP, "Silent Threshold Encryption with One-Shot Adaptive Security", "2025-07-29",
     "Mathias Hall-Andersen, Mark Simkin (Flashbots), Benedikt Wagner",
     "https://ia.cr/2025/1384"),
    (AP, "Robust Distributed Arrays: Provably Secure Networking for Data Availability Sampling", "2025-04-18",
     "Dankrad Feist, Gottfried Herold, Mark Simkin (Flashbots), Benedikt Wagner",
     "https://arxiv.org/abs/2504.13757"),
    (AP, "Time/Space Tradeoffs for Generic Attacks on Delay Functions", "2025-12-05",
     "Kasper Green Larsen, Mark Simkin (Flashbots)",
     "https://link.springer.com/chapter/10.1007/978-3-032-12290-2_15"),
    (AP, "OCash: Fully Anonymous Payments between Blockchain Light Clients", "2024-02-15",
     "Adam Blatchley Hansen, Jesper Buus Nielsen, Mark Simkin (Flashbots)",
     "https://ia.cr/2024/246"),
    (AP, "Cooperative AI via Decentralized Commitment Devices", "2023-11-14",
     "Xinyuan Sun (Flashbots), Davide Crapis, Matt Stephenson, Barnabé Monnot, Thomas Thiery, Jonathan Passerat-Palmbach (Flashbots)",
     "https://arxiv.org/abs/2311.07815"),
    (AP, "Narrowing the Gap between TEEs Threat Model and Deployment Strategies", "2025-06-17",
     "Filip Rezabek, Jonathan Passerat-Palmbach",
     "https://arxiv.org/abs/2506.14964"),
    (AP, "Differentially Private Aggregate Hints in MEV-Share", "2025-08-19",
     "Jonathan Passerat-Palmbach, Sarisht Wadhwa",
     "https://arxiv.org/abs/2508.14284"),
    (AP, "Just-in-Time Resale in an Ahead-of-Time Auction for Faster Execution", "2026-03-20",
     "Burak Öz (Flashbots), Christoph Schlegel (Flashbots), Akaki Mamageishvili, Ali Taslimi",
     "https://arxiv.org/abs/2603.20175"),
    (AP, "To Wait or To Probe: Arbitrage Competition on High-Throughput Blockchains", "2026-05-30",
     "Fei Wu, Burak Öz",
     "https://arxiv.org/abs/2606.00720"),
    (FW, "Why Location Choice Matters", "2026-08-09",
     "Burak Öz (Flashbots), Fei Wu (Flashbots), Luis Correia (Flashbots), Sen Yang, Bruno Mazorra (Flashbots), Stefanos Leonardos",
     "https://writings.flashbots.net/why-location-choice-matters"),
    (FW, "Network Anonymized Mempools", "2026-02-17",
     "",
     "https://writings.flashbots.net/network-anonymized-mempools"),
    (FW, "Scalable Oblivious Accesses to Blockchain Data", "2025-06-02",
     "Afonso Tinoco (Flashbots), Tianyao Gu, Elaine Shi, Andrew Miller (Flashbots)",
     "https://writings.flashbots.net/scalable-oblivious-accesses-to-blockchain-data"),
    (FW, "ZTEE - Trustless Supply Chains", "2024-11-08",
     "Quintus Kilbourn (Flashbots), Sylvain Bellemare, Bunnie, Michael Gao",
     "https://writings.flashbots.net/ZTEE2-Supply-Chains"),
    (FW, "Zero Trust Execution Environments", "2024-10-11",
     "Quintus Kilbourn (Flashbots), Sylvain Bellemare, Jonathan Passerat-Palmbach, Andrew Miller (Flashbots)",
     "https://writings.flashbots.net/ZTEE"),


    (FC, "Prisoners of Geography 2.0: How Protocol Shapes Where Validators Run", "2025-10-06",
     "Sen Yang (Flashbots), Burak Öz (Flashbots), Fei Wu (Flashbots), Fan Zhang",
     "https://collective.flashbots.net/t/prisoners-of-geography-2-0-how-protocol-shapes-where-validators-run/5308"),
    (FC, "To Wait or To Probe: Arbitrage Competition on High-Throughput Blockchains", "2026-06-08",
     "Fei Wu, Burak Öz",
     "https://collective.flashbots.net/t/to-wait-or-to-probe-arbitrage-competition-on-high-throughput-blockchains/5759"),
    (FC, "When Ahead-of-Time Allocation Fails: The Transition to Kairos", "2026-03-31",
     "Burak Öz (Flashbots), Christoph Schlegel (Flashbots), Akaki Mamageishvili",
     "https://collective.flashbots.net/t/when-ahead-of-time-allocation-fails-the-transition-to-kairos/5640"),
    (FC, "Timing Games: Probabilistic backrunning and spam", "2026-03-13",
     "Bruno Mazorra (Flashbots), Christoph Schlegel (Flashbots), Akaki Mamageishvili",
     "https://collective.flashbots.net/t/timing-games-probabilistic-backrunning-and-spam/5614"),
    (FC, "How the MEV Supply Chain Reacts to Circuit Breakers", "2025-12-16",
     "Data Always",
     "https://collective.flashbots.net/t/how-the-mev-supply-chain-reacts-to-circuit-breakers/5439"),
    (FC, "A Consensus Layer Client Diversity Snapshot", "2025-12-18",
     "Data Always",
     "https://collective.flashbots.net/t/a-consensus-layer-client-diversity-snapshot/5431"),
    (FC, "The Free Option Problem in ePBS, Part II", "2025-08-04",
     "Christoph Schlegel, Fei Wu, Burak Öz, Bruno Mazorra",
     "https://collective.flashbots.net/t/the-free-option-problem-in-epbs-part-ii/5145"),
    (FC, "An MEV Perspective on Glamsterdam", "2025-07-23",
     "Data Always, Hasu",
     "https://collective.flashbots.net/t/an-mev-perspective-on-glamsterdam/5116"),
    (FC, "The Free Option Problem in ePBS", "2025-07-23",
     "Christoph Schlegel, Bruno Mazorra",
     "https://collective.flashbots.net/t/the-free-option-problem-in-epbs/5115"),
    (FC, "Detecting Cross-Chain Arbitrages in the Wild", "2025-07-22",
     "Burak Öz",
     "https://collective.flashbots.net/t/detecting-cross-chain-arbitrages-in-the-wild/5107"),
    (FC, "Defining Geographic Decentralisation", "2025-06-27",
     "Phil Daian",
     "https://collective.flashbots.net/t/geographic-decentralisation-research-directions/5040"),
    (FC, "The LVR Gap for Random Block Times", "2025-06-26",
     "Christoph Schlegel",
     "https://collective.flashbots.net/t/the-lvr-gap-for-random-block-times-a-quick-and-useful-approximation/5038"),
    (FC, "Fugitive Nodes", "2025-06-19",
     "Leo Arias",
     "https://collective.flashbots.net/t/fugitive-nodes/4773"),
    (FC, "RISC-V Explorations", "2025-06-19",
     "Leo Arias",
     "https://collective.flashbots.net/t/risc-v/4793"),
    (FC, "The Block Auction Arms Race", "2025-03-03",
     "Data Always",
     "https://collective.flashbots.net/t/the-block-auction-infrastructure-race/4734"),
    (FC, "The Role of Relays in Reorgs", "2024-12-20",
     "Data Always",
     "https://collective.flashbots.net/t/the-role-of-relays-in-reorgs/4247"),
    (FC, "Proposing Rights Allocation \u201cSoK\u201d", "2024-09-13",
     "Christoph Schlegel, Quintus Kilbourn",
     "https://collective.flashbots.net/t/isolating-attesters-from-mev/3837"),
    (FC, "Inelastic vs. Elastic Supply: Why PoS Could Be Less Centralizing Than Execution Tickets", "2024-09-02",
     "Christoph Schlegel",
     "https://collective.flashbots.net/t/inelastic-vs-elastic-supply-why-proof-of-stake-could-be-less-centralizing-than-execution-tickets/3816"),
    (FC, "Pricing Execution Rights when Rewards are Mean Reverting", "2024-06-30",
     "Christoph Schlegel",
     "https://collective.flashbots.net/t/pricing-execution-rights-when-rewards-are-mean-reverting/3618"),
    (FC, "When to Sell Your Blocks", "2023-12-14",
     "Quintus Kilbourn",
     "https://collective.flashbots.net/t/when-to-sell-your-blocks/2814"),

    (ER, "Trustless Payments", "2025-12-10",
     "Bruno Mazorra, Christoph Schlegel, Quintus Kilbourn, Burak Öz, Luis Correia",
     "https://ethresear.ch/t/trustless-payments/23635"),
    (ER, "Dynamic Penalties for ePBS", "2025-11-19",
     "Christoph Schlegel, Bruno Mazorra",
     "https://ethresear.ch/t/dynamic-penalties-for-epbs/23472"),
    (ER, "Understanding Minimum Blob Base Fees", "2024-09-25",
     "Data Always",
     "https://ethresear.ch/t/understanding-minimum-blob-base-fees/20489"),

    (EX, "Counter Mapping", "2025-06-19",
     "Leo Arias",
     "https://link.excalidraw.com/l/7Qr2ek3pfMQ/91UiAs0EApG"),
]

FIELDS = ["category", "title", "date", "authors", "url"]
ORDER = [AP, FW, FC, ER, EX]

root = pathlib.Path(__file__).resolve().parent.parent
docs = root / "docs"
docs.mkdir(exist_ok=True)

records = [dict(zip(FIELDS, r)) for r in ROWS]
records.sort(key=lambda r: r["date"], reverse=True)

# sanity checks
seen = set()
for r in records:
    datetime.date.fromisoformat(r["date"])
    assert r["url"].startswith("http"), r
    if r["url"] in seen:
        print(f"  ! duplicate url: {r['url']}  ({r['title']})")
    seen.add(r["url"])

with open(docs / "publications.json", "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)
    f.write("\n")

with open(docs / "publications.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(records)

# --- markdown table, rendered directly on github.com ---
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def pretty(iso):
    y, m, d = iso.split("-")
    return f"{MONTHS[int(m)-1]} {int(d)}, {y}"

def cell(s):
    return s.replace("|", "\\|")

lines = [
    "# Flashbots Research Publications",
    "",
    "Papers, protocol writings, and forum research from the Flashbots research team.",
    "",
    "A searchable version of this list is at "
    "**https://flashbots.github.io/mev-research/**. The underlying data is in "
    "[`docs/publications.json`](docs/publications.json) and "
    "[`docs/publications.csv`](docs/publications.csv) — both are free to consume.",
    "",
    "Authors tagged *(Flashbots)* are Flashbots-affiliated. Where no author in a row "
    "is tagged, all authors are Flashbots.",
    "",
    "To add a publication, edit `ROWS` in [`tools/build_publications.py`]"
    "(tools/build_publications.py) and run it — this file and the data files regenerate together.",
    "",
]

for cat in ORDER:
    rows = [r for r in records if r["category"] == cat]
    if not rows:
        continue
    lines += [f"## {cat}", "", f"{len(rows)} entries.", "",
              "| Date | Title | Authors |", "| --- | --- | --- |"]
    for r in rows:
        authors = cell(r["authors"]) or "_not listed_"
        lines.append(f"| {pretty(r['date'])} | [{cell(r['title'])}]({r['url']}) | {authors} |")
    lines.append("")

lines.append(f"---")
lines.append("")
lines.append(f"_{len(records)} publications. Generated by `tools/build_publications.py`; edit that file, not this one._")

with open(root / "publications.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"wrote {len(records)} records")
for cat in ORDER:
    print(f"  {sum(1 for r in records if r['category'] == cat):>3}  {cat}")
