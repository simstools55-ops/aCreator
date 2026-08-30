# Article Learning Contract v1.1

## Per-article format
- format: SIMS_ARTICLE_LEARNING_RECORD_V1
- record_version: 1.1.0
- record_status: PROVISIONAL | CONFIRMED
- execution_id: Article Creator JSONと一致
- article_id: 任意。未指定時はexecution_idを使用
- generated_at: YYYY-MM-DD
- article_context: keyword / article_type / monetization / platform / blog_profile_id
- system_evaluation: publication_status / overall_score / warnings / successful_elements / suspected_defects
- human_review: publish_ready / published / manual_edit_minutes / edit_level / edited_components / dimension_scores / reviewer_notes
- diagnosis: confirmed_defects / root_cause_candidates / recommended_changes / asset_change_candidates

## Root cause taxonomy
次から選択する。複数選択可。
- PROJECT_INSTRUCTIONS
- RUNTIME
- KNOWLEDGE
- PATTERN
- CONTRACT
- TEMPLATE
- BLOG_PROFILE
- USER_INPUT
- INPUT_DATA
- SEARCH_LIMITATION
- EXTERNAL_SOURCE
- NONE

## Human dimension scores
未評価時はnull。評価時は0〜100。
- seo_quality
- blogger_voice
- reader_satisfaction
- factual_reliability
- monetization_quality
- publish_workability

## Asset change candidate
- asset_type: PROJECT_INSTRUCTIONS | RUNTIME | KNOWLEDGE | PATTERN | CONTRACT | TEMPLATE | BLOG_PROFILE
- target_file: 実ファイル名または候補
- issue: 観測された問題
- evidence_count: 根拠件数
- priority: A | B | C
- expected_effect: 期待効果
- regression_risk: LOW | MEDIUM | HIGH
- status: OBSERVE | PROPOSE | APPROVED | REJECTED

## Batch format
- format: SIMS_ARTICLE_LEARNING_REPORT_V1
- report_version: 1.1.0
- batch_size: 10
- source_record_ids: exactly 10 unique confirmed records
- metrics / article_history / recurring_defects / successful_patterns / asset_ranking / change_candidates / next_uat_focus / release_assessment

## Release assessment
- recommendation: RELEASE_CANDIDATE | CONTINUE_UAT | HOLD_RELEASE
- critical_defects / major_defects / minor_defects
- publish_ready_rate / average_manual_edit_minutes / average_human_score
- passed_criteria / failed_criteria / rationale

標準基準:
- RELEASE_CANDIDATE: critical=0、major<=1、publish_ready_rate>=0.8、平均修正時間<=20分、平均人間評価>=80。
- HOLD_RELEASE: critical>=1、またはpublish_ready_rate<0.5。
- それ以外はCONTINUE_UAT。

## Validation rules
1. PROVISIONALではhuman_reviewの未確認値をnullとする。
2. CONFIRMEDにはpublish_readyとmanual_edit_minutesを必須とする。
3. edit_levelはNONE | MINOR | MODERATE | MAJOR | REWRITE。
4. root_cause_candidatesは定義済みtaxonomyのみ。
5. 10件レポートはCONFIRMEDのみを集計する。
6. 同一execution_idの重複集計を禁止する。
7. 記事本文、認証情報、個人情報、完全なアフィリエイトURLを保存しない。
8. asset_rankingは根拠件数、公開阻害度、回帰リスクを併記する。
9. Release Recommendationは基準値と根拠を必ず出力する。

## v1.5.0 citation prediction fields
Learning records may store predicted citation sections and later human observations. Absence of observable SERP adoption must remain null and must not be inferred.
