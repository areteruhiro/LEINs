# ボタン設定

[ホームへ戻る](../index.html) / [設定画面の使い方](settings-ui.md)

通話ボタン、フォント、LEINs追加ボタンの表示を調整します。

> 2026年6月21日時点の `LEINsOptions.java`、日本語リソース、`hooks` 実装を照合しています。表示項目はAPK・プラン・LINEバージョンで変わる場合があります。

## 現在の設定項目（6件）

| 表示名 | 説明 | 初期 | 利用範囲 | 設定キー |
|---|---|:---:|---|---|
| LINE通話ボタンを非表示 | トーク内の通話メニューからLINE通話ボタンを非表示にします。 | ON | Trial / Basic / Unlock | `photoboothButtonOption` |
| 音声通話ボタンを非表示 | トーク内の通話メニューから音声通話ボタンを非表示にします。 | OFF | Trial / Basic / Unlock | `voiceButtonOption` |
| ビデオ通話ボタンを非表示（グループ） | グループトーク内の通話メニューからビデオ通話ボタンを非表示にします。 | ON | Trial / Basic / Unlock | `videoButtonOption` |
| ビデオ通話ボタンを非表示（個人） | 個人トーク内の通話メニューからビデオ通話ボタンを非表示にします。 | ON | Trial / Basic / Unlock | `videoSingleButtonOption` |
| アプリ全体を任意のフォントに変更します | 設定したディレクトリに\"lein.ttf\"ファイルを配置してください。\nフォントのメトリクス（行の高さ）を手動調整する場合は\"font.txt\"を編集し ascent=- / descent= の形式で編集して下さい | ON | Unlock | `FontChange` |
| LiffアプリとLINE内Webのフォントを変更します | 設定したディレクトリに\"lein.ttf\"ファイルを配置してください。\nフォントのメトリクス（行の高さ）を手動調整する場合は\"font.txt\"を編集し ascent=- / descent= の形式で編集して下さい | ON | Unlock | `FontChange_Liff_Web` |

## LINE内の詳細設定

スイッチとは別に、機能が有効なときだけ表示される設定ボタンがあります。

- LEINsボタンの位置・余白設定

## 変更後の確認

1. 設定を変更します。
2. 再起動確認が表示された場合はLINEを再起動します。
3. 対象画面で動作を確認します。問題があれば直前の設定をOFFに戻します。
