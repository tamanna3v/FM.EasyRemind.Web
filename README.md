# EasyRemind · EasyDo Utilities

Live: **https://remind.easydo.ai**, served by GitHub Pages from this repo (`main` branch, root).

## Files
- `src/artifact.html`: the single source (styles + markup + script, body-only). Also published as a claude.ai artifact.
- `scripts/build.py`: wraps the source into `index.html`. Run it after every change.
- `index.html`: the built page that remind.easydo.ai serves. Don't edit it by hand.
- `CNAME`, `.nojekyll`, `manifest.json`: GitHub Pages settings.

## Layout
- **Left sidebar:** vertical tabs, one per utility app (EasyDo Utilities). EasyRemind is the first.
- **Right side:** the active app's page, with a header and section tabs: Overview, Subscriptions, Calendar, Analytics, Settings.
- **Phone:** the sidebar opens as a drawer from the ☰ button.
- **Deep links:** `#remind.overview`, `#remind.subscriptions`, `#remind.calendar`, `#remind.analytics`, `#remind.settings`. Old links like `#calendar` still work.

## Add a new utility app
1. In `src/artifact.html`, add an entry to `APPS`: `{id, name, tag, icon, sections, badge(), summary(), actions(), render(sec)}`.
2. Add its strings to `T.en` and `T.bn`, and give it its own `localStorage` key.
3. Keep or remove the "More utilities · Coming soon" placeholder in `sideHtml()`.
4. Run `python3 scripts/build.py`, commit and push. Pages redeploys in about a minute.

## Data
- EasyRemind data lives in the browser (`localStorage` key `easyremind.v1`), so it stays on one browser and one device. Settings has Export and Import (JSON).
- Suite preferences (language, theme) live under `easydo.suite.v1`.
- v2 (accounts + cloud sync) needs a Supabase project; the swap point is `Store.load/save`.
