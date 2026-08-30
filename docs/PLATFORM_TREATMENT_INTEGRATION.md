# Platform Treatment Integration v1.6.2

SIMS Article Creatorは、SIMS Editorial Platformにおいて新規記事作成を担当する専門製品です。

## Control boundary
- RequestはSBMから受け取る。
- SBM発行のSiteID、CaseID、Treatment Request ID、Draft Article IDを変更しない。
- 既存記事を直接修正しない。必要な修正はWriter Referral候補としてSBMへ返す。
- 統合・カニバリ判断が必要な場合はMerge Referral候補としてSBMへ返す。
- 公開済みとは扱わず、成果物生成後は`PUBLICATION_PENDING`を推奨する。

## Compatibility
既存のキーワード起点記事生成と`SIMS_ARTICLE_CREATOR_V1`出力は維持する。Platform Requestの場合のみ共通Envelope付きTreatment Resultを追加する。
