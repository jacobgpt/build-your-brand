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

A brand foundation must already exist: `records/brands/<brand_id>/brand_foundation.json`
(built by the `brand-foundation` skill). If none exists, stop and tell the
user to run that first — never invent a brand foundation here.

If more than one exists, ask which `brand_id` this site is for.

## What you do

### Step 0 — Read everything before writing anything

Read in full:
- `records/brands/<brand_id>/brand_foundation.json` — positioning, audience,
  tone, visual pillars, avoid list. This is ground truth; never contradict
  or invent beyond it.
- `records/brands/<brand_id>/deepresearch.md` if it exists — real competitor
  notes and quoted customer language. This is your proof source.
- **`records/brands/<brand_id>/necessary-beliefs.md`, if it exists** (built
  by `brand-foundation`). When present, this REPLACES the default section
  map in Step 1 — build one section per belief instead of the default arc
  (see Step 1). When absent, fall back to the default HERO → GAP →
  MECHANISM → AUDIENCE → PROOF → CLOSE arc exactly as before.
- **`design.md` at the repo root, if it exists** (built by the
  `design-tokens` skill). When present, this is the source of truth for
  every visual value — use its exact hex codes, named fonts, voice
  USE/AVOID words, and component rules **instead of** deriving your own
  from `visual_pillars` in Step 3. When absent, fall back to deriving
  palette/type/voice directly from `visual_pillars` as before — say
  explicitly which path you took (design.md vs. derived) at the end of the
  build.
- `records/assets/*` if any exist for this brand:
  - `hero.mp4` + `hero-poster.jpg` (built by `hephaestus-production`'s
    hero-video step) — if both exist, this is the hero background (see
    Step 3). **Copy them into `records/website/<brand_id>/assets/`** so
    the site folder is self-contained and deploys as-is.
  - Otherwise a static image asset from a prior `hephaestus-production`
    build (for example `hero-still.png`) can become the hero image —
    copy it into the site's `assets/` too.
  - **Never generate a new image or video here** — this skill is HTML/CSS
    only. If nothing exists, use a CSS gradient/pattern hero built from the
    brand's palette (from `design.md` if present, else derived) instead.
  Say which hero path you took (video / static image / CSS-only).

### Step 1 — Map sections from the brand's actual argument

**If `necessary-beliefs.md` exists**: build exactly one section per belief
listed in that file, in the order they appear, plus a HERO section before
them and a CLOSE (CTA) section after. Each belief's section argues that
specific belief using the language and facts already in the foundation,
research file, or offer brief — never inventing new support for a belief
the source files don't back. Write the section map (belief → section name)
before building anything, then skip straight to Step 2.

**If `necessary-beliefs.md` does not exist**: use the default arc, adapted
to what's actually in the foundation:

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

**If building one section per belief** (`necessary-beliefs.md` present):
for each belief, write copy that makes the reader accept that specific
"I believe that..." statement, using only facts already present in
`brand_foundation.json`, `deepresearch.md`, or `offerbrief.md` — never
inventing new proof for a belief the source files don't back. If a belief
has no real supporting fact anywhere in the brand's files, say so and write
the section on the positioning/mechanism alone rather than fabricating
support.

**Otherwise** (default arc):
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
  from `deepresearch.md` verbatim if present. **Never fabricate a
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

- **CSS inline** in a `<style>` block.
  - **If `design.md` exists**: use its exact hex codes, named fonts,
    component rules, and USE/AVOID voice words verbatim — comment which
    `design.md` section drove which rule (e.g. `/* design.md Palette: signal
    red, accent-only, <5% of layout */`). Do not deviate from its values or
    invent your own alongside them.
  - **If `design.md` does not exist**: fall back to deriving palette/type
    from `visual_pillars` as before — comment which pillar drove which rule
    (e.g. `/* pillar: muted earth tones + safety-orange accent */`). Don't
    default to a generic SaaS-blue/Inter look unless the pillars genuinely
    call for it.
- **Hero**, in priority order:
  1. If both `assets/hero.mp4` and `assets/hero-poster.jpg` exist: an
     autoplay, muted, looping `<video>` background —
     ```html
     <video class="hero-bg" autoplay muted loop playsinline
            poster="assets/hero-poster.jpg">
       <source src="assets/hero.mp4" type="video/mp4">
     </video>
     ```
     (paths into the site's own `assets/` folder, copied in Step 0 — the
     folder must deploy on its own). Headline text must sit in a layer above the video
     with sufficient contrast (a scrim/overlay if `design.md`'s palette
     doesn't already guarantee contrast) — this is a background for text,
     not the reverse.
  2. Else if a real static image asset exists from a prior
     `hephaestus-production` build: `<img src="assets/<file>.png">`.
  3. Else: a CSS gradient/pattern hero using the palette (from `design.md`
     if present, else derived), clearly not a stock-photo placeholder.
- **Fonts**: if `design.md` specifies font families, use exactly those (load
  via `<link>` if a Google Fonts pairing, with the system-stack fallback
  `design.md` lists). If no `design.md`, system font stack by default
  (`-apple-system, "Segoe UI", ...`) unless the brand's visual pillars
  specifically call for a distinct typographic feel — then load one Google
  Fonts pairing via `<link>`, with a system fallback. Never more than two
  font families.
- **Sections** in the Step 1 order. Generous whitespace, one accent color
  used sparingly (status/CTA/emphasis only — never as a body color).
- **Responsive**: collapse cleanly to one column under ~480px. No
  JavaScript framework — vanilla JS only if genuinely needed (e.g. a mobile
  nav toggle), and keep it inline in the same file.
- **No lorem ipsum, no placeholder stock language, no fake logos/stats.**

### Step 4 — Run it and verify before calling it done

Serve it and look. From the repo root:

```
python3 -m http.server 8000
```
then open `http://localhost:8000/records/website/<brand_id>/index.html`.
The site folder carries its own `assets/`, so serving from inside
`records/website/<brand_id>/` or opening `index.html` directly also works,
and the folder deploys as-is.

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
