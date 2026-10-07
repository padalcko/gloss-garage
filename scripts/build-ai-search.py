#!/usr/bin/env python3
"""Generate factual AI resources and linked JSON-LD from current HTML. No network.
HTML is authoritative. Run after build-cases.py; --check does not write files.
"""
from pathlib import Path
from urllib.parse import urlsplit
import argparse, json, re
from site_content import Parser, markdown, clean
ROOT=Path(__file__).resolve().parents[1]
BASE='https://gg-pdr.pl'
BUSINESS=BASE+'/#business'
SCHEMA_RE=re.compile(r'<script\b[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',re.S)
BEGIN='<!-- BEGIN GENERATED SEARCH -->'; END='<!-- END GENERATED SEARCH -->'

def discover():
    pages=[]
    for path in sorted(ROOT.rglob('*.html')):
        if any(x.startswith('.') for x in path.relative_to(ROOT).parts):continue
        source=path.read_text(); tree=Parser(source).root;tags=list(tree.all())
        meta={n.attrs.get('name',n.attrs.get('property')):n.attrs.get('content','') for n in tags if n.tag=='meta'}
        if 'noindex' in meta.get('robots',''):continue
        canonical=[n.attrs['href'] for n in tags if n.tag=='link' and n.attrs.get('rel')=='canonical']
        assert len(canonical)==1, path
        url=BASE+'/'+str(path.relative_to(ROOT)).removesuffix('index.html')
        assert canonical==[url],(path,canonical)
        pages.append(dict(path=path,source=source,tree=tree,tags=tags,url=url,meta=meta,lang=next(n.attrs['lang'] for n in tags if n.tag=='html'),title=next(n.text() for n in tags if n.tag=='h1')))
    return pages

def node(page, **attrs):
    return next(n for n in page['tags'] if all(n.attrs.get(k)==v for k,v in attrs.items()))

def faqs(page):
    return [(next((child for child in n.all() if child.has('pdr-faq__text')), next(n.all('h3'))).text(),
             next(n.all('p')).text()) for n in node(page,id='faq').all('section')]

