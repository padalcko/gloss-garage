# Gloss Garage — звіт про розділ реалізацій

Дата: 2026-10-05. Репозиторій: `gloss-garage`. Локальна реалізація готова; браузерний приймальний аудит залишається невиконаним через відсутність підключених браузерів. Commit, push і deploy не виконувалися.

## Початковий аудит репозиторію

- До змін: тільки `index.html` і `ru/index.html`; обидва файли були ідентичні. Мовні маршрути `/` і `/ru/` підтверджені перемикачем, sitemap та словником повідомлень форми у JS. Інших мов немає.
- URL: каталоги з `index.html`, публічні адреси зі слешем, без `.html`. Нові сторінки продовжують цю структуру; конфігурації редиректів або хостингу в репозиторії немає.
- Header: sticky, логотип GG, social links, PL/RU, телефон. Класичної desktop navigation, burger menu та JS для меню немає. На mobile — фіксована панель із телефоном, WhatsApp, оцінкою й Instagram.
- Реалізації до змін — лише секція `.gallery` із чотирма фото на головній. Окремих кейсів, індексу, lightbox чи carousel не було. Новий індекс доступний за кнопкою в цій секції обох головних; header і мобільна контактна панель збережені.
- Послуги й контакти — секції головної, не окремі URL. Доданий `id="pdr"`; чинний `#contact` збережений.
- CSS: один `styles/style.css`, без framework. Inter 400/500/700/800/900 через Google Fonts, Font Awesome 6.5.1 через CDN. Нові сторінки використовують ці підключення по одному разу.
- Кольори: red `#e30613`, black `#070707`, dark `#111111`, white `#ffffff`, light `#f4f6f8`, text `#111827`, muted `#64748b`, border `#e5e7eb`.
- Контейнер: максимум 1180 px; поля 14 px на mobile, 16 px вище 620 px. Чинні межі: 620 і 980 px. Нове розширення сіток: `min-width:621px` і `min-width:981px`, без нових довільних breakpoints.
- Стиль: uppercase жирні заголовки, прямокутні картки з червоним верхнім бордером 5 px, тінь `0 20px 45px rgba(15,23,42,.06)`. Кнопки black/red/outline з чинними padding і тінями. Радіуси: language switcher 30 px, mobile nav 24 px, її елементи 18 px. Нової дизайн-системи немає.
- Відступи вихідного сайту: секції 72/96 px, grid gap 28 px, галерея 16 px, контактні колонки 64 px. Для нових сторінок базові mobile-відступи 48 px, далі 72/96 px; галерея 28 px для читабельних підписів.
- JS: тільки `js/script.js`, форма надсилає JSON до чинного n8n webhook. На нових сторінках форми немає, тому цей JS не підключається. Код форми не змінено.
- Контакти: `tel:+48884012737`, `https://wa.me/380667835184`, Radwanice, ul. Szkolna 55; Instagram `https://www.instagram.com/pdr.glossgarage`; Facebook `https://www.facebook.com/people/PDR_Wroclaw/100094086760978/`. Усе взято з репозиторію.
- Географія: Wrocław і околиці, майстерня в Radwanice. Нова локальна згадка природно подана у вступах, без повторення міста в кожному абзаці.
- SEO до змін: canonical, pl/ru/x-default, OG і Twitter, AutoRepair `https://gg-pdr.pl/#business`, без BreadcrumbList. RU помилково мала lang=pl і canonical PL — тепер виправлено за додатковим запитом користувача.
- Analytics: GA4 `G-GPXSKXM487` через gtag; окремого GTM-container немає. GA4 збережений на головних і доданий рівно один раз на кожній новій сторінці.
- robots.txt дозволяє індексацію й указує sitemap. Sitemap мав 2 записи з xhtml-alternates; тепер 10. Чинні записи й lastmod збережені, вигадані дати кейсів не додані.
- Вихідні зображення: JPEG/PNG, без srcset; фото головної lazy, hero — CSS background. Усі нові фото — WebP із srcset, dimensions, async decoding. AVIF не додано: попередньої AVIF-архітектури немає.

