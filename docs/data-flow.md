# Engine Data Flow v1.0

## 標準データオブジェクト

1. `InputEnvelope`
2. `KeywordModel`
3. `IntentModel`
4. `ReaderProblemModel`
5. `ArticleTypeDecision`
6. `RiskAssessment`
7. `EditorialBrief`
8. `EvidencePlan`
9. `ArticleStructure`
10. `ArticleDraft`
11. `SupportingComponents`
12. `QualityReport`
13. `PublicationDecision`
14. `ArticleCreatorOutput`

## データ不変条件

- main_keywordはInputEnvelopeから最終出力まで保持する。
- 警告は解消記録なしに削除しない。
- 推測値には`inferred=true`を持たせる。
- 人が提供した実体験とモデル生成説明を区別する。
- 重要主張にはEvidencePlan上の対応項目を持たせる。
- PublicationDecisionはQualityReportを参照可能にする。

## 将来のContract実装

v0.3以降で各オブジェクトのJSON Schema、reason code、warning codeを定義する。
