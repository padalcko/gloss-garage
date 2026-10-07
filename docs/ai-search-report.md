# Gloss Garage — фінальний AI / LLM / GEO / SEO аудит

Дата перевірки: 2026-10-07. Усі зміни локальні. **Commit / push / deploy не виконувалися.** Нові публічні URL нижче — заплановані адреси після публікації, а не твердження про їхню поточну доступність онлайн.

## REFERENCE INVENTORY — LASER TECH SERVICE

Спочатку прочитано архітектуру, генератор, валідатор, правила HTTP-заголовків і robots референсного репозиторію; проскановано всі HTML та пошукові механізми. Повний inventory: `docs/laser-tech-service-search-inventory.json`.

Поточний checkout містить **73 HTML-файли** та **167 файлів із пошуковими механізмами/Markdown**. Це поточне сканування, а не історичні числа з попередньої роботи.

| Механізм | Рішення для Gloss Garage |
| --- | --- |
| `llms.txt`, `llms-full.txt` | Компактна карта + повний польський документ |
| Сусідні `index.md` для HTML | Використано для 6 PL/RU кейсів; для короткої головної — 6 тематичних витягів |
| `scripts/build-ai-search.py`, `scripts/check-ai-search.py` | Адаптовано принцип source → generation → freshness validation; власний контент GG |
| `docs/ai-search.md` | Власна `docs/ai-search-architecture.md` |
| `_headers` | HTTP canonical для повних case representations; noindex для тематичних витягів |
| `robots.txt`, `sitemap.xml` | Crawl доступний; sitemap лише для canonical HTML |
| JSON-LD, FAQ, breadcrumbs | Єдина наявна GG identity; FAQ лише з видимими відповідями |
| canonical, hreflang, OG, Twitter | Повний аудит поточних PL/RU сторінок |
| `rel=alternate`, `rel=describedby` | Discovery у head без спеціальних вигаданих AI meta tags |

Inventory референсу містить лише файлові шляхи, назви metadata fields, schema types і кількості. Чужі тексти, контакти та schema definitions у публічні матеріали GG не перенесено. Репозиторій Laser Tech Service не змінювався.

## INITIAL GLOSS GARAGE INVENTORY

`docs/gloss-garage-search-inventory.json` фіксує стан до змін: 10 HTML, 5 PL/RU пар, дві головні, два індекси робіт, шість сторінок кейсів; послуги `/#pdr`, контакт `/#contact`. Окремих service/contact HTML routes немає. Існували AutoRepair на головних, WebPage/ImageObject/BreadcrumbList на кейсах та індексах, robots, sitemap, соціальні metadata, 40 responsive WebP і генератор кейсів. AI-файлів та FAQ не було.

## AI FILES CREATED

| File | Purpose | Public/internal | URL |
| --- | --- | --- | --- |
| `llms.txt` | Коротка discovery-карта | public | https://gg-pdr.pl/llms.txt |
| `llms-full.txt` | Розширений польський knowledge document | public | https://gg-pdr.pl/llms-full.txt |
| `ai/about.md` | Entity, PDR, фактична географія | public | https://gg-pdr.pl/ai/about.md |
| `ai/contact.md` | Контакти та офіційні профілі | public | https://gg-pdr.pl/ai/contact.md |
| `ai/faq.md` | 10 видимих PL FAQ | public | https://gg-pdr.pl/ai/faq.md |
| `ai/pdr.md` | Метод, оцінка, переваги й обмеження | public | https://gg-pdr.pl/ai/pdr.md |
| `ai/realizacje.md` | Індекс підтверджених робіт | public | https://gg-pdr.pl/ai/realizacje.md |
| `ai/services.md` | Послуги, проблеми, рішення та кейси | public | https://gg-pdr.pl/ai/services.md |
| `realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.md` | Фактичний case document PL | public | https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.md |
| `realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.md` | Фактичний case document PL | public | https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.md |
| `realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.md` | Фактичний case document PL | public | https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.md |
| `ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.md` | Фактичний case document RU | public | https://gg-pdr.pl/ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.md |
| `ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.md` | Фактичний case document RU | public | https://gg-pdr.pl/ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.md |
| `ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.md` | Фактичний case document RU | public | https://gg-pdr.pl/ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.md |
| `scripts/build-ai-search.py` | AI генератор | internal | — |
| `scripts/check-ai-search.py` | AI/SEO перевірки | internal | — |
| `scripts/site_content.py` | HTML parser | internal | — |
| `scripts/build-site.py` | Єдина build-команда | internal | — |
| `docs/ai-search-architecture.md` | Архітектура та додавання кейсів | internal | — |
| `docs/ai-search-report.md` | Цей повний звіт | internal | — |
| `docs/ai-search-validation.json` | Результати перевірок | internal | — |
| `docs/laser-tech-service-search-inventory.json` | Inventory референсу | internal | — |
| `docs/gloss-garage-search-inventory.json` | Початковий inventory GG | internal | — |
| `README.md` | Інструкція розробнику | internal | — |

