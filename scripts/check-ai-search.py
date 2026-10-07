#!/usr/bin/env python3
"""Validate AI/SEO resources, HTML relationships and optional local HTTP delivery."""
from pathlib import Path
from urllib.parse import urljoin,urlsplit,unquote
from urllib.robotparser import RobotFileParser
import argparse,collections,importlib.util,json,re,sys,subprocess,xml.etree.ElementTree as ET
spec=importlib.util.spec_from_file_location('ai',Path(__file__).with_name('build-ai-search.py'))
ai=importlib.util.module_from_spec(spec);spec.loader.exec_module(ai)
R,B=ai.ROOT,ai.BASE
errors=[];counts=collections.Counter();external=set();requests=set()
def check(ok,message):
    if not ok:errors.append(message)
def walk(value):
    if isinstance(value,dict):
        yield value
        for child in value.values():yield from walk(child)
    elif isinstance(value,list):
        for child in value:yield from walk(child)
def norm(text):return re.sub(r'\W+','',text.lower())
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--http');args=ap.parse_args()
    pages=ai.discover();lookup={p['url']:p for p in pages};expected=ai.build(pages)
    ids={p['url']:{n.attrs.get('id') for n in p['tags']} for p in pages}
    schemaids=set()
    for p in pages:
        for raw in ai.SCHEMA_RE.findall(p['source']):
            for value in walk(json.loads(raw)):
                if '@type' in value and '@id' in value:schemaids.add(value['@id'])
    def link(url,source):
        counts['links_checked']+=1;u=urlsplit(urljoin(source,url))
        if u.scheme in ('tel','mailto','data'):return
        if u.netloc!='gg-pdr.pl':external.add(u.geturl());return
        path=unquote(u.path);file=R/path.lstrip('/')
        if path.endswith('/'):file=file/'index.html'
        check(file.is_file(),f'Missing local URL {url} from {source}');requests.add(path)
        if u.fragment and file.suffix=='.html':check(unquote(u.fragment) in ids.get(B+path,set()),f'Missing fragment {url} from {source}')
    robot=RobotFileParser();robot.parse((R/'robots.txt').read_text().splitlines())
    for path,text in expected.items():
        check(path.is_file() and path.read_text()==text,'Stale generated file '+str(path.relative_to(R)))
        if path.suffix in ('.md','.txt'):
            counts['markdown_resources' if path.suffix=='.md' else 'llms_resources']+=1
            u=B+'/'+str(path.relative_to(R));requests.add(urlsplit(u).path)
            check(not re.search('lasertechservice|Laser Tech Service|/Users/|webhook',text,re.I),'Cross-project/private data '+str(path))
            for target in re.findall(r'\]\(([^\s)]+)\)',text):
                check(target.startswith(('https://','tel:','mailto:')),'Nonabsolute resource URL '+target);link(target,u)
            for bot in ('Googlebot','bingbot','GPTBot','OAI-SearchBot','ClaudeBot','PerplexityBot'):
                check(robot.can_fetch(bot,u),'Crawler blocked '+bot+' '+u)
    titles=[];descriptions=[];schema_rows=[]
    for p in pages:
        counts['html_pages']+=1;requests.add(urlsplit(p['url']).path)
        tags=p['tags'];meta=p['meta'];url=p['url'];lang=p['lang']
        check(sum(n.tag=='h1' for n in tags)==1,'H1 '+url)
        check(sum(n.tag=='main' for n in tags)==1,'Main '+url)
        pageids=[n.attrs['id'] for n in tags if 'id' in n.attrs];check(len(pageids)==len(set(pageids)),'Duplicate ID '+url)
        titles.append(next(n.text() for n in tags if n.tag=='title'));descriptions.append(meta.get('description'))
        alternate={n.attrs['hreflang']:n.attrs['href'] for n in tags if n.tag=='link' and n.attrs.get('hreflang')}
        check(set(alternate)=={'pl','ru','x-default'} and alternate.get(lang)==url and alternate.get('x-default')==alternate.get('pl'),'Hreflang '+url)
        for l,u in alternate.items():
            check(u in lookup,'Missing alternate '+u)
            if u in lookup:
                other={n.attrs['hreflang']:n.attrs['href'] for n in lookup[u]['tags'] if n.tag=='link' and n.attrs.get('hreflang')}
                check(other==alternate,'Nonreciprocal '+url)
        for key in ('description','og:title','og:description','og:url','og:type','og:image','og:locale','og:locale:alternate','twitter:card','twitter:title','twitter:description','twitter:image'):
            check(bool(meta.get(key)),'Missing '+key+' '+url)
        check(meta.get('og:url')==url,'OG URL '+url)
        check(meta.get('og:locale')==('pl_PL' if lang=='pl' else 'ru_RU'),'OG locale '+url)
        for key in ('og:image','twitter:image'):link(meta[key],url)
        check([n.attrs.get('href') for n in tags if n.tag=='link' and n.attrs.get('rel')=='describedby']==['/llms.txt'],'Discovery '+url)
        for n in tags:
            for key in ('href','src'):
                if n.attrs.get(key):link(n.attrs[key],url)
            for candidate in n.attrs.get('srcset','').split(','):
                if candidate.strip():link(candidate.split()[0],url)
            if n.tag=='img':check(all(n.attrs.get(k) for k in ('alt','width','height','loading')),'Image attributes '+url)
        for raw in ai.SCHEMA_RE.findall(p['source']):
            data=json.loads(raw);counts['json_ld_blocks']+=1
            for obj in walk(data):
                t=obj.get('@type')
                if t:counts['schema_'+str(t)]+=1;schema_rows.append({'type':t,'page':url})
                if obj.get('@id','').startswith(B):check(obj['@id'] in schemaids,'Unresolved schema identity '+obj['@id'])
                check(not any(k in obj for k in ('aggregateRating','review','price','openingHours','award','employee')),'Unsupported schema '+url)
                if t=='AutoRepair':
                    check(obj['@id']==B+'/#business' and obj['url']==B+'/','Business identity '+url)
                    check(obj['telephone']=='+48884012737' and obj['address']['addressLocality']=='Radwanice' and obj['address']['streetAddress']=='ul. Szkolna 55','NAP mismatch '+url)
                    check(all(s in p['source'] for s in obj['sameAs']),'sameAs not visible '+url)
                if t=='FAQPage':
                    visible=ai.faqs(p);actual=[(q['name'],q['acceptedAnswer']['text']) for q in obj['mainEntity']]
                    check(len(visible)==10 and actual==visible,'FAQ visibility mismatch '+url)
                for key in ('url','image','contentUrl'):
                    if isinstance(obj.get(key),str) and obj[key].startswith(B):link(obj[key],url)
        if p['path'].with_suffix('.md') in expected:
            content=p['path'].with_suffix('.md').read_text();plain=norm(re.sub(r'!?\[([^\]]*)\]\([^)]*\)',r'\1',content))
            # Independent extraction confirms the case body did not drift from its JSON source.
            for n in tags:
                if n.tag=='p' and (n.has('case-lead') or n.parent and n.parent.tag=='section' and any(n.parent.all('h2'))):
                    text=n.text()
                    if 'perspektyw' in text and 'Ocenimy' in text or 'ракурсов' in text and 'Предварительно' in text:continue
                    check(norm(text) in plain,'Case Markdown/source mismatch '+url+' '+text[:60]);counts['case_paragraphs_checked']+=1
    check(len(set(titles))==len(pages),'Duplicate titles');check(len(set(descriptions))==len(pages),'Duplicate descriptions')
    ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9','x':'http://www.w3.org/1999/xhtml'};entries=ET.parse(R/'sitemap.xml').findall('s:url',ns);urls=[]
    for entry in entries:
        u=entry.find('s:loc',ns).text;urls.append(u);link(u,B+'/sitemap.xml')
        check(u in lookup and not u.endswith(('.html','.md','.txt')),'Noncanonical sitemap '+u)
        if u in lookup:
            alts={n.attrs['hreflang']:n.attrs['href'] for n in lookup[u]['tags'] if n.tag=='link' and n.attrs.get('hreflang')}
            check({n.get('hreflang'):n.get('href') for n in entry.findall('x:link',ns)}==alts,'Sitemap hreflang '+u)
    check(len(urls)==len(set(urls)) and set(urls)==set(lookup),'Sitemap coverage');counts['sitemap_urls']=len(urls)
    check('Sitemap: '+B+'/sitemap.xml' in (R/'robots.txt').read_text(),'Robots sitemap')
    headers=(R/'_headers').read_text()
    for path in expected:
        if path.suffix=='.md':
            route='/'+str(path.relative_to(R));check(route+'\n  Content-Type: text/markdown; charset=utf-8' in headers,'MD content type '+route)
            if not route.startswith('/ai/'):
                check('Link: <'+B+route.removesuffix('index.md')+'>; rel="canonical"' in headers,'MD canonical '+route)
    # Technical 404 is excluded from discovery and sitemap. Force rules only cover internal files.
    technical=(R/'404.html').read_text()
    check('name="robots" content="noindex"' in technical,'404 must be noindex')
    redirects=[line.split() for line in (R/'_redirects').read_text().splitlines() if line.strip() and not line.startswith('#')]
    check(redirects==[['/docs/*','/404.html','404!'],['/scripts/*','/404.html','404!'],['/README.md','/404.html','404!']],'Unexpected internal routing')
    for local in ('index.html','ru/index.html'):
        original=subprocess.check_output(['git','show','HEAD:'+local],cwd=R).decode()
        current=(R/local).read_text()
        integration=r'<script\s+async.*?</script>\s*<script>.*?</script>'
        check(re.search(integration,original,re.S).group()==re.search(integration,current,re.S).group(),'Analytics changed '+local)
    requests.update(['/robots.txt','/sitemap.xml'])
    http=[]
    if args.http:
        from urllib.request import urlopen
        for path in sorted(requests):
            with urlopen(args.http.rstrip('/')+path,timeout=15) as response:
                check(response.status==200 and response.url==args.http.rstrip('/')+path,'HTTP redirect/error '+path)
                http.append({'path':path,'status':response.status})
    report={'counts':dict(counts),'errors':errors,'http':http,'external_urls':sorted(external),'schema':schema_rows,'browser':'No browser providers returned by cua.getState; desktop/mobile visual QA unavailable.'}
    (R/'docs/ai-search-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'counts':dict(counts),'errors':errors,'http_checks':len(http)},ensure_ascii=False,indent=2))
    return bool(errors)
if __name__=='__main__':sys.exit(main())
