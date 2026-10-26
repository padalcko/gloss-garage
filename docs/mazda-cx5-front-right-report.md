# Mazda CX-5 — переднє праве крило, PDR

Дата: 2026-10-26. Зміни лише локальні; commit, push і deploy не виконувалися.

## Сторінки

- PL: https://gg-pdr.pl/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/
- RU: https://gg-pdr.pl/ru/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/

Це цільові URL після публікації; перевірки проведені локально.

## Реалізація

Додано четверту картку в обох списках. Збережено надані тексти PL/RU; перший абзац розташований у вступі, наступні — в блоках ремонту й результату за чинним шаблоном. Галерея містить рівно шість фото: 01–03 до ремонту, 04–06 після. Фото 04 (09.19.58) використане як обкладинка картки та Open Graph.

Еталон має звичайну сітку figure/img/figcaption без lightbox або слайдера; використано саме її. Порядок блоків, навігацію, CTA та сітку збережено.

Генератор читає фактичні розміри варіантів із чинного image-audit.json та підтримує вибір обкладинки. Оптимізатор обмежує ширину розміром джерела, щоб не збільшувати фото 960 px до 1086 px. Збережено стандарт іменування проєкту: slug-номер-ширина.webp. Оновлено чинні sitemap, Markdown/LLM ресурси, _headers та автоматично сформовані посилання на кейси на головних PL/RU. Загальне твердження AI-індексу про відсутність фото до/після замінене нейтральним описом підписів.

## Фотографії

Для кожного оригіналу створено чотири WebP: 360×480, 540×720, 768×1024, 960×1280. У таблиці наведено найбільший варіант; вага — у байтах.

| Група | Оригінал | Новий файл у images/realizacje/ | Початковий розмір | Кінцевий розмір |
|---|---|---|---|---|
| До | `photo_2026-10-26 09.19.56.jpeg` | `mazda-cx5-pdr-przedni-prawy-blotnik-01-960.webp` | 960×1280, 137,071 B | 960×1280, 95,708 B |
| До | `photo_2026-10-26 09.19.52.jpeg` | `mazda-cx5-pdr-przedni-prawy-blotnik-02-960.webp` | 960×1280, 99,329 B | 960×1280, 56,298 B |
| До | `photo_2026-10-26 09.19.55.jpeg` | `mazda-cx5-pdr-przedni-prawy-blotnik-03-960.webp` | 960×1280, 137,574 B | 960×1280, 99,888 B |
| Після | `photo_2026-10-26 09.19.58.jpeg` | `mazda-cx5-pdr-przedni-prawy-blotnik-04-960.webp` | 960×1280, 128,926 B | 960×1280, 92,746 B |
| Після | `photo_2026-10-26 09.19.59.jpeg` | `mazda-cx5-pdr-przedni-prawy-blotnik-05-960.webp` | 960×1280, 100,397 B | 960×1280, 58,282 B |
| Після | `photo_2026-10-26 09.19.57.jpeg` | `mazda-cx5-pdr-przedni-prawy-blotnik-06-960.webp` | 960×1280, 116,911 B | 960×1280, 73,886 B |

Шість найбільших WebP: 476,808 B замість 720,208 B JPEG. Усі 24 responsive-файли: 1,106,598 B. Браузер завантажує відповідний варіант через srcset.

Перевірка повторного кодування з вихідних JPEG дала побайтово ідентичні 24 WebP. Це підтверджує обробку лише ресайзом Lanczos і WebP-кодуванням (quality 88), без кадрування, ретуші, AI, зміни кольорів або геометрії. WebP є стисненням із втратами; пікселі не заявляються ідентичними JPEG. Пропорції 3:4 збережені.

## Перевірки

- `python3 scripts/build-site.py` — успішно.
- `python3 scripts/build-ai-search.py --check` — stale та orphan відсутні.
- `scripts/check-ai-search.py` — 12 HTML, 14 Markdown, 937 перевірених посилань, 12 sitemap URL; помилок немає.
- `scripts/check-cases.py --http http://127.0.0.1:8776` — 12 HTML, 10 сторінок розділу реалізацій, 64 WebP, 99 HTTP-перевірок; помилок немає. Використано готовий Python runtime із Pillow без нових залежностей проєкту.
- `git diff --check` — успішно.
- Локальний Chrome: нові детальні сторінки й списки PL/RU на 320, 375, 430, 768, 1024, 1440 px — 24 комбінації без горизонтального переповнення й помилок JavaScript сторінки.
- Усі фото прокручені в область видимості й декодовані. Перевірено порядок джерел, локалізовані підписи до/після, пропорції, 1/2 колонки галереї та обкладинку 04.
- У сенсорному режимі Chrome перевірено tap на картці й перехід на відповідну сторінку. Це емуляція, не перевірка на фізичному телефоні.
- Переглянуто знімки desktop PL та mobile RU. Скриншоти і детальний браузерний протокол: `/tmp/gg-tiguan/`.
- SEO: один H1, унікальні title/description, описові локалізовані alt, canonical, взаємні hreflang PL/RU/x-default, OG з правильними розмірами 960×1280, чинні WebPage/BreadcrumbList без нових типів schema; sitemap без дубльованих URL.

## Збереження попереднього стану

Порівняння виконане зі знімком робочого дерева на початку цього завдання, а не лише HEAD, оскільки вже були локальні зміни футера.

Старі детальні сторінки PL/RU, їхні Markdown та фото, всі CSS/JS побайтово незмінні. Три старі картки у кожному списку побайтово незмінні. Header, footer та mobile nav залишилися без змін. Головні сторінки змінилися лише в автоматично сформованих блоках посилань на кейси та пов'язаного SEO. Інші секції, FAQ, форми, контакти й інтеграції не змінені.

## Створені файли

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
- `realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/index.html`
- `realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/index.md`
- `ru/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/index.html`
- `ru/realizacje/mazda-cx5-pdr-przedni-prawy-blotnik/index.md`

## Змінені файли в цьому завданні

- `_headers`
- `ai/pdr.md`
- `ai/realizacje.md`
- `ai/services.md`
- `docs/ai-search-validation.json`
- `docs/cases-seo.json`
- `docs/cases-validation.json`
- `docs/image-audit.json`
- `index.html`
- `llms-full.txt`
- `llms.txt`
- `realizacje/index.html`
- `ru/index.html`
- `ru/realizacje/index.html`
- `scripts/build-ai-search.py`
- `scripts/build-cases.py`
- `scripts/cases-content.json`
- `scripts/optimize-case-images.py`
- `sitemap.xml`
