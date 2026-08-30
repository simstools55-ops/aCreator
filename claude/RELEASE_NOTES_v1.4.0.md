# SIMS Article Creator v1.4.0 Release Notes

Release date: 2026-08-01

## Scope
実記事実証試験で承認された6項目を、Creator専用の正式仕様として実装した。SharedスナップショットとWriter用mappingは変更していない。

## Added
- Section Depth Weighting Pattern
- Multi-Concept Relationship Diagram Pattern
- Search-intent-readable H2 rule
- Internal-link candidate status (`CANDIDATE_TOPIC` / `CONFIRMED`)
- Freshness expression standard
- R16.5 SERP Self-Review

## Runtime behavior
R16 Quality Audit後、R16.5で検索意図、CTR、タイトル、H2、Featured Snippet、AI Overview適性を点検し、必要に応じてR11、R13、R15へ差し戻す。

## Compatibility
- SIMS_ARTICLE_CREATOR_V1 JSON contract: unchanged
- SIMS_ARTICLE_LEARNING_RECORD_V1: unchanged
- Shared Editorial Knowledge snapshot: unchanged
- Writer mapping: not loaded, not modified
