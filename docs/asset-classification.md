# SIMS Article Creator 設計フェーズ1

## SIMS Writer資産分類・独立化方針

対象：SIMS Writer v1.0.0 Baseline Repository / Claude Project

## 1. 結論

SIMS Writerは新製品の良質な基盤として利用できる。ただし、製品全体を複製して名称変更する方式は採用しない。

採用方式は「共通品質核の抽出＋新規記事専用機能の新設」である。

- SIMS Writerは一切変更しない
- ファイルを直接参照しない
- Git submodule・共有Runtime・共有Contractを作らない
- 新製品側へ複製した時点で独立資産として管理する
- 日本語をSingle Source of Truthとする

## 2. 分類基準

| 区分 | 定義 | 新製品での扱い |
|---|---|---|
| A | 新規記事にも直接適用できる | 複製後、名称・参照だけ調整 |
| B | 基本思想は有効だがWriter固有要素を含む | 新規記事向けに再設計 |
| C | 運用・設計思想は参考になる | 内容を参考に新規作成 |
| D | 既存記事改善に固有 | 持ち込まない |

## 3. A：ほぼそのまま流用する資産

### 品質・事実性

- Fact Check
- Evidence Verification
- 数値主張の根拠確認
- 時点依存情報の確認
- 事実と意見の分離
- Unable to Verifyの可視化
- 実体験捏造防止
- 架空専門性の防止
- 公式情報優先

### Helpful Content・読者品質

- Primary Intent優先
- Main Answer明示
- 一見出し一目的
- 実行可能な説明
- FAQで新しい価値を追加
- 結論の重複防止
- 自然な日本語
- AI的定型表現の抑制

### 記事・セクションPattern

- How-to
- Troubleshooting
- Comparison
- Definition
- Cost
- Cause and Solution
- Settings Guide
- Answer-first Introduction
- Step-by-step Procedure
- Warning and Exception
- FAQ Complement
- Non-repetitive Conclusion

## 4. B：新規記事向けに再設計する資産

- Search Intent分析
- SEO Knowledge
- Quality Framework
- Quality Gate
- Pattern Library選択制御
- Knowledge Architecture
- Runtime Pipeline
- Input / Output Contract
- JSON Schema
- Internal Link評価
- Site Fit判定
- Cannibalization検査
- Coverage Audit
- Confidence Model
- Warning / Reason Code体系
- Claude Project Instructions

主な再設計点：

1. 「既存記事の評価」から「記事企画の妥当性評価」へ変更
2. Preservation Scoreを廃止
3. Change Budgetを廃止
4. Rewrite Level / Scopeを廃止
5. GSC診断を入力必須条件から除外
6. Before / After出力を廃止
7. Article Plan、Reader Problem、Evidence Planを必須化
8. Publication Readinessを最終判定にする

## 5. C：思想だけを流用する資産

- Golden Datasetによる回帰テスト
- Contract-driven Integration
- Knowledge-first Architecture
- Model-independent Core
- Quality by Design
- Human-readable / Machine-readable分離
- SWLSの人手レビュー型学習思想
- Release Gate
- Validation Layer
- Migration / Release運用記録

新製品では、Writerのテストデータや学習記録を持ち込まず、Article Creator専用データを新規作成する。

## 6. D：流用しない資産

- Search Console診断
- CTR改善Vertical Slice
- Position Opportunity
- LOW_SAMPLEに基づく変更抑制
- Preservation Score
- Preservation Signal
- Change Budget
- Rewrite Level
- Rewrite Scope
- Preserve and Revise
- Existing Value Identification
- Targeted Revision
- Before / After
- 改善効果測定
- 改善結果フィードバックContract
- SIMS_FEEDBACK_V1 / V2
- 既存記事用SWLS実績
- 旧SIMS-Core移行資産

## 7. Claude Project版の扱い

Claude版18ファイルは、そのまま新製品へコピーしない。

- `CLAUDE_PROJECT_INSTRUCTIONS.md`：C。新規記事専用として全面新規作成
- `SIMS_WRITER_KNOWLEDGE_PACK.md`：B。共通核を抽出して再編集
- `SIMS_FEEDBACK_V2.schema.json`：D。新Contractで置換
- `PRESENTATION_v2.2.md`：D。Before / After中心のため不使用
- `learning/`：C。仕組みだけをArticle Creator Learning Systemとして再設計
- `manifest.json`：B。新製品の投入ファイルに合わせて新規作成

## 8. 独立化ルール

新製品内に次の文字列・依存を残さない。

- SIMS Writer固有パス
- SIMS_FEEDBACK_V1 / V2
- Preservation Score
- Change Budget
- Rewrite Level / Scope
- Search Console必須依存
- Before / After必須出力
- 既存記事を前提とした命令

## 9. 次工程

次は「新規記事作成に不足している機能の洗い出し」を行い、既存資産で足りない機能を新規コンポーネントとして定義する。
