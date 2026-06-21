# チャット・メッセージ

[ホームへ戻る](../index.html) / [設定画面の使い方](settings-ui.md)

送信取消、入力、リアクション、保存、検索、自動返信を調整します。

> 2026年6月21日時点の `LEINsOptions.java`、日本語リソース、`hooks` 実装を照合しています。表示項目はAPK・プラン・LINEバージョンで変わる場合があります。

## 現在の設定項目（24件）

| 表示名 | 説明 | 初期 | 利用範囲 | 設定キー |
|---|---|:---:|---|---|
| 非表示チャットを再表示されないようにする | 手動で非表示にしたチャットが、自動的にメインのチャットリストに戻ってこないようにします。 | OFF | Trial / Basic / Unlock | `Archived_message` |
| アーカイブ設定 | 非表示チャットの再表示防止期間を設定します | OFF | Trial / Basic / Unlock | `Archived_Stting` |
| リアクション数バッジを表示 | リアクションシート（メッセージ長押し時のオーバーレイ）に、各リアクション種別のカウントバッジを表示します。カウントはリアルタイムで取得されます。 | OFF | Trial / Basic / Unlock | `ReactionCount` |
| 詳細リアクション一覧ボタンを作成 | LINEが端末に保存しているデータをもとに、通常のリアクション一覧に追加情報を表示します。メッセージ長押し時に、そのメッセージだけのリアクション者も確認できます。 | OFF | Trial / Basic / Unlock | `ReactionList_db` |
| Enterキーで送信 有効/無効切り替えボタンのチャットリストで作成 | [設定→トーク→Enterキーで送信]を有効/無効にします | OFF | Trial / Basic / Unlock | `SendEnterChange_ChatList` |
| Enterキーで送信 有効/無効切り替えボタンをトーク内に作成 | トーク内にEnterキー送信のON/OFFボタンを追加します。開いているトークにも即時反映します。 | OFF | Trial / Basic / Unlock | `SendEnterChange_InChat` |
| 音声ボタンを無効化 | チャットの入力欄にあるマイクアイコンを非表示にします。 | OFF | Trial / Basic / Unlock | `RemoveVoiceRecord` |
| 「送信取り消し」を無効 | 取り消されたメッセージのトークを変更する」でメッセージを変更することが出来ます。\n メッセージが非表示の際はメッセージの右に目印がつきます。 \n URI先に`unsent.png`を配置すると画像に変更できます。unsent MARKはお知らせメッセージが非表示の際のみ表示されます | OFF | Trial / Basic / Unlock | `prevent_unsend_message` |
| 送信取消メニューを追加 | メッセージのコンテキストメニューに送信取消関連の項目を追加します | OFF | Trial / Basic / Unlock | `preventUnsendMessage_Context_Menu` |
| 常にミュートメッセージとして送信 | 送るメッセージをすべてサイレント送信にします。 | OFF | Basic / Unlock | `mute_message` |
| メッセージの予約送信 | トーク画面に予約メッセージボタンを作成します。送信設定された時間にLINEが開かれている必要があります。 | OFF | Trial / Basic / Unlock | `MessageSend` |
| メッセージ追加 | メッセージ長押しメニューに追加ボタンを表示し、選択メッセージの直前・直後・指定日時に一時メッセージを挿入します。トークを閉じると追加分は削除されます。 | OFF | Unlock | `MessageAdd` |
| 招待拒否 | グループメニューに招待拒否を追加します。ここで有効にしたあと、グループメニューから友だちを選び、グループごとに有効化します。 | OFF | Basic / Unlock | `GroupInviteReject` |
| 自動返信 | 自動返信を有効にしてから、リプレイメッセージ編集で設定と使い方を確認できます。 | OFF | Basic / Unlock | `AutoReplay` |
| AI要約ボタンを非表示 | (オープン)チャット画面に表示されるAI会話要約ボタンを非表示にします。 | OFF | Trial / Basic / Unlock | `chat_ui_square_ai_summary_button` |
| AIのサジェストアイコンを非表示 | [設定→LINE AIサービス→→アイコンの表示設定→表示しない]\nの期間を遠い未来に設定します(反映させるため一度設定を開いて下さい) | OFF | Trial / Basic / Unlock | `Disable_chat_ui_ai_talk_suggestion` |
| チャットの表示名をカスタマイズ | チャット内グループ名の左に「N」ボタンを追加します。\n最初に「元の名前を保存」にチェックを入れてください。トグル長押しまたは空欄保存で、保存された名前を入力します。 | ON | Trial / Basic / Unlock | `LocalName` |
| 固定チャットの並び順を設定 | 固定（ピン留め）したチャットの表示順を手動で設定できます。数値が小さいほど上に表示されます。 | OFF | Trial / Basic / Unlock | `PinList` |
| 1文字から検索できるようにする | 検索キーワードを1文字から入力できるようにします。 | ON | Trial / Basic / Unlock | `minimumAcceptableKeywordLength` |
| 検索フィルター | 検索結果を送信者名で表示/除外するフィルターボタンをチャットヘッダーに追加します。 | ON | Trial / Basic / Unlock | `SearchFilter` |
| 画像・動画の保存時のファイル名を変更 | チャットから画像・動画を保存するときのファイル名テンプレートを自由に設定できます。使用可能：SenderName, createdTime, Talkname。 | OFF | Basic / Unlock | `PhotoSave` |
| 写真・動画送信制限を回避 | 写真送信時のリサイズ上限とJPEG圧縮を抑え、動画選択時の5分制限も回避します。LINE 15.12.2のみ対応です。 | OFF | Basic / Unlock | `HighQualityPhoto` |
| アルバム自動ダウンロード | アルバムの画像や動画を自動でダウンロードします | OFF | Basic / Unlock | `AlbumAutoDownload` |
| ファイル自動ダウンロード設定 | チャットで受信した対応ファイルを、送信者・種類・サイズ・ネットワークの設定に従って自動ダウンロードします。LINE 15.12.2のみ対応です。 | OFF | Basic / Unlock | `Chat_File_Download` |

## LINE内の詳細設定

スイッチとは別に、機能が有効なときだけ表示される設定ボタンがあります。

- 画像・動画保存ファイル名
- ファイル自動ダウンロード条件
- 固定チャット順
- アーカイブ
- 取消メッセージ表示
- 自動返信

## 変更後の確認

1. 設定を変更します。
2. 再起動確認が表示された場合はLINEを再起動します。
3. 対象画面で動作を確認します。問題があれば直前の設定をOFFに戻します。
