"""Generate bilingual static case pages from existing site chrome and factual content."""
from pathlib import Path
import json,re,html
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'scripts/cases-content.json').read_text())
BASE='https://gg-pdr.pl'
IMAGES={v['file']:v for row in json.loads((ROOT/'docs/image-audit.json').read_text()) for v in row['variants']}
E=lambda s:html.escape(s,quote=True)
COPY={
'pl':dict(label='Realizacje',home='Strona główna',title='Realizacje PDR we Wrocławiu — zdjęcia napraw | Gloss Garage',description='Rzeczywiste naprawy PDR w Gloss Garage we Wrocławiu i okolicach. Zobacz zdjęcia i opisy usuwania wgnieceń z drzwi i błotników bez lakierowania.',h1='Realizacje Gloss Garage — naprawy PDR',lead='Rzeczywiste samochody, konkretne uszkodzenia i naprawy wykonane w Gloss Garage we Wrocławiu i okolicach. Pokazujemy przykłady wgnieceń, które udało się usunąć bez tradycyjnego lakierowania.',gallery='Zdjęcia realizacji',read='Zobacz realizację',tag='PDR · bez lakierowania',cta='Masz podobne wgniecenie?',cta_text='Wyślij nam zdjęcia uszkodzenia z kilku perspektyw. Ocenimy wstępnie, czy można je usunąć metodą PDR bez lakierowania. Ostateczny dobór metody wymaga oględzin.',whatsapp='Wyślij zdjęcia przez WhatsApp',contact='Kontakt',back='Wszystkie realizacje',service='Usługi PDR',crumb='Ścieżka nawigacji'),
'ru':dict(label='Наши работы',home='Главная',title='Работы Gloss Garage — примеры ремонта PDR во Вроцлаве',description='Реальные работы Gloss Garage во Вроцлаве и окрестностях. Фото и описания удаления вмятин на дверях и крыльях методом PDR без покраски.',h1='Работы Gloss Garage — ремонт PDR',lead='Реальные автомобили, конкретные повреждения и ремонт, выполненный Gloss Garage во Вроцлаве и окрестностях. Показываем примеры вмятин, которые удалось удалить без традиционной покраски.',gallery='Фотографии работы',read='Посмотреть работу',tag='PDR · без покраски',cta='У вас похожая вмятина?',cta_text='Отправьте фотографии повреждения с разных ракурсов. Предварительно оценим, можно ли удалить вмятину методом PDR без покраски. Окончательный выбор метода возможен после осмотра.',whatsapp='Отправить фото в WhatsApp',contact='Контакты',back='Все работы',service='Услуги PDR',crumb='Навигационная цепочка')}
def route(lang,slug=''):
 return ('/ru' if lang=='ru' else '')+'/realizacje/'+(slug+'/' if slug else '')
def photo(slug,n,lang,card=False):
 stem=f'/images/realizacje/{slug}-{n:02}'
 sizes='(min-width: 1212px) 329px, (min-width: 981px) calc((100vw - 226px) / 3), (min-width: 621px) calc((100vw - 152px) / 2), calc(100vw - 74px)' if card else '(min-width: 1212px) 576px, (min-width: 621px) calc((100vw - 60px) / 2), calc(100vw - 28px)'
 # Cards and gallery follow introductory text; first image is eager, others lazy.
 loading='eager' if n==1 else 'lazy'
 dimensions=IMAGES[stem.lstrip('/')+'-1086.webp']
 return f'<img src="{stem}-540.webp" srcset="'+', '.join(f'{stem}-{w}.webp {w}w' for w in (360,540,768,1086))+f'" sizes="{sizes}" width="{dimensions['width']}" height="{dimensions['height']}" loading="{loading}" decoding="async" alt="{E(DATA[slug][lang]["alts"][n-1])}">'
