#!/usr/bin/env python3
"""Generate docs/features.html from the current LIME option definitions."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET


CATEGORY_LABELS = {
    "AD": "広告",
    "Ad": "広告",
    "BACKUP": "バックアップ・復元",
    "BROWSER": "ブラウザ",
    "BUTTON": "ボタン",
    "BUTTONS": "ボタン",
    "CALL": "通話",
    "CHAT": "チャット",
    "CHAT_LIST": "チャット一覧",
    "HOME": "ホーム",
    "LAYOUT": "画面レイアウト・UI",
    "NOTIFICATION": "通知",
    "NOTIFICATIONS": "通知",
    "OTHER": "その他",
    "PRIVACY": "プライバシー・既読",
    "THEME": "テーマ",
    "DEVELOPER": "開発者向け",
}

SECTION_LABELS = {
    "layout": "レイアウト・UI",
    "home": "ホーム画面",
    "chat_list": "チャットリスト",
    "browser": "ブラウザ",
    "theme": "テーマ",
    "buttons": "ボタン設定",
    "ad": "広告",
    "privacy": "プライバシー・既読",
    "chat": "チャット",
    "notifications": "通知",
    "call": "着信音・発信音",
    "backup": "バックアップ・復元",
    "other": "その他",
}

AD_KEYS = {"remove_ads", "remove_recommendation", "remove_premium_recommendation"}

OPTION_PATTERN = re.compile(
    r"public Option\s+(\w+)\s*=\s*\n?\s*new Option\((.*?)\);",
    re.S,
)
ARGUMENT_PATTERN = re.compile(
    r'^\s*"([^"]+)",\s*R\.string\.(\w+),\s*R\.string\.(\w+),\s*'
    r"(true|false),\s*OptionCategory\.(\w+)"
    r"(?:,\s*R\.string\.(\w+),\s*(true|false)(?:,\s*(true|false))?)?\s*$",
    re.S,
)


def load_strings(path: Path) -> dict[str, str]:
    root = ET.parse(path).getroot()
    result: dict[str, str] = {}
    for node in root.findall("string"):
        name = node.attrib.get("name")
        if name:
            result[name] = "".join(node.itertext()).strip()
    return result


def parse_options(java_path: Path, strings: dict[str, str]) -> list[dict[str, object]]:
    source = java_path.read_text(encoding="utf-8")
    rows: list[dict[str, object]] = []
    for field_name, arguments in OPTION_PATTERN.findall(source):
        match = ARGUMENT_PATTERN.match(arguments)
        if not match:
            raise ValueError(f"Unsupported Option declaration: {field_name}")
        (
            key,
            title_id,
            description_id,
            checked,
            category,
            subcategory,
            unlock_only,
            free_allowed,
        ) = match.groups()
        if key in AD_KEYS:
            section = "ad"
        elif category == "HOME" and subcategory == "sub_bottom_bar":
            section = "layout"
        elif category == "HOME":
            section = "home"
        else:
            section = {
                "CHAT_LIST": "chat_list",
                "BROWSER": "browser",
                "THEME": "theme",
                "BUTTONS": "buttons",
                "PRIVACY": "privacy",
                "CHAT": "chat",
                "NOTIFICATIONS": "notifications",
                "CALL": "call",
                "BACKUP": "backup",
                "OTHER": "other",
                "DEVELOPER": "other",
            }.get(category, "other")
        is_unlock = unlock_only == "true"
        # The seven-argument constructor defaults freeAllowed to true.
        is_free = (free_allowed == "true") if free_allowed is not None else unlock_only is not None
        if is_unlock:
            access = "unlock"
            access_label = "有料（Unlock）"
        elif is_free:
            access = "free"
            access_label = "無料・有料"
        else:
            access = "paid"
            access_label = "有料（Basic / Unlock）"
        rows.append(
            {
                "field": field_name,
                "key": key,
                "title": strings.get(title_id, key) or key,
                "description": strings.get(description_id, "説明準備中") or "説明準備中",
                "default": "ON" if checked == "true" else "OFF",
                "category": category,
                "category_label": SECTION_LABELS[section],
                "section": section,
                "access": access,
                "access_label": access_label,
            }
        )
    return rows


def render(rows: list[dict[str, object]], source_version: str) -> str:
    counts = Counter(str(row["access"]) for row in rows)
    category_order = {name: index for index, name in enumerate(CATEGORY_LABELS)}
    rows.sort(key=lambda row: (category_order.get(str(row["category"]), 999), str(row["title"])))

    body_rows = []
    for row in rows:
        search = " ".join(
            str(row[key])
            for key in ("title", "key", "description", "category_label", "access_label")
        ).lower()
        body_rows.append(
            '<tr data-access="{access}" data-category="{section}" data-search="{search}">'
            '<td><span class="category">{category}</span></td>'
            '<td><strong>{title}</strong><code>{key}</code></td>'
            '<td>{description}</td>'
            '<td><span class="access {access}">{access_label}</span></td>'
            '<td><span class="default {default_class}">{default}</span></td>'
            "</tr>".format(
                access=html.escape(str(row["access"])),
                section=html.escape(str(row["section"])),
                search=html.escape(search, quote=True),
                category=html.escape(str(row["category_label"])),
                title=html.escape(str(row["title"])),
                key=html.escape(str(row["key"])),
                description=html.escape(str(row["description"])),
                access_label=html.escape(str(row["access_label"])),
                default_class=str(row["default"]).lower(),
                default=html.escape(str(row["default"])),
            )
        )

    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="LEINsの全機能と、無料版・有料版の対応状況を確認できます。">
  <meta name="theme-color" content="#06c755">
  <title>全機能一覧・無料版と有料版 | LEINs Guide</title>
  <link rel="icon" href="assets/leins-icon.png">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="consumer.css">
  <style>
    .feature-page {{ width:min(1180px,calc(100% - 32px)); margin:0 auto; padding:48px 0 72px; }}
    .feature-hero {{ display:grid; gap:16px; margin-bottom:28px; }}
    .feature-hero h1 {{ margin:0; font-size:clamp(2rem,5vw,3.6rem); letter-spacing:-.04em; }}
    .feature-hero p {{ max-width:760px; margin:0; color:var(--muted,#52606d); line-height:1.8; }}
    .summary-grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin:24px 0; }}
    .summary-card {{ padding:18px; border:1px solid rgba(19,36,28,.12); border-radius:18px; background:#fff; }}
    .summary-card strong {{ display:block; font-size:1.75rem; }}
    .feature-tools {{ position:sticky; top:72px; z-index:4; display:flex; flex-wrap:wrap; gap:10px; padding:14px; margin:24px 0; border:1px solid rgba(19,36,28,.12); border-radius:18px; background:rgba(255,255,255,.95); backdrop-filter:blur(12px); }}
    .feature-tools input {{ flex:1 1 260px; min-width:0; padding:12px 14px; border:1px solid #cbd5d0; border-radius:12px; font:inherit; }}
    .filter-button {{ padding:11px 14px; border:1px solid #cbd5d0; border-radius:999px; background:#fff; font:inherit; cursor:pointer; }}
    .filter-button[aria-pressed="true"] {{ color:#fff; border-color:#087f3e; background:#087f3e; }}
    .table-wrap {{ overflow:auto; border:1px solid rgba(19,36,28,.12); border-radius:20px; background:#fff; }}
    .feature-table {{ width:100%; min-width:900px; border-collapse:collapse; }}
    .feature-table th,.feature-table td {{ padding:14px 16px; border-bottom:1px solid #e7ece9; text-align:left; vertical-align:top; }}
    .feature-table th {{ position:sticky; top:0; background:#f3f8f5; color:#31443a; font-size:.82rem; }}
    .feature-table tr:last-child td {{ border-bottom:0; }}
    .feature-table code {{ display:block; margin-top:5px; color:#66756d; font-size:.78rem; }}
    .category,.access,.default {{ display:inline-block; padding:5px 9px; border-radius:999px; white-space:nowrap; font-size:.78rem; font-weight:700; }}
    .category {{ background:#edf3f0; color:#41574c; }}
    .access.free {{ background:#dcfce7; color:#166534; }}
    .access.paid {{ background:#fff1c7; color:#7c4a03; }}
    .access.unlock {{ background:#eee7ff; color:#5b21b6; }}
    .default.on {{ background:#e0f2fe; color:#075985; }}
    .default.off {{ background:#eef1f0; color:#52625a; }}
    .feature-note {{ margin-top:18px; color:#65746c; font-size:.9rem; line-height:1.7; }}
    .empty-state {{ padding:32px; text-align:center; color:#65746c; }}
    @media (max-width:700px) {{
      .summary-grid {{ grid-template-columns:1fr; }}
      .feature-tools {{ top:8px; }}
      .feature-page {{ width:min(100% - 20px,1180px); padding-top:28px; }}
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <nav class="nav" aria-label="メインナビゲーション">
      <a class="brand" href="index.html"><img src="assets/leins-icon.png" alt="" width="40" height="40"><span>LEINs Guide</span></a>
      <div class="nav-links"><a href="index.html">ホーム</a><a href="use.html">使い方</a><a href="features.html" aria-current="page">全機能</a></div>
    </nav>
  </header>
  <main class="feature-page">
    <section class="feature-hero">
      <p class="eyebrow">無料・有料の違いもひと目で確認</p>
      <h1>LEINs 全機能一覧</h1>
      <p>現在の実装にある設定項目をすべて掲載しています。「無料・有料」は無料版でも利用でき、「有料」はライセンス認証後に利用できます。Unlock専用機能は別に表示しています。</p>
    </section>
    <section class="summary-grid" aria-label="機能数">
      <article class="summary-card"><span>表示中の機能</span><strong id="summary-total">{len(rows)}</strong></article>
      <article class="summary-card"><span>無料版で利用可能</span><strong id="summary-free">{counts["free"]}</strong></article>
      <article class="summary-card"><span>有料版で利用可能</span><strong id="summary-paid">{counts["paid"] + counts["unlock"]}</strong></article>
    </section>
    <div class="feature-tools" role="search">
      <input id="feature-search" type="search" placeholder="機能名・説明・設定キーで検索" aria-label="機能を検索">
      <button class="filter-button" type="button" data-filter="all" aria-pressed="true">すべて</button>
      <button class="filter-button" type="button" data-filter="free" aria-pressed="false">無料</button>
      <button class="filter-button" type="button" data-filter="paid" aria-pressed="false">有料</button>
      <button class="filter-button" type="button" data-filter="unlock" aria-pressed="false">Unlock</button>
    </div>
    <div class="table-wrap">
      <table class="feature-table">
        <thead><tr><th>カテゴリ</th><th>機能</th><th>説明</th><th>利用区分</th><th>初期値</th></tr></thead>
        <tbody id="feature-body">
          {"".join(body_rows)}
        </tbody>
      </table>
      <p id="feature-empty" class="empty-state" hidden>一致する機能がありません。</p>
    </div>
    <p class="feature-note">機能区分は LEINs {html.escape(source_version)} のオプション定義を基準に生成しています。LINEやLEINsのバージョン、導入方式によって表示・動作しない項目があります。</p>
  </main>
  <footer><p>LEINs 使い方ガイド</p><a href="index.html">ホームへ戻る</a></footer>
  <script>
    (() => {{
      const search = document.querySelector('#feature-search');
      const rows = [...document.querySelectorAll('#feature-body tr')];
      const buttons = [...document.querySelectorAll('[data-filter]')];
      const empty = document.querySelector('#feature-empty');
      const categoryLabels = {json.dumps(SECTION_LABELS, ensure_ascii=False)};
      const category = new URLSearchParams(location.search).get('category');
      const categoryRows = category ? rows.filter(row => row.dataset.category === category) : rows;
      if (category && categoryLabels[category]) {{
        document.querySelector('h1').textContent = `${{categoryLabels[category]}}の機能一覧`;
      }}
      document.querySelector('#summary-total').textContent = categoryRows.length;
      document.querySelector('#summary-free').textContent = categoryRows.filter(row => row.dataset.access === 'free').length;
      document.querySelector('#summary-paid').textContent = categoryRows.filter(row => row.dataset.access !== 'free').length;
      let filter = 'all';
      const update = () => {{
        const query = search.value.trim().toLowerCase();
        let visible = 0;
        rows.forEach(row => {{
          const matchesText = !query || row.dataset.search.includes(query);
          const matchesFilter = filter === 'all' || row.dataset.access === filter;
          const matchesCategory = !category || row.dataset.category === category;
          row.hidden = !(matchesText && matchesFilter && matchesCategory);
          if (!row.hidden) visible += 1;
        }});
        empty.hidden = visible !== 0;
      }};
      search.addEventListener('input', update);
      buttons.forEach(button => button.addEventListener('click', () => {{
        filter = button.dataset.filter;
        buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
        update();
      }}));
      update();
    }})();
  </script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lime-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("docs/features.html"))
    parser.add_argument("--sync-free-wording", action="store_true")
    args = parser.parse_args()

    java_path = args.lime_root / "app/src/main/java/io/github/hiro/LEINs/LEINsOptions.java"
    strings_path = args.lime_root / "app/src/main/res/values-ja/strings.xml"
    gradle_path = args.lime_root / "app/build.gradle"
    strings = load_strings(strings_path)
    rows = parse_options(java_path, strings)
    version_match = re.search(r'versionName\s*=\s*"([^"]+)"', gradle_path.read_text(encoding="utf-8"))
    version = version_match.group(1) if version_match else "current"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(rows, version), encoding="utf-8", newline="\n")
    print(f"Wrote {args.output} with {len(rows)} features")
    if args.sync_free_wording:
        replacements = {
            Path("docs/index.html"): {
                "アプリ内の「購入する」から選びます": "アプリ内の「選択する」から選びます",
                "ライセンス認証の画面で「購入する」を押すと": "ライセンス認証の画面で「選択する」を押すと",
                "<h3>購入するを押す</h3>": "<h3>選択するを押す</h3>",
                "<h3>お試し</h3><p class=\"price\">0円</p><p>まず動作を確認したい方向けです。</p>":
                    "<h3>無料版</h3><p class=\"price\">0円</p><p>基本機能を無料で利用できます。アプリ内で選ぶと固定キーで認証します。</p>",
            },
            Path("docs/LEINs_User_Wiki_ja/settings-ui.html"): {
                "ライセンス認証の画面で「購入する」を押すと": "ライセンス認証の画面で「選択する」を押すと",
                "<h3>購入するを押す</h3>": "<h3>選択するを押す</h3>",
                "お試し、月額、年額、買い切り、買い切り(追加操作不要)":
                    "無料版、月額、年額、買い切り、買い切り(追加操作不要)",
                '<article><h3>お試し</h3><p class="price">0円</p><p>まず動作を確認したい方向けです。</p><a class="purchase-link" href="https://buy.polar.sh/polar_cl_Lr76mJ5ObaFcXptNLxXSeFy8IDQiKLAkt3v6y134U1H">購入ページを開く</a></article>':
                    '<article><h3>無料版</h3><p class="price">0円</p><p>基本機能を無料で利用できます。アプリ内で選ぶと固定キーで認証します。</p></article>',
            },
        }
        for path, changes in replacements.items():
            content = path.read_text(encoding="utf-8")
            for old, new in changes.items():
                if old in content:
                    content = content.replace(old, new)
                elif new not in content:
                    raise ValueError(f"Expected docs wording not found in {path}: {old}")
            if path == Path("docs/index.html"):
                section_counts: dict[str, Counter[str]] = {
                    section: Counter(
                        str(row["access"])
                        for row in rows
                        if row["section"] == section
                    )
                    for section in SECTION_LABELS
                }
                for section, access_counts in section_counts.items():
                    free_count = access_counts["free"]
                    paid_count = access_counts["paid"] + access_counts["unlock"]
                    pattern = re.compile(
                        rf'(<a class="category-card" href=")'
                        rf'(?:LEINs_User_Wiki_ja/{re.escape(section)}\.html|features\.html\?category={re.escape(section)})'
                        rf'(" data-keywords="[^"]*"><strong>[^<]+</strong><p>.*?</p>)'
                        rf'(?:<span class="category-availability">.*?</span>)?(</a>)'
                    )
                    replacement = (
                        rf'\1features.html?category={section}\2'
                        rf'<span class="category-availability">無料 {free_count} / 有料 {paid_count}</span>\3'
                    )
                    content, replaced = pattern.subn(replacement, content, count=1)
                    if replaced != 1:
                        raise ValueError(f"Category card not found in {path}: {section}")
            path.write_text(content, encoding="utf-8", newline="\n")
            print(f"Updated free-version wording in {path}")


if __name__ == "__main__":
    main()
