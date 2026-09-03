---
description: "Build Your Brand — Lesson 7: The website. Copy-first, design.md-driven, hero-aware."
---

# /build:07-website

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
LESSON 7 · THE WEBSITE
THE STOREFRONT
──────────────────────────────────────────────────
```

> **Timing**     ~20 minutes
> **Goal**       A live one-page site, on-brand, with no claim you cannot back
> **Progress**   `[██████░░░░] 6/9 · starting`

---

## Copy first, then style

The site reads the same source of truth everything else does — the
foundation, the beliefs, `design.md`, and your hero if you built one.
No framework, no external tool, one self-contained file.

---

## STEP 1 — Map the sections from your beliefs

Before anything builds, open `necessary-beliefs.md` and list the page
sections — **one per belief** the visitor has to cross before they'll
act. Hero → problem → mechanism → proof → offer → close, in the order
your beliefs are sequenced (problem-aware → solution-aware →
product-aware → ready-to-buy). The copy decides what sections exist;
the design just dresses them.

> **ACTION:** Your section list written, one per belief. Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Section map locked                              │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[██████░░░░] 6/9 · Step 1/3`

---

## STEP 2 — Build the site

```bash
claude -p "Use brand-website to build a website for the <brand_id> brand"
```

It reads:
- the foundation — `brand_foundation.json`
- `necessary-beliefs.md` — one section per belief, in your mapped
  order
- `design.md` — exact values win over deriving from `visual_pillars`
- the hero from Lesson 6, if you built one: `hero.mp4` +
  `hero-poster.jpg` present → autoplay muted looping video
  background; no hero → a CSS-only hero from `design.md`, no broken
  references

> If the skill stops to ask about the CTA (no pricing/backend set
> yet), answer it — a waitlist `[FILL: connect to real signup]`
> placeholder is fine pre-launch. It won't invent a CTA destination
> for you.

> **ACTION:** Run the build. When
> `records/website/<brand_id>/index.html` exists, type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Site built                                      │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[██████░░░░] 6/9 · Step 2/3`

---

## STEP 3 — Serve it and read it like a stranger

Serve from the **repo root** (not the site's own folder — it
references shared assets by relative path):

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/records/website/<brand_id>/index.html`.

Then read it as a stranger would, holding it to this:

- **The 5-second test** — does the hero say what this is, who it's
  for, and why it's different, before any scrolling?
- **One belief per section** — does each section move exactly one
  belief from your map, in order? A section that exists because
  "websites have those" dilutes the page — cut it.
- **The claims check** — is there anything on that page you couldn't
  back up if someone asked? Any invented testimonial, stat, or logo
  means something went wrong upstream — go back and check the
  source documents rather than publishing it.
- **The CTA test** — is there exactly one clear action, and does
  every section lead to it?
- **The mobile pass** — check it at phone width. Half your visitors
  see it there first.

> **ACTION:** Site renders (hero video or fallback), first line
> works, no unprovable claims. Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Site live locally — read as a stranger           │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[███████░░░] 7/9 · Lesson 7 complete`

---

## DONE

**What you have now:**
- A single self-contained site at
  `records/website/<brand_id>/index.html`, served and checked in
  your browser
- Copy traceable to the foundation — nothing on it you can't back

**Next lesson:** `/build:08-assets` — one more real asset through the
full direction → gate → production pipeline, and a rejection on
purpose.
