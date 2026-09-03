# Build Your Brand

An interactive brand-building course that runs entirely inside Claude Code.
Cold clone to a researched brand, a brand guide, a design system, a hero,
a live one-page site, and one finished on-brand asset — approved by a
human at every consequential step.

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
| 2 | `/build:02-research` | Real web research, sourced — deepresearch.md lands first |
| 3 | `/build:03-foundation` | Validate + review the brand contract |
| 4 | `/build:04-design` | design.md — pick a visual direction from real options, then lock exact hex, fonts, voice |
| 5 | `/build:05-guide` | brand book (HTML + PDF) — scrollable, visual, screenshot-verified |
| 6 | `/build:06-hero` | Hero still through the gate, film-safety-checked (video optional) |
| 7 | `/build:07-website` | Copy-first, design.md-driven, hero-aware site |
| 8 | `/build:08-assets` | A typed creative brief (Aphrodite), gated production (Hephaestus) |
| 9 | `/build:09-done` | Review everything, the pattern behind it — and ship the site live if you want (gated, zero-cost default) |

Full lesson text lives in `course-copy.md`.

**One honest gap:** the hero-video half of Lesson 6 is code-complete and
unit-tested but has never been run for real against Higgsfield — that
spend hasn't been approved in this repo yet. The still half has run for
real, including a real rejection-and-rebuild cycle (a hallucinated logo,
caught by a vision check and fixed) logged in `BUILD_LOG.md`.

## Prerequisites

Two CLIs, two logins — no API keys needed, both auth via browser/CLI login:

```bash
claude --version
claude /login

higgsfield --version
higgsfield auth login
higgsfield account status   # must show your account + credits
```

No Firecrawl key required — `brand-foundation` uses Claude Code's own
built-in web search. Verified from a plain terminal, not just through an
agent harness.

## What's actually in this repo

```
.claude/skills/
  brand-foundation/       interview (intake.md) -> real web research ->
                          nine files per brand:
                          copywriter-prompt.md, deepresearch.md,
                          avatar-sheet.md, offerbrief.md,
                          necessary-beliefs.md, project-knowledge.md
                          (VERIFIED/UNVERIFIED split), brand-book.md,
                          brand_foundation.json (authoritative schema)
  design-tokens/          foundation + brand book -> design.md: exact hex,
                          named fonts, voice USE/AVOID, component rules
  brand-guide/            foundation + design.md -> the visual brand
                          book: brand-guide.html (scrollable, with
                          swatches, type specimens, components) + PDF
                          (story + book) and brand-guide.pdf via headless
                          Chrome
  aphrodite-direction/    one-line idea -> typed creative_brief.json
                          (never picks a tool/model)
  hephaestus-production/  validated brief -> approval gate -> real
                          Higgsfield CLI build -> asset + dated run record.
                          Also handles hero-still and hero-video briefs
                          (brief_id ending -hero-still / -hero-video)
  brand-website/          foundation + necessary-beliefs.md (one section
                          per belief) + design.md + hero (if built) ->
                          single self-contained index.html

.claude/commands/build/   the nine /build: slash-command lessons

schema/
  brand_foundation.schema.json
  creative_brief.schema.json

scripts/
  validate_brief.py       stdlib-only schema validator (both schemas)
  approval_gate.py        the human approval gate — the only path to a build
  hephaestus_build.py     calls the real Higgsfield CLI, downloads the
                          asset (still, video, or general creative asset)
  dashboard_status.py     writes status.json from what's actually on disk,
                          nine stages
  serve_dashboard.py      serves dashboard.html, refreshes on load

dashboard.html            live build-progress view, reads status.json only
course-copy.md            the lesson script / voiceover source, 9 lessons
BUILD_LOG.md              dated record of significant build events — the
                          gate working, including rejections
records/                  everything the skills write, gitkept empty dirs
```

## How it works

- **Brand Foundation** (once per brand) does real research first, then
  reasons about the customer, the offer, the beliefs someone must accept,
  and separates VERIFIED claims from UNVERIFIED ones — writing nine files
  plus a validated `brand_foundation.json` that stays authoritative; the
  six `.md` files are the human layer and must not contradict it.
- **Design Tokens** distills the brand book into `design.md` — specific
  values only, no line that could describe two different brands.
- **Brand Guide** turns the documents into one shareable HTML file (plus a
  PDF export) that answers a designer's or client's questions before they
  ask, including a "what we never claim" panel for anything UNVERIFIED.
- **Hephaestus (hero)** builds a still first, always — a strong still makes
  a strong video, a weak one doesn't. Reviewed pixel-by-pixel before
  animating (a real run once caught a hallucinated logo this way).
- **Aphrodite** reads the foundation and turns a one-line idea into a typed
  creative brief. She decides *what* should exist, never *how*.
- **Hephaestus (assets)** reads the brief exactly as written, runs the
  approval gate, and — only on human `y` — calls the real Higgsfield CLI.
  Every decision, approved or rejected, is written to `records/runs/`
  dated.
- **Brand Website** reads the foundation, `necessary-beliefs.md` (one
  section per belief), `design.md`, and the hero if one exists — copy
  first, then styled, no framework, no external tool.

Nothing in this loop invents a claim, a testimonial, or a stat that isn't
in the foundation or research file. If a section needs something the
research doesn't have, the skills ask or leave a marked placeholder — they
don't make it up. This has been tested for real, more than once — see
`BUILD_LOG.md`.

## The gate

`scripts/approval_gate.py` is the only path a build (still, video, or
general asset) can take. It prints the brief, asks `Approve build? [y/N]`,
and only proceeds on `y`. Every outcome — built or rejected — gets a dated
record in `records/runs/`. This is not decoration: an ungated agent loop's
failure mode isn't one bad output, it's forty overnight, discovered after
the fact.

## Serving the site or dashboard

Both must be served from the **repo root**, not their own folders — they
reference shared files by relative path and Python's `http.server` refuses
to serve above its working directory.

```bash
python3 scripts/serve_dashboard.py     # -> localhost:8787/dashboard.html
python3 -m http.server 8000            # -> localhost:8000/records/website/<brand_id>/index.html
```
