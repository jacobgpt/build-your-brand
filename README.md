# Build Your Brand

An interactive brand-building course that runs entirely inside Claude Code.
Cold clone to a researched brand, a live one-page site, and one finished
on-brand asset — approved by a human at every consequential step.

## Quickstart

```bash
git clone <this-repo-url> build-your-brand
cd build-your-brand
claude
```

Then run the lessons in order, either as slash commands or by asking Claude
directly:

| # | Command | What it does |
|---|---|---|
| 1 | `/build:01-setup` | Confirm both CLIs authenticated, skills visible, dashboard live |
| 2 | `/build:02-research` | Real web research into a sourced research file |
| 3 | `/build:03-foundation` | Validate + review the structured brand contract |
| 4 | `/build:04-website` | Copy-first, on-brand, self-contained site |
| 5 | `/build:05-brief` | A typed creative brief (Aphrodite) |
| 6 | `/build:06-build` | Approval-gated production (Hephaestus), reject one on purpose |
| 7 | `/build:07-done` | Review everything you built, and the pattern behind it |

Full lesson text lives in `course-copy.md`.

**This is seven real lessons, not nine.** An earlier draft script assumed a
separate brand-guide/PDF lesson, a `design.md` lesson, and a hero-video
lesson — none of those have skills behind them in this repo. See the "Honest
gap list" at the end of `course-copy.md` and in `/build:07-done` before
promising them anywhere public.

## Prerequisites

Two CLIs, two logins — no API keys needed, both auth via browser/CLI login:

```bash
claude --version
claude /login

higgsfield --version
higgsfield auth login
higgsfield account status   # must show your account + credits
```

## What's actually in this repo

```
.claude/skills/
  brand-foundation/       real web research -> positioning, audience, tone,
                          visual pillars, avoid-list -> brand_foundation.json
                          + <brand_id>.md (readable brand book)
  aphrodite-direction/    one-line idea -> typed creative_brief.json
                          (never picks a tool/model)
  hephaestus-production/  validated brief -> approval gate -> real Higgsfield
                          CLI build -> asset + dated run record
  brand-website/          brand foundation -> single self-contained
                          index.html, copy-first, no external tools

.claude/commands/build/   the seven /build: slash-command lessons

schema/
  brand_foundation.schema.json
  creative_brief.schema.json

scripts/
  validate_brief.py       stdlib-only schema validator (both schemas)
  approval_gate.py        the human approval gate — the only path to a build
  hephaestus_build.py     calls the real Higgsfield CLI, downloads the asset
  dashboard_status.py     writes status.json from what's actually on disk
  serve_dashboard.py      serves dashboard.html, refreshes on load

dashboard.html            live build-progress view, reads status.json only
course-copy.md            the lesson script / voiceover source
records/                  everything the skills write, gitkept empty dirs
```

## How it works

- **Brand Foundation** (once per brand) does real research, then reasons
  about positioning/audience/tone/visual rules/what to refuse, and writes a
  validated `brand_foundation.json` plus a readable brand book.
- **Aphrodite** reads that foundation and turns a one-line idea into a typed
  creative brief. She decides *what* should exist, never *how*.
- **Hephaestus** reads the brief exactly as written, runs the approval gate,
  and — only on human `y` — calls the real Higgsfield CLI to build the asset.
  Every decision, approved or rejected, is written to `records/runs/` dated.
- **Brand Website** reads the same foundation and writes one self-contained,
  on-brand HTML page — copy first, then styled from the brand's own visual
  pillars, no framework, no external tool.

Nothing in this loop invents a claim, a testimonial, or a stat that isn't in
the foundation or research file. If a section needs something the research
doesn't have, the skills ask or leave a marked placeholder — they don't make
it up.

## The gate

`scripts/approval_gate.py` is the only path a build can take. It prints the
brief, asks `Approve build? [y/N]`, and only proceeds on `y`. Every outcome —
built or rejected — gets a dated record in `records/runs/`. This is not
decoration: an ungated agent loop's failure mode isn't one bad output, it's
forty overnight, discovered after the fact.

## Serving the site or dashboard

Both must be served from the **repo root**, not their own folders — they
reference shared files by relative path and Python's `http.server` refuses
to serve above its working directory.

```bash
python3 scripts/serve_dashboard.py     # -> localhost:8787/dashboard.html
python3 -m http.server 8000            # -> localhost:8000/records/website/<brand_id>/index.html
```
