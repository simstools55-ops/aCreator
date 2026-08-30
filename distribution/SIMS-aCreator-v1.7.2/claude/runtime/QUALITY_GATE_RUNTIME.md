# Quality Gate Runtime v1.2

## Blocking checks
- Contract validity
- Runtime Lock failure
- Fabricated first-party experience
- Material unsupported claim
- Missing primary answer
- Intent mismatch
- Empty, placeholder, or malformed body_html
- Markdown syntax mixed into the copy-ready HTML block
- Affiliate URL supplied but not inserted
- Affiliate article without PR disclosure
- Review article without review-source classification
- Price, cancellation or refund conditions stated by inference

## Publication status
PASS / PASS_WITH_WARNING / NEEDS_EVIDENCE / NEEDS_REVISION / BLOCKED
最も厳しい未解決ゲートを最終判定とする。

## Evidence transparency
未確認情報が存在しても、次のすべてを満たす場合はPASS_WITH_WARNINGを許容できる。
1. 未確認であることを本文とJSONで明示している。
2. 未確認の理由を記録している。
3. 読者が確認すべき公式ページ・予約ページ・問い合わせ方法を示している。
4. 誤認を招く断定・ランキング・最安表現をしていない。
5. YMYL高リスクまたは安全上の重大情報ではない。

Local Guideでは、価格・営業時間が公式取得不可でも、公式関連情報または複数の信頼できる代替情報、基準日、来店前確認の案内が揃う場合、重要度に応じてPASS_WITH_WARNINGを検討する。

## Scored checks
Search intent, reader value, hidden-anxiety resolution, coverage, evidence, evidence transparency, readability, originality, SEO, editorial voice, selection guidance, CTA naturalness, internal-link context, HTML validity, publish readiness.


## v1.2.1 Additional gates
- Central claim evidence is checked before peripheral claims.
- Marketplace listing must not be labeled official without official evidence.
- "Not found" must be scoped to reviewed sources; absence claims require stronger evidence.
- Stale price, refund, cancellation, taxonomy, and制度情報 require a freshness warning or removal.
- `fabrication_risk: NONE` is not used when material claims remain only partially verified.


## Shared v1.3.0 Common Validation

公開前にVAL-FACT-001、VAL-EVIDENCE-002、VAL-CAUSAL-001、VAL-CONSISTENCY-001、VAL-ENTITY-001、VAL-LINK-001を適用する。Creator Identity Lockを維持し、Query Coverage、QUERY_MIX、Winner Query Preservation、SIMS_FEEDBACK_V2、Before／Afterは導入しない。

## Pre-Publish Quality Gate v1.3.0

R18の公開判定前に次の順で一括検査する。

1. Evidence Strength Sync: H1/H2/H3/Outline/本文/FAQ/JSONで断定度を一致させる。
2. Freshness Gate: 「最新」「最新版」「現在」「現在でも」「○年最新」を検出し、確認日・一次情報・適用範囲がない場合は限定表現へ修正する。
3. Promise Gate: 「完全解決」「必ず」「100%」「一発」「5分で」等は本文で保証できる場合のみ許可する。
4. Numeric Consistency Gate: 原因数、方法数、手順数、FAQ数、ポイント数をタイトル・導入・見出し・本文・JSONで一致させる。
5. Concept Separation Gate: 類似機能・制度・プランを、発生場面・適用条件・制約で分離する。
6. FAQ Query Gate: FAQを検索者の自然な疑問文へ正規化し、本文Evidenceを超えない。
7. Internal Link Semantic Gate: 文字列一致でなく、読者の次の疑問、役割分担、リンク先確認で採否を決める。
8. Output Sync Gate: Article Info、Outline、HTML、Quality Report、SIMS_ARTICLE_CREATOR_V1、Learning Recordを最終値へ同期する。

自動修正できる軽微な不一致は修正してから再検査する。中心主張、手順、安全、Evidence、公開値の重大不一致が残る場合はPASSにしない。
