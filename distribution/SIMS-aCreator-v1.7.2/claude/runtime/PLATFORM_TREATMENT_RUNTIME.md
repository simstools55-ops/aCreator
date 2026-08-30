# Platform Treatment Runtime v1.6.2

Platform Requestを受けた場合、次の順序で処理する。

1. Envelope、Contract名、CaseID、Treatment Request IDを確認する。
2. `draft_article_id`を保持する。未指定時だけSBMへ不足として返す。Creatorが独自に正式ArticleIDを発行しない。
3. 既存記事とのrole separation、topics_to_avoid、required_topicsを固定する。
4. 通常のCreator Runtimeで新記事を生成する。
5. Identity Lock、Duplicate Intent、Publication Readinessを検証する。
6. `SIMS_CREATOR_TREATMENT_RESULT_V1`を返す。
7. 既存記事修正や統合が必要なら`follow_up_referrals`としてSBMへ返す。直接Writer／Mergeを起動しない。
8. 実際の公開はSBMのPublication Result登録後に確定する。

Evidence不足時は推測で補わず、`EVIDENCE_INSUFFICIENT`または`USER_DECISION_REQUIRED`を返す。
