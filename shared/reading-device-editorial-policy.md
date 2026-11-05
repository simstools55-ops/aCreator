# Reading Device Editorial Policy — v3.6.5 (T08)

## Scope
For NEW aCreator articles only two selectable styles exist: `DESKTOP_FIRST` (legacy writing behavior, unchanged) and `MOBILE_STORY` (new optional style). PC-first output is ordinary responsive HTML, not PC-only.

## Backward compatibility
Missing/unknown values and historical `BALANCED` or `MOBILE_FIRST` select the legacy writing behavior for new content. Historical values remain readable as data; do not bulk rewrite existing articles. No style setting overrides facts, search intent, safety, approval or publication gates.

## MOBILE_STORY
Use Answer First + Story. Narrative intensity depends on intent: HOW_TO light, comparison moderate, worry/experience strong. Never invent personal experience. `mobile_story_max_chars` accepts integer 24–40, default 28. Count visible characters in each intentionally composed prose segment (not HTML tags); this is an editorial maximum, not a physical-screen-width guarantee. Keep headings, URLs, code, and indivisible UI labels accurate and document exceptions. Prefer semantic paragraphs and natural browser wrapping; avoid gratuitous `<br>` and do not require user CSS. `emoji_policy` supports `NONE` (default) and `SPARING` only for this style; never require emoji or insert them in headings, instructions or safety warnings.

## Existing articles and product boundaries
The article's recorded style and maximum take precedence over site defaults in Doctor/Writer revisions. Without metadata, preserve the observed style; do not infer MOBILE_STORY from short lines alone. No automatic monitoring reset, case creation, rewriting, or publication. aCreator/Shared rules do not themselves implement the Manager UI or downstream persistence.
