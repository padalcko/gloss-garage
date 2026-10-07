# Gloss Garage: AI/search architecture

## Authoritative sources and entity

The website is a static Polish/Russian site. Polish is primary. `index.html` and `ru/index.html` own visible company, services, FAQ and contact information. `scripts/cases-content.json` owns the factual bilingual case descriptions; `scripts/build-cases.py` renders them into HTML. `docs/image-audit.json` supplies actual image dimensions. HTML remains the primary search content.

The stable business identity is `https://gg-pdr.pl/#business` (AutoRepair, a subtype of LocalBusiness and Organization). The workshop address is **ul. Szkolna 55, Radwanice, Poland**; service coverage is **Wrocław and surroundings**, not an invented Wrocław street address or all of Dolny Śląsk. Telephone `+48884012737` and WhatsApp `https://wa.me/380667835184` are distinct existing contact channels. Instagram and Facebook come from existing public HTML and AutoRepair schema. There is no verified business email, opening-hours schedule, logo image, GBP URL, award, author credential or rating added by this work. The existing visible GG wordmark is preserved; the OG photograph is not relabelled as a logo.

## Public resources

| File | Purpose | Authoritative HTML |
| --- | --- | --- |
| `/llms.txt` | Compact discovery map, PL first | `/`, `/#pdr`, `/realizacje/`, `/#contact`, `/#faq` |
| `/llms-full.txt` | Expanded Polish knowledge and all Polish cases | Links to the source sections/cases in each chapter |
| `/ai/about.md` | Company identity and specialization | `/` |
| `/ai/services.md` | Existing service groups, problems, method, evidence | `/#pdr` |
| `/ai/pdr.md` | PDR explanation, assessment and limitations | `/#pdr`, `/#faq` |
| `/ai/faq.md` | The ten visible Polish questions and answers | `/#faq` |
| `/ai/contact.md` | Public contact, location, profiles, website languages | `/#contact`, footer |
| `/ai/realizacje.md` | Automatically discovered case index | `/realizacje/` |
| `/realizacje/<slug>/index.md` | Polish case representation | `/realizacje/<slug>/` |
| `/ru/realizacje/<slug>/index.md` | Russian case representation | `/ru/realizacje/<slug>/` |

All 10 indexable HTML pages link to `/llms.txt` with `rel="describedby"`. The Polish home/index and all individual PL/RU cases also link to their primary Markdown resource using `rel="alternate" type="text/markdown"`. The RU home/index use the global map without incorrectly labelling a Polish extract as a Russian translation. There is no new English HTML version.

`_headers` gives full case Markdown an HTTP canonical to its corresponding HTML, plus UTF-8 Markdown content type. Thematic `/ai/*.md` extracts and aggregated llms files use `X-Robots-Tag: noindex` rather than misleading canonical claims that a fragment/extract is a complete duplicate. They remain publicly fetchable and allowed by robots; this intentionally keeps traditional search landing pages in HTML. Different AI systems may choose whether to consume these supplements. No search visibility guarantee is implied.

`robots.txt` already allows all paths and declares `https://gg-pdr.pl/sitemap.xml`; it remains unchanged. Sitemap contains only the ten canonical indexable HTML routes, with reciprocal PL/RU/x-default pairs. No Markdown, llms, technical pages or developer documentation are included. Unmaintained historical `lastmod` values were removed rather than fabricating modification dates.

## Internal files

- `scripts/build-site.py`: ordered local rebuild of cases, AI outputs, then AI validation.
- `scripts/build-cases.py`: HTML cases/indexes, homepage evidence links, case SEO report and generated sitemap block.
- `scripts/build-ai-search.py`: topical Markdown, PL/RU case Markdown, llms, HTML discovery/schema blocks and Netlify resource headers.
- `scripts/site_content.py`: small standard-library HTML parser and Markdown rendering helper.
- `scripts/check-ai-search.py`: freshness, links/fragments, schema, identity, FAQ visibility, metadata, language pairing, sitemap/robots and optional HTTP checks.
- `scripts/check-cases.py`: HTML nesting, responsive image files/dimensions, sitemap, forms, integration preservation and optional HTTP checks (Pillow required).
- `scripts/optimize-case-images.py`: existing image pipeline extended with an optional filename manifest; preserves earlier image audit records for other cases.
- `docs/*search-inventory.json`: pre-change inventories of both repositories. The reference inventory records file paths, schema types and metadata field names, not another company's content or contacts.
- `docs/ai-search-validation.json`, `docs/cases-validation.json`: check evidence; rerunning without `--http` replaces HTTP results with a static-only report.
- `docs/ai-search-report.md`: complete task report including exact llms content and file changes.
- `README.md`: maintenance quick start.

