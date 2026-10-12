# EasyRemind — deploy to remind.easydo.ai

Static site. No build step, no server, no database (v1 stores data in the browser).

## Option A — Vercel (recommended, 5 minutes)
1. Push this `deploy/` folder to a GitHub repo (e.g. `easydo/easyremind`).
2. vercel.com → Add New → Project → import the repo. Framework: **Other**. Root: `/`. Deploy.
3. Project → Settings → Domains → add `remind.easydo.ai`.
4. In your DNS for easydo.ai add:  `CNAME  remind  cname.vercel-dns.com`
5. Wait for the green check. HTTPS is automatic.

## Option B — Cloudflare Pages
1. pages.cloudflare.com → Create → Upload assets → drag this folder.
2. Custom domains → `remind.easydo.ai` (if easydo.ai DNS is on Cloudflare it's one click; otherwise CNAME to `<project>.pages.dev`).

## Option C — any static host / your own nginx
Serve `index.html` at the root. Nothing else required.

## v2 (accounts + cloud sync) prerequisites
- A Supabase project (free tier): URL + anon key.
- Resend (email reminders) API key.
- Stripe + SSLCommerz keys for Pro billing.
Storage is isolated in `Store.load/save` inside index.html, so the Supabase adapter swaps in there.