### Наявні assets до змін

| Файл | Розміри | Байт |
|---|---:|---:|
| `images/gloss-garage-usuwanie-wgniecen-gradobicie-1.jpg` | 1508×965 | 48836 |
| `images/gloss-garage-usuwanie-wgniecen-gradobicie-2.jpg` | 800×500 | 78135 |
| `images/gloss-garage-usuwanie-wgniecen-gradobicie-3.jpg` | 542×656 | 30142 |
| `images/gloss-garage-usuwanie-wgniecen-gradobicie-4.jpg` | 1008×756 | 83290 |
| `images/gloss-garage-usuwanie-wgniecen-gradobicie-5.jpg` | 1422×800 | 71141 |
| `images/gloss-garage-usuwanie-wgniecen-gradobicie-6.jpg` | 480×270 | 7756 |
| `images/gloss-garage-usuwanie-wgniecen-gradobicie-7.jpg` | 1707×2560 | 534104 |
| `images/gloss-garage-usuwanie-wgniecen-gradobicie.jpg` | 1000×667 | 606997 |
| `images/hero-img.png` | 1694×928 | 1936152 |
| `images/og-image.jpg` | 1731×909 | 1868061 |

## A. Created files

- `docs/cases-seo.json`
- `docs/cases-validation.json`
- `docs/image-audit.json`
- `docs/realizacje-report.md`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-1086.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-360.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-540.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-768.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-02-1086.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-02-360.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-02-540.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-02-768.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-03-1086.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-03-360.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-03-540.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-03-768.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-04-1086.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-04-360.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-04-540.webp`
- `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-04-768.webp`
- `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-1086.webp`
- `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-360.webp`
- `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-540.webp`
- `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-768.webp`
- `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-02-1086.webp`
- `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-02-360.webp`
- `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-02-540.webp`
- `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-02-768.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-1086.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-360.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-540.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-768.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-1086.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-360.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-540.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-768.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-1086.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-360.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-540.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-768.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-1086.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-360.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-540.webp`
- `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-768.webp`
- `realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.html`
- `realizacje/index.html`
- `realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.html`
- `realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.html`
- `ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/index.html`
- `ru/realizacje/index.html`
- `ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/index.html`
- `ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/index.html`
- `scripts/build-cases.py`
- `scripts/cases-content.json`
- `scripts/check-cases.py`
- `scripts/optimize-case-images.py`
- `styles/cases.css`
- `styles/ru.css`

## B. Modified files

- `index.html` — якір послуг і кнопка до індексу кейсів у чинній галереї.
- `ru/index.html` — російський переклад, lang/canonical/OG/Twitter, активний RU, локалізовані aria/alt/поля форми; посилання на кейси та якір послуг.
- `sitemap.xml` — 8 нових URL із мовними альтернативами.

`.vscode/settings.json` змінено користувачем під час роботи; цей файл не редагувався агентом і не належить до реалізації. `styles/style.css`, `js/script.js`, `robots.txt` залишилися побайтово незмінними від HEAD.

## C–D. New URLs and languages

Повні адреси для майбутнього розгортання (live-доступність нових сторінок не заявляється):

### PL

- https://gg-pdr.pl/realizacje/
- https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/
- https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/
- https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/

### RU

- https://gg-pdr.pl/ru/realizacje/
- https://gg-pdr.pl/ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/
- https://gg-pdr.pl/ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/
- https://gg-pdr.pl/ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/

## E. SEO

Кожен кейс має один H1, унікальні title/description, self-canonical, взаємні pl/ru/x-default, OG і Twitter. JSON-LD: WebPage + BreadcrumbList, посилання на чинний `#business`; без дублювання AutoRepair, рейтингів, цін або дат публікації.

### https://gg-pdr.pl/realizacje/

