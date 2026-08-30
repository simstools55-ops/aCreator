# Article Learning Enhancement v0.7.2

v0.7.2では、記事単位のLearning Recordと10記事単位のLearning Reportを強化しました。

## 追加点
- 詳細な原因分類
- 6項目の人間評価
- 改善対象ファイル候補
- Article History
- Asset Ranking
- Release Recommendation

## 運用
1. 記事生成時のPROVISIONAL Recordを保存。
2. 公開判断後、UAT Human Feedbackを返す。
3. CONFIRMED Recordを保存。
4. 10件をまとめて再投入。
5. Learning ReportとRelease Recommendationを確認。

学習結果は自動的に製品へ反映されません。改善候補を人間が承認してから更新します。
