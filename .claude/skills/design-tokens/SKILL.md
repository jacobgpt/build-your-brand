---
name: design-tokens
description: Use when a brand foundation exists and the user wants a design.md — the specific palette, type, voice, and component rules every future build (website, hero assets) should read and obey. Distills brand_foundation.json + the brand book into locked, checkable values. brand-website reads this file when present.
---

# Design Tokens

You turn the brand foundation's `visual_pillars` and `tone` from prose into
locked, specific values a build can obey without reinterpreting them. This
is compression, not new invention — every value here must trace back to
something already decided in the foundation or brand book. If you're
inventing a palette or voice rule from scratch because the foundation
doesn't specify one, that's a sign the foundation itself is too vague — say
so, don't paper over it with an arbitrary pick.

## When this triggers

A brand foundation already exists (`records/brands/<brand_id>/brand_foundation.json`,
built by `brand-foundation`) and the user wants a `design.md` — the file
every later build (`brand-guide`, `brand-website`, `hephaestus-production`)
reads for exact values instead of guessing. design.md is written BEFORE the
brand guide — colour and type get settled here, and the guide then shows
them off.

## Prerequisite

`records/brands/<brand_id>/brand_foundation.json` must exist. If it doesn't,
stop and tell the user to run `brand-foundation` first — never invent a
design system with no foundation behind it. If more than one brand exists,
ask which `brand_id`.

## What you do

### Step 0 — Read everything first

Read in full:
- `records/brands/<brand_id>/brand_foundation.json` — `visual_pillars`,
  `avoid`, `tone`, `positioning`. This is where every value below must trace
  back to.
- `records/brands/<brand_id>/brand-book.md` if present, for the fuller
  prose version of the same decisions.
- `records/brands/<brand_id>/deepresearch.md` if present — the competitor
  teardown (visual language, type, palette, positioning per competitor, plus
  the category pattern) is your map of what's already taken and what's
  open. "Everyone in this category uses warm serif type" is a reason to
  pick something else — use it.
- `records/brands/<brand_id>/intake.md` if present — the user's stated
  colour/type preferences and any look they explicitly hated. These
  constrain every option you present.

### Step 0.5 — Present options first, never default silently

Before locking anything, present **2-3 real options** for the visual
direction, each grounded in evidence: what the competitors already look
like (from `deepresearch.md`'s teardown), what the user said they want
and hate (from `intake.md`), and what the foundation's visual pillars
demand. For each option give: a one-line concept, the palette (exact
hex), the type pairing, and one sentence on how it breaks or uses the
category pattern. Then **ask the user to pick and wait for their answer.**
Only after they choose do you write the final values below.

Never just pick one direction and write the file — that's the exact
defaulting this step exists to prevent. If the user says "you decide,"
pick the one with the strongest grounding and say why, but still show
them the others first.

### Step 1 — Palette: exact hex, named role, one line each

For each color the brand actually uses (typically 3-6: one or two neutrals,
one accent, optional secondary/state colors), write:

```
- `#0B0B0C` — ink (primary text, near-black not pure black)
- `#F5F3EF` — bone (background, warm off-white)
- `#E11D2E` — signal red (accent only: CTAs, live/status indicators — never body text, never >5% of any single layout)
```

Every entry: hex code, a name, and the role — where it's allowed to appear
and where it isn't. "Warm blue" is not a value. If a `visual_pillars` entry
says something like "desaturated and utilitarian," that constrains the
saturation/lightness of every hex you pick — don't contradict it with a
vibrant color "because it looks nice."

### Step 2 — Typography

Name real font families (system stack or a specific Google Fonts pairing —
never more than two families total), and the rule for when each is used:

```
- Display/headlines: `ui-monospace, "SF Mono", Consolas, monospace` — every H1/H2, always uppercase-tracked
- Body: `-apple-system, "Segoe UI", sans-serif` — never smaller than 15px, 1.5 line-height minimum
```

If the foundation's visual pillars call for a distinct typographic feel
("monospace workhorse," "never a script face"), the choice must satisfy
that constraint explicitly — say which pillar drove it.

### Step 2.5 — Type scale, motion, and signature structures

Deepen the typography section beyond families:

```
- Type scale: display 48/1.1, h2 32/1.2, body 16/1.5, caption 13/1.4
- Motion: 150-200ms ease-out for hover/fade, never bouncy, never
  parallax-scroll sections
```

And in Voice (Step 3), add **signature sentence structures** — the
2-3 constructions this brand uses so often they become recognizable
(e.g. "X, not Y" contrast lines; one-sentence paragraphs for
emphasis; colon-then-payoff lists). A copywriter should be able to
hear this brand with their eyes closed.

### Step 3 — Voice: USE and AVOID words

Pull this from `tone` in the foundation, made checkable:

```
USE:   plain, dependable, on-schedule, equipment, workday
AVOID: cozy, artisanal, hand-crafted, curated, delight, journey
```

5-10 words per list. A word belongs in AVOID if it's the kind of word a
generic competitor in this category already overuses, or if the foundation's
`tone` field explicitly disclaims it ("never sounds like...").

### Step 4 — Component rules

Concrete, checkable rules for recurring UI patterns — not a full design
system, just the load-bearing few:

```
- Buttons: solid accent fill, no gradient, no shadow, sharp corners (0-2px radius)
- Cards/sections: hairline border (1px, 8-12% opacity), never a drop shadow
- Spacing: generous — no section under 64px vertical padding
```

Derive these from the same visual pillars (e.g. a pillar about "flat
lighting, no staging" implies flat UI too — no shadows, no gradients).

### Step 5 — Mood (one paragraph, not a list)

2-4 sentences describing the felt sense a finished asset should have if
every rule above is followed correctly — this is the gut-check a builder
uses when a rule doesn't cover a specific case. Ground it in the
foundation's `positioning`, don't invent new adjectives.

### Step 6 — Write the file

Save as `design.md` at the **repo root** (not inside `records/`) — every
build reads it from there. Use this section order::

```
# Design Tokens — <brand_id>

## Palette
## Typography
## Voice
## Components
## Mood
```

### Step 7 — Tighten before handing off

Re-read every line. **If any single line could describe two different
brands, it isn't finished** — tighten it or cut it. This is the actual bar,
not a suggestion: a rule like "clean, modern typography" fails it; "grotesk
sans, uppercase tracked headlines, never a serif" passes it.

### Step 8 — Tell the user

Print the `design.md` path. Tell them: `brand-website` (and
`hephaestus-production`, once it reads design tokens too) will pick this up
automatically on the next build.

## Cross-check interview (optional but recommended)

If anything feels off after Step 0.5's options, run the 5-question
interview to sanity-check or build from scratch:

1. The name, and what it sells.
2. Three words for the brand.
3. Colours, as hex.
4. Three brands to borrow from, and the one thing to take from each.
5. Voice: what it always does, what it never does.

Specifics only: hex codes and named brands, never "clean" or
"modern".

## Boundaries — never do these

- Never invent a palette, font, or voice rule that doesn't trace back to
  something in the brand foundation or brand book — if the foundation is
  too thin to derive a value from, say so and ask, don't guess.
- Never write a value that could apply to any brand ("clean," "modern,"
  "bold" with no further specificity).
- Never overwrite an existing `design.md` silently — if one exists, tell the
  user and ask whether to revise it or start over.
- Never skip the options step (Step 0.5) — write design.md only after the
  user has chosen from real, evidence-grounded options.
- Never write outside the repo root (`design.md` lives at the root, not in
  `records/`).