- Title: Realizacje PDR we Wrocławiu — zdjęcia napraw | Gloss Garage
- Meta description: Audi A4, Toyota Corolla i Volkswagen Tiguan: rzeczywiste naprawy PDR w Gloss Garage. Zobacz usuwanie wgnieceń z drzwi i błotników bez lakierowania.
- Canonical: https://gg-pdr.pl/realizacje/
- og:image: https://gg-pdr.pl/images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-1086.webp
- hreflang pl: https://gg-pdr.pl/realizacje/
- hreflang ru: https://gg-pdr.pl/ru/realizacje/
- hreflang x-default: https://gg-pdr.pl/realizacje/

### https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/

- Title: Audi A4 — naprawa prawego błotnika PDR | Gloss Garage
- Meta description: Wgniecenie na prawym przednim błotniku czarnego Audi A4 usunięte metodą PDR. Zdjęcia realizacji Gloss Garage i wyjaśnienie naprawy bez lakierowania.
- Canonical: https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/
- og:image: https://gg-pdr.pl/images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-1086.webp
- hreflang pl: https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/
- hreflang ru: https://gg-pdr.pl/ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/
- hreflang x-default: https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/

### https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/

- Title: Toyota Corolla — drzwi pod lampą PDR | Gloss Garage
- Meta description: Naprawa wgniecenia prawych przednich drzwi białej Toyoty Corolli w Gloss Garage. Zobacz, jak lampa PDR pomaga kontrolować geometrię powierzchni.
- Canonical: https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/
- og:image: https://gg-pdr.pl/images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-1086.webp
- hreflang pl: https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/
- hreflang ru: https://gg-pdr.pl/ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/
- hreflang x-default: https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/

### https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/

- Title: Volkswagen Tiguan — tylny błotnik bez szpachli | Gloss Garage
- Meta description: Usunięcie wgniecenia prawego tylnego błotnika ciemnoszarego Volkswagena Tiguana metodą PDR. Realizacja Gloss Garage z zachowaniem oryginalnego lakieru.
- Canonical: https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/
- og:image: https://gg-pdr.pl/images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-1086.webp
- hreflang pl: https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/
- hreflang ru: https://gg-pdr.pl/ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/
- hreflang x-default: https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/

### https://gg-pdr.pl/ru/realizacje/

- Title: Работы Gloss Garage — примеры ремонта PDR во Вроцлаве
- Meta description: Реальные работы Gloss Garage: Audi A4, Toyota Corolla и Volkswagen Tiguan. Фото удаления вмятин на дверях и крыльях методом PDR без покраски.
- Canonical: https://gg-pdr.pl/ru/realizacje/
- og:image: https://gg-pdr.pl/images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-1086.webp
- hreflang pl: https://gg-pdr.pl/realizacje/
- hreflang ru: https://gg-pdr.pl/ru/realizacje/
- hreflang x-default: https://gg-pdr.pl/realizacje/

### https://gg-pdr.pl/ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/

- Title: Audi A4: ремонт переднего крыла без покраски | Gloss Garage
- Meta description: Удаление вмятины на правом переднем крыле чёрного Audi A4 методом PDR в Gloss Garage. Фото работы и преимущества сохранения заводской краски.
- Canonical: https://gg-pdr.pl/ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/
- og:image: https://gg-pdr.pl/images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-1086.webp
- hreflang pl: https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/
- hreflang ru: https://gg-pdr.pl/ru/realizacje/audi-a4-pdr-przedni-prawy-blotnik/
- hreflang x-default: https://gg-pdr.pl/realizacje/audi-a4-pdr-przedni-prawy-blotnik/

### https://gg-pdr.pl/ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/

- Title: Toyota Corolla: контроль двери лампой PDR | Gloss Garage
- Meta description: Ремонт вмятины на правой передней двери белой Toyota Corolla. Фотографии Gloss Garage показывают контроль геометрии поверхности с помощью лампы PDR.
- Canonical: https://gg-pdr.pl/ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/
- og:image: https://gg-pdr.pl/images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-1086.webp
- hreflang pl: https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/
- hreflang ru: https://gg-pdr.pl/ru/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/
- hreflang x-default: https://gg-pdr.pl/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi/

