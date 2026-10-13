# Publication tools

Requires Python 3 and PyYAML (`pip install pyyaml`). Run from the repo root.

## Preview the site locally

```sh
python3 tools/build_publications.py && python3 -m http.server -d docs 8000
```

Open http://localhost:8000. The build writes `docs/publications.json` and
`docs/publications.csv` (git-ignored) and regenerates `publications.md`.
Rerun it after editing the YAML; the server can stay up.
