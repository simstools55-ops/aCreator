# Knowledge Architecture v1.0

## 目的

Editorial Coreが参照する知識を、再現可能・監査可能・更新可能な形で管理する。

## 原則

1. Runtimeは処理順序を決め、Knowledgeは判断基準を提供する。
2. Knowledgeは本文を直接決めず、Editorial Brief、Evidence Plan、Quality Gateの判断を拘束する。
3. 適用対象外のKnowledgeを無理に使わない。
4. 根拠・安全性・契約は、SEOや文章表現より常に優先する。
5. 時点依存情報は、鮮度確認なしに確定表現へ変換しない。

## レイヤー

- L0 Contract / Safety：絶対遵守
- L1 Product Policy：製品原則
- L2 Domain Knowledge：検索意図、読者、SEO、証拠等
- L3 Article Type Pattern：次フェーズで実装
- L4 Request Context：ユーザー入力、サイト条件、記事条件

## 競合時の優先順位

Contract > Safety/YMYL > Evidence > Product Policy > Reader Value > Search Intent > Article Pattern > SEO Tactics > Style Preference

## 更新単位

各Knowledgeは、ID、版、目的、適用条件、禁止事項、出力への影響を持つ。外部状況に依存する知識は更新日と再確認条件を持つ。
