# Contract Test Cases

1. 正常な最小入力が通る
2. `main_keyword`欠落で失敗する
3. 未知のトップレベル項目で失敗する
4. formatが異なる出力で失敗する
5. 公開判定が列挙外なら失敗する
6. quality scoreが0〜100外なら失敗する
7. first_party_experience.used=trueでも根拠がないケースを意味検証で失敗させる
8. BLOCKEDなのにblocking_issuesが空のケースを意味検証で失敗させる

JSON Schemaは構文契約を担当し、7〜8は後続のSemantic Validatorで実装する。
