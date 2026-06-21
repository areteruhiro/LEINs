# 通話・着信音

[ホームへ戻る](../index.html) / [設定画面の使い方](settings-ui.md)

通話画面、入出力音量、着信音・発信音を調整します。

> 2026年6月21日時点の `LEINsOptions.java`、日本語リソース、`hooks` 実装を照合しています。表示項目はAPK・プラン・LINEバージョンで変わる場合があります。

## 現在の設定項目（11件）

| 表示名 | 説明 | 初期 | 利用範囲 | 設定キー |
|---|---|:---:|---|---|
| 通話画面にLINEを開くボタンを追加 | 通話画面にLINEアプリを開くボタンを追加します。通話中にチャットを確認したいときに便利です。 | ON | Trial / Basic / Unlock | `CallOpenApplication` |
| SilentCheck | 着信音を鳴らす前にスマホがサイレントモードかどうかを確認し、サイレント中は着信音をスキップします。 | OFF | Trial / Basic / Unlock | `SilentCheck` |
| 通話中は着信設定を自動で切り替え | 設定→通話→通話の着信許可の有無を通話開始/切断で変更します | OFF | Trial / Basic / Unlock | `CallComing` |
| LINE通話の入出力音量をブースト | LINE通話画面に「音量」ボタンを追加し、入力・出力ブーストを調整します。端末上限を超える増幅はOSとハードウェアに依存します。 | OFF | Basic / Unlock | `CallVolumeBoost` |
| 本体の発着信音を鳴らす（非root） | LINE通話の着信音を、LINEの内蔵音ではなくスマホのデフォルト着信音に変更します。非rootユーザー向けの機能です。 | OFF | Trial / Basic / Unlock | `callTone` |
| LINE着信音をミュート (root) | LINEの着信音を完全に無音にします。rootユーザー向けの機能です。 | OFF | Trial / Basic / Unlock | `MuteTone` |
| 発信音を無効化 | 電話をかけているときに鳴るダイアルトーンを無効にします。 | OFF | Trial / Basic / Unlock | `DialTone` |
| (発信音を鳴らす)着信音を利用する | LINE通話の着信・発信音量として端末の着信音量を使用します。 | OFF | Trial / Basic / Unlock | `ringtonevolume` |
| 着信音 停止ボタンを追加 | 非rootユーザー向けの着信音再生機能に「停止ボタン」を追加します。 | OFF | Trial / Basic / Unlock | `StopCallTone` |
| 通話終了時に効果音を再生(非root要) | 通話終了時に効果音（lineapp_endthis_16k.wav）を再生します。LEINsの設定フォルダにファイルを置いてください。 | OFF | Trial / Basic / Unlock | `CallDisconnectTone` |
| オリジナルの着信音に変更 | LINEの着信音をシステムの着信音ピッカーで選択した音に変更します。 | OFF | Trial / Basic / Unlock | `Original_Tone` |

## 変更後の確認

1. 設定を変更します。
2. 再起動確認が表示された場合はLINEを再起動します。
3. 対象画面で動作を確認します。問題があれば直前の設定をOFFに戻します。
