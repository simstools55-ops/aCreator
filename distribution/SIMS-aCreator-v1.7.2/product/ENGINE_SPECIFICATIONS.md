# Engine Specifications v1.0

## 共通契約

各Engineは `status`, `inputs_used`, `outputs`, `warnings`, `blocking_issues`, `assumptions` を返す。

## 主要Engine

### Input Validation Engine
入力必須条件と矛盾を検査する。入力にない体験・資格・検証結果を補わない。

### Keyword Understanding Engine
キーワードの意味単位を分解し、曖昧性候補を列挙する。

### Search Intent Engine
主検索意図を1つ選び、副次意図を優先順で保持する。根拠のないSERP観測を主張しない。

### Reader Problem Engine
人口統計的な架空ペルソナより、検索時の状況・知識・不安・制約を優先する。

### Article Planning Engine
Briefを唯一の計画上のSingle Source of Truthとして生成する。

### Evidence Planning Engine
主張を「一般知識」「確認済み」「要確認」「使用禁止」に分類する。

### Structure Design Engine
見出しごとに目的、回答する疑問、必要根拠、推奨形式を割り当てる。

### Content Generation Engine
Brief外の新しい重要主張を勝手に追加しない。追加が必要なら警告へ送る。

### Link & Monetization Engine
読者利益、関連性、タイミング、透明性の4条件を満たす場合だけCTAを提案する。

### Quality Audit Engine
最低限、Intent Match、Problem Resolution、Evidence Integrity、Structure、SEO、Naturalness、Consistency、Safetyを採点する。

### Publication Readiness Gate
重大欠陥を平均点で相殺しない。Blocking issueが1件でもあればPASSにしない。