# Keep visible service-to-case links in sync before reusing home chrome.
for language in COPY:
 homepage=ROOT/('ru/index.html' if language=='ru' else 'index.html')
 text=homepage.read_text()
 links=(', '.join(f'<a href="{route(language,slug)}">{E(row["car"])}</a>' for slug,row in DATA.items()))
 block='<!-- BEGIN CASE EVIDENCE --><p>'+('Przykłady napraw: ' if language=='pl' else 'Примеры ремонта: ')+links+'.</p><!-- END CASE EVIDENCE -->'
 text=re.sub(r'<!-- BEGIN CASE EVIDENCE -->.*?<!-- END CASE EVIDENCE -->',lambda _:block,text,flags=re.S)
 homepage.write_text(text)
seo=[]
for lang in COPY:
 c=COPY[lang];home='/ru/' if lang=='ru' else '/';template=(ROOT/('ru/index.html' if lang=='ru' else 'index.html')).read_text()
 template=re.sub(r'<!-- BEGIN GENERATED SEARCH -->.*?<!-- END GENERATED SEARCH -->\n?', '', template, flags=re.S)
 header=re.search(r'<header.*?</header>',template,re.S).group()
 footer=re.search(r'<footer.*?</footer>',template,re.S).group()
 mobile=re.search(r'<nav class="mobile-bottom-nav".*?</nav>',template,re.S).group()
 fonts=re.search(r'<link rel="preconnect".*?</head>',template,re.S).group().replace('</head>','')
 analytics=re.search(r'<script\s+async.*?</script>\s*<script>.*?</script>',template,re.S).group()
 for slug in ['',*DATA]:
  d=DATA[slug][lang] if slug else c;url=BASE+route(lang,slug);cover=slug or next(iter(DATA));og=BASE+f'/images/realizacje/{cover}-01-1086.webp'
  switch='<div class="language-switcher" aria-label="'+('Выбор языка' if lang=='ru' else 'Wybór języka')+'">'
  switch+=' <span class="language-switcher__separator"> / </span> '.join(f'<a href="{route(l,slug)}" hreflang="{l}" class="language-switcher__link'+(' language-switcher__link--active" aria-current="page"' if l==lang else '"')+f'>{l.upper()}</a>' for l in COPY)+'</div>'
  pageheader=re.sub(r'<div class="language-switcher".*?</div>',lambda m:switch,header,flags=re.S)
  crumbs=[(c['home'],BASE+home),(c['label'],BASE+route(lang))]
  if slug:crumbs.append((DATA[slug]['car'],url))
  breadcrumb='<nav class="container case-breadcrumbs" aria-label="'+c['crumb']+'"><ol>'+''.join(f'<li><a href="{u.removeprefix(BASE)}">{E(t)}</a></li>' if i<len(crumbs)-1 else f'<li aria-current="page">{E(t)}</li>' for i,(t,u) in enumerate(crumbs))+'</ol></nav>'
  schema={'@context':'https://schema.org','@graph':[{'@type':'WebPage','@id':url+'#webpage','url':url,'name':d['title'],'description':d['description'],'inLanguage':lang,'isPartOf':{'@id':BASE+'/#website'},'publisher':{'@id':BASE+'/#business'},'about':[{'@id':BASE+'/#business'},{'@id':BASE+home+'#pdr-service'}],'primaryImageOfPage':{'@type':'ImageObject','url':og},'breadcrumb':{'@id':url+'#breadcrumbs'}},{'@type':'BreadcrumbList','@id':url+'#breadcrumbs','itemListElement':[{'@type':'ListItem','position':i+1,'name':t,'item':u} for i,(t,u) in enumerate(crumbs)]}]}
  body=breadcrumb+f'<section class="section"><div class="container case-heading"><p class="section__label">Gloss Garage · '+('Wrocław i okolice' if lang=='pl' else 'Вроцлав и окрестности')+f'</p><h1>{E(d["h1"])}</h1><p class="case-lead">{E(d["lead"])}</p></div></section>'
  if slug:
   body+=f'<section class="section gallery"><div class="container"><h2>{c["gallery"]}</h2><div class="case-gallery">'+''.join('<figure>'+photo(slug,n,lang)+f'<figcaption>{E(alt)}</figcaption></figure>' for n,alt in enumerate(d['alts'],1))+'</div></div></section>'
   body+='<div class="section"><div class="container case-copy">'+''.join(f'<section><h2>{E(h)}</h2><p>{E(p)}</p></section>' for h,p in d['sections'])+'</div></div>'
  else:
   body+='<section class="section gallery" aria-label="'+c['label']+'"><div class="container case-cards">'
   for i,(s,car) in enumerate(DATA.items()):
    img=photo(s,1,lang,True)
    if i:img=img.replace('loading="eager"','loading="lazy"')
    body+=f'<article class="card case-card">{img}<h2>{car["car"]}</h2><p>{E(car[lang]["damage"])}. '+('Naprawa w Gloss Garage z zachowaniem oryginalnego lakieru.' if lang=='pl' else 'Ремонт в Gloss Garage с сохранением оригинальной краски.')+f'</p><p class="case-tag">{c["tag"]}</p><a class="btn btn--black" href="{route(lang,s)}" aria-label="{c["read"]}: {car["car"]}">{c["read"]}</a></article>'
   body+='</div></section>'
  body+=f'<section class="section contact case-cta"><div class="container case-copy"><h2>{c["cta"]}</h2><p>{c["cta_text"]}</p><div class="case-actions"><a class="btn btn--red" href="https://wa.me/380667835184" target="_blank" rel="noopener noreferrer">{c["whatsapp"]}</a><a class="btn btn--outline" href="{home}#contact">{c["contact"]}</a></div><nav class="case-links" aria-label="{c["label"]}"><a href="{route(lang)}">{c["back"]}</a><a href="{home}#pdr">{c["service"]}</a></nav></div></section>'
  alternates='\n'.join(f'<link rel="alternate" hreflang="{l}" href="{BASE+route("pl" if l=="x-default" else l,slug)}">' for l in ('pl','ru','x-default'))
  meta=f'<title>{E(d["title"])}</title><meta name="description" content="{E(d["description"])}"><link rel="canonical" href="{url}">\n'+alternates
  for attr,name,value in [('property','og:type','website'),('property','og:title',d['title']),('property','og:description',d['description']),('property','og:url',url),('property','og:image',og),('property','og:image:width',str(IMAGES[og.removeprefix(BASE+'/')]['width'])),('property','og:image:height',str(IMAGES[og.removeprefix(BASE+'/')]['height'])),('property','og:image:alt',DATA[cover][lang]['alts'][0]),('property','og:locale','pl_PL' if lang=='pl' else 'ru_RU'),('property','og:locale:alternate','ru_RU' if lang=='pl' else 'pl_PL'),('name','twitter:card','summary_large_image'),('name','twitter:title',d['title']),('name','twitter:description',d['description']),('name','twitter:image',og)]:meta+=f'\n<meta {attr}="{name}" content="{E(value)}">'
  document=f'<!doctype html>\n<html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">\n{meta}\n<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">\n{fonts}<link rel="stylesheet" href="/styles/cases.css">\n{analytics}\n<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body class="case-page">\n{pageheader}\n<main>{body}</main>\n{footer}\n{mobile}\n</body></html>\n'
  path=ROOT/route(lang,slug).strip('/')/'index.html';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(document)
  seo.append(dict(url=url,title=d['title'],description=d['description'],canonical=url,hreflang={l:BASE+route('pl' if l=='x-default' else l,slug) for l in ('pl','ru','x-default')},og_image=og))
(ROOT/'docs/cases-seo.json').write_text(json.dumps(seo,ensure_ascii=False,indent=2)+'\n')
# Preserve non-case sitemap entries; replace the generated case/index block.
p=ROOT/'sitemap.xml';s=p.read_text();s=re.sub(r'\s*<!-- PDR CASES START -->.*?<!-- PDR CASES END -->\s*','\n',s,flags=re.S)
entries='\n  <!-- PDR CASES START -->\n'
for row in seo:
 entries+='  <url>\n    <loc>'+row['url']+'</loc>\n'+''.join(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{u}" />\n' for l,u in row['hreflang'].items())+'  </url>\n'
entries+='  <!-- PDR CASES END -->\n';p.write_text(s.replace('</urlset>',entries+'</urlset>'))
print('Generated',len(seo),'pages')
