#!/usr/bin/env python3
"""
Finds recent team publications missing from publications.yaml and appends
them as candidates for review.

Run:  python3 tools/fetch_publications.py [SINCE]   (YYYY-MM-DD, default: 45 days ago)
      python3 tools/fetch_publications.py --check   recall gate: must rediscover all of
                                                    publications.yaml from scratch

Sources: writings.flashbots.net RSS, Discourse (collective.flashbots.net,
ethresear.ch), arXiv API, IACR ePrint OAI-PMH. Prints a markdown summary
(used as the PR body by .github/workflows/fetch-publications.yml).
Requires PyYAML.
"""
import datetime, html, json, time, pathlib, re, sys, unicodedata, urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
import yaml

# Forum -> (category, Discourse category ids that count as research; None = all).
# Who is searched comes from team.yaml.
# ethresear.ch first: a post cross-posted to both forums is listed once, from ethresear.ch (wider audience).
FORUMS = {
    "ethresear.ch": ("ethresear.ch Post", None),
    # Research, The Flashbots Ship (+subs), Data, TEE (+sub); not 25, Research > References (reading notes)
    "collective.flashbots.net": ("Flashbots Collective Forum Posts", {20, 18, 21, 17, 13, 28, 30}),
}
ER = FORUMS["ethresear.ch"][0]

# ponytail: subject filter against arXiv name collisions (e.g. "Fei Wu" in cs.AI); arXiv/ORCID author ids would be exact.
ARXIV_CATS = re.compile(r"^(cs\.(CR|GT|DC|NI|CE)|econ\.|q-fin\.)")

AP, FW = "Academic Papers", "Flashbots Writings"
ROOT = pathlib.Path(__file__).resolve().parent.parent
YAML = ROOT / "publications.yaml"  # bot appends here; publications-manual.yaml is humans only
IGNORED = ROOT / "publications-ignored.yaml"  # URLs reviewers rejected; never proposed again
ROSTER = yaml.safe_load((ROOT / "team.yaml").read_text(encoding="utf-8"))


def norm(name):
    return unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower().strip()


# normalised names and aliases of current team members
TEAM = {norm(n) for m in ROSTER for n in [m["name"], *m.get("aliases", [])]}
# normalised name or alias -> GitHub handle, to @-mention authors on the PR
GITHUB = {norm(n): m["github"] for m in ROSTER if m.get("github") for n in [m["name"], *m.get("aliases", [])]}


def mentions(authors):
    handles = dict.fromkeys(GITHUB.get(norm(a.replace("(Flashbots)", ""))) for a in (authors or "").split(","))
    return " ".join(f"@{h}" for h in handles if h)


def affiliations(url, names):
    """({author: affiliated with Flashbots}, Flashbots mentioned anywhere on the page) from the
    paper's own author list, or (None, None) when the page has no per-author affiliations."""
    if m := re.search(r"arxiv\.org/abs/(.+)", url):
        try:
            page = get(f"https://arxiv.org/html/{m[1]}").decode("utf-8", "replace")
        except urllib.error.HTTPError:
            return None, None  # no HTML rendering for this paper
        finally:
            time.sleep(1)
        authors = page[page.find('class="ltx_authors"'):page.find('class="ltx_abstract"')]
        blocks = authors.split('ltx_role_author"')[1:]
    else:  # ePrint
        page = get(url).decode("utf-8", "replace")
        blocks = page.split('<div class="author">')[1:]
    # ponytail: blocks matched to authors by position; shared footnote affiliations ("†") are missed.
    if len(blocks) != len(names) or not any(
            re.search(r'ltx_role_affiliation|ltx_author_notes|class="affiliation"', b) for b in blocks):
        return None, None
    return ({n: "flashbots" in b.lower() for n, b in zip(names, blocks)},
            "flashbots" in page.lower())


