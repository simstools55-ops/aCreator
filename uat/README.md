# SIMS Article Creator UAT / Learning Foundation

## 1記事ごとの運用
1. Claudeで記事を生成する。
2. 完成記事JSONと同時に出る `SIMS_ARTICLE_LEARNING_RECORD_V1` を保存する。
3. 記事を確認・修正・公開する。
4. `UAT_HUMAN_FEEDBACK_TEMPLATE.md` の項目をClaudeへ返す。
5. Claudeが `record_status: CONFIRMED` のLearning Recordを再出力する。

## 10記事ごとの運用
CONFIRMEDのLearning Record 10件をClaudeへまとめて渡し、Article Learning Reportの生成を依頼する。

## 重要
Claude Projectが会話を越えて自動的にファイルを蓄積するわけではありません。Learning Recordは利用者側で保存してください。10件集まった時点で再投入します。
