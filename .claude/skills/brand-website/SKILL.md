---
name: brand-website
description: Use when a brand foundation already exists and the user wants a website, landing page, or one-pager built for it. Reads brand_foundation.json (and its research file if present) and builds a single self-contained on-brand index.html — copy first, then styled from the brand's actual visual pillars. No external tools, no image/video generation — pure Claude Code HTML/CSS.
---

# Brand Website

You build a real, running, on-brand one-page site — copy written first, then
dressed in the brand's own visual pillars, never a generic template default.
This is standalone HTML/CSS/vanilla JS: no build step, no framework, no
external design tool, no image or video generation. If it needs a package
manager, you've overbuilt it.

## Prerequisite

A brand foundation must already exist: `records/brands/<brand_id>.json`
(built by the `brand-foundation` skill). If none exists, stop and tell the
user to run that first — never invent a brand foundation here.

If more than one exists, ask which `brand_id` this site is for.

## What you do

### Step 0 — Read everything before writing anything

Read in full:
- `records/brands/<brand_id>.json` — positioning, audience, tone, visual
  pillars, avoid list. This is ground truth; never contradict or invent
  beyond it.
- `records/brands/<brand_id>-research.md` if it exists — real competitor
  notes and quoted customer language. This is your proof source.
- `records/briefs/*.json` and `records/assets/*` if any exist for this
  brand — if a real built asset already exists (from `hephaestus-production`),
  it can become the hero image. **Never generate a new image or video here**
  — this skill is HTML/CSS only. If no asset exists, use a CSS
  gradient/pattern hero built from the brand's palette instead. Say which
  path you took.

### Step 1 — Map sections from the brand's actual argument

One section per point the brand foundation makes, not a generic template.
Default arc, adapted to what's actually in the foundation:

```
HERO → THE GAP (why the obvious alternative falls short) → HOW THIS IS DIFFERENT
(the positioning's actual mechanism) → WHO THIS IS FOR (the audience, in their
own terms) → PROOF (only if the research file has real quotes/facts — skip
this section entirely if there's nothing real to put in it) → CLOSE (CTA)
```

Write the section map as a short numbered list — section name + which part
of the brand foundation it argues — before building anything.

### Step 2 — Write the copy FIRST, before any HTML

This is the discipline the whole build rests on. Draft every section's
headline, sub-head, and body in the brand's actual `tone` field — not
generic marketing voice.

- **Hero**: the `positioning` statement, sharpened into a real headline +
  sub-hook. Emphasize the actual differentiator, not a vague claim.
- **The Gap**: what the research file (if any) shows the obvious
  alternatives get wrong or leave generic. If no research file exists, use
  the brand foundation's own framing of "why not the obvious alternative"
  from `positioning`.
- **How this is different**: name the actual mechanism from `positioning` in
  plain language.
- **Who this is for**: use the `audience` field's specific description, not
  a demographic bucket.
- **Proof** (only if real material exists): quote real customer language
  from `<brand_id>-research.md` verbatim if present. **Never fabricate a
  testimonial, stat, or customer quote.** If there's nothing real, cut this
  section — an honest 5-section page beats a 6-section page with an invented
  testimonial.
- **Close**: a real CTA. Ask the user what it should point to (an email, a
  waitlist, a real link) — never invent a destination.

**Never invent a claim, stat, or number that isn't in the brand foundation
or research file.** If a section needs something you don't have, ask the
user or leave a clearly marked `[FILL: ...]` placeholder and tell them.

### Step 3 — Build the page

One self-contained `records/website/<brand_id>/index.html`:

- **CSS inline** in a `<style>` block. Every visual choice traced to a
  specific `visual_pillars` entry or the `avoid` list — comment which pillar
  drove which rule (e.g. `/* pillar: muted earth tones + safety-orange accent */`).
  Derive an actual palette and type pairing from the pillars' descriptions —
  don't default to a generic SaaS-blue/Inter look unless the pillars
  genuinely call for it.
- **Hero**: if a real asset exists (Step 0), `<img src="../../assets/<file>.png">`
  (relative path back to the shared `records/assets/` folder — do not copy
  the file). If not, a CSS gradient/pattern hero using the derived palette,
  clearly not a stock-photo placeholder.
- **Fonts**: system font stack by default (`-apple-system, "Segoe UI", ...`)
  unless the brand's visual pillars specifically call for a distinct
  typographic feel — then load one Google Fonts pairing via `<link>`, with
  a system fallback. Never more than two font families.
- **Sections** in the Step 1 order. Generous whitespace, one accent color
  used sparingly (status/CTA/emphasis only — never as a body color).
- **Responsive**: collapse cleanly to one column under ~480px. No
  JavaScript framework — vanilla JS only if genuinely needed (e.g. a mobile
  nav toggle), and keep it inline in the same file.
- **No lorem ipsum, no placeholder stock language, no fake logos/stats.**

### Step 4 — Run it and verify before calling it done

**Serve from the repo root, not the site's own folder** — `python3 -m
http.server` refuses to serve anything above its working directory, and this
site references shared assets via `../../assets/...` (outside
`records/website/<brand_id>/`). Serving from the site's own folder will 404
any real hero image. Print the correct instruction:

```
python3 -m http.server 8000   # run from the REPO ROOT
```
then open `http://localhost:8000/records/website/<brand_id>/index.html`.
(Opening `index.html` directly as a `file://` URL also works, since relative
`../../assets/...` paths resolve fine on a real filesystem — only the local
dev server has the traversal restriction.)

Check, as the visitor would, not as the coder:
- Every claim on the page traces to the brand foundation or research file —
  nothing invented.
- The accent color is rare, not everywhere.
- It reads coherently top to bottom — each section earns its place.
- Resize narrow (~390px) and confirm it collapses cleanly, no overflow.

Fix anything that fails, re-check. Only then tell the user it's done.

## Boundaries — never do these

- Never generate an image or video for this site — reuse an existing
  Hephaestus-built asset or use a CSS-only hero. Image/video generation is
  `hephaestus-production`'s job, not this skill's.
- Never invent a testimonial, stat, or customer quote not present in the
  research file.
- Never build a second page, a CMS, a database, or a framework build step —
  this is one static HTML file. If the user wants more than that, tell them
  it's out of scope for this skill.
- Never deploy anywhere — this skill only produces a file that runs locally.
