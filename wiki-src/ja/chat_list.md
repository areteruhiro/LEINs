# チャットリスト

[ホームへ戻る](../index.html) / [設定画面の使い方](settings-ui.md)

トーク一覧上部の検索・ショートカット・作成ボタンを整理します。

> 2026年6月21日時点の `LEINsOptions.java`、日本語リソース、`hooks` 実装を照合しています。表示項目はAPK・プラン・LINEバージョンで変わる場合があります。

## 現在の設定項目（6件）

| 表示名 | 説明 | 初期 | 利用範囲 | 設定キー |
|---|---|:---:|---|---|
| 検索バーを非表示 | チャットリスト上部の検索バーを非表示にします。 | OFF | Trial / Basic / Unlock | `removeSearchBar` |
| アルバムショートカットを非表示 | チャットリストのヘッダーにあるアルバムショートカットを非表示にします。 | OFF | Trial / Basic / Unlock | `removeNaviAlbum` |
| オープンチャットショートカットを非表示 | チャットリストのヘッダーにあるオープンチャットショートカットを非表示にします。 | OFF | Trial / Basic / Unlock | `removeNaviOpenchat` |
| チャットリスト内のAiボタンの削除 | チャットリストのヘッダーにあるAIフレンドショートカットを非表示にします。 | OFF | Trial / Basic / Unlock | `removeNaviAichat` |
| チャットリスト内でのトークルームを作成ボタンの非表示 | チャットリストにある新規トーク作成ボタンを非表示にします。 | OFF | Trial / Basic / Unlock | `removeCreateChatButton` |
| 「もっと」ボタンを非表示 | チャットリストにある「：」ボタンを非表示にします。 | OFF | Trial / Basic / Unlock | `removeMoreButton` |

## 変更後の確認

1. 設定を変更します。
2. 再起動確認が表示された場合はLINEを再起動します。
3. 対象画面で動作を確認します。問題があれば直前の設定をOFFに戻します。
