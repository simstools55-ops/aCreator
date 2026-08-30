from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def test_identity_and_common_validation():
 text=(ROOT/"claude/runtime/QUALITY_GATE_RUNTIME.md").read_text(encoding="utf-8")
 for c in ["VAL-FACT-001","VAL-EVIDENCE-002","VAL-CAUSAL-001","VAL-CONSISTENCY-001","VAL-ENTITY-001","VAL-LINK-001"]: assert c in text
 assert "SIMS_FEEDBACK_V2、Before／Afterは導入しない" in text
