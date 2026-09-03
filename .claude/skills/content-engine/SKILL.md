---
name: content-engine
description: Use when the student wants ongoing content — pillars mined from the foundation, brand-locked carousels built as HTML and rendered to PNG, captions, and a 2-week calendar. Re-runnable any time to refill the calendar.
---

# Content Engine

A repeatable content machine: 4-5 pillars, a batch of on-brand
carousels rendered as finished PNGs (not instructions — actual
image files), ready captions, and a 2-week calendar. The brand
actually shows up, and every post advances a belief.

## Prerequisites

- `records/brands/<brand_id>/` with `necessary-beliefs.md`,
  `avatar-sheet.md`, `brand-book.md`.
- `design.md` at the repo root — the carousels use its EXACT fonts
  and colours, so the feed looks like the brand.
- Google Chrome (headless render).

## What you do

### Step 1 — Pillars and ideas

Read `necessary-beliefs.md`, `avatar-sheet.md` (verbatim language
especially), and the brand book's messaging library. Write
`records/content/<brand_id>/content-plan.md`:

**4-5 content pillars**, chosen from:
- **Problem** — the pain, in their words
- **Mechanism** — how the fix actually works
- **Proof** — results/specs, sourced only
- **Behind-the-build** — how it's made, founder reality
- **Contrarian take** — the belief the market gets wrong (from the
  research's category pattern)
- **Customer voice** — verbatim quotes, transformations

Plus **15-20 post ideas**, each mapped to ONE belief, tagged
carousel / single / reel-script, each with its pillar and the
research line it's built from. An idea with no source line is cut.

The student reviews this file before anything gets built.

### Step 2 — Carousels: HTML, rendered to PNG, brand-locked

Pick the best 3-4 carousel ideas. For each, write a slide-by-slide
script — **hook slide** (bold claim/number/question that stops the
scroll) → **4-6 value slides** (one beat each, the argument step by
step) → **CTA slide** (what to do next + handle). Big type, minimal
words, real copy in the brand voice — if a slide needs a paragraph,
it's two slides.

Then build each slide as its own single HTML file at
`records/content/<brand_id>/carousels/<topic>/slide-N.html`:

- Exact `design.md` tokens: canvas background, text colours,
  display font for headlines, accent used per the accent rule.
  The carousel must be recognizable as this brand from thumbnail
  size — if it could be anyone's carousel, the tokens aren't in.
- 1080×1350 (IG portrait) or 1080×1080 (square), fixed dimensions,
  no scroll, one idea per slide.
- Numbered footer (N/total + handle) for swipe rhythm.

Render each slide to PNG with headless Chrome:

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in records/content/<brand_id>/carousels/<topic>/slide-*.html; do
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --force-color-profile=srgb --window-size=1080,1350 \
    --virtual-time-budget=4000 \
    --screenshot="${f%.html}.png" "file://$PWD/$f"
done
```

**Then look at the PNGs.** Check the fonts actually loaded (Google
Fonts fail silently in headless — if the render shows fallback
type, wait longer or self-host the font), the palette is exact, no
text overflows. A garbled render is not "close enough" — fix and
re-render.

### Step 3 — Captions

Write `records/content/<brand_id>/captions.md` per asset:

```
### [asset label]
Hook: [scroll-stopping first line — customer's words]
Body: [2-5 short lines, value, brand voice]
CTA: [what to do + handle/link]
Tags: [5-10, niche over generic]
```

### Step 4 — The 2-week calendar

`records/content/<brand_id>/calendar.md`:

| Day | Format | Pillar | Asset | Caption | Belief |
|-----|--------|--------|-------|---------|--------|

Balanced across pillars and formats; never the same pillar twice
in a row; hooks front-loaded into the first week. Include the
already-rendered carousels first so the calendar starts with assets
that exist, not promises.

## Output layout

```
records/content/<brand_id>/
  content-plan.md      pillars + 15-20 sourced ideas
  carousels/          slide HTML + rendered PNGs
  captions.md         per-asset captions
  calendar.md         the 2-week schedule
```

## Boundaries — never do these

- Never build a post around an UNVERIFIED claim or an unsourced
  stat — an idea with no source line doesn't get made.
- Never use fonts or colours that aren't in `design.md` — the
  carousel IS the brand's feed presence.
- Never call a carousel done without rendering and looking at the
  PNGs.
- Never paraphrase customer language when the verbatim quote
  exists — verbatim is the point.

## How this connects

Beliefs from `necessary-beliefs.md`, language from
`avatar-sheet.md`, visual tokens from `design.md`, category
insight from `deepresearch.md`. Re-run anytime — the plan step
regenerates ideas against whatever's been published.
