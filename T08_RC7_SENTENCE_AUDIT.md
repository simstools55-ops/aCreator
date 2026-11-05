# T08 RC7 — 文長検査・Coverage維持（UAT）

通常文は指定文字数以下を原則とする。文章は「。」「！」「？」で分割し、HTMLタグを除いた表示文字で測る。改行や段落を分割しても1文の長さは変わらない。

必須報告項目：`prose_over_limit_raw` / `prose_over_limit_approved_exception` / `prose_over_limit_unresolved` / `exception_details`。

例外は不可分なUI操作パス、正式名称、URL等のみ。一般説明文が長い場合は例外にせず短文化する。例外を使った場合は根拠を明記する。

M01〜M14のCoverage表を本文見出しに照合し、present/evidence_limited/missingを維持する。根拠不足は公開判定へ独立して反映する。

**注意：** この検査は文章編集上の品質チェックであり、公開の事実確認や実機確認を代替しない。