### https://gg-pdr.pl/ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/

- Title: Volkswagen Tiguan: заднее крыло без шпаклёвки | Gloss Garage
- Meta description: Вмятина на правом заднем крыле тёмно-серого Volkswagen Tiguan удалена методом PDR. Фото ремонта Gloss Garage с сохранением оригинального покрытия.
- Canonical: https://gg-pdr.pl/ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/
- og:image: https://gg-pdr.pl/images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-1086.webp
- hreflang pl: https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/
- hreflang ru: https://gg-pdr.pl/ru/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/
- hreflang x-default: https://gg-pdr.pl/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik/

RU-головна: `lang=ru`, canonical/og:url `https://gg-pdr.pl/ru/`, og:locale `ru_RU`, активний RU; перемикач PL веде на `/`. Повідомлення форми тепер отримують російську мову через наявний JS. Структура полів, required, autocomplete, endpoint і назви полів не змінені.

## F. Image audit

Усі джерела: автентичні PNG 1086×1448. Розподіл за видимим вмістом та даними користувача: Tiguan — темно-сірий задній правий кузовний елемент із лючком пального; Corolla — білі праві передні двері під дзеркалом і лампа; Audi — чорний передній правий елемент біля фари/колеса. Самі фото не підтверджують модель незалежно від наданих користувачем даних. Позначення before/after не використані.

Таблиця порівнює оригінал із найбільшим production-варіантом. Усі додаткові варіанти включено окремо в загальний підсумок.

| Original file | Car | New file | Original dimensions | New dimensions | Original bytes | Optimized bytes | Format | Saving |
|---|---|---|---|---|---:|---:|---|---:|
| `18ED3312-F1C0-4D1A-872B-8C902340F66E.PNG` | Volkswagen Tiguan | `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-1086.webp` | 1086×1448 | 1086×1448 | 2958743 | 156660 | WebP | 94.71% |
| `ADF70FFF-A853-4FBC-B9B2-2F2A743376FB.PNG` | Volkswagen Tiguan | `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-1086.webp` | 1086×1448 | 1086×1448 | 3101870 | 148812 | WebP | 95.20% |
| `C30B8DB6-AEBB-4B01-B3BA-18FB1F45CE1B.PNG` | Volkswagen Tiguan | `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-1086.webp` | 1086×1448 | 1086×1448 | 3692519 | 321330 | WebP | 91.30% |
| `3FA86D0D-3D2D-4D70-9CDB-F4E3763DDB1B.PNG` | Volkswagen Tiguan | `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-1086.webp` | 1086×1448 | 1086×1448 | 3415897 | 193066 | WebP | 94.35% |
| `97DAB8BB-26C9-4FDB-A3BC-008419A1B07A.PNG` | Toyota Corolla | `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-1086.webp` | 1086×1448 | 1086×1448 | 2838529 | 98978 | WebP | 96.51% |
| `08D81894-BA01-4A30-AE20-D4973AC1C599.PNG` | Toyota Corolla | `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-02-1086.webp` | 1086×1448 | 1086×1448 | 1891347 | 96718 | WebP | 94.89% |
| `D3F01399-A227-49CB-9B55-0F953254F3C3.PNG` | Audi A4 | `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-1086.webp` | 1086×1448 | 1086×1448 | 3113585 | 454006 | WebP | 85.42% |
| `F4676386-C695-4DD1-AC3D-1AA886C434C7.PNG` | Audi A4 | `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-02-1086.webp` | 1086×1448 | 1086×1448 | 2913937 | 388884 | WebP | 86.65% |
| `A55F1895-C1D8-4394-ACC9-2F1ED21AC8C2.PNG` | Audi A4 | `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-03-1086.webp` | 1086×1448 | 1086×1448 | 2556756 | 272854 | WebP | 89.33% |
| `D41491B1-7010-40E6-B3B4-9332163C05FC.PNG` | Audi A4 | `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-04-1086.webp` | 1086×1448 | 1086×1448 | 2687639 | 304412 | WebP | 88.67% |

