# Citation Candidate Pattern v1.0

## Purpose
完成稿からAI OverviewまたはFeatured Snippetの引用候補になり得る段落を自己診断する。

## Candidate types
- AI_OVERVIEW
- FEATURED_SNIPPET
- FAQ
- COMPARISON_TABLE
- HOWTO_STEPS

## Selection rules
- 最大5件。
- 段落単独で疑問へ答えられる。
- 条件・例外・対象が明確。
- Evidence statusがVERIFIED、USER_PROVIDED、またはNOT_APPLICABLE。
- CTA、広告、未確認体験、過剰約束を含まない。

## Output
- section
- candidate_type
- candidate_summary
- confidence: HIGH / MEDIUM / LOW
- selection_reason
- evidence_refs

## Boundary
候補選定は引用・掲載の保証ではない。公開用本文に「AIに引用される」等の約束を記載しない。
