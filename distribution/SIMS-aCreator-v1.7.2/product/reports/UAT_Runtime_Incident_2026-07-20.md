# UAT Runtime Incident — 2026-07-20

## 症状
Claudeが `knowledge/`、`runtime/`、`patterns/`、`contracts/` 配下の資産を「環境に実在しない」と判断し、Project Instructions本文だけで記事を生成した。

## 原因
Project Instructionsのロード順序がファイルパス形式で記述され、Claude Project上のKnowledge資産をローカルファイルシステムとして解釈させる余地があった。

## 影響
Safety・Evidence・Pattern・Contractの完全適用を保証できず、JSON Contractも簡略形式へ逸脱した。

## 修正
- Project Knowledge Bindingを明文化
- パス表記を論理識別名として定義
- Safety CoreをProject Instructionsへ常設
- robots制限時のEvidence Fallbackを追加
- 疑似体験表現を抑止

## 判定
Priority: P1 / Regression risk: LOW / Release: v1.0.1