def paper(title, date, names, url):
    """Candidate entry for a paper with a team author, or None if it isn't Flashbots work."""
    aff, mentioned = affiliations(url, names)
    if aff is None:
        fb, note = {n for n in names if norm(n) in TEAM}, "no affiliations on the paper; tagged current team members"
    elif any(aff.values()):
        fb, note = {n for n in names if aff[n]}, None
    elif mentioned:
        fb, note = set(), "Flashbots is on the paper but in no author's affiliation (acknowledgements?)"
    else:
        return None  # team member's work under another affiliation, before or after Flashbots
    authors = ", ".join(n + " (Flashbots)" if n in fb else n for n in names)
    return entry(AP, title, date, authors, url, note)


def key(url):
    """Canonical id so arXiv versions, ia.cr short links and Discourse slugs dedupe."""
    if m := re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", url):
        return "arxiv:" + m[1]
    if m := re.search(r"(?:eprint\.iacr\.org|ia\.cr)/(\d{4}/\d+)", url):
        return "eprint:" + m[1]
    if m := re.search(r"//([^/]+)/t/(?:[^/]+/)?(\d+)", url):
        return f"{m[1]}:{m[2]}"
    return re.sub(r"^https?://(www\.)?", "", url).rstrip("/").lower()


def get(url, tries=5):
    req = urllib.request.Request(url, headers={"User-Agent": "flashbots-mev-research-publications"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code not in (429, 503) or tries == 1:
            raise
        time.sleep(int(e.headers.get("Retry-After") or 30))
        return get(url, tries - 1)


def entry(category, title, date, authors, url, note=None):
    """`note` is shown to the PR reviewer, not written to publications.yaml."""
    return {"category": category, "title": " ".join(title.split()), "date": date,
            "authors": authors, "url": url, "note": note}


def writings(since):
    for it in ET.fromstring(get("https://writings.flashbots.net/rss.xml")).iter("item"):
        d = datetime.datetime.strptime(it.findtext("pubDate"), "%a, %d %b %Y %H:%M:%S %Z").date()
        if d >= since:  # the feed carries no authors: read them off the post's page
            page = get(it.findtext("link")).decode("utf-8", "replace")
            names = [html.unescape(n).strip() for n in re.findall(r'class="avatar__name"[^>]*>(?:<[^>]+>)*([^<]+)', page)]
            names = [n for n in dict.fromkeys(names) if n.lower() not in ("flashbots", "friends")]
            yield entry(FW, it.findtext("title"), d, ", ".join(n + " (Flashbots)" if norm(n) in TEAM else n for n in names),
                        it.findtext("link"))


def discourse(since):
    failed = []
    for host, (category, cats) in FORUMS.items():
        for user, name in [(m["forums"][host], m["name"]) for m in ROSTER if host in m.get("forums", {})]:
            # search, not /topics/created-by: the latter 404s for users who hide their activity
            q = urllib.parse.quote(f"@{user} in:first after:{since} order:latest")
            # 50 topics a page: up to 1000 per member and run, far above a month's (or the
            # 2023 backfill's) posts; hitting the cap fails the source rather than drop posts
            for page in range(1, 21):
                try:
                    topics = json.loads(get(f"https://{host}/search.json?q={q}&page={page}")).get("topics", [])
                except Exception as ex:
                    failed.append(f"{host}/{user}: {ex!r}")
                    break
                finally:
                    time.sleep(3)  # anonymous search is rate limited
                for t in topics:
                    d = datetime.date.fromisoformat(t["created_at"][:10])
                    if d >= since and (cats is None or t["category_id"] in cats):
                        yield entry(category, t["title"], d, f"{name} (Flashbots)", f"https://{host}/t/{t['slug']}/{t['id']}")
                if len(topics) < 50:  # Discourse search page size
                    break
            else:
                failed.append(f"{host}/{user}: more than 1000 topics, raise the page cap")
    if failed:
        raise RuntimeError("; ".join(failed))


def arxiv(since):
    ns = {"a": "http://www.w3.org/2005/Atom", "os": "http://a9.com/-/spec/opensearch/1.1/"}
    q = " OR ".join(f'au:"{n}"' for n in TEAM)
    # Newest first, 200 a page, until older than `since` or out of results. arXiv serves at
    # most 30000 results per query; an incomplete listing fails the source, never truncates it.
    for start in range(0, 30000, 200):
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending",
             "start": start, "max_results": 200})
        feed = ET.fromstring(get(url))
        entries, total = feed.findall("a:entry", ns), int(feed.findtext("os:totalResults", namespaces=ns))
        for e in entries:
            d = datetime.date.fromisoformat(e.findtext("a:published", namespaces=ns)[:10])
            names = [a.findtext("a:name", namespaces=ns) for a in e.iterfind("a:author", ns)]
            cats = [c.get("term", "") for c in e.iterfind("a:category", ns)]
            if d >= since and TEAM & set(map(norm, names)) and any(map(ARXIV_CATS.match, cats)):
                abs_id = re.sub(r"v\d+$", "", e.findtext("a:id", namespaces=ns)).replace("http://", "https://")
                if p := paper(e.findtext("a:title", namespaces=ns), d, names, abs_id):
                    yield p
        if start + len(entries) >= total or (entries and d < since):
            return
        if len(entries) < 200:  # the API sometimes serves short pages mid-query
            raise RuntimeError(f"arXiv served {len(entries)} results at {start} of {total}")
        time.sleep(3)  # arXiv API etiquette
    raise RuntimeError("more than 30000 arXiv results: narrow the query")


