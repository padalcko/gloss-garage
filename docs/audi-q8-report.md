# Audi Q8 — локальний звіт

Створено PL/RU HTML та Markdown, 8 WebP (по 4 на оригінал), браузерний протокол. Зміни повністю локальні: без commit, push і deploy.

URL після публікації:
- https://gg-pdr.pl/realizacje/audi-q8-usuwanie-wgniecenia-maski-pdr/
- https://gg-pdr.pl/ru/realizacje/audi-q8-usuwanie-wgniecenia-maski-pdr/

Спільний slug відповідає чинній архітектурі сайту. Картки додано першими, обкладинка — після ремонту. Збережено готові тексти дослівно, перевірено програмно. Усі 8 існуючих сторінок кейсів побайтово збігаються з HEAD. CSS, JS, header/footer, контакти й інтеграції не змінено.

## Фото

Оригінали 960×1280. Без ретуші, кадрування, зміни кольору або генеративного AI. WebP quality 88, адаптивні ширини 360/540/768/960, висоти 480/720/1024/1280. Розміри нижче у байтах.

| Фото | JPEG | WebP 360 | WebP 540 | WebP 768 | WebP 960 |
|---|---:|---:|---:|---:|---:|
| ДО, 15.23.00 |169199|27592|48942|87154|130852|
| ПІСЛЯ, 15.23.07 |191023|31448|60216|105272|155464|

Галерея за еталоном: статична, без слайдера. Порядок PRZED → PO / ДО → ПОСЛЕ перевірено; alt точні, srcset/sizes та фактичні width/height присутні. Перше фото eager, друге lazy.

## Перевірки

- build-site.py: PASS; build-ai-search.py --check: без застарілих файлів.
- check-ai-search.py: 14 HTML, 16 Markdown, 1092 посилання, 14 sitemap URL; 0 помилок.
- check-cases.py --http http://127.0.0.1:8776: 111 HTTP перевірок, 0 помилок.
- git diff --check: PASS.
- Canonical, взаємні hreflang PL/RU/x-default, sitemap, OG/Twitter, JSON-LD та внутрішні посилання: PASS.
- Article, BreadcrumbList і ImageObject посилаються на існуючу сутність бізнесу. datePublished не додано, оскільки фактичної публікації ще не було; його слід встановити при публікації. Дату ремонту не вигадано.
- Chrome: обидві мови на 320/375/430/768/1024/1440 px; немає горизонтального скролу та JS-помилок; фото завантажуються, перемикач мов здійснює перехід на відповідний кейс. WhatsApp href відповідає існуючому номеру; повідомлення не надсилалися.
- Візуально переглянуто повний скриншот PL 375 px; скриншоти всіх 12 конфігурацій у /tmp/gg-q8/.
- Виміряний CLS: 0.0001–0.0246. Нульовий CLS не підтверджено; глобальні стилі та завантаження шрифтів не змінювалися. Це локальні вимірювання, не польові Core Web Vitals.

## Створені та змінені файли

```text
 M _headers
 M ai/pdr.md
 M ai/realizacje.md
 M ai/services.md
 M docs/ai-search-validation.json
 M docs/cases-seo.json
 M docs/cases-validation.json
 M docs/image-audit.json
 M index.html
 M llms-full.txt
 M llms.txt
 M realizacje/index.html
 M ru/index.html
 M ru/realizacje/index.html
 M scripts/build-cases.py
 M scripts/cases-content.json
 M scripts/check-cases.py
 M sitemap.xml
?? docs/audi-q8-browser-validation.json
?? images/realizacje/audi-q8-maska-po-naprawie-pdr-wroclaw-360.webp
?? images/realizacje/audi-q8-maska-po-naprawie-pdr-wroclaw-540.webp
?? images/realizacje/audi-q8-maska-po-naprawie-pdr-wroclaw-768.webp
?? images/realizacje/audi-q8-maska-po-naprawie-pdr-wroclaw.webp
?? images/realizacje/audi-q8-wgniecenie-maski-przed-pdr-wroclaw-360.webp
?? images/realizacje/audi-q8-wgniecenie-maski-przed-pdr-wroclaw-540.webp
?? images/realizacje/audi-q8-wgniecenie-maski-przed-pdr-wroclaw-768.webp
?? images/realizacje/audi-q8-wgniecenie-maski-przed-pdr-wroclaw.webp
?? realizacje/audi-q8-usuwanie-wgniecenia-maski-pdr/index.html
?? realizacje/audi-q8-usuwanie-wgniecenia-maski-pdr/index.md
?? ru/realizacje/audi-q8-usuwanie-wgniecenia-maski-pdr/index.html
?? ru/realizacje/audi-q8-usuwanie-wgniecenia-maski-pdr/index.md
```
