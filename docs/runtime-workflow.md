# Runtime Workflow v1.0

## ステージ

### R00 Initialize
処理ID、Contract版、言語、基準日を設定する。

### R01 Validate Input
メインキーワード、補助情報、サイト文脈を検査する。

### R02 Understand Keyword
主題、対象、行動、制約、時期、場所、曖昧性を抽出する。

### R03 Analyze Intent
Primary Intent、Secondary Intent、検索ファネル、緊急度を判定する。

### R04 Define Reader Problem
想定読者、検索直前の状況、課題、懸念、読了後状態を定義する。

### R05 Select Article Type
単一または複合Blueprintを選択する。

### R06 Assess Risk and Sufficiency
YMYL、鮮度、根拠、実体験、商品情報の不足を評価する。

### R07 Build Editorial Brief
記事目的、中心回答、必須論点、独自価値、除外範囲を確定する。

### R08 Build Evidence Plan
各重要主張に必要な根拠、出典種別、確認状態を割り当てる。

### R09 Design Structure
タイトル、メタ、導入、H2/H3、FAQ、リンク、CTAを設計する。

### R10 Structure Gate
検索意図、論点網羅、重複、順序、過剰SEOを検査する。

### R11 Generate Draft
承認済み構成に従って本文を生成する。

### R12 Add Supporting Components
FAQ、内部リンク候補、広告・CTA案、更新注意を追加する。

### R13 Evidence Verification
事実、数値、比較、最新性、体験表現を検査する。

### R14 Quality Audit
SEO、Helpful Content、E-E-A-T、自然さ、一貫性、読者満足を監査する。

### R15 Publication Gate
PASS / PASS_WITH_WARNING / NEEDS_REVISION / NEEDS_EVIDENCE / NEEDS_EXPERT_REVIEW / BLOCKEDを決定する。

### R16 Output
人間向け成果物と構造化JSONを同時出力する。

## 差戻しルール

- Intent不整合 → R03
- 読者課題不整合 → R04
- 論点不足 → R07
- 根拠不足 → R08
- 見出し重複・順序不良 → R09
- 本文のみの表現問題 → R11
- CTA過剰 → R12

無制限ループを避けるため、同一ステージの自動再試行は最大2回とする設計を推奨する。

## R09.5 / R13.1 / R16.5 v1.5.0
Section Priority、Answer First、Copy Template、Citation CandidateをRuntimeへ統合した。
