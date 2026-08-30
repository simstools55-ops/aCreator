# Release Notes — SIMS Article Creator v1.0.0

Release date: 2026-07-20

## 概要
メインキーワードから、検索意図分析、記事設計、根拠計画、本文、FAQ、内部リンク、品質審査、公開判定、構造化JSONまでを生成する正式安定版。

## 主な機能
- 8種類のArticle PatternとPattern Composer
- Knowledge Architectureと優先順位制御
- Evidence / Fabrication Prevention / YMYL Safety Gate
- Personal Blogger向けEditorial VoiceとPublish Mode
- AdSense / Affiliate分岐と収益導線制御
- JSON Contract v1.2
- SWLS Learning Record / 10記事Learning Report

## 品質確認
実記事UAT 10記事と追加YMYL試験を完了。契約、Knowledge、Pattern、Quality、Learning、UAT Packageの静的検証を実施した。

## 互換性
SIMS WriterおよびSIMS-Blog-Managerとは独立して動作する。v0.7.2からは設定・資産を引き継げるが、Claude Projectは本配布版で全置換することを推奨する。

## Known limitations
- 検索順位や収益成果を保証しない。
- 外部情報の正確性・最新性は入力資料と利用環境に依存する。
- YMYLは専門家レビューが必要になる場合がある。
- 自動自己改変は行わず、Learning結果は人間承認を必要とする。
