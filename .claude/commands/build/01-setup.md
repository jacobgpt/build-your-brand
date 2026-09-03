---
description: "Build Your Brand — Lesson 1: Setup. Confirm both CLIs and skills, launch the dashboard."
---

# /build:01-setup

```ansi
     ██  [38;5;208m█████[0m  [38;5;208m██[0m  ██████  ██████  ██████
     ██ [38;5;208m██   ██[0m [38;5;208m██[0m ██      ██    ██ ██   ██
     ██ [38;5;208m███████[0m [38;5;208m██[0m ██      ██    ██ ██████
██   ██ [38;5;208m██   ██[0m [38;5;208m██[0m ██      ██    ██ ██   ██
 █████  [38;5;208m██   ██[0m [38;5;208m██[0m  ██████  ██████  ██████

          T H E   C R E A T I V E   A R C H I T E C T
```

```
──────────────────────────────────────────────────
LESSON 1 · SETUP
THE TOOLCHAIN
──────────────────────────────────────────────────
```

> **Timing**     ~5 minutes
> **Goal**       Both CLIs authenticated, skills visible, dashboard live
> **Progress**   `[░░░░░░░░░░] 0/9`

---

## First, what this course is

Most people using AI have one assistant and forty browser tabs. Every job
starts from scratch, nothing remembers the last one, no record of why
anything was decided.

This is the other thing. Agents with fixed jobs, a gate that needs your
approval before anything gets made, a written record of every decision.
By the end you'll have a researched brand, a design system, a visual
brand book, a hero, a live site, and a finished asset — on your own
machine, in files you can inspect.

**By the end you'll have, all built from zero:**
- A researched brand foundation — 9 files, including a ready-to-paste
  AI copywriter prompt
- (After Lesson 10) launch-ready ads, a belief-mapped email
  sequence, and a 2-week content calendar
- A `design.md` — your visual direction, chosen from real options
- A scrollable visual brand book (HTML + PDF) — palette, type, and
  components shown live
- A hero still (and video, if you spend on it) — built through an
  approval gate
- A live one-page site, on-brand, no claim you can't back
- One finished on-brand asset, plus a rejection record proving the
  gate works

Owned, not rented: files on your machine, in a structure you can
audit.

Nine lessons, one at a time:

| # | Lesson | Time |
|---|--------|------|
| 1 | Setup — you're here | 5 min |
| 2 | Interview + deep research → foundation docs | 35 min |
| 3 | Brand foundation — validate + own the contract | 10 min |
| 4 | design.md — choose from real options | 10 min |
| 5 | The brand guide — visual brand book | 15 min |
| 6 | The hero — still through the gate (+ video) | 20 min |
| 7 | The website — copy-first, on-brand | 20 min |
| 8 | Direction + production — asset + the gate tested | 15 min |
| 9 | What you built — review + launch | 10 min |
| 10 | Grow — ads, email, content engines | 30-45 min |

The first half builds the foundation; the second half turns it into
things people can see and click; the tenth lesson keeps it showing
up after the course ends.

---

**Before you start, you'll want:** both CLIs installed, a Higgsfield
account with some credits (only Lessons 6 and 8 spend any), and about
2.5 hours total for the course. Nothing else — no design tools, no
API keys.

---

## STEP 1 — Authenticate both CLIs

Two CLIs, two logins. Run each and check the output:

```bash
claude --version
claude /login

higgsfield --version
higgsfield auth login
higgsfield account status
```

That last one must show your account and a credit balance. If it
doesn't, the auth didn't take — run the login again before you go on.

> **ACTION:** Run the five commands above. `higgsfield account status`
> must show your account + credits. When it's green, type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Both CLIs authenticated                         │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[░░░░░░░░░░] 0/9 · Step 1/3`

---

## STEP 2 — Confirm the skills loaded

Claude Code picks up any skill in the project folder automatically.
Nothing to install:

```bash
claude -p "list your available skills"
```

You should see `brand-foundation`, `design-tokens`, `brand-guide`,
`hephaestus-production`, `aphrodite-direction`, and `brand-website`.
If you see none, you're running `claude` from the wrong directory —
skills are project-scoped, so `cd` into the repo and try again.

> **ACTION:** Run the skills check. All six names listed? Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Skills visible                                  │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[░░░░░░░░░░] 0/9 · Step 2/3`

---

## STEP 3 — Open the dashboard

Second terminal:

```bash
python3 scripts/serve_dashboard.py
```

Then open `http://localhost:8787/dashboard.html`. It reads the actual
files in `records/` — not a progress bar that lies to you, a view of
what exists on disk. It'll fill in as you build.

> **ACTION:** Dashboard open in your browser? Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Toolchain verified, dashboard live              │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[█░░░░░░░░░] 1/9 · Lesson 1 complete`

---

## DONE

**What you have now:**
- Both CLIs authenticated, credits confirmed
- All six skills visible to Claude Code
- A live dashboard showing the real state of your build

**Next lesson:** `/build:02-research` — the interview, then real
competitor research. Everything you build afterwards stands on what
this next lesson produces, so it's the one that matters most.
