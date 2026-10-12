# Publication tools

Requires Python 3 and PyYAML (`pip install pyyaml`). Run from the repo root.

## Preview the site locally

```sh
python3 tools/build_publications.py && python3 -m http.server -d docs 8000
```

Open http://localhost:8000. The build writes `docs/publications.json` and
`docs/publications.csv` (git-ignored) and regenerates `publications.md`.
Rerun it after editing the YAML; the server can stay up.

## Fetch new publications

The monthly workflow (`.github/workflows/fetch-publications.yml`) runs this
and opens a PR; to run it by hand:

```sh
python3 tools/fetch_publications.py [YYYY-MM-DD]   # appends candidates since that date (default: 45 days ago) to publications.yaml
python3 tools/fetch_publications.py --check        # recall gate: must rediscover every entry of publications.yaml
```

Who is searched comes from `team.yaml`; rejected URLs go in `publications-ignored.yaml`.
