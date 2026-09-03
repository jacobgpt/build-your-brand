---
description: "Build Your Brand — Lesson 1: Setup. Confirm both CLIs and skills, launch the dashboard."
---

# /build:01-setup

Do this now, in order:

1. Run and show the output of:
   ```
   claude --version
   claude /login
   higgsfield --version
   higgsfield auth login
   higgsfield account status
   ```
   `higgsfield account status` must show your account and a credit
   balance. If it doesn't, the login didn't take — run it again before
   moving on.

2. Confirm your skills are visible:
   ```
   claude -p "list your available skills"
   ```
   You should see `brand-foundation`, `design-tokens`, `brand-guide`,
   `hephaestus-production`, `aphrodite-direction`, and `brand-website`.
   Skills are project-scoped — if none show up, make sure you're in the
   `build-your-brand` folder (`cd build-your-brand`) and try again.

3. Open a second terminal and run:
   ```
   python3 scripts/serve_dashboard.py
   ```
   then open `http://localhost:8787/dashboard.html`. It reads the actual
   files you've built in `records/` — not a progress bar that lies to
   you.

**Done when:** skills listed, Higgsfield green, dashboard open.
**Next:** `/build:02-research`
