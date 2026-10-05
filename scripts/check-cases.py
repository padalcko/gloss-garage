"""Check all static routes, new case SEO/images, sitemap and preservation boundaries.
Run: PYTHONPATH=/tmp/ltsmarket-image-tools python3 scripts/check-cases.py
Optional --http http://127.0.0.1:8766 verifies local HTTP without redirects.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import xml.etree.ElementTree as ET
import json,re,subprocess,sys
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]; BASE='https://gg-pdr.pl'; errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__();self.tags=[];self.stack=[];self.feed(s);check(not self.stack,'Unclosed HTML: '+str(self.stack))
 def handle_starttag(self,t,a):
  self.tags.append((t,dict(a)))
  if t not in ('area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'):self.stack.append(t)
 def handle_startendtag(self,t,a):self.tags.append((t,dict(a)))
 def handle_endtag(self,t):
  check(bool(self.stack) and self.stack[-1]==t,'Invalid nesting: '+t+' in '+str(self.stack[-3:]))
  if self.stack:self.stack.pop()
 def attrs(self,t):return [a for tag,a in self.tags if tag==t]
paths=list(ROOT.rglob('*.html')); pages={};sources={}
for p in paths:
 route='/'+str(p.relative_to(ROOT)).removesuffix('index.html');s=p.read_text();sources[route]=s;pages[route]=Page(s)
requests=set(pages)
for route,p in pages.items():
 check(len(p.attrs('h1'))==1,route+' H1 count')
 ids=[a['id'] for _,a in p.tags if 'id' in a];check(len(ids)==len(set(ids)),route+' duplicate IDs')
 for tag,a in p.tags:
  for key in ('href','src'):
   if key not in a:continue
   u=urlsplit(a[key]);path=unquote(u.path)
   if u.scheme and u.netloc!='gg-pdr.pl':continue
   if u.netloc and u.netloc!='gg-pdr.pl':continue
   if not path:path=route
   if not path.startswith('/'):continue
   local=ROOT/path.lstrip('/');local=local/'index.html' if path.endswith('/') else local
   check(local.is_file(),route+' missing '+a[key]);requests.add(path)
   if u.fragment and local.suffix=='.html':check(re.search(r'id=[\"\x27]'+re.escape(u.fragment)+r'[\"\x27]',local.read_text()),route+' missing anchor '+a[key])
  if tag=='img' and '/realizacje/' in a.get('src',''):
   check(all(a.get(k) for k in ('alt','width','height','srcset','sizes','loading','decoding')),route+' image attributes')
   for candidate in a['srcset'].split(','):
    file,width=candidate.strip().split();im=Image.open(ROOT/file.lstrip('/'));check(im.width==int(width[:-1]),file+' width mismatch');check(not im.getexif() and 'exif' not in im.info,file+' metadata');requests.add(file)
 check(sum('gtag/js?' in a.get('src','') for a in p.attrs('script'))==1,route+' GA4 duplication/missing')
 canonical=[a['href'] for a in p.attrs('link') if a.get('rel')=='canonical'];check(canonical==[BASE+route],route+' canonical')
 for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>',sources[route],re.S):json.loads(raw)
seo=json.loads((ROOT/'docs/cases-seo.json').read_text());titles=[];descs=[]
for row in seo:
 route=row['url'].removeprefix(BASE);p=pages[route];s=sources[route];lang='ru' if route.startswith('/ru/') else 'pl'
 check(p.attrs('html')[0]['lang']==lang,route+' language')
 actual={a['hreflang']:a['href'] for a in p.attrs('link') if a.get('rel')=='alternate'};check(actual==row['hreflang'],route+' hreflang')
 for l,u in actual.items():
  target=pages[u.removeprefix(BASE)];back={a['hreflang']:a['href'] for a in target.attrs('link') if a.get('rel')=='alternate'};check(back.get(lang)==row['url'],route+' reciprocal '+l)
 titles.append(row['title']);descs.append(row['description'])
 check('/js/script.js' not in s,route+' unnecessary form JS')
 check('https://wa.me/380667835184' in s and 'tel:+48884012737' in s,route+' contact preservation')
 schema=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',s,re.S).group(1));check([x['@type'] for x in schema['@graph']]==['WebPage','BreadcrumbList'],route+' schema')
 check(not re.search(r'"(?:datePublished|aggregateRating|review|price|offers)"',json.dumps(schema)),route+' invented schema')
 check(p.attrs('img')[0]['loading']=='eager',route+' first image lazy')
 check(all(a['loading']=='lazy' for a in p.attrs('img')[1:]),route+' subsequent image not lazy')
check(len(set(titles))==8 and len(set(descs))==8,'Unique SEO')
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9','x':'http://www.w3.org/1999/xhtml'};tree=ET.parse(ROOT/'sitemap.xml');locs=[]
for url in tree.findall('s:url',ns):
 loc=url.find('s:loc',ns).text;locs.append(loc);route=loc.removeprefix(BASE);check(route in pages,'Sitemap missing route '+loc)
 check(not loc.endswith('.html'),'Sitemap html URL '+loc)
 mapping={a.attrib['hreflang']:a.attrib['href'] for a in url.findall('x:link',ns)}
 expected={a['hreflang']:a['href'] for a in pages[route].attrs('link') if a.get('rel')=='alternate'};check(mapping==expected,'Sitemap alternates '+loc)
check(len(locs)==len(set(locs))==10,'Sitemap count');check(set(locs)=={BASE+r for r in pages},'Sitemap coverage')
for file in ['styles/style.css','js/script.js','robots.txt']:
 check((ROOT/file).read_bytes()==subprocess.check_output(['git','show','HEAD:'+file],cwd=ROOT),file+' modified')
# The PL home is unchanged except the service anchor and one gallery link.
original=subprocess.check_output(['git','show','HEAD:index.html'],cwd=ROOT).decode()
expected=original.replace('<section class="section">','<section class="section" id="pdr">',1)
expected=expected.replace('          </div>\n\n          <div class="gallery__grid">','            <p><a class="btn btn--black" href="/realizacje/">Zobacz realizacje</a></p>\n          </div>\n\n          <div class="gallery__grid">',1)
check((ROOT/'index.html').read_text()==expected,'PL scope changed')
# RU translation keeps form fields and constraints, links and integration identifiers.
old=Page(original);ru=pages['/ru/']
for tag in ('input','textarea','form'):
 def structural(p):return [{k:v for k,v in a.items() if k not in ('placeholder',)} for a in p.attrs(tag)]
 check(structural(old)==structural(ru),'RU form structure '+tag)
http=[]
if '--http' in sys.argv:
 from urllib.request import urlopen
 base=sys.argv[sys.argv.index('--http')+1].rstrip('/')
 for path in sorted(requests):
  with urlopen(base+path,timeout=15) as response:
   check(response.status==200 and response.url==base+path,'HTTP redirect/error '+path);http.append({'path':path,'status':response.status})
report={'html_pages':len(pages),'case_pages':len(seo),'sitemap_urls':len(locs),'webp_files':len(list((ROOT/'images/realizacje').glob('*.webp'))),'http':http,'errors':errors,'browser':'Unavailable: neither chrome nor iab provider is connected. Viewport, console and CWV checks not run.'}
(ROOT/'docs/cases-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({**report,'http':len(http)},ensure_ascii=False,indent=2));sys.exit(bool(errors))
