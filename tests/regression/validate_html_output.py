#!/usr/bin/env python3
import json, re
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[2]
data=json.loads((ROOT/'examples/output/example-output.json').read_text(encoding='utf-8'))
assert data['contract_version']=='1.3.0'
body=data['article']['body_html']
assert body and '上記参照' not in body and 'セクション5と同一' not in body
assert data['article']['publishing_format']=='HTML'
assert data['publish']['platform'] in {'HTML','WORDPRESS','HATENA'}
assert not re.search(r'^#{1,6}\s|^```|\[[^]]+\]\([^)]+\)', body, re.M), 'Markdown syntax mixed into HTML'
class P(HTMLParser): pass
P().feed(body)
for tag in ('<p>','<h2>','<a '): assert tag in body
print('HTML output validation: PASS')
