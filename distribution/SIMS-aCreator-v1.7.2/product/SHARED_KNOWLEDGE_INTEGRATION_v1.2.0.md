# Shared Knowledge Validation v1.2.0

## Required checks

1. `shared/VERSION`が`1.1.0`であること。
2. `shared/SOURCE.md`がArticle Creator 1.2.0への統合を示すこと。
3. `shared/SNAPSHOT_MANIFEST.json`に記録された全ファイルが存在すること。
4. 全SHA-256が一致すること。
5. `mappings/article-creator/application-mapping.md`が含まれること。
6. Repository版とClaude Project版のSharedスナップショットが同一であること。
7. SharedがRuntimeの論理ロード順に含まれること。
8. 既存Knowledge Manifest、Pattern Manifest、JSON Contractが変更されていないこと。
9. Writer専用制御がCreator Runtimeへ混入していないこと。
10. 既存v1.1.0回帰テストがすべて通ること。

## Failure policy

- 欠落・ハッシュ不一致・Source不整合はrelease blockingとする。
- Shared参照不能時のRuntimeフォールバック欠如はrelease blockingとする。
- JSON Contractの非互換変更はrelease blockingとする。
- 文書上の軽微な表記差はwarningとするが、Snapshot自体の改変はwarningに降格しない。