Оптимізація: EXIF orientation застосовується до пікселів, RGB, Lanczos resize, WebP quality=88/method=6. EXIF/GPS не передаються; усі 40 вихідних файлів перевірено — EXIF відсутній. Оригінали не копіювалися в production. Не застосовувалися AI, ретуш, підсилення різкості, HDR чи зміна геометрії.

Візуально переглянуто контактний аркуш усіх 10 WebP та центральні фрагменти найбільших варіантів у натуральному масштабі: відбиття та світлові лінії залишаються розбірливими. Це перевірка файлів зображень, не браузерного layout.

## G. Responsive images

| File | Dimensions | Bytes |
|---|---:|---:|
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-360.webp` | 360×480 | 27536 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-540.webp` | 540×720 | 51308 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-768.webp` | 768×1024 | 89736 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-1086.webp` | 1086×1448 | 156660 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-360.webp` | 360×480 | 31676 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-540.webp` | 540×720 | 57986 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-768.webp` | 768×1024 | 93684 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-1086.webp` | 1086×1448 | 148812 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-360.webp` | 360×480 | 50472 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-540.webp` | 540×720 | 100622 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-768.webp` | 768×1024 | 185296 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-1086.webp` | 1086×1448 | 321330 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-360.webp` | 360×480 | 38276 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-540.webp` | 540×720 | 71982 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-768.webp` | 768×1024 | 124360 |
| `images/realizacje/volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-1086.webp` | 1086×1448 | 193066 |
| `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-360.webp` | 360×480 | 22294 |
| `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-540.webp` | 540×720 | 38478 |
| `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-768.webp` | 768×1024 | 60068 |
| `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-01-1086.webp` | 1086×1448 | 98978 |
| `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-02-360.webp` | 360×480 | 22854 |
| `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-02-540.webp` | 540×720 | 39470 |
| `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-02-768.webp` | 768×1024 | 63674 |
| `images/realizacje/toyota-corolla-pdr-prawe-przednie-drzwi-02-1086.webp` | 1086×1448 | 96718 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-360.webp` | 360×480 | 79718 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-540.webp` | 540×720 | 157772 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-768.webp` | 768×1024 | 277884 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-01-1086.webp` | 1086×1448 | 454006 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-02-360.webp` | 360×480 | 78966 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-02-540.webp` | 540×720 | 149998 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-02-768.webp` | 768×1024 | 246210 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-02-1086.webp` | 1086×1448 | 388884 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-03-360.webp` | 360×480 | 52286 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-03-540.webp` | 540×720 | 98122 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-03-768.webp` | 768×1024 | 170330 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-03-1086.webp` | 1086×1448 | 272854 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-04-360.webp` | 360×480 | 54358 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-04-540.webp` | 540×720 | 106130 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-04-768.webp` | 768×1024 | 183308 |
| `images/realizacje/audi-a4-pdr-przedni-prawy-blotnik-04-1086.webp` | 1086×1448 | 304412 |

