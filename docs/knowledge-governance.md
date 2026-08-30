# Knowledge Governance

## Single Source of Truth

`claude/knowledge/KNOWLEDGE_MANIFEST.json`をKnowledge登録簿とする。Manifestにない文書はRuntime必須Knowledgeとして扱わない。

## 変更ルール

- 意味変更はKnowledgeのversionを更新する。
- 安全性・契約・公開判定への影響を記録する。
- 廃止時は削除せず、最初にdeprecatedへ変更し代替IDを指定する。
- 外部SEO情報を恒久ルールへ直接コピーしない。製品原則に翻訳して採用する。

## 監査

Knowledgeテストでは、Manifestのファイル存在、重複ID、必須属性、Runtime参照、UTF-8、Writer依存を検証する。
