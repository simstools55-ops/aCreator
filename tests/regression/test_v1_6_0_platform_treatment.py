import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def test_identity():
 assert (ROOT/'VERSION').read_text().strip()=='1.7.2'
 assert (ROOT/'SHARED_VERSION').read_text().strip()=='3.3.0'
 ident=json.loads((ROOT/'PRODUCT_IDENTITY.json').read_text())
 assert ident['product_code']=='CREATOR'
def test_contracts():
 for f in ['common-envelope-v1.schema.json','creator-treatment-request-v1.schema.json','creator-treatment-result-v1.schema.json','publication-result-v1.schema.json']:
  json.loads((ROOT/'contracts/platform'/f).read_text())
def test_boundary():
 text=(ROOT/'claude/PROJECT_INSTRUCTIONS.md').read_text()
 assert '直接編集せず' in text and 'Merge Referral' in text and 'Shared Versionは3.3.0' in text
