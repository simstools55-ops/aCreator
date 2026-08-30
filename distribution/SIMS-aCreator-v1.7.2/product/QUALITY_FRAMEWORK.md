# Product Quality Framework

SIMS Article Creator uses stage-specific gates rather than one final score.

- Planning Gate
- Coverage Gate
- Evidence Gate
- Draft Quality Gate
- Editorial Review Gate
- Publication Gate

A stage may return PASS, PASS_WITH_WARNING, NEEDS_REVISION, NEEDS_EVIDENCE, NEEDS_EXPERT_REVIEW or BLOCKED.


## Shared v1.3.0 Common Validation

公開前にVAL-FACT-001、VAL-EVIDENCE-002、VAL-CAUSAL-001、VAL-CONSISTENCY-001、VAL-ENTITY-001、VAL-LINK-001を適用する。Creator Identity Lockを維持し、Query Coverage、QUERY_MIX、Winner Query Preservation、SIMS_FEEDBACK_V2、Before／Afterは導入しない。

## Pre-Publish Quality Gate v1.3.0
公開前にEvidence Strength、Freshness、Promise、Numeric Consistency、Concept Separation、FAQ Query、Internal Link Semantics、Output Syncを一括検査する。重大不一致が残る場合はPASSを禁止する。