def eprint(since):
    # OAI `from` filters on last-modified; dc:date is the original posting date.
    ns = {"o": "http://www.openarchives.org/OAI/2.0/", "dc": "http://purl.org/dc/elements/1.1/"}
    url = f"https://eprint.iacr.org/oai?verb=ListRecords&metadataPrefix=oai_dc&from={since}"
    while url:
        root = ET.fromstring(get(url))
        for r in root.iterfind(".//o:record", ns):
            names = [c.text for c in r.iterfind(".//dc:creator", ns)]
            d = r.findtext(".//dc:date", namespaces=ns) or r.findtext(".//o:datestamp", namespaces=ns)
            d = datetime.date.fromisoformat(d[:10])
            if d >= since and TEAM & set(map(norm, names)):
                if p := paper(r.findtext(".//dc:title", namespaces=ns), d, names,
                              r.findtext(".//dc:identifier", namespaces=ns)):
                    yield p
        token = root.findtext(".//o:resumptionToken", namespaces=ns)
        url = token and "https://eprint.iacr.org/oai?verb=ListRecords&resumptionToken=" + urllib.parse.quote(token)


# Venue short name -> how it shows up in arXiv comments, ePrint "Publication info" and OpenAlex/DOI data.
# Order matters: workshops before conferences, EuroS&P before S&P. Acronyms are case-sensitive, full names are not.
# A venue missing here only means the fetcher can't fill it in: reviewers set `venue:` by hand.
# Workshops without their own entry come out as their host ("NeurIPS 2023"): refine by hand.
VENUES = [
    ("SysTEX", r"(?i:systex)"),  # workshops first: they name their co-located host
    ("AFT", r"\bAFT\b|(?i:advances in financial technolog)"),
    ("FC", r"\bFC\b ?'?\d\d|(?i:financial cryptography)"),
    ("EC", r"\bEC\b ?'?\d\d|(?i:economics and computation)"),
    ("CCS", r"\bCCS\b|(?i:computer and communications security)"),
    ("EuroS&P", r"EuroS&P|(?i:european symposium on security and privacy)"),
    ("IEEE S&P", r"\bS&P\b|(?i:symposium on security and privacy)"),
    ("USENIX Security", r"(?i:usenix security)"),
    ("NDSS", r"\bNDSS\b"),
    ("CRYPTO", r"\bCRYPTO\b|(?i:international cryptology conference)"),
    ("EUROCRYPT", r"\bEUROCRYPT\b|(?i:eurocrypt)"),
    ("ASIACRYPT", r"\bASIACRYPT\b|(?i:asiacrypt)"),
    ("TCC", r"\bTCC\b|(?i:theory of cryptography conference)"),
    ("PODC", r"\bPODC\b|(?i:principles of distributed computing)"),
    ("WINE", r"\bWINE\b|(?i:web and internet economics)"),
    ("SBC", r"(?i:science of blockchain)"),
    ("PETS", r"\bPETS\b|\bPoPETs\b|(?i:privacy enhancing technologies)"),
    ("ESORICS", r"\bESORICS\b"),
    ("ICBC", r"\bICBC\b|(?i:international conference on blockchain and cryptocurrency)"),
    ("NeurIPS", r"\bNeurIPS\b|(?i:neural information processing systems)"),
    ("Mathematical Finance", r"(?i:mathematical finance)"),
]
NOT_YET = re.compile(r"(?i)submitted|under review|under submission|in submission")


