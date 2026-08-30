from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
CLAUDE=ROOT/'claude'

def test_versions():
    assert tuple(map(int, (ROOT/'VERSION').read_text().strip().split('.'))) >= (1,3,0)
    assert (ROOT/'SHARED_VERSION').read_text().strip() == '3.3.0'
    assert tuple(map(int, (CLAUDE/'VERSION').read_text().strip().split('.'))) >= (1,3,0)
    assert (ROOT/'shared/VERSION').read_text().strip()=='2.5.0'

def test_pre_publish_gate_present():
    q=(CLAUDE/'runtime/QUALITY_GATE_RUNTIME.md').read_text(encoding='utf-8')
    for term in ['Pre-Publish Quality Gate','Freshness Gate','Promise Gate','Numeric Consistency Gate','Output Sync Gate']:
        assert term in q

def test_howto_and_faq_patterns_in_snapshot():
    assert (ROOT/'shared/patterns/howto-evidence-strength-heading-pattern.md').exists()
    assert (ROOT/'shared/patterns/faq-query-normalization-pattern.md').exists()

def test_identity_lock_preserved():
    scope=json.loads((ROOT/'shared/SNAPSHOT_SCOPE.json').read_text())
    assert scope['target_product']=='article-creator'
    assert scope['excluded_mapping']=='writer'

def test_no_writer_runtime_added():
    p=(CLAUDE/'PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
    assert 'Never load or apply `mappings/writer/`' in p
