# EasyRemind · EasyDo Utilities

Live: **https://remind.easydo.ai**, served by GitHub Pages from this repo (`main` branch, root).

## Files
- `src/artifact.html`: the single source (styles + markup + script, body-only). Also published as a claude.ai artifact.
- `scripts/build.py`: wraps the source into `index.html`. Run it after every change.
- `index.html`: the built page that remind.easydo.ai serves. Don't edit it by hand.
- `CNAME`, `.nojekyll`, `manifest.json`: GitHub Pages settings.

## Layout (v1.3)
- **Right app-rail:** vertical switcher on the right edge — **Remind** (EasyRemind) and **Tasks**, with an overdue/today badge on Tasks.
- **Left sidebar:** the active app's navigation. EasyRemind: Overview, Subscriptions, Calendar, Analytics, Settings. Tasks: Inbox, Today, Next 7 days, All, Completed, then Lists and Tags.
- **Phone:** bottom tab bar, with a switch to the other app as the last tab.
- **Deep links:** `#dashboard`, `#subs`, `#calendar`, `#analytics`, `#settings`; `#tasks/inbox`, `#tasks/today`, `#tasks/week`, `#tasks/all`, `#tasks/done`, `#tasks/list:<id>`, `#tasks/tag:<tag>`.

## Tasks (v1.3)
TickTick-style to-do app inside the same shell: quick-add with natural syntax (`today`, `tomorrow`, `fri`, `in 3 days`, `25/10`, Bangla `আজ`/`কাল`, `!high`/`!med`/`!low`, `#tag`, `~list`), priorities, due dates, lists with colours, tags, subtasks, notes, grouped views (Overdue / Today / Next 7 days / Later / No date), search, sort, completed history with clear, JSON export/import. Detail opens as a side panel on desktop and a modal on phones. Tasks and lists live in the same `easyremind.v1` store as subscriptions, so Settings → Export/Import carries both.

## Data
- All data (subscriptions, tasks, lists, settings) lives in the browser (`localStorage` key `easyremind.v1`), so it stays on one browser and one device. Settings has Export and Import (JSON).
- v2 (accounts + cloud sync) needs a Supabase project; the swap point is `Store.load/save`.
