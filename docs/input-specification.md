# 入力仕様 v1.0

## 1. 目的
SIMS Article Creatorが、推測で重要情報を補わず、新規記事の企画・執筆・品質判定を再現可能に実行するための入力契約を定める。

## 2. 入力レベル

### 必須
- `main_keyword`: 記事の主対象となる検索語。空文字不可。

### 推奨
- `supporting_keywords`: 関連語・補助語。検索意図の補強に使用する。
- `site_context`: サイト名、ジャンル、想定読者、既存カテゴリ。
- `article_goal`: 情報提供、問題解決、比較、購入支援など。
- `reference_date`: 情報の基準日。最新性が重要なテーマでは必須相当。

### 任意
- `reader_hint`
- `article_type_hint`
- `source_materials`
- `first_party_experience`
- `internal_link_candidates`
- `monetization_context`
- `style_preferences`
- `constraints`

## 3. 推定してよい項目
- 検索意図候補
- 想定読者候補
- 記事タイプ候補
- 読者課題候補
- 一般的な構成案

推定値は必ず`assumptions`に記録し、事実として扱わない。

## 4. 推定してはいけない項目
- ユーザーの実体験
- 商品を実際に使用した感想
- 独自調査結果
- 口コミ件数・評価点
- 価格、仕様、法令、制度、医療・金融上の断定
- 存在しない出典

不足時は`missing_information`または`evidence_items`へ記録する。

## 5. 入力検証
- メインキーワードが空欄なら`BLOCKED`。
- 曖昧語だけで主題を確定できない場合は`NEEDS_INPUT`。
- YMYLかつ根拠資料がない場合、断定本文を制限し`NEEDS_EXPERT_REVIEW`または`NEEDS_EVIDENCE`。
- 実体験を要求する記事で一次情報がない場合、体験談を生成しない。
- 相反する制約がある場合は`INPUT_CONFLICT`を出力する。

## 6. 入力JSON
入力JSONの正式スキーマは`claude/contracts/schemas/article-creator-input.schema.json`を正とする。
