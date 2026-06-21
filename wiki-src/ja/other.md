# 上級者向け

[ホームへ戻る](../index.html) / [設定画面の使い方](settings-ui.md)

セキュリティ、LSPatch、設定保存、ログ、開発者向け機能をまとめています。

> 2026年6月21日時点の `LEINsOptions.java`、日本語リソース、`hooks` 実装を照合しています。表示項目はAPK・プラン・LINEバージョンで変わる場合があります。

## 現在の設定項目（14件）

| 表示名 | 説明 | 初期 | 利用範囲 | 設定キー |
|---|---|:---:|---|---|
| ⚠ E2EE暗号化を無効化 | ⚠ 危険: エンドツーエンド暗号化を無効化します。自分だけでなく、相手側の暗号化も解除される可能性があります。リスクを完全に理解した上でのみ使用してください。 | OFF | Trial / Basic / Unlock | `E2EE_Disable` |
| サブ端末をメイン端末に偽装 | LINEのショップ用サブ端末判定をfalseに固定し、サブ端末をメイン端末に偽装します。 | OFF | Unlock | `FiASubDeviceGateFalse` |
| フォアグラウンド通知の発行 | LINEをフォアグラウンドサービスとして常時起動し、LINEを開いていなくても通知が届くようにします。バッテリー消費が増える場合があります。 | OFF | Trial / Basic / Unlock | `SystemForegroundService` |
| LEINsの更新を自動確認 | LEINsのGitHubページを自動確認し、新しいバージョンがあれば通知します。 | OFF | Trial / Basic / Unlock | `AutoUpDateCheck` |
| "(AntiApk)設定項目トークボタンを開く " |  | OFF | Trial / Basic / Unlock | `SettingClick` |
| LINE設定項目フィルター | LINEのメイン設定に表示する項目を選択できます。新しく検出された項目は自動で追加されます。 | OFF | Trial / Basic / Unlock | `Setting_Filter` |
| SharedPreferences設定モード | 起動時にSAF同期ではなくアプリ内のSharedPreferencesキャッシュからLEINs設定を読み込みます。オフの場合は従来のSAF設定を使用します。 | OFF | Trial / Basic / Unlock | `SharedPreferencesSettingsMode` |
| FCMトークンを取得 | LINEのログイントークンをログに記録します。外部ツールと連携する上級者向けの機能です。 | OFF | Trial / Basic / Unlock | `TokenGet` |
| SHA-1 HEXログ出力 | FCMトークンを取得が上手に出来ない場合に有効にします。 | OFF | Trial / Basic / Unlock | `HexOutput` |
| 生体情報連携を許可をLSpach/NPachでも可能に |  | OFF | Trial / Basic / Unlock | `Biometric_information` |
| Sonyランチャーのバッジ数を修正 | Sonyのホームランチャーで未読バッジ数が表示されない問題を修正します。Sonyデバイス以外では不要です。 | OFF | Trial / Basic / Unlock | `SonyLauncherCount` |
| 年齢確認をスキップ | 現在この機能は機能していません | OFF | Trial / Basic / Unlock | `AgeCheckSkip` |
| 通信内容をログに出力 (開発者用) | LINEが送受信するすべての通信内容をログに記録します。デバッグ・開発用途向けです。 | OFF | Trial / Basic / Unlock | `output_communication` |
| スタンプのお試しを有効化 | 解除ライセンス向けのスタンプ試用補助機能です。ライセンス認証後に有効化してください。 | OFF | Unlock | `Stamp_Trial` |

## LINE内の詳細設定

スイッチとは別に、機能が有効なときだけ表示される設定ボタンがあります。

- LINE設定項目フィルター
- 設定保存先・ライセンス・トークン
- 通信リクエスト/レスポンス改変
- 更新履歴・寄付者一覧

## 変更後の確認

1. 設定を変更します。
2. 再起動確認が表示された場合はLINEを再起動します。
3. 対象画面で動作を確認します。問題があれば直前の設定をOFFに戻します。
