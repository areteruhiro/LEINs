# LEINs Web Brand Spec

This GitHub Pages guide uses real project and device assets.

## Product

- Product name: LEINs
- Repository: https://github.com/areteruhiro/LEINs
- Description: Android/Xposed customization module for LINE, maintained independently from LINE and related services.

## Assets

| Asset | Path | Source |
|---|---|---|
| App icon | `assets/leins-icon.png` | Copied from `app/src/main/ic_launcher-playstore.png` |
| Settings screen screenshot | `assets/screenshots/leins-main.png` | Captured from connected Android device with `adb shell screencap` |
| Category screen screenshot | `assets/screenshots/leins-categories.png` | Captured from connected Android device with `adb shell screencap` |
| Code-recreated UI mockups | `index.html` section `#ui-styles` | Recreated from `MainActivity.java`, `MainActivityMiuix.kt`, `MainActivityExpressive.kt`, and `UiStyle.java` in `LIME-beta-hiro` |
| LINE-embedded UI mockups | `index.html` section `#line-embedded` | Recreated from `EmbedOptions.java`, `LeinsEmbedOptionsView.kt`, `MiuixEmbedOptionsView.kt`, `ExpressiveEmbedOptionsView.kt`, and `LEINsOptions.java` in `LIME-beta-hiro` |

## Visual System

- Primary color: LEINs green `#06c755`
- Dark green: `#048f3e`
- Accent blue: `#2f6fed`
- Neutral background: `#f6f8f7`
- Surface: `#ffffff`
- Radius: 8px for web UI surfaces, matching a practical documentation/tool feel
- Imagery: real Android UI screenshots in phone-like frames, plus HTML/CSS mockups recreated from the app UI source code

## Copy Principles

- Explain features for first-time users before showing internal keys.
- Keep warning language calm and practical.
- Avoid implying affiliation with LINE or any related service.
- Do not invent unsupported claims; uncertain features stay in `LEINs_User_Wiki_ja/unknowns.md`.
