from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[2]
manifest=json.loads((root/'claude/patterns/PATTERN_MANIFEST.json').read_text(encoding='utf-8'))
assert manifest['format']=='SAC_PATTERN_MANIFEST_V1'
ids=set()
for p in manifest['patterns']:
    assert p['id'] not in ids
    ids.add(p['id'])
    f=root/'claude/patterns'/p['file']
    assert f.exists(), f
    text=f.read_text(encoding='utf-8')
    standard=['## 適用対象','## 推奨構成','## 必須品質ゲート','## Evidenceルール','## 合成ルール']
    auxiliary=['## Purpose','## Rules']
    assert all(h in text for h in standard) or all(h in text for h in auxiliary), f
assert len(ids)>=8
for req in ['PATTERN_INDEX.md','PATTERN_ROUTING.md','PATTERN_COMPOSER_RULES.md']:
    assert (root/'claude/patterns'/req).exists()
print('PATTERN_VALIDATION_PASS',len(ids))
