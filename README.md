# Gloss Garage

Static Polish/Russian PDR site: https://gg-pdr.pl/.

## How to add a new PDR realization

1. Confirm the vehicle, damaged panel, repair method and outcome; use authentic photos.
2. Optimize photos with `scripts/optimize-case-images.py ORIGINALS --manifest MANIFEST.json` (Pillow required). The JSON manifest maps a descriptive case slug to ordered original filenames. The pipeline creates descriptive WebP filenames and responsive sizes.
3. Add factual PL/RU copy and descriptive photo alts to `scripts/cases-content.json`.
4. Run `python3 scripts/build-site.py`. It creates case HTML/metadata/schema, cards, homepage evidence links, Markdown, llms and sitemap entries.
5. Run `python3 scripts/build-ai-search.py --check`, `python3 scripts/check-ai-search.py`, `python3 scripts/check-cases.py`, and `git diff --check`.
6. Check desktop/mobile and contact/navigation behavior. Review before any commit, push or deployment.

Detailed architecture, image manifest example, file ownership and validation limits: [docs/ai-search-architecture.md](docs/ai-search-architecture.md).

The build uses Python's standard library; image optimization and case-image validation need Pillow. AI documents are generated supplements. HTML remains canonical. Developer files are excluded from public delivery by Netlify rules in `_redirects`; local `http.server` does not apply those rules.
