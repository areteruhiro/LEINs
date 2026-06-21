# ブラウザ・リンク

[ホームへ戻る](../index.html) / [設定画面の使い方](settings-ui.md)

LINE内リンクの開き方とWeb表示を調整します。

> 2026年6月21日時点の `LEINsOptions.java`、日本語リソース、`hooks` 実装を照合しています。表示項目はAPK・プラン・LINEバージョンで変わる場合があります。

## 現在の設定項目（4件）

| 表示名 | 説明 | 初期 | 利用範囲 | 設定キー |
|---|---|:---:|---|---|
| リンクを外部ブラウザで開く | LINE内のリンクをタップすると、LINE内蔵ブラウザではなくスマホの標準ブラウザで開きます。 | ON | Trial / Basic / Unlock | `redirect_webview` |
| ブラウザアプリを使用 | 上の「外部ブラウザで開く」が有効なとき、ブラウザタブではなく独立したブラウザアプリとして開きます。 | OFF | Trial / Basic / Unlock | `open_in_browser` |
| 設定を LINE に埋め込まない | LINE内に表示されるLEINsの歯車ボタンを非表示にします。LEINsアプリからは引き続き設定を変更できます。 | OFF | Trial / Basic / Unlock | `removeOption` |
| LINE内Webをダーク表示にする | LINE内蔵ブラウザとLIFFのWebViewページにダーク表示用のスタイルを適用します。 | OFF | Basic / Unlock | `web_dark` |

## 変更後の確認

1. 設定を変更します。
2. 再起動確認が表示された場合はLINEを再起動します。
3. 対象画面で動作を確認します。問題があれば直前の設定をOFFに戻します。
