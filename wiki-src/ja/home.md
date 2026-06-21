# ホーム画面

[ホームへ戻る](../index.html) / [設定画面の使い方](settings-ui.md)

ホーム画面のサービス、コマース、ミニアプリ表示を整理します。

> 2026年6月21日時点の `LEINsOptions.java`、日本語リソース、`hooks` 実装を照合しています。表示項目はAPK・プラン・LINEバージョンで変わる場合があります。

## 現在の設定項目（5件）

| 表示名 | 説明 | 初期 | 利用範囲 | 設定キー |
|---|---|:---:|---|---|
| サービス項目を非表示 | ホーム画面のサービス一覧にあるショートカットをすべて非表示にします。 | OFF | Trial / Basic / Unlock | `remove_Services` |
| サービスアイコンのラベルを非表示 | ホーム画面のサービスアイコン下にあるラベルテキストを非表示にします。 | OFF | Trial / Basic / Unlock | `remove_service_labels` |
| 更新されたプロフィールを削除 | ホーム画面上部に表示される「プロフィールを更新しました」のバナーを非表示にします。 | OFF | Trial / Basic / Unlock | `RemoveProfileNotification` |
| ショッピング・コマース項目を非表示 | LINE内のショッピング・コマース関連のボタンやバナーを非表示にします。 | ON | Trial / Basic / Unlock | `RemoveCommerce` |
| ミニアプリ項目を削除 | LINEの下部/ホームナビゲーションからミニアプリ項目を削除します。 | OFF | Trial / Basic / Unlock | `RemoveMini` |

## 変更後の確認

1. 設定を変更します。
2. 再起動確認が表示された場合はLINEを再起動します。
3. 対象画面で動作を確認します。問題があれば直前の設定をOFFに戻します。