- Для кожного фото: 360×480, 540×720, 768×1024, 1086×1448. Без upscaling та непотрібних 1200/1600 px.
- `srcset` містить усі чотири ширини на кожному зображенні нових сторінок; fallback `src` — 540 px.
- Картки: перше фото кожного автомобіля. Окремих дубльованих thumbnail-файлів немає. Повний кадр 3:4 без обрізання; gallery використовує всі фото.
- Card sizes: `(min-width: 1212px) 329px, (min-width: 981px) calc((100vw - 226px) / 3), (min-width: 621px) calc((100vw - 152px) / 2), calc(100vw - 74px)`.
- Gallery sizes: `(min-width: 1212px) 576px, (min-width: 621px) calc((100vw - 60px) / 2), calc(100vw - 28px)`.
- 1212 px у sizes — точка насичення контейнера 1180+32, а не новий CSS breakpoint.
- Перший кадр сторінки eager, інші lazy; усі decoding=async і width/height=1086/1448. Немає preload і масових fetchpriority=high.
- Фактичний LCP-елемент не визначено без браузера. На першому екрані є текстовий вступ; перше фото не lazy на випадок участі в LCP. Не заявляємо, що саме фото є LCP.
- Вибір currentSrc на різних DPR не виміряний. На високому DPR браузер може обрати 768 або 1086 px; це очікувана поведінка srcset, а не примусове завантаження desktop-файлу.

## H. Total image saving

- TOTAL ORIGINAL IMAGE SIZE: **29,170,822 bytes / 29.17 MB**.
- TOTAL PRODUCTION IMAGE SIZE (усі 40 файлів): **5,260,574 bytes / 5.26 MB**.
- SAVED: **23.91 MB / 81.97%**.
- Найбільші 10 WebP окремо: 2,435,720 bytes / 2.44 MB; економія 91.65%.
- MB тут десяткові (1 MB = 1 000 000 bytes). Загальний production-обсяг — дисковий, а не вага одного відкриття сторінки: браузер вибирає один candidate для кожного фото.

## I. ALT table

ALT однаковий для різних ширин одного кадру; кожен кадр має власний опис. Позначення `-{width}` охоплює 360/540/768/1086.

| Filename | PL alt | RU alt |
|---|---|---|
| `volkswagen-tiguan-pdr-prawy-tylny-blotnik-01-{width}.webp` | Prawy tylny błotnik szarego Volkswagena Tiguana między lampą, klapką wlewu i nadkolem | Правое заднее крыло серого Volkswagen Tiguan между фонарём, лючком бака и аркой |
| `volkswagen-tiguan-pdr-prawy-tylny-blotnik-02-{width}.webp` | Prawy tylny błotnik Volkswagena Tiguana widziany z dołu od strony tylnej lampy | Правое заднее крыло Volkswagen Tiguan, вид снизу со стороны заднего фонаря |
| `volkswagen-tiguan-pdr-prawy-tylny-blotnik-03-{width}.webp` | Widok wzdłuż prawego boku Volkswagena Tiguana z odbiciami na tylnym błotniku | Вид вдоль правого борта Volkswagen Tiguan с отражениями на заднем крыле |
| `volkswagen-tiguan-pdr-prawy-tylny-blotnik-04-{width}.webp` | Prawy tylny błotnik Volkswagena Tiguana nad kołem, widok ukośny przy tylnej lampie | Правое заднее крыло Volkswagen Tiguan над колесом, ракурс рядом с задним фонарём |
| `toyota-corolla-pdr-prawe-przednie-drzwi-01-{width}.webp` | Prawe przednie drzwi białej Toyoty Corolli z odbiciem pasów lampy PDR poniżej lusterka | Правая передняя дверь белой Toyota Corolla с отражением полос лампы PDR под зеркалом |
| `toyota-corolla-pdr-prawe-przednie-drzwi-02-{width}.webp` | Zbliżenie prawych przednich drzwi Toyoty Corolli z załamaniem odbicia światła lampy PDR | Крупный план правой передней двери Toyota Corolla с изгибом отражения лампы PDR |
| `audi-a4-pdr-przedni-prawy-blotnik-01-{width}.webp` | Prawy przedni błotnik czarnego Audi A4 z odbiciem tablicy kontrolnej PDR przy reflektorze | Правое переднее крыло чёрного Audi A4 с отражением контрольного экрана PDR рядом с фарой |
| `audi-a4-pdr-przedni-prawy-blotnik-02-{width}.webp` | Zbliżenie odbicia linii tablicy PDR na prawym przednim błotniku Audi A4 | Крупный план отражения линий экрана PDR на правом переднем крыле Audi A4 |
| `audi-a4-pdr-przedni-prawy-blotnik-03-{width}.webp` | Krawędź prawego przedniego błotnika Audi A4 przy kole i połączeniu ze zderzakiem | Край правого переднего крыла Audi A4 у колеса и стыка с бампером |
| `audi-a4-pdr-przedni-prawy-blotnik-04-{width}.webp` | Prawy przedni błotnik Audi A4 nad kołem, widok z niskiej perspektywy | Правое переднее крыло Audi A4 над колесом, вид снизу |

