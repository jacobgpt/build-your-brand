---
name: brand-foundation
description: Use when the user wants to build, define, or establish their brand from scratch before making any assets — e.g. "build my brand", "let's define my brand foundation", "I'm starting a new brand for X". Produces a structured brand_foundation.json that aphrodite-direction reads automatically for every future brief, so all assets come out on-brand instead of generic.
---

# Brand Foundation

You do the strategic thinking a real brand book front-loads — positioning,
audience, tone, visual rules, what to refuse — compressed into one working
session instead of weeks of back-and-forth. This is not a form-fill: reason
about the input the way a strategist would, push back internally on generic
answers, and only write down what's actually specific and defensible.

## When this triggers

The user describes their business/brand in a paragraph and wants a brand
foundation established before (or instead of) making a specific asset. This
runs ONCE per brand, not per asset — after it exists, `aphrodite-direction`
picks it up automatically for every brief.

## What you do

1. Read the user's description of their business, product, or brand. If it's
   under ~2 sentences or too thin to research (see Boundaries), ask for more
   before continuing.
2. **Deep research first — do not skip this.** Use web search/fetch to
   actually look at the real market before reasoning about positioning. This
   is what separates a defensible brand from a guess:
   - Search for 2-3 direct competitors or category leaders. Note what they
     promise, how they look/sound, and where they're generic or weak.
   - Search for how real customers in this space talk about the problem
     (reviews, forums, social — whatever surfaces fastest). Pull a few actual
     phrases, not paraphrases — real language beats invented language.
   - Note anything timely (a trend, a common complaint, a gap) that makes a
     specific angle defensible right now.
   - Keep this proportionate — this is a fast, single-pass research step
     (aim for 5-10 minutes of searching, not an exhaustive dossier). The goal
     is real grounding, not a research report.
   - Save what you found to `records/brands/<brand_id>-research.md`: a short,
     scannable doc — competitor notes, real customer language (quoted), and
     the opening you found. Cite sources (URLs) inline.
3. Using that research (not just the user's paragraph), think through, and
   do not accept the first generic answer for any of these:
   - **Positioning**: what is this, for whom, and why not the obvious
     alternative? A positioning that a competitor could paste onto their own
     business unchanged has failed. Use what you found in research — if every
     competitor already says "durable" or "premium," that word is dead, find
     the actual gap.
   - **Audience**: describe one real person, not a demographic ("18-35
     interested in fitness" is not an audience — "someone who's tried three
     productivity apps and quit all of them" is closer). Ground this in the
     real language you found, if any.
   - **Tone**: how it sounds, and explicitly what it never sounds like.
   - **Visual pillars** (3-6): concrete, checkable rules — palette direction,
     type feel, photography vs. illustration, composition habits. Someone
     should be able to look at a finished asset and check it against these.
   - **Avoid**: the visual/tonal cliches this brand explicitly refuses. This
     is the competitive fence — what every other brand in this space does
     that this one won't. Prefer cliches you actually observed in the
     competitor research over generic guesses.
4. Write it as JSON matching **exactly** the schema at
   `schema/brand_foundation.schema.json` (resolve from the repo root).
   - `brand_id`: slugify the brand/business name.
   - `created_at`: current ISO 8601 timestamp.
5. Save it to `records/brands/<brand_id>.json` at the **repo root**.
6. Validate immediately:
   `python3 scripts/validate_brief.py records/brands/<brand_id>.json --schema brand_foundation`
   Fix and re-run until it prints `VALID`. Never hand off an unvalidated foundation.
7. **Write a human-readable companion**: `records/brands/<brand_id>.md` — the
   same content as prose, the way a real brand book reads, so the user can
   actually review and sanity-check it without parsing JSON. Reference the
   research file at the top (e.g. "grounded in: `<brand_id>-research.md`").
8. Tell the user it's ready, print all three file paths (research, json, md),
   print the `VALID` line. Tell them: from now on, `aphrodite-direction` will
   automatically use this for every brief unless they tell it not to.

## How this connects to the rest of the loop

Once `records/brands/<brand_id>.json` exists, `aphrodite-direction` looks for
it (see that skill's instructions) and folds `positioning`, `audience`,
`tone`, `visual_pillars`, and `avoid` into every `creative_brief.json` it
writes — so "a static ad for X" comes out matching the established brand
instead of generic stock-photo direction. If more than one brand foundation
exists, ask the user which one applies before writing a brief.

## Boundaries — never do these

- Never write a brand foundation from a one-word input ("make my brand
  cool") — push back and ask what the business actually is first if the
  input is too thin to reason about.
- Never accept an `avoid` list that's empty — every real brand has refused
  something. If the user can't name one, ask "what does everyone else in
  this space do that you don't want to look like?"
- Never skip validation.
- Never overwrite an existing `brand_id` silently — if one exists, tell the
  user and ask whether to version it or replace it.
