# SIMS Article Creator JSON Contract v1.0

## Format
`SIMS_ARTICLE_CREATOR_V1`

## Contract方針
- SIMS Writerの`SIMS_FEEDBACK_V1/V2`とは互換性を持たせない。
- 新規記事の企画、生成、根拠、品質、公開可否を一つの実行記録として保存する。
- 不明値は捏造せず、`null`、空配列、警告、未充足項目で表現する。
- Contractの破壊的変更はformatまたはmajor versionを更新する。

## トップレベル
- `format`
- `contract_version`
- `execution`
- `input_summary`
- `analysis`
- `editorial_brief`
- `seo_assets`
- `outline`
- `article`
- `faq`
- `internal_links`
- `monetization`
- `evidence`
- `quality`
- `publication_gate`
- `warnings`
- `missing_information`

## Reason Codes
正式一覧は`claude/contracts/reason-codes/REASON_CODES.md`を参照。

## Warning Codes
正式一覧は`claude/contracts/warning-codes/WARNING_CODES.md`を参照。

## v1.5.0 additions
Output JSON includes outline priority, detailed internal links, SERP self-review ratings, and citation candidates.