`_redirects` forces `/docs/*`, `/scripts/*` and `/README.md` to a 404 response on Netlify. This prevents developer source/report delivery on the published site, including existing reports, without deleting files. Public runtime JS remains under `/js/`, unaffected. `404.html` is a small noindex error page using the existing stylesheet. Netlify serves it for other missing routes automatically. Python's plain local HTTP server does **not** implement `_headers` or `_redirects`; Netlify delivery must be verified after a separately authorized deployment.

## Build and ownership

```sh
python3 scripts/build-site.py
python3 scripts/build-ai-search.py --check
python3 scripts/check-ai-search.py
python3 scripts/check-cases.py  # requires Pillow
```

Do not edit generated Markdown, llms, case HTML, case indexes or marked HTML/schema/header blocks by hand. Change home HTML or `cases-content.json`, then rebuild. The header generator preserves unrelated rules outside its generated block. Orphan Markdown is reported for review, never deleted automatically. A repeated complete build is deterministic.

Update business facts in both homepages (visible content and original AutoRepair definitions), then regenerate. The builder derives identity/contact from the Polish source; its short editorial labels and summary phrases should also be reviewed if geography, channels or scope change. Validation rejects divergent entity fields, missing/invalid URLs and stale generated outputs.

## How to add a new PDR realization

1. Obtain authentic photos and confirmed facts. Do not infer repair dates, duration, cost, certifications or before/after order from photos.
2. Choose a descriptive slug, e.g. `marka-model-pdr-element`. Use the existing keys and PL/RU structure of a case in `scripts/cases-content.json`: `car`, `title`, `description`, `h1`, `lead`, `damage`, `sections`, `alts`. Photo order and alt count must agree.
3. Prepare an image manifest outside the public site, for example:
   ```json
   {"marka-model-pdr-element": ["original-01.PNG", "original-02.PNG"]}
   ```
   Run `python3 scripts/optimize-case-images.py /path/to/originals --manifest /path/to/manifest.json`. This generates descriptive 360/540/768/1086 WebP variants and records actual dimensions in `docs/image-audit.json`. Existing photos are not regenerated unless included in the manifest. Source originals must be large enough for the largest intended variant; inspect them before encoding.
4. Run `python3 scripts/build-site.py`. It creates both HTML case routes, metadata, WebPage/ImageObject/BreadcrumbList relationships, index cards, service-to-case links, Markdown cases, AI realization index, llms files, sitemap alternates and HTTP canonical rules.
5. Run both validators. For local HTTP: `python3 -m http.server 8776 --bind 127.0.0.1`, then add `--http http://127.0.0.1:8776` to both validation commands. Run `git diff --check`.
6. Review desktop/mobile rendering, actual image selection, overflow, language switching, FAQ, navigation and contact actions in a connected browser. Do not submit a live lead as a test without authorization.
7. Review the full diff and publication state. Commit, push and deploy are separate authorized actions.

## Standards and limits

The approach takes generation, HTML source ownership, discovery links, canonical representations and freshness checks from the reference project, without transferring its business content. The lighter topic-plus-case organization fits this site because services/contact are sections of the homepage, not independent routes.

[Google's AI-search guidance](https://developers.google.com/search/docs/appearance/ai-features) says standard SEO fundamentals apply and extra AI files or special schema are not required. [llms.txt](https://llmstxt.org/) is a discovery proposal, not a ranking standard. [AutoRepair](https://schema.org/AutoRepair) provides the existing business semantics. [Netlify redirect options](https://docs.netlify.com/manage/routing/redirects/redirect-options/) document forced rules and custom 404 handling. FAQPage describes the visible answers; no FAQ rich-result eligibility is claimed.
