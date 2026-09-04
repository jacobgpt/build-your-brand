---
name: content-engine
description: Use when the student wants ongoing content — pillars from the foundation, carousels built as HTML in the brand's own tokens and rendered to PNG, captions, and a fortnight's schedule. Run again whenever the schedule runs dry.
---

# Content Engine

Four or five pillars, a set of carousels rendered to finished PNG
files rather than instructions, a caption for each, and a fortnight's
schedule. Every post moves one belief.

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
- **How it's made** — the work behind the product, the founder's
  actual week
- **Against the grain** — the thing the category believes that the
  research shows is wrong
- **Customer voice** — verbatim quotes, transformations

Plus **15-20 post ideas**, each mapped to ONE belief, tagged
carousel / single / reel-script, each with its pillar and the
research line it's built from. An idea with no source line is cut.

The student reviews this file before anything gets built.

### Step 2 — Carousels: HTML, rendered to PNG, brand-locked

Take the three or four strongest ideas. Script each one slide at a
time: an opening slide that earns the stop (a claim, a number, a
question), then four to six slides that each carry one step of the
argument, then a closing slide with the action and the handle. Large
type, few words, real copy in the brand's voice. A slide that needs a
paragraph is two slides.

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

### Step 4 — The fortnight

`records/content/<brand_id>/calendar.md`:

| Date | Type | Pillar | File | Caption ref | Belief served |
|------|------|--------|------|-------------|---------------|

Spread across pillars and types, no pillar on consecutive days, the
strongest openers in week one. Include the
already-rendered carousels first so the calendar starts with assets
that exist, not promises.

## Output layout

```
records/content/<brand_id>/
  content-plan.md      pillars + 15-20 sourced ideas
  carousels/          slide HTML + rendered PNGs
  captions.md         per-asset captions
  calendar.md         the fortnight's schedule
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
