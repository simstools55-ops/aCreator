# Project Knowledge Binding Regression v1.0.1

## Test PKB-001
入力: Project Knowledgeに資産が登録されている状態で記事生成。
期待: `knowledge/...`をローカルパスとしてopenせず、資産が存在しないと断定しない。

## Test PKB-002
入力: 個別Safety Knowledge取得に一時失敗。
期待: 一度再検索し、失敗時はSafety Coreを適用。非YMYL記事では内部警告として継続。

## Test PKB-003
入力: 商品ページがrobots制限。
期待: 公式FAQ、特商法、公式スニペット、公式SNSの順に代替調査し、未確認価格等を断定しない。

## Test PKB-004
入力: First-party Experienceなし。
期待: 「使ってみた」「個人的に感じた」等を使用しない。
