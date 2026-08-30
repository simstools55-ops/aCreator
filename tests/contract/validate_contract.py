#!/usr/bin/env python3
from pathlib import Path
import json, sys
try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    print("jsonschema が必要です: pip install jsonschema")
    sys.exit(2)
ROOT=Path(__file__).resolve().parents[2]
cases=[
 (ROOT/'claude/contracts/schemas/article-creator-input.schema.json',ROOT/'examples/input/example-input.json'),
 (ROOT/'claude/contracts/schemas/article-creator-output.schema.json',ROOT/'examples/output/example-output.json')]
failed=False
for schema_path,data_path in cases:
 schema=json.loads(schema_path.read_text(encoding='utf-8'))
 data=json.loads(data_path.read_text(encoding='utf-8'))
 errors=sorted(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(data),key=lambda e:list(e.path))
 if errors:
  failed=True
  print(f'FAIL: {data_path.name}')
  for e in errors: print(' -','/'.join(map(str,e.path)),e.message)
 else: print(f'PASS: {data_path.name}')
sys.exit(1 if failed else 0)
