# Shared Editorial Knowledge Runtime v1.2.0

## Purpose

SIMS-Shared-Editorial-Knowledgeを唯一の共通知識正本とし、Article Creatorの新規記事生成Runtimeへスナップショットとして適用する。

## Source and immutability

- 正本は`SIMS-Shared-Editorial-Knowledge`である。
- Article Creator内の`shared/`およびClaude Project内の`shared/`は読取専用スナップショットである。
- Sharedの修正はArticle Creator側で行わず、正本更新後にスナップショットを再生成する。
- `SNAPSHOT_MANIFEST.json`のSHA-256で改変と欠落を検証する。

## Logical load order

1. Shared Snapshot ManifestとSourceを検証する。
2. Sharedの`mappings/article-creator/application-mapping.md`を読み、Creator向け適用範囲を確定する。
3. Shared Knowledgeを共通判断層として適用する。
4. Article Creator専用Knowledgeを新規記事生成層として適用する。
5. Safety、Evidence、Contract、ユーザー入力を最優先で競合解決する。
6. Pattern、Runtime、Templateへ結果を引き渡す。

## Shared capabilities

- Intent Analysis
- Hidden Anxiety
- SERP Entity Preservation
- Evidence Transparency
- Internal Link Semantics
- FAQ Evolution
- Decision Support
- Conditional Editorial Opinion
- Freshness Safety

## Article Creator application

- Intent AnalysisとHidden AnxietyはEditorial BriefとCoverage Mapへ反映する。
- SERP Entity PreservationはSEOタイトル、H1、見出し、本文の主要エンティティ整合に使用する。
- Evidence TransparencyとFreshness SafetyはEvidence PlanとPublication Gateへ反映する。
- Internal Link Semanticsは文脈型内部リンク候補の採否に使用する。
- FAQ Evolutionは本文で未解決の意思決定質問だけをFAQ候補とする。
- Decision SupportとConditional Editorial Opinionは、比較・レビュー・購入検討記事の選択支援に使用する。

## Compatibility guardrails

- 既存の出力順序、HTML出力、JSON Contract、reason code、warning codeを変更しない。
- Creator専用のOutline、Initial Heading、First Draft、Intro、Conclusion生成規則を維持する。
- Writer専用のPreservation Score、Rewrite Budget、Rewrite Level、Existing Content Protectionは導入しない。
- Shared信号は記事生成品質を補強するが、入力事実やEvidenceを上書きしない。
- Shared資産を取得できない場合は既存Knowledgeへフォールバックし、非YMYL記事生成を直ちに停止しない。

## Audit

Quality Report内部監査に以下を記録する。

- shared_source_version
- shared_snapshot_status
- shared_capabilities_applied
- shared_warnings

これらは既存JSON Contractへ新規必須フィールドとして追加しない。Contract互換を守るため、既存の監査・警告領域で扱う。


## Shared v1.3.0 Common Validation

公開前にVAL-FACT-001、VAL-EVIDENCE-002、VAL-CAUSAL-001、VAL-CONSISTENCY-001、VAL-ENTITY-001、VAL-LINK-001を適用する。Creator Identity Lockを維持し、Query Coverage、QUERY_MIX、Winner Query Preservation、SIMS_FEEDBACK_V2、Before／Afterは導入しない。