`_headers` і `_redirects` — конфігурація Netlify, не landing pages. `404.html` — технічна noindex сторінка. Для `/docs/*`, `/scripts/*`, `/README.md` налаштовані примусові HTTP 404: внутрішня документація не повинна віддаватися як публічний контент після застосування правил на Netlify. Це ще не live-перевірка правил.

## AI FILES UPDATED

Раніше AI knowledge files не було; їх створено. Оновлені пов'язані файли:

| File | Changes |
| --- | --- |
| `index.html`, `ru/index.html` | Видимі PDR пояснення, 10 FAQ на мову, service → case links, семантичний address, discovery і schema; фактичні розміри фото/OG |
| 8 HTML під `realizacje/`, `ru/realizacje/` | Website/business/service relationships, discovery, семантична адреса з shared footer; індексні descriptions більше не обмежені трьома назвами авто |
| `scripts/build-cases.py` | Автоматичні evidence links; актуальні image dimensions із manifest; не копіює homepage AI/schema в case head; стабільний sitemap rebuild |
| `scripts/check-cases.py` | Dynamic case counts, hreflang окремо від Markdown alternate, image dimensions, збереження форм; старе обмеження «PL homepage unchanged» замінено релевантними перевірками |
| `scripts/optimize-case-images.py` | Optional filename manifest для нових кейсів, збереження audit інших фотографій |
| `sitemap.xml` | Прибрано застарілі lastmod, стабілізовано формат; ті самі 10 canonical URLs |
| `styles/style.css` | Лише FAQ spacing та стиль address, що зберігає вигляд старого contact paragraph |
| `docs/cases-seo.json`, `docs/cases-validation.json` | Перегенеровано дані та результати перевірок |

## MARKDOWN KNOWLEDGE BASE

```text
ai/about.md
ai/contact.md
ai/faq.md
ai/pdr.md
ai/realizacje.md
ai/services.md
realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.md
realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.md
realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.md
ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.md
ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.md
ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.md
```

## LLMS

Фінальний `llms.txt`:

```markdown
# Gloss Garage

> Gloss Garage — profesjonalne usuwanie wgnieceń bez lakierowania metodą PDR we Wrocławiu i okolicach. PDR — Paintless Dent Repair / usuwanie wgnieceń bez lakierowania.

Adres: ul. Szkolna 55, Radwanice, Polska. Obszar obsługi: Wrocław i okolice.
Języki witryny: polski (główny) i rosyjski. Canonical website: https://gg-pdr.pl/.
Telefon: +48884012737. WhatsApp: https://wa.me/380667835184.
HTML pozostaje nadrzędnym źródłem; Markdown to uzupełniająca reprezentacja.

## Główne strony

- [Gloss Garage](https://gg-pdr.pl/)
- [Usługi PDR — wgniecenia parkingowe, po gradobiciu, trudne elementy](https://gg-pdr.pl/#pdr)
- [Realizacje](https://gg-pdr.pl/realizacje/)
- [Kontakt i wycena](https://gg-pdr.pl/#contact)
- [FAQ](https://gg-pdr.pl/#faq)
- [Русская версия](https://gg-pdr.pl/ru/)

## Realizacje

- [Audi A4 — prawy przedni błotnik bez lakierowania](https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/)
- [Toyota Corolla — naprawa prawych przednich drzwi PDR](https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/)
- [Volkswagen Tiguan — PDR prawego tylnego błotnika](https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/)

## Materiały AI-readable

- [Gloss Garage — PDR, Wrocław i okolice](https://gg-pdr.pl/ai/about.md)
- [Usługi Gloss Garage](https://gg-pdr.pl/ai/services.md)
- [PDR — Paintless Dent Repair](https://gg-pdr.pl/ai/pdr.md)
- [Pytania o naprawę PDR w Gloss Garage](https://gg-pdr.pl/ai/faq.md)
- [Kontakt — Gloss Garage](https://gg-pdr.pl/ai/contact.md)
- [Realizacje PDR — Gloss Garage](https://gg-pdr.pl/ai/realizacje.md)
- [Pełny dokument wiedzy](https://gg-pdr.pl/llms-full.txt)
```

Фінальний `llms-full.txt` наведено **повністю** наприкінці звіту, щоб не переривати аудит.

## SCHEMA

| Schema type | Page | Purpose |
| --- | --- | --- |
| AutoRepair | `/`, `/ru/` | Та сама компанія `/#business`, телефон, Radwanice, зона обслуговування, sameAs |
| LocalBusiness / Organization | Успадковані через AutoRepair | Не створено дубльованих company entities |
| WebSite | `/`, `/ru/` | Єдиний `/#website`, publisher Gloss Garage, мови сайту |
| WebPage | Усі 10 indexable HTML | Сторінка, мова, зв'язок із сайтом і бізнесом |
| Service | `/`, `/ru/` | PDR, provider, areaServed, subjectOf → документовані кейси |
| FAQPage / Question / Answer | `/`, `/ru/` | По 10 відповідей, тотожних видимому HTML |
| BreadcrumbList / ListItem | Обидва індекси + 6 кейсів | Home → Realizacje → автомобіль |
| ImageObject | Обидва індекси + 6 кейсів | primaryImageOfPage, реальні фото |
| PostalAddress / City / Place | В entity та service | Фактична адреса і географія |

