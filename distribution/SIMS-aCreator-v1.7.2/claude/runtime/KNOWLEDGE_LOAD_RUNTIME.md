# Knowledge Load Runtime v1.2.0

## Project Knowledge Binding
Knowledge資産はClaude Projectへ登録されたProject Knowledgeとして参照する。`knowledge/...`等の表記は論理識別名であり、ローカルファイルパスとしてopenしない。

## Step K0 Shared snapshot validation
`shared/SNAPSHOT_MANIFEST.json`、`shared/SOURCE.md`、`shared/mappings/article-creator/application-mapping.md`をProject Knowledge内で論理照合する。Sharedは読取専用であり、内容を直接編集しない。取得不能時は既存Knowledgeへフォールバックし、内部警告を記録する。

## Step K1 Creator Manifest validation
Project Knowledge内でManifest、重複ID、status、対応資産の存在を論理照合する。直接取得できない場合は一度再検索し、なお取得不能ならLOAD_WARNINGとして記録する。

## Step K2 Shared core load
Intent Analysis、Hidden Anxiety、SERP Entity Preservation、Evidence Transparency、Internal Link Semantics、FAQ Evolution、Decision Support、Conditional Editorial Opinion、Freshness Safetyを共通知識層として適用する。

## Step K3 Creator core load
K-POLICY、K-INTENT、K-READER、K-HELPFUL、K-COVERAGE、K-SEO、K-READABILITY、K-EEATを適用する。

## Step K4 Conditional load
YMYL、time-sensitive claims、internal links、monetizationの入力条件に応じて追加Knowledgeを適用する。

## Step K5 Precedence
Safety、Evidence、Contract、ユーザー入力を最優先とし、共通編集判断ではSharedを正本として扱う。Creator Knowledgeは新規記事生成への具体化を担う。

## Step K6 Runtime binding
- Shared Intent/Hidden Anxiety/Decision Support → Editorial BriefとCoverage Map
- Shared SERP Entity → SEOタイトル、H1、見出し、本文の整合
- Shared Evidence/Freshness → Evidence PlanとPublication Gate
- Shared Internal Link/FAQ → Blueprint、FAQ、最終監査
- Intent/Reader/Coverage → Editorial Brief
- Evidence/Freshness/Safety → Evidence PlanとPublication Gate
- Helpful/SEO/Readability/Originality → DraftとEditorial Review
- Links/Monetization → Article Blueprintと最終監査

## Step K7 Fallback
個別Knowledgeを取得できない場合はProject Instructions内のSafety Core、Web Evidence Fallback、Editorial Opinion規則を必ず適用する。非YMYL記事では内部読込警告だけを理由に記事生成を停止しない。

## Step K8 Audit
適用Knowledge ID、警告、未解決競合を記録する。未解決の重大競合はNEEDS_REVISION以上とする。「資産が存在しない」と断定するのは、Project Knowledgeへの登録状況が明示的に確認できた場合に限る。
