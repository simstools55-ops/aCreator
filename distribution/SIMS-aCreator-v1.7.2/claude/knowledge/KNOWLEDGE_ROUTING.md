# Knowledge Routing

1. 全件を無条件に本文へ流し込まない。
2. Manifestを読み、`always`と入力条件に合致するKnowledgeだけを有効化する。
3. priorityの小さい順に読み、競合時はPrecedence規則で解決する。
4. Article Type固有知識は、v0.6.0 Pattern Libraryから追加ロードする。
5. 適用したKnowledge IDを内部監査情報として保持する。

- `UAT_QUALITY_ENHANCEMENT_KNOWLEDGE.md`: 実記事UAT由来のHidden Anxiety、Intent Gap、Selection Guidance、Evidence Transparency、HTML出力規則。

- AI Overview / Featured Snippet / citation candidate設計時は `AI_OVERVIEW_STRUCTURE_KNOWLEDGE.md` を読み込む。
