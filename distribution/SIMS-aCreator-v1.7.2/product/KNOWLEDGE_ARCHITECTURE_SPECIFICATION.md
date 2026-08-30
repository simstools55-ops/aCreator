# Knowledge Architecture Specification v1.0

## Scope

SIMS Article CreatorのEditorial Core、Quality System、Publication Gateが利用する判断知識を定義する。

## Non-goals

- 特定キーワードの検索結果を固定保存しない。
- 検索エンジンの一時的な順位要因を断定しない。
- SIMS WriterのKnowledgeをRuntime依存として読み込まない。
- 記事タイプ別構成の詳細はPattern Libraryへ分離する。

## Required capabilities

- Knowledge routing
- Applicability filtering
- Precedence and conflict resolution
- Freshness awareness
- Claim and source classification
- Safety escalation
- Quality Gate linkage
- Testable manifest

## Acceptance criteria

1. すべてのKnowledgeがManifestへ登録されている。
2. RuntimeがKnowledge Indexを最初に参照する。
3. YMYL・Evidence・SafetyがSEOより優先される。
4. 根拠不足を生成で補完しない。
5. 記事タイプKnowledgeと一般Knowledgeを分離できる。
