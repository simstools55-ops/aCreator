# Product Architecture v1.0

## 1. 目的

SIMS Article Creatorの処理を、単発の文章生成ではなく、検証可能な記事制作パイプラインとして定義する。

## 2. レイヤー構成

1. Input Layer
2. Keyword Understanding Layer
3. Intent & Reader Layer
4. Editorial Planning Layer
5. Evidence & Safety Layer
6. Content Architecture Layer
7. Content Generation Layer
8. Monetization Layer
9. Quality Assurance Layer
10. Output & Contract Layer

## 3. Engine構成

| Engine | 主責務 |
|---|---|
| Input Validation Engine | 必須入力、矛盾、危険領域、欠落を検出 |
| Keyword Understanding Engine | 主題、修飾語、対象、状況、曖昧性を構造化 |
| Search Intent Engine | Primary/Secondary Intentと検索段階を判定 |
| Reader Problem Engine | 読者状況、顕在・潜在課題、読了後状態を定義 |
| Article Type Engine | 最適な記事タイプと複合型を判定 |
| Article Planning Engine | Editorial Briefを作成 |
| Evidence Planning Engine | 主張ごとの根拠要件、鮮度、確認状態を管理 |
| Structure Design Engine | タイトル、導入、H2/H3、FAQ、CTA配置を設計 |
| Content Generation Engine | 承認済みBriefと構成に限定して本文生成 |
| Link & Monetization Engine | 内部リンク、広告、CTAの適切性を設計 |
| Quality Audit Engine | SEO、読者満足、事実性、一貫性を監査 |
| Publication Readiness Gate | PASS系または差戻し・停止を決定 |

## 4. Engine分離原則

- 各Engineは前段の構造化出力を入力とする。
- 本文生成Engineは検索意図や根拠を独自に再定義しない。
- 品質監査で構成上の欠陥が見つかった場合、本文だけを修正せず該当Engineへ戻す。
- 不足情報は警告として保持し、暗黙に消去しない。
- 公開判定と文章完成判定を分離する。

## 5. 停止可能性

以下では全文生成を停止できる。

- キーワードが複数の重大な意味に分岐し、選択根拠がない
- YMYL高リスクかつ必要根拠が不足
- 商品・制度・価格等の最新確認が必要だが確認不能
- 実体験が必須の企画なのに提供されていない
- 違法・危険行為を実用的に促進する内容

停止時も、分析結果、必要情報、次の入力事項を出力する。
