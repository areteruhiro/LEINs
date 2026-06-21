# プライバシー・既読

[ホームへ戻る](../index.html) / [設定画面の使い方](settings-ui.md)

既読送信、未読維持、既読者確認、ブロック確認を調整します。

> 2026年6月21日時点の `LEINsOptions.java`、日本語リソース、`hooks` 実装を照合しています。表示項目はAPK・プラン・LINEバージョンで変わる場合があります。

## 現在の設定項目（14件）

| 表示名 | 説明 | 初期 | 利用範囲 | 設定キー |
|---|---|:---:|---|---|
| メッセージを常に未読のままにする | 各チャットにON/OFFスイッチを追加します。OFFにすると、そのチャットを開いても相手に既読が通知されません。 | OFF | Trial / Basic / Unlock | `prevent_mark_as_read` |
| (常に既読を付けない)既読を付ける相手の編集 | 特定のチャットだけ既読送信を個別に制御します。「常に未読のまま」と併用できます。 | OFF | Trial / Basic / Unlock | `PreventMarkAsRead_Setting` |
| チャットを開くと未読バッジを消す | 「常に未読のまま」が有効でも、チャットを開いた際に未読バッジだけを消します。 | OFF | Trial / Basic / Unlock | `MarkAsRead` |
| ここまで既読ボタンの作成 | メッセージ長押しメニューに「ここまで既読」を追加します。 | OFF | Trial / Basic / Unlock | `MarkAsRead_Button` |
| 「送信したら既読」スイッチを削除 | チャットリストの長押しメニューから「未読にする」の項目を削除します。 | OFF | Trial / Basic / Unlock | `remove_keep_unread` |
| 「送信したら既読」スイッチを表示（非root） | rootなしでLINEを使っているユーザー向けに「未読にする」スイッチを表示します。 | OFF | Trial / Basic / Unlock | `Keep_UnreadLSpatch` |
| チャットリストに「送信したら既読」切り替えボタンを追加 | チャットリストのヘッダーに送信したら既読ボタンを追加します。長押しメニューを開いた後も未読のまま維持できます。 | OFF | Trial / Basic / Unlock | `Keep_unread_PopupListView` |
| 送信したメッセージの既読者確認 | 送信したメッセージに既読確認アクションを追加し、誰が読んだか確認できるようにします。 | OFF | Trial / Basic / Unlock | `ReadChecker` |
| クイック既読確認ボタン（新） | メッセージを長押しすると、既読確認ボタンが表示されます。 | OFF | Trial / Basic / Unlock | `ReadCheckerNewOption` |
| 既読確認データベース更新をLINEから行う | 既読確認用のデータベース更新を検出して記録します | OFF | Trial / Basic / Unlock | `ReadCheckerSqliteUpdateCapture` |
| 既読確認に自分のメッセージのみ表示 | 既読確認の一覧で、受信したメッセージを非表示にして自分の送信メッセージだけを表示します。 | OFF | Trial / Basic / Unlock | `MySendMessage` |
| 既読データリセットボタン（緊急用） | 既読確認ボタンの横にデータリセットボタンを追加します。既読情報が正しく表示されない場合のみ使用してください。 | OFF | Trial / Basic / Unlock | `ReadCheckerChatdataDelete` |
| >ブロック監視[誤検知可能性有] | ブロックされた可能性のあるユーザーの名前を変更します | ON | Basic / Unlock | `BlockCheck` |
| チャットリスト右上の＋メニューに\"常に既読をつけない\"\"自動返信\"のクイック切替を追加します。 | チャットリスト右上の＋メニュー末尾に LEINs 項目を追加し、既読防止と自動返信をすばやく切り替えます。 | OFF | Trial / Basic / Unlock | `QuickToggleButton` |

## LINE内の詳細設定

スイッチとは別に、機能が有効なときだけ表示される設定ボタンがあります。

- 既読送信の相手別設定
- ブロックリスト
- チャットリスト未読カウントのリセット

## 変更後の確認

1. 設定を変更します。
2. 再起動確認が表示された場合はLINEを再起動します。
3. 対象画面で動作を確認します。問題があれば直前の設定をOFFに戻します。