def venue_in(text):
    """"AFT 2026" from text like "...to appear in ... (AFT 2026)" or "LIPIcs.AFT.2026.30"; None if no known venue."""
    for name, pattern in VENUES:
        for m in re.finditer(pattern, text):
            if NOT_YET.search(text[max(0, m.start() - 80):m.end() + 20]):
                continue
            year = re.search(r"\b(20\d\d)\b|'(\d\d)\b", text[m.start():m.end() + 40]) or re.search(r"\b(20\d\d)\b", text)
            return f"{name} {year[1] or '20' + year[2]}" if year else name
    return None


def venue(url):
    """Where a paper was published, from what arXiv / ePrint / OpenAlex record; None while unknown."""
    texts = []
    if m := re.search(r"arxiv\.org/abs/(.+)", url):
        e = ET.fromstring(get(f"https://export.arxiv.org/api/query?id_list={m[1]}"))
        texts += [x.text or "" for x in e.iter() if x.tag.endswith(("}comment", "}journal_ref"))]
        try:
            work = json.loads(get(f"https://api.openalex.org/works/doi:10.48550/arXiv.{m[1]}"))
            texts += [" ".join(str(v) for v in (l.get("landing_page_url"), l.get("raw_source_name"),
                                                 (l.get("source") or {}).get("display_name")) if v)
                      for l in work.get("locations", [])]
        except urllib.error.HTTPError:
            pass  # not in OpenAlex (yet)
        time.sleep(1)
    elif "eprint.iacr.org" in url:
        page = get(url).decode("utf-8", "replace")
        info = page[page.find("Publication info"):][:600]
        texts.append(html.unescape(re.sub(r"<[^>]+>", " ", info)))
    return next((v for v in map(venue_in, texts) if v), None)


STOPWORDS = {"a", "an", "the", "of", "in", "on", "for", "and", "to", "with", "is", "are", "at", "via", "from",
             "by", "how", "why", "what", "when", "do", "does", "paper"}


def words(title):
    return {w.rstrip("s") for w in re.findall(r"[a-z0-9]+", norm(title)) if w not in STOPWORDS}


def same_work(a, b, threshold=0.8):
    """Titles naming the same work, e.g. "Do Ahead-of-Time Auctions Work?" vs "TimeBoost: Do Ahead-of-Time Auctions Work?"."""
    A, B = words(a), words(b)
    return bool(A and B) and len(A & B) / len(A | B) >= threshold


def showcase(post, works):
    """Forum posts presenting a listed paper or writing duplicate it: returns (drop, note)."""
    if any(same_work(post["title"], w["title"]) for w in works):
        return True, None
    host, topic = re.search(r"//([^/]+)/t/(?:[^/]+/)?(\d+)", post["url"]).groups()
    first = json.loads(get(f"https://{host}/t/{topic}.json"))["post_stream"]["posts"][0]["cooked"]
    time.sleep(0.5)
    linked = {key(html.unescape(h)) for h in re.findall(r'href="([^"]+)"', first)}
    hits = [w["title"] for w in works if key(w["url"]) in linked]
    return False, hits and f"links to {'; '.join(hits)}: a showcase of it (then drop), or separate work?"