def build(pages):
    lookup={p['url']:p for p in pages};home=lookup[BASE+'/']; output={};resources={}
    # Read the existing entity definition, never duplicate editorial business data.
    business=next(json.loads(raw) for raw in SCHEMA_RE.findall(home['source']) if json.loads(raw).get('@type')=='AutoRepair')
    assert business['@id']==BUSINESS
    contacts=node(home,**{'class':'footer__contacts'})
    social=business['sameAs']; whatsapp=next(n.attrs['href'] for n in contacts.all('a') if 'wa.me/' in n.attrs.get('href',''))
    cases=[p for p in pages if re.fullmatch(r'/(ru/)?realizacje/[^/]+/',urlsplit(p['url']).path)]
    plcases=[p for p in cases if p['lang']=='pl']
    def add(path,title,canonical,body):
        content=f'# {title}\n\nŹródło HTML: [{title}]({canonical})\n\nJęzyk: Polski. HTML jest źródłem nadrzędnym.\n\n'+clean(body)
        output[ROOT/path]=content;resources[path]=(title,canonical)
    summary=business['description']+'\n\nPDR — Paintless Dent Repair / usuwanie wgnieceń bez lakierowania.'
    contact=f"Firma: {business['name']}\n\nWitryna: [{BASE}/]({BASE}/)\n\nAdres: {business['address']['streetAddress']}, {business['address']['addressLocality']}, Polska.\n\nObszar obsługi: Wrocław i okolice. Adres warsztatu znajduje się w Radwanicach.\n\nTelefon: [{business['telephone']}](tel:{business['telephone']})\n\nWhatsApp: [{whatsapp}]({whatsapp})\n\nJęzyki witryny: polski (główny), rosyjski (alternatywny).\n\n"
    contact+='\n'.join(f'- [{"Instagram" if "instagram" in u else "Facebook"}]({u})' for u in social)
    contact+='\n\n[Formularz kontaktowy i wycena ze zdjęć]('+BASE+'/#contact).'
    add('ai/about.md','Gloss Garage — PDR, Wrocław i okolice',BASE+'/',summary+'\n\n'+contact+'\n\n[Usługi PDR]('+BASE+'/#pdr) · [Wykonane naprawy]('+BASE+'/realizacje/)')
    services=node(home,id='pdr')
    servicebody='Metoda wszystkich poniższych napraw: PDR (Paintless Dent Repair). Obszar: Wrocław i okolice.\n\n'
    for card in services.all('article'):
        servicebody+='## '+next(card.all('h3')).text()+'\n\n'+next(card.all('p')).text()+'\n\nRozwiązanie: usunięcie wgniecenia metodą PDR, po ocenie możliwości naprawy. [Usługa i kontakt]('+BASE+'/#pdr).\n\n'
    servicebody+='## Udokumentowane przykłady\n\n'+'\n'.join('- ['+p['title']+']('+p['url']+')' for p in plcases)
    add('ai/services.md','Usługi Gloss Garage',BASE+'/#pdr',servicebody)
    pdrbody=markdown(next(n for n in services.all('div') if n.has('section__head')),BASE+'/')
    pdrbody+='\n\n## Ocena, korzyści i ograniczenia\n\n'+'\n\n'.join('### '+q+'\n\n'+a for q,a in faqs(home)[:5])
    add('ai/pdr.md','PDR — Paintless Dent Repair',BASE+'/#pdr',pdrbody)
    add('ai/faq.md','Pytania o naprawę PDR w Gloss Garage',BASE+'/#faq','\n\n'.join('## '+q+'\n\n'+a for q,a in faqs(home)))
    add('ai/contact.md','Kontakt — Gloss Garage',BASE+'/#contact',contact)
    body='Gloss Garage wykonuje naprawy PDR we Wrocławiu i okolicach. Poniżej udokumentowane realizacje; zdjęcia nie są oznaczone jako porównania przed i po.\n\n'
    data=json.loads((ROOT/'scripts/cases-content.json').read_text())
    for p in plcases:
        slug=p['path'].parent.name;d=data[slug]
        body+='## '+d['car']+'\n\nProblem: '+d['pl']['damage']+'.\n\nRozwiązanie: naprawa metodą PDR bez ponownego lakierowania.\n\n[Pełny opis HTML]('+p['url']+') · [Markdown]('+p['url']+'index.md) · [Русский]('+BASE+'/ru/realizacje/'+slug+'/).\n\n'
    add('ai/realizacje.md','Realizacje PDR — Gloss Garage',BASE+'/realizacje/',body)
    for p in cases:
        ru=p['lang']=='ru';slug=p['path'].parent.name;d=data[slug];lang=p['lang'];root='/ru/' if ru else '/'
        fields=[('Автомобиль' if ru else 'Samochód',d['car']),('Повреждение / элемент кузова' if ru else 'Uszkodzenie / element karoserii',d[lang]['damage']),('Метод' if ru else 'Metoda','PDR — Paintless Dent Repair'),('Исполнитель' if ru else 'Wykonawca','Gloss Garage')]
        text='# '+p['title']+'\n\n'+('Источник HTML' if ru else 'Źródło HTML')+': ['+p['title']+']('+p['url']+')\n\n'+('Язык: Русский. HTML — основной источник.' if ru else 'Język: Polski. HTML jest źródłem nadrzędnym.')+'\n\n'
        text+='\n'.join('- '+k+': '+v for k,v in fields)+'\n\n'+d[lang]['lead']+'\n\n'
        text+='\n\n'.join('## '+h+'\n\n'+body for h,body in d[lang]['sections'])+'\n\n'
        text+=('## Фотографии\n\n' if ru else '## Zdjęcia\n\n')+'\n\n'.join(markdown(n,p['url']) for n in p['tree'].all('figure'))
        text+='\n\n['+('Услуги PDR' if ru else 'Usługi PDR')+']('+BASE+root+'#pdr) · ['+('Контакты' if ru else 'Kontakt')+']('+BASE+root+'#contact)\n'
        target=p['path'].with_suffix('.md');output[target]=clean(text);resources[str(target.relative_to(ROOT))]=(p['title'],p['url'])
    llms='# Gloss Garage\n\n> '+summary.replace('\n\n',' ')+'\n\nAdres: ul. Szkolna 55, Radwanice, Polska. Obszar obsługi: Wrocław i okolice.\nJęzyki witryny: polski (główny) i rosyjski. Canonical website: '+BASE+'/.\nTelefon: '+business['telephone']+'. WhatsApp: '+whatsapp+'.\nHTML pozostaje nadrzędnym źródłem; Markdown to uzupełniająca reprezentacja.\n\n## Główne strony\n\n'
    for title,url in [('Gloss Garage',BASE+'/'),('Usługi PDR — wgniecenia parkingowe, po gradobiciu, trudne elementy',BASE+'/#pdr'),('Realizacje',BASE+'/realizacje/'),('Kontakt i wycena',BASE+'/#contact'),('FAQ',BASE+'/#faq'),('Русская версия',BASE+'/ru/')]:llms+='- ['+title+']('+url+')\n'
    llms+='\n## Realizacje\n\n'+''.join('- ['+p['title']+']('+p['url']+')\n' for p in plcases)
    llms+='\n## Materiały AI-readable\n\n'+''.join('- ['+title+']('+BASE+'/'+path+')\n' for path,(title,_) in resources.items() if path.startswith('ai/'))
    llms+='- [Pełny dokument wiedzy]('+BASE+'/llms-full.txt)\n'
    output[ROOT/'llms.txt']=llms
    output[ROOT/'llms-full.txt']='# Gloss Garage — pełny dokument wiedzy\n\nPolski jest językiem głównym. HTML pozostaje źródłem nadrzędnym.\n\n'+'\n\n'.join(output[ROOT/path] for path in resources if path.startswith('ai/') or not path.startswith('ru/'))
    # Add schema with existing business identity; retain the existing AutoRepair block.
    for p in pages:
        url=p['url'];ru=p['lang']=='ru';homeurl=BASE+('/ru/' if ru else '/');serviceid=homeurl+'#pdr-service'
        original=re.sub(re.escape(BEGIN)+r'.*?'+re.escape(END)+r'\n?', '',p['source'],flags=re.S)
        graph=[]
        if url==homeurl:
            graph=[{'@type':'WebSite','@id':BASE+'/#website','url':BASE+'/','name':'Gloss Garage','inLanguage':['pl','ru'],'publisher':{'@id':BUSINESS}},
                   {'@type':'WebPage','@id':url+'#webpage','url':url,'name':p['title'],'inLanguage':p['lang'],'isPartOf':{'@id':BASE+'/#website'},'about':{'@id':BUSINESS}},
                   {'@type':'Service','@id':serviceid,'url':homeurl+'#pdr','name':'PDR — Paintless Dent Repair','serviceType':'Удаление вмятин без покраски' if ru else 'Usuwanie wgnieceń bez lakierowania','provider':{'@id':BUSINESS},'areaServed':business['areaServed'],'subjectOf':[{'@id':c['url']+'#webpage'} for c in cases if c['lang']==p['lang']]},
                   {'@type':'FAQPage','@id':url+'#faq','url':url+'#faq','inLanguage':p['lang'],'isPartOf':{'@id':url+'#webpage'},'mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in faqs(p)]}]
        md=(url+'index.md') if p in cases else BASE+'/ai/about.md' if url==BASE+'/' else BASE+'/ai/realizacje.md' if url==BASE+'/realizacje/' else None
        block=BEGIN+'\n<link rel="describedby" href="/llms.txt">\n'
        if md:block+='<link rel="alternate" type="text/markdown" href="'+md+'">\n'
        if graph:block+='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False)+'</script>\n'
        block+=END+'\n'
        output[p['path']]=original.replace('</head>',block+'</head>',1)
    headers='# BEGIN GENERATED AI HEADERS\n'
    for path,(_,canonical) in resources.items():
        headers+='\n/'+path+'\n  Content-Type: text/markdown; charset=utf-8\n  X-Content-Type-Options: nosniff\n'
        # Full case documents are alternate representations; topical extracts are noindex supplements.
        if path.startswith('ai/'):
            headers+='  X-Robots-Tag: noindex\n'
        else:
            headers+='  Link: <'+canonical+'>; rel="canonical"\n'
    for name in ('llms.txt','llms-full.txt'):
        headers+='\n/'+name+'\n  Content-Type: text/plain; charset=utf-8\n  X-Content-Type-Options: nosniff\n  X-Robots-Tag: noindex\n'
    headers+='# END GENERATED AI HEADERS\n'
    h=ROOT/'_headers';existing=h.read_text() if h.exists() else ''
    pattern=r'# BEGIN GENERATED AI HEADERS.*?# END GENERATED AI HEADERS\n?'
    output[h]=re.sub(pattern,lambda _:headers,existing,flags=re.S) if '# BEGIN GENERATED AI HEADERS' in existing else existing+headers
    return output

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',action='store_true');args=ap.parse_args()
    output=build(discover());stale=[]
    for path,text in output.items():
        if not path.exists() or path.read_text()!=text:
            stale.append(str(path.relative_to(ROOT)))
            if not args.check:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
    expected={p for p in output if p.suffix=='.md'}
    orphans=[str(p.relative_to(ROOT)) for base in ('ai','realizacje','ru/realizacje') for p in (ROOT/base).rglob('*.md') if p not in expected]
    print(json.dumps({'stale' if args.check else 'updated':stale,'orphans_require_review':orphans},ensure_ascii=False,indent=2))
    if orphans or args.check and stale:raise SystemExit(1)
if __name__=='__main__':main()
