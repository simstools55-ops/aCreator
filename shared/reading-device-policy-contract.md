# Reading Device Policy Contract — v3.6.5

`reading_device_policy`: new article choices `DESKTOP_FIRST` (legacy behavior) or `MOBILE_STORY`; missing, unknown, historical `BALANCED`/`MOBILE_FIRST` -> legacy behavior for new articles. Do not rewrite historical stored values.

`mobile_story_max_chars`: optional integer 24–40, default 28, applicable only to `MOBILE_STORY`.

`emoji_policy`: `NONE` or `SPARING` for `MOBILE_STORY`, default `NONE`; historical `EXPRESSIVE` is not selectable in the new UI. Article-level recorded style wins for revisions; absent metadata means preserve existing presentation, not infer mobile story.

These are editorial controls, not new case statuses or mandatory additions to existing JSON output schemas. Preserve existing validation, approval and publication gates. No user CSS required.
