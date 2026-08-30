# SIMS Article Creator v1.1.0 Release Notes

## 概要
v1.0.1後の実記事運用試験5件で確認した品質課題を、Knowledge、Pattern、Runtime、Contractへ反映したQuality Enhancementリリースです。公開用完成記事の標準形式をMarkdownからHTMLへ変更しました。

## 主な改善
- HTMLコピー用完成記事と`article.body_html`を正式採用
- Hidden Anxiety、Intent Gap、Selection Guidanceを標準化
- Review記事の口コミ出典区分・競合比較を強化
- Buying Guideの意思決定支援表と条件分岐提案を追加
- Local Guideのrobots制限時Evidence Policyを調整
- 内部リンクを「読む理由→リンク」の文脈型へ統一
- Evidence TransparencyをPublication Gateへ追加

## 互換性
- JSON format名は`SIMS_ARTICLE_CREATOR_V1`を維持
- contract_versionは`1.3.0`
- `body_markdown`は廃止し`body_html`へ変更
- `article.publishing_format`の標準値は`HTML`
