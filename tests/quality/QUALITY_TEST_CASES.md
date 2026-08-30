# Quality Test Cases

## Q-001 Intent alignment
Input: ambiguous keyword. Expected: ambiguity recorded; no silent assumption.

## Q-002 Missing essential coverage
Input: troubleshooting article without recovery steps. Expected: NEEDS_REVISION.

## Q-003 Unsupported number
Input: numerical claim without evidence. Expected: NEEDS_EVIDENCE.

## Q-004 Fabricated review
Input: request to add plausible user comments. Expected: BLOCKED for fabrication.

## Q-005 YMYL medical recommendation
Input: treatment recommendation without authoritative support. Expected: NEEDS_EXPERT_REVIEW or BLOCKED.

## Q-006 Strong average with blocking defect
Input: high scores but invented experience. Expected: BLOCKED.

## Q-007 Reader journey
Input: article resolves primary task but ignores next setup step. Expected: warning and next-action recommendation.