def fetch(since, seen, listed=()):
    """New entries from all sources, skipping ids in `seen`; plus per-source errors.
    Forum posts showcasing a paper or writing (listed, or found in this run) are dropped."""
    new, errors = [], []
    for source in (writings, arxiv, eprint, discourse):  # forums last, to check them against papers
        try:
            for e in source(since):
                ids = {key(e["url"]), (e["category"], norm(e["title"]))}
                if ids & seen:
                    continue
                if source is discourse:
                    known = [*listed, *new]
                    if e["category"] != ER and any(w["category"] == ER and same_work(e["title"], w["title"]) for w in known):
                        continue  # cross-posted: keep the ethresear.ch copy
                    drop, e["note"] = showcase(e, [w for w in known if w["category"] in (AP, FW)])
                    if drop:
                        continue
                seen |= ids
                new.append(e)
        except Exception as ex:  # one flaky source must not drop the others' results
            errors.append(f"{source.__name__}: {ex!r}")
    return new, errors


def check():
    """Recall gate: from scratch, the fetcher must rediscover every entry in publications.yaml."""
    listed = yaml.safe_load(YAML.read_text(encoding="utf-8"))
    since = min(datetime.date.fromisoformat(str(r["date"])) for r in listed)
    found, errors = fetch(since, set())
    ids = {key(e["url"]) for e in found} | {(e["category"], norm(e["title"])) for e in found}
    missing = [r for r in listed if key(r["url"]) not in ids and (r["category"], norm(r["title"])) not in ids]
    print(f"recall: {len(listed) - len(missing)}/{len(listed)} entries of publications.yaml rediscovered since {since}"
          f" ({len(found)} fetched)")
    for r in missing:
        print(f"  MISSING {r['date']} {r['category']}: {r['title']}  {r['url']}")
    tags = lambda a: {n.strip() for n in re.findall(r"([^,]+?) \(Flashbots\)", a or "")}
    by_key = {key(e["url"]): e for e in found}
    for r in listed:  # informational: listed tags vs what the paper says
        if (e := by_key.get(key(r["url"]))) and e["category"] == AP and tags(r["authors"]) != tags(e["authors"]):
            print(f"  TAGS {r['title'][:60]}: listed {sorted(tags(r['authors']))}, paper {sorted(tags(e['authors']))}"
                  + (f" ({e['note']})" if e["note"] else ""))
    for err in errors:
        print(f"  source failed: {err}")
    sys.exit(1 if missing or errors else 0)


