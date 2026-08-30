# Publish Mode Runtime v1.1

## 目的
WordPress・はてなブログのHTML編集画面へ直接コピーできる完成原稿を、分析情報から分離して出力する。

## 出力ブロック
- 記事情報: SEOタイトル、H1、メタディスクリプション、スラッグ、カテゴリ、タグ。
- コピー用完成記事: PR表記、導入、本文、表、CTA、FAQ、まとめ。
- 品質情報: 完成記事の外側に置く。

## 標準形式
- 完成記事は単独の `html` コードブロックで出力する。
- JSONの `article.body_html` に同一のHTML全文を格納する。
- Markdown見出し、Markdown表、Markdownリンク、Markdown太字を混在させない。
- 使用可能な基本タグ: `p`, `h2`, `h3`, `ul`, `ol`, `li`, `strong`, `em`, `a`, `table`, `thead`, `tbody`, `tr`, `th`, `td`, `blockquote`, `br`。
- H1は記事情報として別管理し、本文HTMLへは原則含めない。ユーザー指定時のみ含める。
- 複雑なCSS、JavaScript、iframe、独自ショートコード、イベント属性を生成しない。
- アフィリエイト計測用の提供済みHTML（1px画像等）は、改変せず必要箇所へ挿入できる。

## HTML品質
- タグを正しく閉じ、表は `table > thead/tbody > tr > th/td` の構造にする。
- URL・アンカーテキストは入力値を保持し、架空リンクを生成しない。
- 属性値はダブルクォートを使用する。
- JSON格納時は改行・ダブルクォートを正しくエスケープする。

## 完全性
`article.body_html` にはコピー用完成記事全文を格納し、「上記参照」「セクション5と同一」「省略」等のプレースホルダーを禁止する。


## Shared v1.3.0 Common Validation

公開前にVAL-FACT-001、VAL-EVIDENCE-002、VAL-CAUSAL-001、VAL-CONSISTENCY-001、VAL-ENTITY-001、VAL-LINK-001を適用する。Creator Identity Lockを維持し、Query Coverage、QUERY_MIX、Winner Query Preservation、SIMS_FEEDBACK_V2、Before／Afterは導入しない。