## J. Sitemap

Додані всі 8 URL із розділів C–E. Для кожної пари мов: pl → польська сторінка, ru → відповідна російська сторінка, x-default → польська сторінка. Повний mapping наведено для кожної сторінки в E та в `docs/cases-seo.json`.

Перевірено весь sitemap: 10 унікальних URL, усі відповідають локальним index.html, self-canonical та HTML hreflang. Немає тестових URL, `.html` або відсутніх сторінок. Локальні HTTP-запити повертають 200 без редиректів. Production-редиректи/404 не перевірялися — змін ще не розгорнуто.

## K. Internal links

- PL/RU головна → відповідний індекс реалізацій (кнопка в наявній галереї).
- Індекс → Audi, Toyota, Volkswagen своєю мовою.
- Кейс → свій індекс, мовна головна, `#pdr`, `#contact`, чинний WhatsApp.
- Перемикач мови на кожній новій сторінці → точний мовний відповідник цього кейсу/індексу.
- Breadcrumbs: головна → реалізації → автомобіль; видимі та JSON-LD узгоджені.
- Header/footer/social/телефон/мобільна контактна панель взяті з відповідної головної.
- Блогу немає; штучних посилань не додано. Форми й зовнішні повідомлення не надсилалися.

## L. Mobile audit

Статичні правила перевірено, але **браузерний audit не виконаний**. `cua.getState()` повернув порожній список браузерів; спроби Chrome та IAB завершилися `Browser is not available`. Неможливо чесно підтвердити відсутність overflow, накладань чи console errors.

У всіх рядках нижче: header/cards/gallery/CTA/floating controls **не перевірені в рендері**. Числа — розрахунок CSS, не результат screenshot-тесту.

| Viewport | Cards columns | Gallery columns | Card image CSS px | Gallery image CSS px | Horizontal overflow / header / CTA / floating controls |
|---:|---:|---:|---:|---:|---|
| 320 | 1 | 1 | 246.0 | 292.0 | Не перевірено в браузері |
| 360 | 1 | 1 | 286.0 | 332.0 | Не перевірено в браузері |
| 375 | 1 | 1 | 301.0 | 347.0 | Не перевірено в браузері |
| 390 | 1 | 1 | 316.0 | 362.0 | Не перевірено в браузері |
| 430 | 1 | 1 | 356.0 | 402.0 | Не перевірено в браузері |
| 768 | 2 | 2 | 308.0 | 354.0 | Не перевірено в браузері |
| 1024 | 3 | 2 | 266.0 | 482.0 | Не перевірено в браузері |
| 1280 | 3 | 2 | 328.7 | 576.0 | Не перевірено в браузері |
| 1440 | 3 | 2 | 328.7 | 576.0 | Не перевірено в браузері |

Передбачено: minmax(0,1fr), перенесення H1/breadcrumbs/кнопок, max-width зображень, відсутність каруселі та горизонтального скролера. На mobile — одна колонка, повні кадри. Чинний відступ body/footer під fixed contact panel збережений. Це не замінює ручну перевірку перекриттів.

Доступність: один H1, секції H2, унікальні alt, семантичні a/nav/figure, breadcrumbs aria-current, назви посилань карток із моделлю, :focus-visible на нових сторінках, кнопки ≥48 px, мовні посилання ≥44 px заввишки. Фактичний keyboard/focus audit не проведений. Burger menu не існує — перевірка не застосовується.

