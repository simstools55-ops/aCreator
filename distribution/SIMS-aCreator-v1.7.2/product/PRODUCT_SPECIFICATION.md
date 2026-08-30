# Product Specification v1.0.0

## 製品目的
メインキーワードから、記事企画、根拠計画、構成、完成本文、品質報告、公開判定、構造化JSONを一貫生成する。

## 対象利用者
個人ブロガー、AdSense運営者、アフィリエイト運営者。WordPress・はてなブログ等で利用できる編集成果物を提供する。

## 必須成果物
- Keyword / Search Intent分析
- Reader Problem Model
- Pattern選択・合成
- Editorial Brief
- Coverage Map / Evidence Plan
- SEOタイトル・メタディスクリプション
- H2/H3構成
- 完成本文
- 必要な場合のFAQ・内部リンク・収益導線
- Quality Report / Publication Decision
- SIMS_ARTICLE_CREATOR_V1 JSON Output
- Article Learning Record

## Runtime
R00 InitializeからR18 Publish Mode Output and JSONまでの制御された工程を使用する。Risk & Sufficiency、Evidence Verification、Quality Audit、Publication Gateは省略不可。

## Knowledge / Pattern
Knowledge ManifestとPrecedenceに従って必要資産だけをロードする。8種類のPrimary PatternをPattern Composerで組み合わせ、共通のIntent-first、FAQ補完、内部リンク関連性、資産保護、YMYL Safety規則を適用する。

## Contract
- JSON Contract: 1.2.0
- Learning Record: 1.1.0
- 破壊的変更はMajor versionでのみ行う。

## Safety
医療・健康、金融、法律、安全、重大な生活判断ではSafety Knowledgeを優先する。診断、保証、根拠のない因果説明を禁止し、必要に応じてNEEDS_EXPERT_REVIEWまたはBLOCKEDとする。

## Learning Governance
SWLSは監査可能な改善候補抽出システムであり、自動自己改変を行わない。人間確認済みの記録と回帰テストを正式変更の条件とする。

## 非機能要件
- SIMS Writer非依存
- 日本語Single Source of Truth
- UTF-8
- JSON互換性
- 警告保持
- 捏造防止
- YMYL慎重化
- 再現可能な工程
- GitHub上書き可能な完全配布

## リリース判定
実記事UAT 10記事と追加YMYL試験を完了し、v1.0.0をOfficial Baselineとして承認する。
