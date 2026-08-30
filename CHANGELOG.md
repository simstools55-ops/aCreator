## v1.7.2 - 2026-08-30
- Consolidated user-facing naming to aCreator / SIMS Manager; internal contracts unchanged.

# Changelog

## [1.6.0] - 2026-08-05
- Adopted SIMS Editorial Platform treatment contracts.
- Synced product-scoped Shared Editorial Knowledge 3.3.0 assets.
- Added CaseID, Treatment Request ID and Draft Article ID preservation rules.
- Added SBM-routed follow-up referrals for Writer and Merge.
- Preserved legacy SIMS_ARTICLE_CREATOR_V1 article generation output.
- Added repository and Claude package identity metadata.

## 1.4.0 - 2026-08-01
- Creator quality controls implemented from Phase 2 real-article validation.
- Added two auxiliary patterns, three knowledge extensions, and R16.5 SERP Self-Review.
- Updated Claude Project package to v1.4.0.
- Shared snapshot remains unchanged.

# 1.2.3 - Shared Validation Sync

- Shared Snapshot v1.3.0へ更新
- 共通ValidationをQuality Gateへ接続
- Identity LockとHTML出力Contractを維持

# Changelog

## 1.2.2 - 2026-07-23

### Fixed
- Excluded Writer mapping from Article Creator Shared snapshot.
- Added Creator identity lock and snapshot scope metadata.
- Added regression test for product boundary.

## 1.2.1 - 2026-07-22
- 運用試験LearningをEvidence・Definition・Buying Guide Runtimeへ反映。
- Marketplace Evidence Level、Source Scope、Central Claim優先検証を追加。
- Publication GateとLearning root causeを整理。
- Shared Editorial Knowledge v1.1.1へ同期。

## 1.2.0 - 2026-07-21

- SIMS-Shared-Editorial-Knowledge v1.1.0を読取専用スナップショットとして統合
- Repository版とClaude Project版へ`shared/`を追加
- Sharedを共通編集知識のSingle Source of TruthとしてRuntimeへ接続
- Creator専用Knowledge、Pattern、Contract、出力形式を維持
- Shared Snapshot SHA-256検証とRepository/Claude同一性検証を追加
- v1.1.0のJSON Contract、HTML、Learning、UAT回帰互換を確認

## [1.1.0] - 2026-07-20

### Changed
- 公開用完成記事の標準形式をMarkdownからHTMLへ変更
- JSON Contractを1.3.0へ更新し、`article.body_html`を`article.body_html`へ移行
- Review、Buying Guide、Local Guide、HowToの実記事UAT知見をPattern Libraryへ反映
- robots制限時のEvidence PolicyとPublication Gate判定を調整

### Added
- Hidden Anxiety Pattern、Selection Guidance、Intent Gap／代替提案ルール
- 意思決定支援表（不安→確認事項→判断基準）
- 文脈型内部リンクとReview記事の競合比較モジュール
- HTML出力回帰テストとv1.1.0運用試験反映レポート

## [1.0.1] - 2026-07-20

### Fixed
- Claude Project上のKnowledge資産をローカルファイルパスとして扱う誤解を修正
- Project Knowledge参照失敗時の再検索・Safety Coreフォールバックを追加
- robots制限時の公式情報優先フォールバック手順を追加
- First-party Experience未提供時の疑似体験表現を抑止

### Added
- Project Knowledge Binding回帰テスト
- 実運用不具合記録 `UAT_Runtime_Incident_2026-07-20.md`

## 1.0.0 - 2026-07-20 - Official Baseline
- 実記事UAT 10記事と追加YMYL試験の結果を正式反映
- UAT Final ReportとSWLS Final Learning Reportを追加
- Pattern Library Update v1.1、Knowledge Update v1.1を正式化
- Runtime Improvement Proposal v1.1を追加
- README、Product Specification、Release Notesを正式版へ更新
- VERSION、Validation Report、Claude Project配布資産を同期
- JSON Contract v1.2.0とLearning Record v1.1.0を正式採用

## 0.7.2 - Learning Enhancement
- Learning Record v1.1.0へ更新
- 詳細な原因分類を追加
- 6項目の人間評価を追加
- asset_change_candidatesを追加
- 10記事レポートにarticle_historyとasset_rankingを追加
- Release Recommendation基準を実装
- UAT Human Feedbackテンプレートを拡張


## 0.7.1 - Learning Foundation
- Added per-article SIMS_ARTICLE_LEARNING_RECORD_V1 output.
- Added provisional and confirmed UAT record states.
- Added ten-record SIMS_ARTICLE_LEARNING_REPORT_V1 aggregation.
- Added human feedback template and asset-level root-cause routing.
- Added governance rules preventing unapproved automatic self-modification.
- Updated Article Creator contract to 1.2.0.

## 0.7.0 - 2026-07-19
- Personal Blogger Edition基盤を追加
- Runtime Lock、Monetization Router、Editorial Voice、Publish Modeを追加
- Blog Profile / Author Profile / Affiliate Inputテンプレートを追加
- Review Pattern 2.0とGolden Article「ピアノ講座 口コミ」回帰テストを追加
- Input/Output Contractを1.1.0へ拡張
- PR表記、アフィリエイトリンク、body_html完全性の品質ゲートを強化

## 0.6.0 - UAT Prototype
- 8種類のPattern Libraryを実装
- Pattern Manifest / Routing / Composer Rulesを追加
- Pattern Composer RuntimeをEditorial Pipelineへ統合
- UAT Request、Evaluation Sheet、Editorial Learning Recordを追加
- Pattern/UAT静的検証を追加
- Claude Project投入用プロトタイプを整備


## [0.5.0] - 2026-07-19

### Added
- Knowledge Architecture v1.0
- Knowledge Index、Manifest、Routing、Precedence、Conflict Resolution
- Search Intent、Reader Model、Helpful Content、E-E-A-T、SEO、Evidence、Freshness、Safety、YMYL、Readability、Originality、Internal Link、Monetization Knowledge
- Claim ClassificationとSource Quality階層
- Knowledge Load Runtime
- KnowledgeテストとManifest検証
- Claude Project Instructions

### Changed
- READMEの版表示と開発状況を修正
- Runtimeのロード順序をKnowledge Architecture対応へ更新
- Editorial CoreからKnowledgeへの参照境界を明文化

## [0.4.0] - 2026-07-19

### Added
- Editorial Core、Coverage Engine、Reader Journey Engine
- Evidence Gate、Fabrication Prevention
- Editorial Review、Publication Readiness Gate
- Quality Frameworkと関連テスト

## [0.3.0] - 2026-07-19

### Added
- Input / Output Specification
- SIMS_ARTICLE_CREATOR_V1 JSON Contract
- JSON Schema、Reason Codes、Warning Codes、Examples、Contract Test

## [1.5.0] - 2026-08-01
### Added
- Section PriorityをCoverage Map・Outline・Runtimeへ統合。
- AI Overview Structure Knowledge、Copy Template Pattern、Citation Candidate Pattern。
- SERP Self-Reviewの5段階評価とcitation_candidates。
- 内部リンク候補のanchor・placement・priority・reason標準化。
- Learning Recordへ予測引用セクションを追加。
