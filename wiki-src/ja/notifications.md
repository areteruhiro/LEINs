# 通知

[ホームへ戻る](../index.html) / [設定画面の使い方](settings-ui.md)

通知フィルター、画像・操作ボタン、サイレント通知を調整します。

> 2026年6月21日時点の `LEINsOptions.java`、日本語リソース、`hooks` 実装を照合しています。表示項目はAPK・プラン・LINEバージョンで変わる場合があります。

## 現在の設定項目（14件）

| 表示名 | 説明 | 初期 | 利用範囲 | 設定キー |
|---|---|:---:|---|---|
| 特定のユーザー名、グループ名のみ以外の通知をオフ | 指定した連絡先・グループからの通知だけを受け取り、それ以外は全て通知をキャンセルします。LINE内のLEINsボタンからリストを管理できます。 | OFF | Trial / Basic / Unlock | `CansellNotification` |
| 特定グループの通知をミュート | 指定したグループからの通知をオフにします。LINE内のLEINsボタンからミュートリストを管理できます。 | OFF | Trial / Basic / Unlock | `Disabled_Group_notification` |
| LINE通知のカスタマイズ | 画像メッセージの通知に実際の画像を添付し、LINEを開かずにプレビューできます。通知が1〜3秒遅れる場合があります。 | OFF | Trial / Basic / Unlock | `PhotoAddNotification` |
| グループ通知 | グループ通知で通知を発行します | OFF | Trial / Basic / Unlock | `GroupNotification` |
| 通知にコピーアクションを追加 | メッセージ通知に「コピー」ボタンを追加します。LINEを開かずに通知からテキストをコピーできます。 | OFF | Trial / Basic / Unlock | `AddCopyAction` |
| リアクションを通知 | 誰かが自分のメッセージにリアクションしたとき通知します。LEINsのバックグラウンド実行を許可する必要があります。 | OFF | Trial / Basic / Unlock | `NotificationReaction` |
| 通知に既読ボタンを追加 | メッセージ通知に既読ボタンを追加します。LINEを開かずに通知から既読にできます。 | OFF | Trial / Basic / Unlock | `CreateMarkAsCheck` |
| 通知の「通知をオフ」アクションを削除 | 通知を展開したときに表示される「チャットをミュート」アクションを削除します。 | ON | Trial / Basic / Unlock | `remove_reply_mute` |
| オリジナル通知IDを使う | LINEのオリジナル通知IDを使用します。通知の返信ボタンが動かないバグを修正しますが、同じ相手からの新しい通知が古いものを上書きします。 | OFF | Trial / Basic / Unlock | `original_ID` |
| サイレントメッセージの無効(次回の通知ありの通知で通知されます) | 相手がサイレント送信したメッセージも、通常の通知音・バイブで知らせます。 | OFF | Trial / Basic / Unlock | `DisableSilentMessage` |
| アルバム追加の通知をミュート | グループアルバムに写真が追加されたときの通知を非表示にします。 | ON | Trial / Basic / Unlock | `DisableNotificationAlbumAdd` |
| 着信通知にミュートボタンを追加 | 着信通知にミュートボタンを追加し、通知から直接着信音を止められます。 | OFF | Trial / Basic / Unlock | `CreatedMute` |
| 着信通知に返信ボタンの作成 | 着信通知に返信アクションを追加します。 | OFF | Trial / Basic / Unlock | `CreateCallReply` |
| 既読ボタンを押した際に通知を削除する | 既読ボタンを作成するを有効にして下さい | OFF | Trial / Basic / Unlock | `CreateMarkAsCheck_Notification_delete` |

## LINE内の詳細設定

スイッチとは別に、機能が有効なときだけ表示される設定ボタンがあります。

- ミュート対象グループ
- 通知フィルター対象

## 変更後の確認

1. 設定を変更します。
2. 再起動確認が表示された場合はLINEを再起動します。
3. 対象画面で動作を確認します。問題があれば直前の設定をOFFに戻します。