12 JSON-LD script blocks; синтаксис, посилання identity та видимість FAQ перевірено. Не додавалися reviews, AggregateRating, ціни, години роботи, нагороди чи персонал. Це локальна semantic/syntax перевірка, не результат Google Rich Results Test.

## SEO

- Canonical: кожна з 10 indexable сторінок має один self-canonical з HTTPS і clean trailing slash; наявні публічні адреси перевірені HTTP GET — 200 без redirects.
- Hreflang: 5 reciprocal PL/RU пар; `x-default` дорівнює польській версії, HTML і sitemap узгоджені.
- Sitemap: 10 унікальних canonical HTML; Markdown, llms, developer docs та 404 виключено.
- Robots: `User-agent: *`, `Allow: /`, правильний Sitemap; файл не змінено, AI crawlers і assets не заблоковано.
- Metadata: унікальні title/description; OG URL, locale, alternate locale, image і Twitter поля перевірено. Головне OG зображення фактично 1731×909, metadata виправлено.
- Internal linking: головна/PDR → індекс і кейси; індекс → кейси; кейси → PDR/contact/index; мовні перемикачі та breadcrumbs збережено. Публічні документи мають абсолютні URL і source links.
- Image SEO: 40 WebP з описовими назвами, 4 responsive sizes, alt, dimensions, loading, decoding збережено; dimensions головних JPG виправлено. Фото не перейменовувалися і не замінювалися.
- Semantics: main/section/article/nav/header/footer уже використовувалися; address додано без зміни контактів. Основний текст та FAQ є в HTML, не завантажуються JavaScript.
- Existing analytics, form field structure, runtime JS та WhatsApp канали збережено. Жодних lead-form submissions не виконувалося.

Повний перелік canonical URLs і перевірених metadata до змін є в inventory; фінальна case metadata — `docs/cases-seo.json`, schema page mapping — `docs/ai-search-validation.json`.

## ENTITY

**Gloss Garage → надає PDR / Paintless Dent Repair → усуває вм'ятини без повторного лакування → обслуговує Wrocław і околиці → адреса ul. Szkolna 55, Radwanice.**

Телефон: +48 884 012 737. WhatsApp: +380 66 783 51 84. Це різні наявні канали, їх не уніфікували довільно. Instagram `https://www.instagram.com/pdr.glossgarage` і Facebook `https://www.facebook.com/people/PDR_Wroclaw/100094086760978/` підтверджені HTML та збережені в sameAs. Наявність PL/RU означає мови сайту, не непідтверджені мовні навички працівників.

## REALIZATIONS

