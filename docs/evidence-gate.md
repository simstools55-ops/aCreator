# Evidence Gate Specification

## Claim classes

- E0: common, stable background knowledge
- E1: factual claim that should be verified
- E2: numerical, comparative, product, legal, medical, financial or time-sensitive claim
- E3: high-risk YMYL claim requiring authoritative evidence or expert review

## Gate behavior

- E0 may proceed without a citation plan.
- E1 requires a source note or explicit uncertainty label.
- E2 requires a named source type, freshness date and verification status.
- E3 requires authoritative evidence and may return NEEDS_EXPERT_REVIEW.

## Prohibited substitutions

The system must not replace missing evidence with plausible wording, consensus language, fabricated survey results, invented customer reviews or synthetic personal experience.
