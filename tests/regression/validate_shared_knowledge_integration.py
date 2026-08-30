from pathlib import Path
import hashlib, json, sys
root=Path(__file__).resolve().parents[2]
errors=[]

def validate_snapshot(base):
    manifest_path=base/'SNAPSHOT_MANIFEST.json'
    if not manifest_path.exists(): return [f'missing {manifest_path}']
    m=json.loads(manifest_path.read_text(encoding='utf-8'))
    if m.get('source_repository')!='SIMS-Shared-Editorial-Knowledge': errors.append(f'bad source repository: {base}')
    if m.get('source_version')!='2.5.0': errors.append(f'bad source version: {base}')
    for item in m.get('files',[]):
        p=base/item['path']
        if not p.exists(): errors.append(f'missing snapshot file: {p}')
        elif hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']: errors.append(f'hash mismatch: {p}')
    return errors

validate_snapshot(root/'shared')
validate_snapshot(root/'claude'/'shared')
for rel in ['VERSION','knowledge/intent-analysis.md','knowledge/hidden-anxiety.md','knowledge/evidence-transparency.md','knowledge/faq-evolution.md','knowledge/internal-link-semantics.md','knowledge/serp-entity-preservation.md','mappings/article-creator/application-mapping.md','validation/shared-knowledge-validation.md']:
    a=root/'shared'/rel; b=root/'claude'/'shared'/rel
    if not a.exists() or not b.exists() or a.read_bytes()!=b.read_bytes(): errors.append(f'repository/claude mismatch: {rel}')
pi=(root/'claude'/'PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
kr=(root/'claude'/'runtime'/'KNOWLEDGE_LOAD_RUNTIME.md').read_text(encoding='utf-8')
if 'Shared Knowledge Integration v1.2.2' not in pi: errors.append('project instructions not integrated')
if 'Shared core load' not in kr: errors.append('runtime not integrated')
for forbidden in ['Preservation Scoreを適用する','Rewrite Budgetを適用する','Rewrite Levelを適用する']:
    if forbidden in kr: errors.append(f'writer-only runtime introduced: {forbidden}')
if errors:
    print('SHARED_INTEGRATION_VALIDATION_FAIL')
    print('\n'.join(errors)); sys.exit(1)
print('SHARED_INTEGRATION_VALIDATION_PASS')
