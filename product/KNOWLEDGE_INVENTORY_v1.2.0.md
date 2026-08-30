# Knowledge Inventory and Classification v1.2.0

## Sharedへ移行・共通利用

| Shared Knowledge | Creatorでの適用 |
|---|---|
| intent-analysis | 検索意図、Intent Gap、構成範囲 |
| hidden-anxiety | 未解決不安、注意点、FAQ候補 |
| serp-entity-preservation | SEOタイトル・H1・本文の主要エンティティ整合 |
| evidence-transparency | 根拠強度、未確認表示、公開判定 |
| internal-link-semantics | 文脈型内部リンクの関連性評価 |
| faq-evolution | 本文で未解決の質問だけをFAQ化 |
| decision-support | 比較軸、選び方、次の行動 |
| conditional-editorial-opinion | 根拠付き編集意見 |
| freshness-safety | 時点情報、更新確認、安全側判断 |

## Article Creator専用として維持

- Article Outline Generation
- Initial Heading Planning
- First Draft Strategy
- Intro Generation
- Conclusion Generation
- Article Blueprint / Coverage Map
- Individual Blogger Voice
- Affiliate Article Generation / CTA
- Monetization Balance
- Publish Mode HTML Packaging
- Article Learning Record

既存`claude/knowledge/`はCreator専用適用層および互換フォールバックとして維持する。Sharedと重なる判断ではSharedを共通正本として優先し、Creator Knowledgeは新規記事生成への具体化だけを担う。

## Writer専用であり導入しない

- Preservation Score
- Rewrite Budget / Change Budget
- Rewrite Level / Rewrite Scope
- Existing Content Protection
- Existing Internal Link Preservation
- GSC診断に基づく既存記事改善制御

## Pattern Libraryの扱い

既存Pattern Libraryは新規記事生成専用のためCreator側に残す。Shared Knowledgeの判断結果をPattern選択へ入力するが、PatternファイルそのものはSharedへ移動しない。

## Validation Knowledgeの扱い

共通知識スナップショットの完全性検証はShared由来とし、Article CreatorのContract・HTML・Learning・UAT検証はCreator専用として維持する。
