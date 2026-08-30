from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[2]
required=[root/'claude/runtime/ARTICLE_LEARNING_RUNTIME.md',root/'claude/contracts/ARTICLE_LEARNING_CONTRACT.md',root/'claude/templates/ARTICLE_LEARNING_RECORD_TEMPLATE.json',root/'claude/templates/ARTICLE_LEARNING_REPORT_TEMPLATE.json',root/'uat/UAT_HUMAN_FEEDBACK_TEMPLATE.md']
missing=[str(p) for p in required if not p.exists()]
if missing:
 print('MISSING',*missing,sep='\n');sys.exit(1)
r=json.loads((root/'claude/templates/ARTICLE_LEARNING_RECORD_TEMPLATE.json').read_text(encoding='utf-8'))
b=json.loads((root/'claude/templates/ARTICLE_LEARNING_REPORT_TEMPLATE.json').read_text(encoding='utf-8'))
assert r['format']=='SIMS_ARTICLE_LEARNING_RECORD_V1' and r['record_version']=='1.1.0'
assert set(r['human_review']['dimension_scores'])=={'seo_quality','blogger_voice','reader_satisfaction','factual_reliability','monetization_quality','publish_workability'}
assert 'asset_change_candidates' in r['diagnosis']
assert b['format']=='SIMS_ARTICLE_LEARNING_REPORT_V1' and b['batch_size']==10 and b['report_version']=='1.1.0'
assert 'article_history' in b and 'asset_ranking' in b and 'release_assessment' in b
assert b['release_assessment']['recommendation'] in {'RELEASE_CANDIDATE','CONTINUE_UAT','HOLD_RELEASE'}
inst=(root/'claude/PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
assert 'Learning Enhancement v0.7.2' in inst and 'Release Recommendation' in inst
contract=(root/'claude/contracts/ARTICLE_LEARNING_CONTRACT.md').read_text(encoding='utf-8')
for token in ['SEARCH_LIMITATION','BLOG_PROFILE','asset_ranking','RELEASE_CANDIDATE']:
 assert token in contract
print('Learning Enhancement validation: PASS')