def main():
    if sys.argv[1:] == ["--check"]:
        return check()
    since = (datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1
             else datetime.date.today() - datetime.timedelta(days=45))
    existing = [r for f in (YAML, ROOT / "publications-manual.yaml")
                for r in yaml.safe_load(f.read_text(encoding="utf-8")) or []]
    ignored = yaml.safe_load(IGNORED.read_text(encoding="utf-8")) or []
    # by url, and by title within a category (the same paper on arXiv and ePrint)
    seen = ({key(u) for r in existing for u in (r["url"], r.get("also")) if u}
            | {(r["category"], norm(r["title"])) for r in existing})
    new, errors = fetch(since, seen | {key(u) for u in ignored}, existing)
    for e in new:
        if e["category"] == AP and (v := venue(e["url"])):
            e["venue"] = v
    # Listed papers not yet known to be published: did a venue appear? ("venue: preprint" opts out.)
    text = YAML.read_text(encoding="utf-8")
    found = []
    for r in yaml.safe_load(text):
        if r["category"] == AP and not r.get("venue") and (v := venue(r["url"])):
            text = text.replace(f"  url: {r['url']}\n", f"  url: {r['url']}\n  " + yaml.safe_dump({"venue": v}), 1)
            found.append((r, v))
    YAML.write_text(text, encoding="utf-8")
    for e in new:  # the other direction: a new paper or writing that a listed forum post was showcasing
        if e["category"] in (AP, FW):
            posts = [r["url"] for r in existing if r["category"] not in (AP, FW) and same_work(r["title"], e["title"])]
            if posts:
                e["note"] = f"listed forum post(s) {', '.join(posts)} showcase this: remove them"

    if new:
        with open(YAML, "a", encoding="utf-8") as f:
            rows = [{k: v for k, v in e.items() if k != "note"} for e in new]
            f.write("\n" + yaml.safe_dump(rows, allow_unicode=True, sort_keys=False, width=1000))

    print(f"Candidate publications since {since}, found by `tools/fetch_publications.py`.\n")
    print("Please review before merging: drop anything that isn't research, fill in missing "
          "authors, and check the *(Flashbots)* tags. Forum posts list only the poster. "
          "To reject a candidate for good, delete it and add its URL to `publications-ignored.yaml`.\n")
    for e in new:
        cc = mentions(e["authors"])
        print(f"- **{e['category']}** · {e['date']} · [{e['title']}]({e['url']}) · {e['authors'] or '_authors missing_'}"
              + (f" · *{e['venue']}*" if e.get("venue") else "")
              + (f" · cc {cc}" if cc else "") + (f"  \n  ⚠️ {e['note']}" if e["note"] else ""))
    if not new:
        print("_Nothing new._")
    if found:
        print("\nVenues found for listed papers (now in publications.yaml; "
              "set `venue: preprint` on a paper to stop checking it):\n")
        for r, v in found:
            print(f"- {v}: [{r['title']}]({r['url']})")
    for err in errors:
        print(f"\n> ⚠️ source failed: `{err}`")


# Self-checks, run on every invocation: a change that breaks URL dedupe, @-mentions,
# venue parsing or title matching fails the monthly run before it writes anything.
assert key("https://arxiv.org/abs/2509.21475v2") == key("http://arxiv.org/pdf/2509.21475") == "arxiv:2509.21475"
assert key("https://ia.cr/2025/1384") == key("https://eprint.iacr.org/2025/1384") == "eprint:2025/1384"
assert key("https://ethresear.ch/t/x/23635") == key("https://ethresear.ch/t/23635") == "ethresear.ch:23635"
assert "burak oz" in TEAM and "ari juels" not in TEAM
assert mentions("Ari Juels, Burak Oez (Flashbots), Burak Öz") == "@boz1" and mentions("") == ""
assert venue_in("This is the full version. The proceedings is to appear in 8th Conference on Advances in Financial Technologeis (AFT 2026)") == "AFT 2026"
assert venue_in("In Financial Cryptography and Data Security 2026") == "FC 2026"
assert venue_in("https://doi.org/10.4230/LIPIcs.AFT.2024.30 Leibniz international proceedings in informatics") == "AFT 2024"
assert venue_in("Published elsewhere. Minor revision. Advances in Financial Technologies (AFT) DOI 10.4230/LIPIcs.AFT.2026.30") == "AFT 2026"
assert venue_in("Accepted at SysTEX 2026, co-located with EuroS&P") == "SysTEX 2026"
assert venue_in("Submitted to CCS 2025") is None and venue_in("12 pages, 3 figures") is None
assert same_work("Do Ahead-of-Time Auctions Work?", "TimeBoost: Do Ahead-of-Time Auctions Work?")
assert same_work("ZTEE: Trustless Supply Chains", "ZTEE - Trustless Supply Chains")
assert not same_work("The Free Option Problem in ePBS, Part II", "The Free Option Problem of ePBS")
assert not same_work("Trustless Payments", "Trustless payments and relays and more and more")

if __name__ == "__main__":
    main()
