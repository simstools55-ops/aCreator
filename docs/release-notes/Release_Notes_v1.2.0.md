# SIMS Article Creator v1.2.0 Release Notes

## Release theme
Shared Knowledge Integration

## Implemented
- SIMS-Shared-Editorial-Knowledge v1.1.0をSingle Source of Truthとして統合
- RepositoryとClaude Projectへ読取専用`shared/`スナップショットを搭載
- Shared Snapshot Manifest、Source、SHA-256完全性検証を追加
- Knowledge Load RuntimeとProject InstructionsをShared優先方式へ更新
- Article Creator専用Knowledge、Pattern、Contract、HTML出力、Learningを維持

## Compatibility
- SIMS_ARTICLE_CREATOR_V1 JSON Contract変更なし
- SIMS_ARTICLE_LEARNING_RECORD_V1変更なし
- 公開用HTML出力形式変更なし
- Writer専用Preservation／Rewrite制御は未導入

## Validation
全既存回帰テスト、Shared完全性検証、Repository／Claude同一性検証に合格。
