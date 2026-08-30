from pathlib import Path

def test_creator_snapshot_excludes_writer_mapping():
    root=Path(__file__).resolve().parents[2]
    s=root/'claude'/'shared'
    assert not (s/'mappings'/'writer').exists()
    assert (s/'mappings'/'article-creator').exists()
    assert 'article-creator' in (s/'SNAPSHOT_SCOPE.json').read_text(encoding='utf-8')
