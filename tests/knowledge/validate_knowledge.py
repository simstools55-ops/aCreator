from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[2]
errors=[]
m=json.loads((root/'claude/knowledge/KNOWLEDGE_MANIFEST.json').read_text(encoding='utf-8'))
if m.get('format')!='SIMS_ARTICLE_CREATOR_KNOWLEDGE_MANIFEST_V1': errors.append('manifest format')
ids=[]
for e in m.get('entries',[]):
    ids.append(e.get('id'))
    if not (root/'claude/knowledge'/e.get('file','')).exists(): errors.append('missing '+str(e.get('file')))
    if not isinstance(e.get('priority'),int): errors.append('priority '+str(e.get('id')))
    if e.get('status') not in ('active','deprecated'): errors.append('status '+str(e.get('id')))
if len(ids)!=len(set(ids)): errors.append('duplicate id')
pri={e['id']:e['priority'] for e in m['entries']}
if not (pri['K-SAFETY'] < pri['K-SEO']): errors.append('precedence safety/seo')
for p in root.rglob('*'):
    if p.is_file() and p.suffix.lower() in ('.md','.json','.py','.txt','.csv'):
        try: t=p.read_text(encoding='utf-8')
        except Exception as ex: errors.append('utf8 '+str(p)); continue
        if p.name != 'validate_knowledge.py' and ('SIMS-Writer-v' in t or '../SIMS-Writer' in t): errors.append('writer dependency '+str(p))
print('PASS' if not errors else 'FAIL')
for x in errors: print(x)
sys.exit(1 if errors else 0)
