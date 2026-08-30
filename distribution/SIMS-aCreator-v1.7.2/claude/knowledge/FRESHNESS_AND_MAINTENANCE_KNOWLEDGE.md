# Freshness and Maintenance Knowledge

## High-change fields
価格、在庫、法令、制度、製品仕様、UI、提供機能、営業時間、人物の役職、統計、ランキング。

## Rules
- 情報基準日をEditorial Briefと最終出力へ持たせる。
- 高変動情報は確認できない場合に具体値を断定しない。
- 年号の装飾的付与を避ける。
- 更新トリガーと推奨再確認時期を定義する。
- Evergreen部分とUpdate-dependent部分を分離する。

## Freshness Expression Standard v1.4.0
- 高変動トピックでは、原則として`執筆時点（YYYY年M月時点）`または`確認時点（YYYY年M月時点）`を使用する。
- 年月だけの装飾的な`最新版`表現は、当該範囲を実際に再確認した場合に限る。
- UI、料金、法令、仕様、人物、在庫などは基準年月と確認範囲をセットで示す。
- 低変動トピックでは、年月が読者価値を高めない場合は日付を省略できる。
- 固定年月を本文に入れた場合は、Quality Reportへ更新トリガーを記録する。
