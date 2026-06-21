# 広告

[ホームへ戻る](../index.html) / [設定画面の使い方](settings-ui.md)

広告・おすすめ・LYPプレミアム案内の表示を減らします。

> 2026年6月21日時点の `LEINsOptions.java`、日本語リソース、`hooks` 実装を照合しています。表示項目はAPK・プラン・LINEバージョンで変わる場合があります。

## 現在の設定項目（3件）

| 表示名 | 説明 | 初期 | 利用範囲 | 設定キー |
|---|---|:---:|---|---|
| 広告を非表示 | LINEの広告バナーを非表示にします。トークリストやホーム画面の広告に効果があります。 | ON | Trial / Basic / Unlock | `remove_ads` |
| おすすめを非表示 | LINEのホーム画面に表示されるサービスのおすすめカードを削除します。 | ON | Trial / Basic / Unlock | `remove_recommendation` |
| LYPプレミアムの広告を非表示 | LYPプレミアムへの加入を促すバナーやポップアップを非表示にします。 | ON | Trial / Basic / Unlock | `remove_premium_recommendation` |

## 変更後の確認

1. 設定を変更します。
2. 再起動確認が表示された場合はLINEを再起動します。
3. 対象画面で動作を確認します。問題があれば直前の設定をOFFに戻します。
