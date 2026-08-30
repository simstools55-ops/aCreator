#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[2]
errors=[]
required_files=[
 'claude/knowledge/BLOG_PROFILE_AND_AUTHOR_VOICE.md','claude/knowledge/AFFILIATE_ARTICLE_KNOWLEDGE.md',
 'claude/runtime/MONETIZATION_ROUTER_RUNTIME.md','claude/runtime/EDITORIAL_VOICE_RUNTIME.md','claude/runtime/PUBLISH_MODE_RUNTIME.md',
 'claude/templates/BLOG_PROFILE_TEMPLATE.md','claude/templates/AUTHOR_PROFILE_TEMPLATE.md','claude/templates/AFFILIATE_INPUT_TEMPLATE.md']
for f in required_files:
 if not (ROOT/f).exists(): errors.append('missing '+f)
out=json.loads((ROOT/'examples/output/example-output.json').read_text(encoding='utf-8'))
body=out['article']['body_html']
checks={
 'golden keyword':out['input_summary']['main_keyword']=='ピアノ講座 口コミ',
 'affiliate type':out['monetization']['type']=='AFFILIATE',
 'pr disclosure':'アフィリエイトリンク' in body and out['monetization']['pr_disclosure_inserted'],
 'affiliate links':body.count(out['monetization']['affiliate_url'])==out['monetization']['affiliate_link_count'],
 'full body':len(body)>300 and '上記' not in body,
 'editorial voice':out['editorial_voice']['editorial_opinion_used'],
 'no fabricated experience':not out['editorial_voice']['first_party_experience_used'],
 'copy ready':out['publish']['copy_ready']}
for k,v in checks.items():
 if not v: errors.append(k)
if errors:
 print('FAIL v0.7.0'); [print(' -',e) for e in errors]; sys.exit(1)
print('PASS v0.7.0 quality and golden article regression')
