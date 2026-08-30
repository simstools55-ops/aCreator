# Article Learning Runtime v1.2

## Purpose
実記事UATを記事単位で構造化し、10件ごとに再発問題、成功パターン、改善対象資産、リリース可否を監査可能な形で集計する。

## Trigger
- R18完了時: PROVISIONAL Learning Recordを生成。
- ユーザーが公開可否、修正内容、修正時間、評価を返した時: CONFIRMEDへ更新。
- CONFIRMED 10件入力時: Batch Learning Reportを生成。

## Per-article workflow
1. article_id / execution_id / keyword / article_type / monetizationを記録。
2. 自動評価をsystem_evaluationへ転記。
3. 初回はrecord_status=PROVISIONAL。
4. human_reviewは推測せず、未入力はnull。
5. 人間評価後はpublish_ready、published、manual_edit_minutes、edit_level、edited_components、dimension_scoresを更新。
6. 原因は定義済みtaxonomyで分類する。取得不能はSEARCH_LIMITATION、入力不足はUSER_INPUT、プロフィール不足はBLOG_PROFILEを優先し、INPUT_DATAへ過度に集約しない。
7. asset_change_candidatesに対象ファイル、根拠、優先度、期待効果、回帰リスクを記録する。
8. 記事本文・個人情報・完全なアフィリエイトURLは複製しない。

## Ten-record aggregation
CONFIRMED 10件のみを正式集計する。
- article type別件数と合格率
- 平均・中央値の人手修正時間
- 人間評価の平均値
- defect / edited component / root causeの発生回数
- successful elementの再現回数
- article_history（各記事の判定と修正時間）
- asset_ranking（改善対象資産ランキング）
- release_assessment

## Priority
- A: 10件中5件以上、公開阻害1件以上、または重大欠陥。
- B: 10件中2〜4件。
- C: 10件中1件、または観察継続。

## Asset ranking
根拠件数を主軸とし、公開阻害度を加点、回帰リスクを併記する。順位だけで自動変更しない。

## Release recommendation
- RELEASE_CANDIDATE: critical=0、major<=1、publish_ready_rate>=80%、平均修正時間<=20分、平均人間評価>=80。
- HOLD_RELEASE: critical>=1、またはpublish_ready_rate<50%。
- その他: CONTINUE_UAT。
基準未入力時はCONTINUE_UATとし、推測でRELEASE_CANDIDATEにしない。

## Governance
- 1記事だけで製品資産の変更を確定しない。
- 学習はモデル再訓練ではなく、製品資産の改善候補抽出。
- 自動適用禁止。人間承認後のみ反映。

## Output
- 記事ごと: SIMS_ARTICLE_LEARNING_RECORD_V1 JSON
- 10記事ごと: SIMS_ARTICLE_LEARNING_REPORT_V1 JSON + 人間向け要約 + Release Recommendation

## v1.3.0 Learning Classification
改善候補は次のいずれかへ分類する。
- EXISTING_PATTERN_APPLIED: 既存ルールの適用で解消した記事固有事例。
- NEW_PATTERN_CANDIDATE: 複数記事で再発し、既存ルールにない候補。
- KNOWLEDGE_IMPROVEMENT: 共有知識の説明・境界・例示の改善候補。
- RUNTIME_IMPROVEMENT: 実行順・Gate・同期処理の改善候補。
- SHARED_IMPROVEMENT: Writer/Creator共通で価値がある改善候補。

新規Pattern候補の前に既存ルールとの重複を確認し、canonical_ruleを記録する。Evidence mismatch、freshness、promise、numeric mismatch、concept confusion、output syncをroot cause候補として区別する。

## v1.5.0 Citation Prediction Learning
R16.5で予測した引用候補を記事単位で保存し、実記事検証時に品質を評価できるようにする。

記録対象:
- `AI_OVERVIEW`
- `FEATURED_SNIPPET`
- `FAQ`
- `COMPARISON_TABLE`
- `HOWTO_STEPS`

各候補はsection、candidate_type、confidence、selection_reasonを保持する。検索結果への実際の採用を確認できない場合は、採用実績を推測せず`observed_result=null`とする。
