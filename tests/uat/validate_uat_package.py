from pathlib import Path
import json
root=Path(__file__).resolve().parents[2]
required=['uat/README.md','uat/UAT_REQUEST_TEMPLATE.md','uat/UAT_EVALUATION_SHEET.md','uat/EDITORIAL_LEARNING_RECORD_TEMPLATE.json','claude/runtime/PATTERN_COMPOSER_RUNTIME.md']
for rel in required: assert (root/rel).exists(), rel
j=json.loads((root/'uat/EDITORIAL_LEARNING_RECORD_TEMPLATE.json').read_text(encoding='utf-8'))
assert j['format']=='SIMS_EDITORIAL_LEARNING_RECORD_V1'
print('UAT_PACKAGE_VALIDATION_PASS')
