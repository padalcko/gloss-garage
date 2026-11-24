"""Generate contact pages using the current localized home page components."""
from pathlib import Path
import re, json, html
ROOT=Path(__file__).resolve().parents[1]
BASE='https://gg-pdr.pl'
copy={
'pl': dict(title='Kontakt | Gloss Garage – PDR Wrocław', desc='Skontaktuj się z Gloss Garage we Wrocławiu. Usuwanie wgnieceń bez lakierowania metodą PDR. Sprawdź adres serwisu, telefon i wyślij zdjęcia uszkodzenia.', h1='Kontakt', home='Strona główna', crumb='Ścieżka nawigacji', brand='Gloss Garage – PDR Wrocław', intro=['Masz wgniecenie na karoserii samochodu? Skontaktuj się z Gloss Garage we Wrocławiu. Specjalizujemy się w usuwaniu wgnieceń bez lakierowania metodą PDR, naprawie uszkodzeń parkingowych oraz wgnieceń powstałych w wyniku gradobicia.','Prześlij nam zdjęcia uszkodzenia lub odwiedź nasz serwis. Pomożemy ocenić możliwości naprawy i ustalić dalsze szczegóły.'], details='Dane kontaktowe', address='Adres serwisu', phone='Telefon', map='Jak do nas trafić?', maptext='Odwiedź Gloss Garage we Wrocławiu. Skorzystaj z poniższej mapy, aby sprawdzić lokalizację naszego serwisu i wyznaczyć trasę dojazdu.', map_title='Mapa dojazdu do Gloss Garage w Radwanicach', route='Wyznacz trasę', contact='Skontaktuj się z nami', formtext=['Chcesz poznać możliwości naprawy wgniecenia bez lakierowania? Skorzystaj z formularza kontaktowego lub prześlij zdjęcia uszkodzenia przez WhatsApp.','Skontaktujemy się z Tobą, aby omówić szczegóły naprawy.']),
'ru': dict(title='Контакты | Gloss Garage – PDR Вроцлав', desc='Свяжитесь с Gloss Garage во Вроцлаве. Удаление вмятин без покраски по технологии PDR. Адрес сервиса, телефон и оценка повреждений по фото.', h1='Контакты', home='Главная', crumb='Навигационная цепочка', brand='Gloss Garage – PDR Вроцлав', intro=['Обнаружили вмятину на кузове автомобиля? Обратитесь в Gloss Garage во Вроцлаве. Мы специализируемся на удалении вмятин без покраски по технологии PDR, ремонте парковочных повреждений и вмятин, образовавшихся вследствие града.','Отправьте нам фотографии повреждения или посетите наш сервис. Мы поможем оценить возможность ремонта и согласовать дальнейшие детали.'], details='Контактные данные', address='Адрес сервиса', phone='Телефон', map='Как нас найти?', maptext='Посетите Gloss Garage во Вроцлаве. Воспользуйтесь картой ниже, чтобы посмотреть расположение нашего сервиса и построить маршрут.', map_title='Карта проезда в Gloss Garage в Радванице', route='Построить маршрут', contact='Свяжитесь с нами', formtext=['Хотите узнать, можно ли удалить вмятину без покраски? Воспользуйтесь контактной формой или отправьте фотографии повреждения через WhatsApp.','Мы свяжемся с вами, чтобы обсудить детали ремонта.'])}
copy['pl'].update(intro=['Profesjonalne usuwanie wgnieceń bez lakierowania. Skontaktuj się z nami, prześlij zdjęcia uszkodzenia lub odwiedź nasz serwis w Radwanicach koło Wrocławia.'], contact='Napisz do nas', photo='Wyślij zdjęcia uszkodzenia do oceny')
copy['ru'].update(intro=['Профессиональное удаление вмятин без покраски. Свяжитесь с нами, отправьте фотографии повреждения или посетите наш сервис в Радваницах рядом с Вроцлавом.'], contact='Напишите нам', photo='Отправьте фото повреждения для оценки')
def get(pattern,s): return re.search(pattern,s,re.S).group()
def esc(s): return html.escape(s,quote=True)
for lang,c in copy.items():
 home='/ru/' if lang=='ru' else '/'; path=home+'kontakt/'; url=BASE+path
 source=(ROOT/('ru/index.html' if lang=='ru' else 'index.html')).read_text()
 header=get(r'<header.*?</header>',source)
 switch='<div class="language-switcher" aria-label="'+('Выбор языка' if lang=='ru' else 'Wybór języka')+'">'+ ' <span class="language-switcher__separator"> / </span> '.join(f'<a href="{"/ru" if l=="ru" else ""}/kontakt/" hreflang="{l}" class="language-switcher__link'+(' language-switcher__link--active" aria-current="page"' if l==lang else '"')+f'>{l.upper()}</a>' for l in ('pl','ru'))+'</div>'
 header=re.sub(r'<div class="language-switcher".*?</div>',lambda _:switch,header,flags=re.S).replace(f'href="{path}"',f'href="{path}" aria-current="page"',1)
 footer=get(r'<footer.*?</footer>',source); mobile=get(r'<nav class="mobile-bottom-nav".*?</nav>',source); form=get(r'<form id="leadForm".*?</form>',source)
 source_head=re.sub(r'<!-- BEGIN GENERATED SEARCH -->.*?<!-- END GENERATED SEARCH -->\n?', '', source, flags=re.S)
 fonts=get(r'<link rel="preconnect".*?</head>',source_head).replace('</head>','')
 analytics=get(r'<script\s+async.*?</script>\s*<script>.*?</script>',source)
 alternates=''.join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{"/ru" if l=="ru" else ""}/kontakt/">' for l in ('pl','ru','x-default'))
 schema={'@context':'https://schema.org','@graph':[{'@type':'ContactPage','@id':url+'#webpage','url':url,'name':c['title'],'description':c['desc'],'inLanguage':lang,'isPartOf':{'@id':BASE+'/#website'},'about':{'@id':BASE+'/#business'},'breadcrumb':{'@id':url+'#breadcrumbs'}},{'@type':'BreadcrumbList','@id':url+'#breadcrumbs','itemListElement':[{'@type':'ListItem','position':1,'name':c['home'],'item':BASE+home},{'@type':'ListItem','position':2,'name':c['h1'],'item':url}]}]}
 meta=f'<title>{esc(c["title"])}</title><meta name="description" content="{esc(c["desc"])}"><meta name="robots" content="index, follow"><link rel="canonical" href="{url}">{alternates}'
 for attr,key,value in [('property','og:type','website'),('property','og:title',c['title']),('property','og:description',c['desc']),('property','og:url',url),('property','og:image',BASE+'/images/og-image.jpg'),('property','og:locale','pl_PL' if lang=='pl' else 'ru_RU'),('property','og:locale:alternate','ru_RU' if lang=='pl' else 'pl_PL'),('name','twitter:card','summary_large_image'),('name','twitter:title',c['title']),('name','twitter:description',c['desc']),('name','twitter:image',BASE+'/images/og-image.jpg')]:meta+=f'<meta {attr}="{key}" content="{esc(value)}">'
 ps=lambda items: ''.join('<p>'+esc(x)+'</p>' for x in items)
 icon=lambda paths: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+paths+'</svg>'
 pin=icon('<path d="M20 10c0 5-8 11-8 11S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>')
 phone=icon('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.1-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7l.4 2.8a2 2 0 0 1-.6 1.7L7.6 9.5a16 16 0 0 0 6.9 6.9l1.3-1.3a2 2 0 0 1 1.7-.6l2.8.4a2 2 0 0 1 1.7 2Z"/>')
 message=icon('<path d="M21 11.5a8.5 8.5 0 0 1-12.7 7.4L3 21l1.5-5A8.5 8.5 0 1 1 21 11.5Z"/><path d="M8 11h8M8 14h5"/>')
 address_query='ul.%20Szkolna%2055%2C%2055-010%20Radwanice%2C%20Polska'
 body=f'''<nav class="container case-breadcrumbs" aria-label="{c['crumb']}"><ol><li><a href="{home}">{c['home']}</a></li><li aria-current="page">{c['h1']}</li></ol></nav>
 <section class="contact-intro"><div class="container"><h1>{c['h1']}</h1><p class="contact-intro__brand"><strong>{c['brand']}</strong></p>{ps(c['intro'])}</div></section>
 <section class="contact-section"><div class="container"><div class="contact-cards">
 <article class="contact-card">{pin}<div><h3>{c['address']}</h3><p>ul. Szkolna 55<br>55-010 Radwanice, Polska</p></div></article>
 <article class="contact-card">{phone}<div><h3>{c['phone']}</h3><a href="tel:+48884012737">+48 884 012 737</a></div></article>
 <article class="contact-card">{message}<div><h3>WhatsApp</h3><a href="https://wa.me/380667835184" target="_blank" rel="noopener noreferrer">+380 66 783 51 84</a><p>{c['photo']}</p></div></article></div>
 </div></section>
 <section class="contact-section contact-work"><div class="container contact-work__grid"><div class="contact-work__column"><h2>{c['contact']}</h2>{form}</div>
 <div class="contact-work__column"><h2>{c['map']}</h2><div class="map contact-map"><iframe src="https://www.google.com/maps?q={address_query}&amp;output=embed" loading="lazy" title="{c['map_title']}"></iframe></div><a class="btn btn--black" href="https://www.google.com/maps/dir/?api=1&amp;destination={address_query}" target="_blank" rel="noopener noreferrer">{c['route']}</a></div></div></section>'''
 document=f'<!doctype html><html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">{meta}<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">{fonts}<link rel="stylesheet" href="/styles/cases.css"><link rel="stylesheet" href="/styles/contact.css">{analytics}<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script><!-- BEGIN GENERATED SEARCH -->\n<link rel="describedby" href="/llms.txt">\n<!-- END GENERATED SEARCH -->\n</head><body class="case-page contact-page">{header}<main>{body}</main>{footer}{mobile}<script src="/js/script.js"></script></body></html>\n'
 target=ROOT/path.strip('/')/'index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(document)
p=ROOT/'sitemap.xml';s=p.read_text();s=re.sub(r'\s*<!-- CONTACT PAGES START -->.*?<!-- CONTACT PAGES END -->','',s,flags=re.S)
alternates=''.join(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{BASE}{"/ru" if l=="ru" else ""}/kontakt/" />\n' for l in ('pl','ru','x-default'))
entries='\n  <!-- CONTACT PAGES START -->\n'+''.join(f'  <url>\n    <loc>{BASE}{"/ru" if l=="ru" else ""}/kontakt/</loc>\n{alternates}  </url>\n' for l in ('pl','ru'))+'  <!-- CONTACT PAGES END -->\n'
p.write_text(s.replace('</urlset>',entries+'</urlset>'))
print('Generated 2 contact pages')
