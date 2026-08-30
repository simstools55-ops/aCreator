from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[2]
errors=[]
for p in root.rglob('*'):
    if p.is_file():
        try: p.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            if p.suffix not in {'.zip'}: errors.append(f'UTF-8: {p}')
for p in root.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'JSON: {p}: {e}')
required=[
 'docs/editorial-core-architecture.md','docs/quality-framework.md',
 'claude/runtime/EDITORIAL_CORE_RUNTIME.md','claude/runtime/QUALITY_GATE_RUNTIME.md',
 'tests/quality/QUALITY_TEST_CASES.md']
for r in required:
    if not (root/r).exists(): errors.append(f'MISSING: {r}')
if errors:
    print('FAIL'); print('\n'.join(errors)); sys.exit(1)
print('PASS')
