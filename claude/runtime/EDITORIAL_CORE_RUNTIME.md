# Editorial Core Runtime v1.0

Execute in this exact order.

1. Validate input.
2. Analyze keyword meaning and ambiguity.
3. Select primary and secondary search intents.
4. Build the reader model.
5. Produce the Editorial Brief.
6. Produce the Coverage Map.
7. Produce the Reader Journey.
8. Produce the Evidence Plan.
9. Stop with NEEDS_EVIDENCE or NEEDS_EXPERT_REVIEW when required.
10. Produce the Article Blueprint and outline.
11. Draft the article.
12. Run editorial review.
13. Run publication readiness.
14. Emit the final article and SIMS_ARTICLE_CREATOR_V1 JSON.

Never invent facts, evidence, experience, quotes or reviews. Never skip planning artifacts.


## Shared v1.3.0 Common Validation

公開前にVAL-FACT-001、VAL-EVIDENCE-002、VAL-CAUSAL-001、VAL-CONSISTENCY-001、VAL-ENTITY-001、VAL-LINK-001を適用する。Creator Identity Lockを維持し、Query Coverage、QUERY_MIX、Winner Query Preservation、SIMS_FEEDBACK_V2、Before／Afterは導入しない。
