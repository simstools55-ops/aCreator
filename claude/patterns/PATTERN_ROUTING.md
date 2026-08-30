# Pattern Routing v1.0

## 判定原則
検索語の表面形ではなく、読了後に読者が取りたい行動でPrimary Patternを決定する。

| 読者の中心行動 | Primary Pattern |
|---|---|
| 手順を実行する | HOWTO |
| 不具合を直す | TROUBLESHOOTING |
| 二つ以上を選ぶ | COMPARISON |
| 購入候補を絞る | BUYING_GUIDE |
| 意味・仕組みを理解する | DEFINITION |
| 使用評価を確認する | REVIEW |
| 場所を訪問・利用する | LOCAL_GUIDE |
| 年・季節の最新情報を得る | SEASONAL |

## 複合判定
- Primaryは必ず1件。
- Secondaryは原則0〜2件。
- 「おすすめ」が含まれても購入意図が弱ければBUYING_GUIDEをPrimaryにしない。
- 「できない」「エラー」はTROUBLESHOOTINGを優先する。
- 年号だけを理由にSEASONALをPrimaryにせず、鮮度依存が中心の場合のみ採用する。

- 再利用可能な入力物が中心価値なら COPY_TEMPLATE を補助適用する。
- R16.5では CITATION_CANDIDATE を補助適用する。
