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


## BOS連携・完成記事JSON出力ゲート（v2.0.2、最終出力直前に必須）
- 通常の記事作成依頼およびBOSからの記事作成依頼は、記事企画のみで終了してはならない。公開可能な場合は完成記事HTML全文と `SIMS_ARTICLE_CREATOR_V1` の記事作成結果JSONを両方出力する。
- 記事作成結果JSONは `format: SIMS_ARTICLE_CREATOR_V1` とし、`article.body_html` に完成記事HTML全文を省略せずJSON文字列として格納する。HTML表示とJSON本文は同一内容にする。
- `publication_gate` は文字列ではなく、必ず `{status, reason_codes, blocking_issues, required_actions}` を持つオブジェクトとする。statusは既存Contract列挙値を使う。
- 記事企画は途中成果物、学習記録 `SIMS_ARTICLE_LEARNING_RECORD_V1` は別成果物である。企画JSONまたは学習記録JSONを完成記事JSONとして提出しない。
- 公開に不可欠な根拠・実測・本人の経験が不足し、捏造せず記事を完成できない場合、`publication_gate.status` を `BLOCKED` とし、理由・不足資料・必要な利用者操作を具体的に返す。未確認の実測値、体験談、HTML本文を作り上げない。BLOCKED時は `article.body_html` を空文字列とし、完成記事とは称さない。
- 最終出力前に既存の `contracts/schemas/article-creator-output.schema.json` と照合し、記事JSONの必須フィールド、gateの型、HTML全文、出力種別を検査する。合格しなければ公開可能な完成記事として提出しない。
- BOS側の仕様は変更しない。既存のHTMLコピー用ブロック、SEO情報、品質判定、学習記録の出力順序と独立性を維持する。