## M. Performance and technical validation

- Статична перевірка: **10 HTML, 8 нових сторінок, 10 sitemap URL, 40 WebP; 0 помилок**.
- Локальна HTTP-перевірка: **61 URL/ресурсів**, усі 200 без редиректів. Результати: `docs/cases-validation.json`.
- Перевірені вкладеність HTML, H1, ID, локальні посилання/якорі, canonical, reciprocal hreflang, sitemap, JSON-LD, GA4, контакти, srcset widths, dimensions, lazy, EXIF.
- Новий JS відсутній; форма JS не підключена до кейсів. Додано невеликий CSS для розділу та scoped CSS для довших RU-написів; глобальна CSS-архітектура збережена.
- Font Awesome потрібний наявним header/footer/mobile icons; важких gallery-бібліотек немає. Google Fonts не дублюються в межах сторінки.
- CLS: місце під фото зарезервовано через width/height, але числовий CLS не виміряний. Завантаження шрифту може впливати на метрику.
- LCP/FCP/TBT/INP: не виміряні. Lighthouse/Performance trace/console/coverage недоступні без браузера; field INP також потребує реальних даних відвідувань. Немає вигаданих балів чи твердження про проходження CWV.
- Фактичне завантаження responsive candidate на mobile і візуальна незмінність дизайну не підтверджені браузером. Код польської головної перевірено на точний дозволений diff.
- `git diff --check` пройдено. Commit/push/deploy не виконувалися.

### Повторення перевірок

```sh
python3 scripts/build-cases.py
PYTHONPATH=/tmp/ltsmarket-image-tools python3 scripts/check-cases.py
PYTHONPATH=/tmp/ltsmarket-image-tools python3 scripts/check-cases.py --http http://127.0.0.1:8766
```

Pillow потрібний для оптимізації/перевірки зображень. Шлях `/tmp/ltsmarket-image-tools` — наявна локальна інсталяція цього сеансу. Для відтворення фото: `python3 scripts/optimize-case-images.py DIRECTORY_WITH_ORIGINAL_PNGS` у середовищі з Pillow.

## N. Existing issues found — not modified

- `styles/style.css` посилається на відсутній `/images/hero-car.jpg` у `.section--dark`. Нові кейси не використовують цей клас; чинну проблему головних не змінено.
- Фактичні розміри старих gallery JPEG не збігаються із заявленими 800×600; старі фото не мають responsive srcset.
- `images/og-image.jpg` фактично 1731×909 і 1.87 MB, тоді як OG metadata головних заявляють 1200×630.
- Старий hero PNG — 1.94 MB, CSS background без responsive variants.
- На PL-головній є існуючі узагальнені твердження про ринкову вартість, показники «30 min»/«100%» без доказів у репозиторії. У нових кейсах цифри/гарантії не повторювалися. RU-головна зберігає існуючі цифри як переклад вихідного вмісту; нових показників не додано.
- Вихідний CSS body `overflow-x:hidden` може приховати проблему ширини; тому одного аналізу scrollWidth недостатньо для приймального mobile audit.
- Старий footer і language switcher потребують окремого повного accessibility audit; наявну дизайн-систему не переписано.
- Фактична доставка форми/webhook, GA4 collection, доступність зовнішніх CDN/соцмереж і production-hosting не перевірялися.

Виправлена за окремим дозволом проблема: RU-головна була повною PL-копією; перекладено і виправлено мову, SEO та перемикач.

## Що залишається до остаточного приймання

У браузері перевірити всі наведені viewport для обох індексів і шести кейсів, RU-головну, клавіатуру/мовні переходи, перекриття fixed controls, console/network, currentSrc на DPR 1/2/3, LCP/CLS/FCP/TBT. Після окремо дозволеного розгортання — live URL/redirect/canonical перевірка. Код і локальний HTTP пройшли перевірки; браузерне підтвердження не підмінено статичними результатами.
