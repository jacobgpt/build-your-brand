---
description: "Build Your Brand — Lesson 1: Setup. Confirm both CLIs and skills, launch the dashboard."
---

# /build:01-setup

Do this now, in order:

1. Run and show the output of:
   ```
   claude --version
   higgsfield --version
   higgsfield account status
   ```
   If `higgsfield account status` doesn't show a real account + credits, tell
   the user to run `higgsfield auth login` and stop here until it does.

2. Confirm skills are visible in this project:
   ```
   claude -p "list your available skills"
   ```
   You should see `brand-foundation`, `aphrodite-direction`,
   `hephaestus-production`, and `brand-website`. If none show up, the user is
   not running from the repo root — tell them to `cd` into
   `build-your-brand` and retry.

3. Tell the user to open a second terminal and run:
   ```
   python3 scripts/serve_dashboard.py
   ```
   then open `http://localhost:8787/dashboard.html`. This reads real files
   in `records/` — nothing self-reported.

**Done when:** skills listed, Higgsfield green, dashboard open.
**Next:** `/build:02-foundation`
