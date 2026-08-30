# 出力仕様 v1.1

## 1. 出力の二層構造
Human-readable Outputと`SIMS_ARTICLE_CREATOR_V1` JSONを分離して出力する。

## 2. 公開判定
- `PASS`: 公開可能
- `PASS_WITH_WARNING`: 注意点確認後に公開可能
- `NEEDS_REVISION`: 修正後に再検査
- `NEEDS_EVIDENCE`: 根拠追加が必要
- `NEEDS_EXPERT_REVIEW`: 専門家または人による確認が必要
- `BLOCKED`: 現状では公開不可

## 3. HTML完成記事
- セクション5は単独のHTMLコードブロックとする。
- 本文は原則として`<p>`から始め、`<h2>`・`<h3>`、リスト、表、リンク、FAQ、まとめをHTMLで記述する。
- Markdown記法を混在させない。
- H1は記事情報として別出力し、本文へは原則含めない。
- JSONの`article.body_html`に同一全文を格納する。

## 4. JSON整合性
- `format`は固定値`SIMS_ARTICLE_CREATOR_V1`
- `contract_version`は`1.3.0`
- `article.main_keyword`と入力のメインキーワードは一致
- `article.publishing_format`は`HTML`
- `publish.platform`は`HTML`、`WORDPRESS`、`HATENA`のいずれか
- `publication_gate.status`と警告・blocking issueに矛盾がない
- 実体験がない場合、`first_party_experience.used=false`
- 未確認の重要主張は`evidence.items`に存在する

正式スキーマは`claude/contracts/schemas/article-creator-output.schema.json`を正とする。
