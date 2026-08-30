# aCreator v1.7.2

# aCreator

aCreatorは、メインキーワードからEditorial Brief、Pattern、Coverage、Evidence Plan、記事本文、編集審査、公開判定、構造化JSONを生成する独立製品です。

## 正式バージョン
`v1.7.2`

## 中核フロー
入力検証 → Keyword Intelligence → Search Intent → Reader Model → Pattern Selection / Composer → Risk & Evidence → Editorial Brief → Coverage Map → Blueprint → Writing → Editorial Review → Publication Gate → JSON

## 主な機能
- 8種類のPattern Library
- Knowledge Architectureとロード優先順位
- Evidence Gate / Fabrication Prevention
- Safety / YMYL Gate
- Personal Blogger向けEditorial Voice / Publish Mode
- AdSense / Affiliate分岐
- JSON Contract v1.4.0
- SWLS Learning Record / 10記事Learning Report

## 主要ディレクトリ
- `claude/`：Claude Project投入用の正式資産
- `docs/`：設計・仕様・Release Notes
- `product/`：製品仕様、品質方針、UAT/SWLS報告
- `uat/`：UAT依頼・評価・Learningテンプレート
- `tests/`：契約、Knowledge、Pattern、Quality、Learning、回帰テスト
- `distribution/`：配布成果物用

## セットアップ
Claude Projectには、配布版ZIPの中身を既存ファイルと混在させず全置換してください。`claude/PROJECT_INSTRUCTIONS.md`をProject Instructionsへ設定し、`claude/shared/`と`claude/knowledge/`以下をKnowledgeとして投入します。Sharedは読取専用スナップショットです。

## UATと学習
SWLSは自動再学習ではありません。記事ごとのLearning Recordを人間が確認し、10件単位のLearning Reportで再発傾向を監査してから、Runtime・Knowledge・Pattern・Contract・Templateの改善候補へ昇格します。

## 品質と安全
根拠不足、体験捏造、意図不整合、過剰CTA、リンク欠落、本文未格納をPublication Gateで検出します。YMYLではSEOよりSafetyと専門家確認を優先します。

## 製品境界
aWriter、SIMS Managerとは別リポジトリ・別Claude Projectとして運用し、実行時依存を持ちません。

## リリース情報
- [Release Notes v1.1.0](docs/release-notes/RELEASE_NOTES_v1.1.0.md)
- [UAT Final Report](product/reports/UAT_FINAL_REPORT_v1.1.0.md)
- [SWLS Final Learning Report](product/reports/SWLS_FINAL_LEARNING_REPORT_v1.1.0.md)


## Shared Knowledge Integration

共通編集知識の唯一の正本は`SIMS-Shared-Editorial-Knowledge`です。本リポジトリの`shared/`および`claude/shared/`はv1.1.0正本から生成したスナップショットで、直接編集は禁止です。Creator固有の新規記事生成Knowledge、Pattern、Runtime、Contractは従来どおり本製品で管理します。


## v1.2.2
Evidence表現と購入記事の販売者確認を運用試験結果に基づき強化しました。

## v1.4.0 Creator Quality Controls
- 見出し重要度による文章量制御
- 複数概念の比較表・関係図提案
- 番号非依存の検索意図型H2
- Internal Link Candidate状態管理
- Freshness表現標準化
- R16.5 SERP Self-Review

Sharedスナップショットは変更せず、Creator専用資産のみ更新しています。

## v1.5.0 highlights
- Section Priority Engine
- Copy-ready Template Blocks
- AI Overview / Featured Snippet Citation Candidates
- Detailed Internal Link Candidate Planning
- Five-point SERP Self-Review
- Citation Prediction Learning Records


## v1.6.2 Platform Treatment Integration
- SIMS Editorial Platform 1.xへ接続
- Shared Editorial Knowledge 3.3.0へ同期
- SBM発行のCaseID、Treatment Request ID、Draft Article IDを保持
- `SIMS_CREATOR_TREATMENT_REQUEST_V1` / `SIMS_CREATOR_TREATMENT_RESULT_V1`へ対応
- 既存の`SIMS_ARTICLE_CREATOR_V1`記事生成Contractを後方互換として維持
- Writer・Mergeへの後続処置は直接実行せず、SBMへReferral候補として返却
