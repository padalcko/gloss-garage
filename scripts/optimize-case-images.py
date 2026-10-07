"""Resize and encode authentic source photos; requires Pillow with WebP support."""
from PIL import Image, ImageOps
from pathlib import Path
import json,sys,argparse
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('source',type=Path)
parser.add_argument('--manifest',type=Path,help='JSON mapping slug to ordered original filenames; overrides legacy photo groups')
args=parser.parse_args();source=args.source
groups=[('volkswagen-tiguan-pdr-prawy-tylny-blotnik',['18ED3312-F1C0-4D1A-872B-8C902340F66E','ADF70FFF-A853-4FBC-B9B2-2F2A743376FB','C30B8DB6-AEBB-4B01-B3BA-18FB1F45CE1B','3FA86D0D-3D2D-4D70-9CDB-F4E3763DDB1B']),('toyota-corolla-pdr-prawe-przednie-drzwi',['97DAB8BB-26C9-4FDB-A3BC-008419A1B07A','08D81894-BA01-4A30-AE20-D4973AC1C599']),('audi-a4-pdr-przedni-prawy-blotnik',['D3F01399-A227-49CB-9B55-0F953254F3C3','F4676386-C695-4DD1-AC3D-1AA886C434C7','A55F1895-C1D8-4394-ACC9-2F1ED21AC8C2','D41491B1-7010-40E6-B3B4-9332163C05FC'])]
if args.manifest:
 groups=list(json.loads(args.manifest.read_text()).items())
else:
 groups=[(slug,[name+'.PNG' for name in names]) for slug,names in groups]
out=root/'images/realizacje';out.mkdir(exist_ok=True)
previous=root/'docs/image-audit.json'
replaced={slug for slug,_ in groups}
rows=[row for row in json.loads(previous.read_text()) if row['slug'] not in replaced] if previous.exists() else []
for slug,ids in groups:
 for n,id in enumerate(ids,1):
  p=source/id; original=Image.open(p); im=ImageOps.exif_transpose(original).convert('RGB'); variants=[]
  for w in (360,540,768,1086):
   resized=im.resize((w,round(im.height*w/im.width)),Image.Resampling.LANCZOS)
   name=f'{slug}-{n:02}-{w}.webp'; dest=out/name; resized.save(dest,'WEBP',quality=88,method=6)
   check=Image.open(dest);assert not check.getexif() and 'exif' not in check.info
   variants.append({'file':'images/realizacje/'+name,'width':w,'height':resized.height,'bytes':dest.stat().st_size})
  rows.append({'original':p.name,'slug':slug,'number':n,'width':original.width,'height':original.height,'bytes':p.stat().st_size,'variants':variants})
(root/'docs/image-audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Photos:',len(rows),'Original:',sum(x['bytes'] for x in rows),'All variants:',sum(v['bytes'] for x in rows for v in x['variants']))
