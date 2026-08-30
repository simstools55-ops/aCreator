# SIMS Article Creator Contract v1.3

## 不変条件
1. formatはSIMS_ARTICLE_CREATOR_V1、contract_versionは1.4.0。
2. メインキーワード入力は記事生成Runtimeを開始する。
3. 本文生成前にEditorial BriefとMonetization判定を作成する。
4. 入力にない実体験を生成しない。
5. 事実、Editorial Opinion、User-provided Experienceを区分する。
6. 根拠未確認の重要主張を断定しない。
7. affiliate_url入力時はPR表記とリンク挿入を検証する。
8. body_htmlへ公開用完成記事のHTML全文を格納する。
9. 人間向け出力とJSONのタイトル、HTML本文、リンク数、公開判定を一致させる。
10. 公開用HTMLへMarkdown記法を混在させない。
11. BLOCKEDでも分析結果と不足情報を返す。
12. 記事生成完了時はSIMS_ARTICLE_LEARNING_RECORD_V1を別オブジェクトとして出力する。
13. Learning Recordに記事本文または秘密情報を複製しない。

## v1.5.0 output additions
- `outline[].priority` is required and uses ★★★★★ / ★★★★☆ / ★★★☆☆.
- `internal_links[]` uses `CONFIRMED`, `CANDIDATE_TOPIC`, or `UNAVAILABLE` and includes priority and reason.
- `quality.serp_self_review` records six 1–5 ratings with reasons.
- `citation_candidates` records up to five predicted AI Overview / Featured Snippet / FAQ / comparison / how-to citation candidates.