| Vehicle | Problem | Solution | Canonical PL / RU |
| --- | --- | --- | --- |
| Audi A4 | Wgniecenie prawego przedniego błotnika | PDR без повторного лакування | [PL](https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/) / [RU](https://gg-pdr.pl/ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/) |
| Toyota Corolla | Wgniecenie prawych przednich drzwi | PDR без повторного лакування | [PL](https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/) / [RU](https://gg-pdr.pl/ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/) |
| Volkswagen Tiguan | Wgniecenie prawego tylnego błotnika | PDR без повторного лакування | [PL](https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/) / [RU](https://gg-pdr.pl/ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/) |

Для кожного доступні 2 HTML і 2 Markdown мовні версії. Факти про результат узяті з наявних кейсів; не додано дат, цін, тривалості чи непідтвердженого порядку «до/після».

## VALIDATION

| Перевірка | Результат |
| --- | --- |
| `build-ai-search.py --check` | 0 stale resources, 0 orphan resources |
| `check-ai-search.py --http` | 10 indexable HTML, 12 Markdown, 2 llms, 736 link occurrences, 36 case paragraphs, 78 локальних HTTP URL; 0 errors |
| `check-cases.py --http` | 8 case/index pages, 40 WebP, 70 локальних HTTP URL; 0 errors |
| Live canonical HTTP GET | Усі 10 URL: 200, redirects = 0; це перевірка існуючих сторінок, не нових неопублікованих файлів |
| Повторний повний build | Артефакти ідентичні; sitemap не накопичує порожні рядки |
| Майбутній четвертий кейс | В ізольованій копії `/tmp` перевірено новий slug, фото 16:9, PL/RU HTML/Markdown, cards, service links, llms, sitemap, headers; старий image audit збережено |
| `git diff --check` | Без помилок |
| Desktop/mobile browser QA | Не виконано: `cua.getState()` повернув порожній список browsers |
| Lighthouse/CWV, console, реальне currentSrc | Не виконано без браузера |
| Netlify `_headers`/`_redirects` після deploy | Не виконано: публікація заборонена завданням |

Тестовий четвертий кейс існував лише в тимчасовій копії, у робочому репозиторії залишаються три справжні кейси. Local `http.server` перевіряє доступність файлів, але не моделює Netlify routing/headers. Зовнішні social endpoints не перевірялися на володіння акаунтом: вони використані як уже підтверджені репозиторієм.

## PROBLEMS FOUND

1. Не було llms/Markdown discovery та maintenance workflow — створено.
2. PDR limitations і FAQ не були зібрані на головній — додано видимі PL/RU тексти.
3. Не вистачало явних WebSite/Service/FAQ relationships — додано зі спільними identity.
4. Неправильні dimensions головних фото та OG — виправлено за реальними файлами.
5. Lastmod головних залишався історичним і не підтримувався — прибрано без вигаданих дат.
6. Генератор sitemap накопичував whitespace; case template міг скопіювати homepage AI schema; валідатор припускав лише hreflang alternate і фіксовану кількість кейсів — виправлено.
7. Оптимізатор фото мав лише hardcoded originals, HTML — hardcoded пропорції — додано manifest і фактичні dimensions.
8. Developer docs/scripts могли віддаватися зі статичного кореня — додано обмежені Netlify 404 rules; публічний `/js/` не зачіпається.
9. Browser QA та live hosting rules залишаються неперевіреними до доступного браузера / дозволеної публікації.

## DATA NEEDED FROM OWNER

Для поточної реалізації блокувальних прогалин немає. Не вигадували та не додавали: публічний email, години роботи, postal code, підтверджений Google Business Profile URL, окремий logo image, сертифікації/стаж/нагороди, ширшу географію Dolny Śląsk. Їх можна додати лише після отримання фактичних даних.

Варто підтвердити чинність різних телефону/WhatsApp та наявного старого hero-твердження «naprawa od 30 min» / «ремонт от 30 мин». Воно було на сайті до завдання, збережене в дизайні, але не перетворене на обіцянку строків у новій knowledge base. Нові FAQ пояснюють, що строк залежить від оцінки пошкодження.

## FILES CHANGED

- `docs/cases-seo.json`
- `docs/cases-validation.json`
- `index.html`
- `realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.html`
- `realizacje/index.html`
- `realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.html`
- `realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.html`
- `ru/index.html`
- `ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.html`
- `ru/realizacje/index.html`
- `ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.html`
- `ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.html`
- `scripts/build-cases.py`
- `scripts/check-cases.py`
- `scripts/optimize-case-images.py`
- `sitemap.xml`
- `styles/style.css`

## FILES CREATED

- `.gitignore`
- `404.html`
- `README.md`
- `_headers`
- `_redirects`
- `ai/about.md`
- `ai/contact.md`
- `ai/faq.md`
- `ai/pdr.md`
- `ai/realizacje.md`
- `ai/services.md`
- `docs/ai-search-architecture.md`
- `docs/ai-search-report.md`
- `docs/ai-search-validation.json`
- `docs/gloss-garage-search-inventory.json`
- `docs/laser-tech-service-search-inventory.json`
- `llms-full.txt`
- `llms.txt`
- `realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.md`
- `realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.md`
- `realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.md`
- `ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.md`
- `ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.md`
- `ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.md`
- `scripts/build-ai-search.py`
- `scripts/build-site.py`
- `scripts/check-ai-search.py`
- `scripts/site_content.py`

## FILES REMOVED

Жодного. Вихідні зображення, робочі сторінки, інтеграції та файли референсного репозиторію не видалялися. `.gitignore` лише виключає Python bytecode/cache з переліку Git-змін.

## MAINTENANCE

`python3 scripts/build-site.py` запускає cases → AI → validation. Деталі й приклад manifest: `docs/ai-search-architecture.md`; короткий workflow: `README.md`. Генератор оновлює всю структуру при додаванні реального кейсу; ручне редагування generated outputs не потрібне.

## SOURCES AND PUBLICATION

[Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features): SEO fundamentals залишаються основою, спеціальні AI-файли не є вимогою чи гарантією потрапляння у відповіді. [llms.txt](https://llmstxt.org/) — додаткова discovery convention. [Schema.org AutoRepair](https://schema.org/AutoRepair) — тип чинної entity. [Netlify redirects](https://docs.netlify.com/manage/routing/redirects/redirect-options/) — конфігурація внутрішніх 404 rules.

**Commit: ні. Push: ні. Deploy: ні.** Код і звіт готові до локального перегляду; браузерна перевірка та перевірка заголовків після дозволеної публікації залишаються окремими кроками.

## LLMS-FULL — COMPLETE FINAL CONTENT

```markdown
# Gloss Garage — pełny dokument wiedzy

Polski jest językiem głównym. HTML pozostaje źródłem nadrzędnym.

# Gloss Garage — PDR, Wrocław i okolice

Źródło HTML: [Gloss Garage — PDR, Wrocław i okolice](https://gg-pdr.pl/)

Język: Polski. HTML jest źródłem nadrzędnym.

Gloss Garage — profesjonalne usuwanie wgnieceń bez lakierowania metodą PDR we Wrocławiu i okolicach.

PDR — Paintless Dent Repair / usuwanie wgnieceń bez lakierowania.

Firma: Gloss Garage

Witryna: [https://gg-pdr.pl/](https://gg-pdr.pl/)

Adres: ul. Szkolna 55, Radwanice, Polska.

Obszar obsługi: Wrocław i okolice. Adres warsztatu znajduje się w Radwanicach.

Telefon: [+48884012737](tel:+48884012737)

WhatsApp: [https://wa.me/380667835184](https://wa.me/380667835184)

Języki witryny: polski (główny), rosyjski (alternatywny).

- [Instagram](https://www.instagram.com/pdr.glossgarage)
- [Facebook](https://www.facebook.com/people/PDR_Wroclaw/100094086760978/)

[Formularz kontaktowy i wycena ze zdjęć](https://gg-pdr.pl/#contact).

[Usługi PDR](https://gg-pdr.pl/#pdr) · [Wykonane naprawy](https://gg-pdr.pl/realizacje/)


# Usługi Gloss Garage

Źródło HTML: [Usługi Gloss Garage](https://gg-pdr.pl/#pdr)

Język: Polski. HTML jest źródłem nadrzędnym.

Metoda wszystkich poniższych napraw: PDR (Paintless Dent Repair). Obszar: Wrocław i okolice.

## Drobne wgniecenia

Usuwamy wgniecenia parkingowe, uszkodzenia drzwi oraz niewielkie deformacje karoserii powstałe w wyniku drobnych uderzeń.

Rozwiązanie: usunięcie wgniecenia metodą PDR, po ocenie możliwości naprawy. [Usługa i kontakt](https://gg-pdr.pl/#pdr).

## Wgniecenia po gradobiciu

Naprawiamy maski, dachy, drzwi, błotniki oraz inne elementy karoserii uszkodzone podczas gradobicia.

Rozwiązanie: usunięcie wgniecenia metodą PDR, po ocenie możliwości naprawy. [Usługa i kontakt](https://gg-pdr.pl/#pdr).

## Trudne elementy

Pracujemy również z przetłoczeniami, błotnikami i miejscami o utrudnionym dostępie od wewnętrznej strony karoserii.

Rozwiązanie: usunięcie wgniecenia metodą PDR, po ocenie możliwości naprawy. [Usługa i kontakt](https://gg-pdr.pl/#pdr).

## Udokumentowane przykłady

- [Audi A4 — prawy przedni błotnik bez lakierowania](https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/)
- [Toyota Corolla — naprawa prawych przednich drzwi PDR](https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/)
- [Volkswagen Tiguan — PDR prawego tylnego błotnika](https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/)


# PDR — Paintless Dent Repair

Źródło HTML: [PDR — Paintless Dent Repair](https://gg-pdr.pl/#pdr)

Język: Polski. HTML jest źródłem nadrzędnym.

Specjalizacja

## Naprawa PDR bez lakierowania

Specjalizujemy się w usuwaniu wgnieceń bez konieczności szpachlowania i lakierowania. Technologia PDR pozwala zachować oryginalną powłokę lakierniczą samochodu, jego wygląd oraz wartość rynkową.

PDR polega na przywracaniu kształtu samej blachy. Odbicia linii lampy lub tablicy kontrolnej pomagają ocenić geometrię powierzchni. Stan lakieru, położenie i charakter deformacji decydują o możliwości naprawy; PDR nie zastępuje naprawy pękniętej powłoki lakierniczej.

Przykłady napraw: [Audi A4](https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/) , [Toyota Corolla](https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/) , [Volkswagen Tiguan](https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/) .

## Ocena, korzyści i ograniczenia

### Co to jest PDR?

PDR (Paintless Dent Repair) to usuwanie wgnieceń z karoserii bez szpachlowania i ponownego lakierowania. Metoda przywraca kształt blachy i pozwala zachować istniejącą powłokę lakierniczą.

### Czy można usunąć wgniecenie bez lakierowania?

Tak, jeśli stan lakieru, charakter i położenie wgniecenia pozwalają zastosować PDR. Możliwość naprawy oceniamy dla konkretnego uszkodzenia.

### Ile trwa naprawa PDR?

Czas zależy od uszkodzenia i zakresu prac. Ustalamy go po ocenie wgniecenia; nie każde uszkodzenie wymaga takiej samej pracy.

### Czy każde wgniecenie można naprawić metodą PDR?

Nie. Pęknięcia lakieru, charakter deformacji lub utrudniony dostęp mogą ograniczać zastosowanie PDR. Metoda nie naprawia uszkodzonej powłoki lakierniczej. Ostateczny dobór sposobu naprawy wymaga oględzin.

### Czy lakier pozostaje oryginalny?

Naprawa PDR nie wymaga nakładania nowego lakieru. Jeśli element ma fabryczną powłokę i kwalifikuje się do tej metody, można ją zachować.


# Pytania o naprawę PDR w Gloss Garage

Źródło HTML: [Pytania o naprawę PDR w Gloss Garage](https://gg-pdr.pl/#faq)

Język: Polski. HTML jest źródłem nadrzędnym.

## Co to jest PDR?

PDR (Paintless Dent Repair) to usuwanie wgnieceń z karoserii bez szpachlowania i ponownego lakierowania. Metoda przywraca kształt blachy i pozwala zachować istniejącą powłokę lakierniczą.

## Czy można usunąć wgniecenie bez lakierowania?

Tak, jeśli stan lakieru, charakter i położenie wgniecenia pozwalają zastosować PDR. Możliwość naprawy oceniamy dla konkretnego uszkodzenia.

## Ile trwa naprawa PDR?

Czas zależy od uszkodzenia i zakresu prac. Ustalamy go po ocenie wgniecenia; nie każde uszkodzenie wymaga takiej samej pracy.

## Czy każde wgniecenie można naprawić metodą PDR?

Nie. Pęknięcia lakieru, charakter deformacji lub utrudniony dostęp mogą ograniczać zastosowanie PDR. Metoda nie naprawia uszkodzonej powłoki lakierniczej. Ostateczny dobór sposobu naprawy wymaga oględzin.

## Czy lakier pozostaje oryginalny?

Naprawa PDR nie wymaga nakładania nowego lakieru. Jeśli element ma fabryczną powłokę i kwalifikuje się do tej metody, można ją zachować.

## Czy można naprawić wgniecenie na drzwiach?

Tak, zależnie od stanu konkretnego elementu. W naszych realizacjach pokazujemy naprawę prawych przednich drzwi Toyoty Corolli metodą PDR.

## Czy można naprawić błotnik?

Tak, jeśli uszkodzenie kwalifikuje się do PDR. Przykłady Gloss Garage to prawy przedni błotnik Audi A4 i prawy tylny błotnik Volkswagena Tiguana.

## Czy naprawiacie wgniecenia po gradobiciu?

Tak. Oferta obejmuje wgniecenia po gradobiciu na maskach, dachach, drzwiach, błotnikach i innych elementach karoserii. Każde uszkodzenie wymaga oceny.

## Jak wycenić naprawę i czy można wysłać zdjęcie?

Wyślij kilka zdjęć wgniecenia z różnych perspektyw przez WhatsApp lub opisz uszkodzenie w formularzu kontaktowym. Zdjęcia pozwalają na wstępną ocenę; ostateczny dobór metody wymaga oględzin.

## Gdzie znajduje się Gloss Garage?

Adres Gloss Garage to ul. Szkolna 55, Radwanice. Obsługujemy Wrocław i okolice. Telefon: +48 884 012 737; WhatsApp: +380 66 783 51 84.


# Kontakt — Gloss Garage

Źródło HTML: [Kontakt — Gloss Garage](https://gg-pdr.pl/#contact)

Język: Polski. HTML jest źródłem nadrzędnym.

Firma: Gloss Garage

Witryna: [https://gg-pdr.pl/](https://gg-pdr.pl/)

Adres: ul. Szkolna 55, Radwanice, Polska.

Obszar obsługi: Wrocław i okolice. Adres warsztatu znajduje się w Radwanicach.

Telefon: [+48884012737](tel:+48884012737)

WhatsApp: [https://wa.me/380667835184](https://wa.me/380667835184)

Języki witryny: polski (główny), rosyjski (alternatywny).

- [Instagram](https://www.instagram.com/pdr.glossgarage)
- [Facebook](https://www.facebook.com/people/PDR_Wroclaw/100094086760978/)

[Formularz kontaktowy i wycena ze zdjęć](https://gg-pdr.pl/#contact).


# Realizacje PDR — Gloss Garage

Źródło HTML: [Realizacje PDR — Gloss Garage](https://gg-pdr.pl/realizacje/)

Język: Polski. HTML jest źródłem nadrzędnym.

Gloss Garage wykonuje naprawy PDR we Wrocławiu i okolicach. Poniżej udokumentowane realizacje; zdjęcia nie są oznaczone jako porównania przed i po.

## Audi A4

Problem: Wgniecenie prawego przedniego błotnika.

Rozwiązanie: naprawa metodą PDR bez ponownego lakierowania.

[Pełny opis HTML](https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/) · [Markdown](https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.md) · [Русский](https://gg-pdr.pl/ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/).

## Toyota Corolla

Problem: Wgniecenie prawych przednich drzwi.

Rozwiązanie: naprawa metodą PDR bez ponownego lakierowania.

[Pełny opis HTML](https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/) · [Markdown](https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.md) · [Русский](https://gg-pdr.pl/ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/).

## Volkswagen Tiguan

Problem: Wgniecenie prawego tylnego błotnika.

Rozwiązanie: naprawa metodą PDR bez ponownego lakierowania.

[Pełny opis HTML](https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/) · [Markdown](https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.md) · [Русский](https://gg-pdr.pl/ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/).


# Audi A4 — prawy przedni błotnik bez lakierowania

Źródło HTML: [Audi A4 — prawy przedni błotnik bez lakierowania](https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/)

Język: Polski. HTML jest źródłem nadrzędnym.

- Samochód: Audi A4
- Uszkodzenie / element karoserii: Wgniecenie prawego przedniego błotnika
- Metoda: PDR — Paintless Dent Repair
- Wykonawca: Gloss Garage

W czarnym Audi A4 usunęliśmy wgniecenie na prawym przednim błotniku metodą PDR. Naprawa w Gloss Garage pozwoliła przywrócić kształt powierzchni bez klasycznego szpachlowania i lakierowania.

## Problem: wgniecenie przedniego błotnika

Uszkodzenie znajdowało się na prawym przednim błotniku, przy przednim kole. Na czarnym lakierze odbicia otoczenia oraz linii tablicy kontrolnej uwidaczniają zmiany kształtu powierzchni. Zdjęcia pokazują ten sam obszar z kilku perspektyw.

## Co zrobiliśmy w Gloss Garage

Usunęliśmy wgniecenie metodą PDR, odtwarzając geometrię blachy bez nakładania nowej warstwy lakieru. Zachowane pokrycie lakiernicze umożliwiło naprawę bez przechodzenia do klasycznego procesu blacharsko-lakierniczego.

## Dlaczego PDR był odpowiednim rozwiązaniem

Podobne wgniecenia często można naprawić bez lakierowania, jeśli powłoka nie jest uszkodzona, a charakter i położenie deformacji pozwalają na pracę PDR. Celem jest przywrócenie kształtu samej blachy, a nie wyrównanie powierzchni warstwą szpachli.

## PDR czy szpachlowanie i lakierowanie?

Zachowanie fabrycznej farby oznacza brak potrzeby dobierania nowego odcienia i mniejszą ingerencję w oryginalne wykończenie błotnika. W wielu przypadkach ograniczenie zakresu prac może oznaczać niższy koszt i krótszy czas naprawy. Nie jest to jednak reguła: wybór metody wymaga oceny konkretnego uszkodzenia.

## Rezultat naprawy

Wgniecenie zostało usunięte bez ponownego lakierowania błotnika. Galeria dokumentuje powierzchnię i jej odbicia z różnych kątów. Nie traktujemy tych ujęć jako porównania „przed i po”, ponieważ nie mamy potwierdzonej kolejności wykonania zdjęć.

## Zdjęcia

![Prawy przedni błotnik czarnego Audi A4 z odbiciem tablicy kontrolnej PDR przy reflektorze](https://gg-pdr.pl/images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-540.webp)

Prawy przedni błotnik czarnego Audi A4 z odbiciem tablicy kontrolnej PDR przy reflektorze

![Zbliżenie odbicia linii tablicy PDR na prawym przednim błotniku Audi A4](https://gg-pdr.pl/images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-02-540.webp)

Zbliżenie odbicia linii tablicy PDR na prawym przednim błotniku Audi A4

![Krawędź prawego przedniego błotnika Audi A4 przy kole i połączeniu ze zderzakiem](https://gg-pdr.pl/images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-03-540.webp)

Krawędź prawego przedniego błotnika Audi A4 przy kole i połączeniu ze zderzakiem

![Prawy przedni błotnik Audi A4 nad kołem, widok z niskiej perspektywy](https://gg-pdr.pl/images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-04-540.webp)

Prawy przedni błotnik Audi A4 nad kołem, widok z niskiej perspektywy

[Usługi PDR](https://gg-pdr.pl/#pdr) · [Kontakt](https://gg-pdr.pl/#contact)


# Toyota Corolla — naprawa prawych przednich drzwi PDR

Źródło HTML: [Toyota Corolla — naprawa prawych przednich drzwi PDR](https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/)

Język: Polski. HTML jest źródłem nadrzędnym.

- Samochód: Toyota Corolla
- Uszkodzenie / element karoserii: Wgniecenie prawych przednich drzwi
- Metoda: PDR — Paintless Dent Repair
- Wykonawca: Gloss Garage

Biała Toyota Corolla trafiła do Gloss Garage z wgnieceniem na prawych przednich drzwiach. Wykonaliśmy naprawę metodą PDR. Zdjęcia z lampą pokazują, jak można oceniać geometrię powierzchni podczas takiej pracy.

## Problem: wgniecenie drzwi

Uszkodzenie znajdowało się na prawych przednich drzwiach, poniżej lusterka. Na jasnym lakierze drobne nierówności nie zawsze są wyraźne w zwykłym świetle. Dlatego istotna jest obserwacja odbicia uporządkowanych pasów światła.

## Naprawa i kontrola lampą PDR

Wgniecenie usunęliśmy metodą PDR. Specjalna lampa tworzy na lakierze jasne pasy: ich załamania i zmiany szerokości pomagają dostrzec zagłębienia oraz niewielkie różnice poziomu blachy. Dzięki temu specjalista PDR może kontrolować kształt powierzchni dokładniej niż przy samym oświetleniu ogólnym.

## Dlaczego warto zachować fabryczny lakier

Jeżeli stan powłoki i charakter wgniecenia na to pozwalają, drzwi nie wymagają szpachlowania i ponownego lakierowania. PDR jest szczególnie interesujący dla właściciela, który chce zachować możliwie dużo oryginalnego wykończenia samochodu.

## Kiedy rozważyć klasyczne lakierowanie

PDR nie zastępuje naprawy uszkodzonej powłoki. Pęknięcia lakieru lub charakter deformacji mogą wymagać innego rozwiązania. Ocena przed rozpoczęciem prac pozwala dobrać metodę zamiast automatycznie kierować drzwi do szpachlowania i malowania.

## Rezultat i dokumentacja

Wykonaliśmy naprawę wgniecenia bez ponownego lakierowania drzwi. Dwa ujęcia z lampą ilustrują kontrolę geometrii powierzchni; nie przypisujemy im niepotwierdzonych etykiet „przed” i „po”.

## Zdjęcia

![Prawe przednie drzwi białej Toyoty Corolli z odbiciem pasów lampy PDR poniżej lusterka](https://gg-pdr.pl/images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-540.webp)

Prawe przednie drzwi białej Toyoty Corolli z odbiciem pasów lampy PDR poniżej lusterka

![Zbliżenie prawych przednich drzwi Toyoty Corolli z załamaniem odbicia światła lampy PDR](https://gg-pdr.pl/images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-02-540.webp)

Zbliżenie prawych przednich drzwi Toyoty Corolli z załamaniem odbicia światła lampy PDR

[Usługi PDR](https://gg-pdr.pl/#pdr) · [Kontakt](https://gg-pdr.pl/#contact)


# Volkswagen Tiguan — PDR prawego tylnego błotnika

Źródło HTML: [Volkswagen Tiguan — PDR prawego tylnego błotnika](https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/)

Język: Polski. HTML jest źródłem nadrzędnym.

- Samochód: Volkswagen Tiguan
- Uszkodzenie / element karoserii: Wgniecenie prawego tylnego błotnika
- Metoda: PDR — Paintless Dent Repair
- Wykonawca: Gloss Garage

W ciemnoszarym Volkswagenie Tiguanie usunęliśmy wgniecenie na prawym tylnym błotniku. Technologia PDR pozwoliła naprawić element bez szpachli i ponownego lakierowania.

## Uszkodzenie przy tylnym nadkolu

Wgniecenie dotyczyło prawego tylnego błotnika. Zdjęcia pokazują obszar pomiędzy tylną lampą, klapką wlewu paliwa i nadkolem. Odbicia oświetlenia oraz otoczenia pomagają obserwować przebieg powierzchni z różnych kątów.

## Naprawa metodą PDR

Gloss Garage usunął wgniecenie, przywracając geometrię panelu bez pokrywania go szpachlą i nowym lakierem. W tej realizacji zachowaliśmy oryginalną powłokę lakierniczą.

## Dlaczego tylny błotnik wymaga uwagi

Tylny błotnik jest częścią nadwozia, której klasyczna naprawa może oznaczać szerszą ingerencję w wykończenie niż samo usunięcie deformacji. Jeśli powłoka jest zachowana, warto sprawdzić możliwość PDR przed podjęciem decyzji o lakierowaniu.

## PDR a naprawa blacharsko-lakiernicza

Przy odpowiednim rodzaju uszkodzenia PDR pozwala uniknąć szpachlowania oraz dobierania koloru nowej farby. Zachowanie fabrycznego lakieru ogranicza zakres ingerencji, ale możliwość takiej naprawy zależy od położenia i charakteru wgniecenia. Nie każde uszkodzenie nadaje się do tej metody.

## Rezultat: odtworzony kształt panelu

Wgniecenie zostało usunięte technologią PDR bez ponownego lakierowania. Prawidłowy przebieg powierzchni ma znaczenie zwłaszcza przy przetłoczeniach i nadkolu. Galeria przedstawia kilka ujęć naprawianego obszaru, bez niepotwierdzonego podziału na zdjęcia „przed i po”.

## Zdjęcia

![Prawy tylny błotnik szarego Volkswagena Tiguana między lampą, klapką wlewu i nadkolem](https://gg-pdr.pl/images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-540.webp)

Prawy tylny błotnik szarego Volkswagena Tiguana między lampą, klapką wlewu i nadkolem

![Prawy tylny błotnik Volkswagena Tiguana widziany z dołu od strony tylnej lampy](https://gg-pdr.pl/images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-540.webp)

Prawy tylny błotnik Volkswagena Tiguana widziany z dołu od strony tylnej lampy

![Widok wzdłuż prawego boku Volkswagena Tiguana z odbiciami na tylnym błotniku](https://gg-pdr.pl/images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-540.webp)

Widok wzdłuż prawego boku Volkswagena Tiguana z odbiciami na tylnym błotniku

![Prawy tylny błotnik Volkswagena Tiguana nad kołem, widok ukośny przy tylnej lampie](https://gg-pdr.pl/images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-540.webp)

Prawy tylny błotnik Volkswagena Tiguana nad kołem, widok ukośny przy tylnej lampie

[Usługi PDR](https://gg-pdr.pl/#pdr) · [Kontakt](https://gg-pdr.pl/#contact)
```
