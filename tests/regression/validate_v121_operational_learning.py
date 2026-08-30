from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def test_versions():
 assert (ROOT/"VERSION").read_text().strip()=="1.2.1"
 assert (ROOT/"shared/VERSION").read_text().strip()=="1.1.1"
def test_runtime_markers():
 q=(ROOT/"claude/runtime/QUALITY_GATE_RUNTIME.md").read_text(encoding="utf-8")
 assert "Central claim evidence" in q and "Marketplace listing" in q
