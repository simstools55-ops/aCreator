# Runtime Workflow v1.5

R00 Initialize
R01 Runtime Lock and Validate Input
R02 Understand Keyword
R03 Analyze Intent
R04 Define Reader Problem
R05 Select and Compose Pattern
R06 Monetization Router
R07 Load Blog and Author Profile
R08 Assess Risk and Sufficiency
R09 Build Editorial Brief
R10 Build Evidence Plan
R11 Design Structure and CTA
R12 Structure Gate
R13 Generate Draft with Editorial Voice
R14 Add Supporting Components and Affiliate Links
R15 Evidence Verification
R16 Quality Audit
R16.5 SERP Self-Review
R17 Publication Gate
R18 Publish Mode Output and JSON

## 差戻し
意図不整合、根拠不足、構成不良、体験捏造、CTA過剰、リンク欠落、本文未格納を検出した場合は対応ステージへ戻す。同一ステージの自動再試行は最大2回。


## v1.2.1 Article-type refinements
### Definition
冒頭一文定義、混同概念との差、読者の隠れた不安、効果と限界の順で設計する。補助トピックは本題より前面に出さない。
### Buying Guide
販売チャネルをEvidence Levelで分類し、販売者確認チェックリストを示す。価格は鮮度確認できない限り固定値を中心主張にしない。

## R16.5 SERP Self-Review v1.4.0
公開判定前に、完成稿を次の7項目で自己点検する。

1. 検索意図充足 — Primary Intentへ冒頭から直接回答しているか。
2. CTR競争力 — タイトル・メタが記事固有の価値を正確に示しているか。
3. タイトル競争力 — 過剰約束、未確認の最新性、条件省略、主要語欠落がないか。
4. H2競争力 — 番号なしでも各H2の意味が伝わり、目次だけで記事範囲が理解できるか。
5. Featured Snippet適性 — 定義、手順、比較、一覧が簡潔な回答形式になっているか。
6. AI Overview適性 — 中心主張が根拠に結び付き、概念・条件・例外が明確か。
7. AI Citation Candidate — AI OverviewまたはFeatured Snippetに引用される候補段落を特定できるか。候補は中心回答、定義、手順、比較表、FAQから最大5件とする。

### Return rules
- 意図、タイトル、H2に問題があればR11へ差し戻す。
- 本文の優先順位、重複、説明量に問題があればR13へ差し戻す。
- 根拠・鮮度・主張強度に問題があればR15へ差し戻す。
- 自動差し戻しは既存の最大2回制限に従う。
- 自己レビュー結果はQuality Reportに要約し、公開用本文へ内部スコアを表示しない。

## R09.5 Section Priority Engine v1.5.0
Coverage Map完成後、各予定セクションへ内部優先度を付与する。

- `★★★★★` — Primary Answer / Decision Critical
- `★★★★☆` — Supporting Decision / Major HowTo
- `★★★☆☆` — Context / Supplementary

### Rules
1. 優先度はCoverage MapとOutline JSONへ保持する。
2. `★★★★★`は記事前半へ配置し、検索者が最初に必要とする答えを先送りしない。
3. 解説量は固定文字数ではなく、検索意図、Evidence、読者負荷、記事タイプに応じて調整する。
4. ユーザー指定見出しは削除・統合せず、解説量のみ調整する。
5. HOWTO記事では「最短手順」「最初にやること」「成功確認」の優先度を原則`★★★★★`とする。
6. 比較記事では比較軸、選び方、推奨条件を原則`★★★★★`または`★★★★☆`とする。

## R13.1 Answer First and Copy-Ready Block Check v1.5.0
本文生成時に次を確認する。

- 導入の最初の100文字前後で中心回答、最初の行動、または結論が伝わるか。
- HOWTO記事では、必要に応じて「まずここだけ」「最初の3ステップ」を短く提示する。
- テンプレート、設定値、チェックリスト、手順雛形など再利用価値が高い内容は、Copy Template Blockとして独立させる。
- Copy Template Blockは、本文の説明を置き換えず、読者がそのまま利用できる完成形だけを示す。

### Self-review output v1.5.0
Quality Reportには各項目を5段階（1〜5）と短い理由で記録する。

- search_intent
- ctr_competitiveness
- title_competitiveness
- h2_competitiveness
- featured_snippet_readiness
- ai_overview_readiness

さらに`citation_candidates`へ、候補セクション、候補テキストの要約、適性種別、信頼度、選定理由を記録する。公開本文へ内部スコアは表示しない。
