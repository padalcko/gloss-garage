# Виправлення моделі: Mazda CX-5

Виправлено лише реалізацію переднього правого крила PL/RU. Попередня реалізація Volkswagen Tiguan (заднє крило), включно з фото, побайтово незмінна.

Нові маршрути:
- https://gg-pdr.pl/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/
- https://gg-pdr.pl/ru/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/

Старий PL URL перевірено: HTTP 200. У `_redirects` додано 301! для старих PL/RU адрес, варіантів без слеша, index.html та index.md. Конфігурація перевірена статично; застосування редиректів на хостингу потребує публікації.

Перевірки:
- 99 локальних HTTP-перевірок без помилок.
- 24 перевірки Chrome: PL/RU сторінки та списки, ширини 320, 375, 430, 768, 1024, 1440 px. Без переповнення, зламаних фото або JS-помилок; навігація карток працює.
- Усі шість фото збережені в порядку 01–06: три до, три після; обкладинка 04. SHA-256 усіх 24 варіантів підтверджує незмінність байтів.
- Детальні HTML-сторінки відрізняються лише моделлю, маршрутами та граматичним узгодженням. Структура, header/footer, CSS/JS і галерея незмінні.
- Canonical, hreflang, JSON-LD, sitemap, внутрішні посилання та актуальність AI-ресурсів перевірені штатними валідаторами.
- Старий slug залишено лише в правилах redirect та їх валідаторі.
- Commit, push, deploy не виконувалися.

## Змінені та перейменовані файли

Старі файли цієї реалізації замінено перейменованими, без дублювання. Попередній звіт перейменовано; його дані описують початкове створення реалізації.

- `_headers`
- `_redirects`
- `ai/pdr.md`
- `ai/realizacje.md`
- `ai/services.md`
- `docs/ai-search-validation.json`
- `docs/cases-seo.json`
- `docs/cases-validation.json`
- `docs/image-audit.json`
- `docs/mazda-cx5-correction-report.md`
- `docs/mazda-cx5-front-right-report.md`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-01-360.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-01-540.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-01-768.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-01-960.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-02-360.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-02-540.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-02-768.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-02-960.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-03-360.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-03-540.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-03-768.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-03-960.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-04-360.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-04-540.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-04-768.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-04-960.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-05-360.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-05-540.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-05-768.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-05-960.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-06-360.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-06-540.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-06-768.webp`
- `images/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik-06-960.webp`
- `index.html`
- `llms-full.txt`
- `llms.txt`
- `realizacje/index.html`
- `realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/index.html`
- `realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/index.md`
- `ru/index.html`
- `ru/realizacje/index.html`
- `ru/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/index.html`
- `ru/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/index.md`
- `scripts/cases-content.json`
- `scripts/check-ai-search.py`
- `sitemap.xml`
