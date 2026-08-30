# Pattern Composer Runtime v1.0

## 入力
Keyword Intelligence、Search Intent、Reader Problem、Article Type候補、Freshness/YMYL判定。

## 実行
1. PATTERN_MANIFESTを確認する。
2. PATTERN_ROUTINGでPrimaryを1件選ぶ。
3. 必要時だけSecondaryを最大2件選ぶ。
4. PATTERN_COMPOSER_RULESに従って構成モジュールを合成する。
5. Pattern固有品質ゲートをQuality Reportへ渡す。

## 失敗時
- Primaryを決められない: `NEEDS_REVISION`、reason=`PATTERN_AMBIGUOUS`
- 必要な根拠がない: `NEEDS_EVIDENCE`
- YMYL High: `NEEDS_EXPERT_REVIEW`

## 完了条件
Pattern Selection Reportと合成済みArticle Blueprintが生成されていること。
