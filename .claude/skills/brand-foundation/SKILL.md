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

## Output layout

Everything for one brand lives in **one directory**:
`records/brands/<brand_id>/`, containing seven files:

```
records/brands/<brand_id>/
  deepresearch.md          research dossier — market, competitors, real
                            customer language, proof points. Sourced.
  avatar-sheet.md           the customer — pains, desires, beliefs,
                            objections, verbatim language
  offerbrief.md             product, promise, unique mechanism, proof,
                            pricing
  necessary-beliefs.md      the 4-6 beliefs someone must accept to buy
  project-knowledge.md      the synthesis, VERIFIED vs UNVERIFIED split
  brand-book.md             the readable brand book
  brand_foundation.json     the structured contract (schema unchanged)
```

`brand_foundation.json` stays the single authoritative machine contract —
every other skill in this repo reads it, not the prose files. The six `.md`
files are the human layer written from the **same reasoning**: they must
never contradict the JSON, and any claim that isn't sourced from research or
the user's own input about their own product goes in `project-knowledge.md`'s
UNVERIFIED section and **nowhere else** — never presented as fact in
`avatar-sheet.md`, `offerbrief.md`, `necessary-beliefs.md`, or `brand-book.md`.

## What you do

Write each file **as it completes**, not all at the end — the user should
see `deepresearch.md` land before you've even started reasoning about
positioning.

1. Read the user's description of their business, product, or brand. If it's
   under ~2 sentences or too thin to research (see Boundaries), ask for more
   before continuing.

2. **Deep research first — do not skip this, and do not reason about the
   brand before this file exists.** Use web search/fetch to actually look at
   the real market:
   - Search for 2-3 direct competitors or category leaders. Note what they
     promise, how they look/sound, and where they're generic or weak.
   - Search for how real customers in this space talk about the problem
     (reviews, forums, social — whatever surfaces fastest). Pull a few actual
     phrases, not paraphrases — real language beats invented language.
   - Note anything timely (a trend, a common complaint, a gap) that makes a
     specific angle defensible right now.
   - Keep this proportionate — a fast, single-pass research step (5-10
     minutes of searching, not an exhaustive dossier).
   - **Write `records/brands/<brand_id>/deepresearch.md` now**, before doing
     anything else: competitor notes, real customer language (quoted
     verbatim), the opening you found. Cite sources (URLs) inline for every
     claim. This file is the ONLY place external market facts get sourced —
     everything downstream cites back to it, never re-sources independently.

3. **Write `avatar-sheet.md`** — the customer, built only from what
   `deepresearch.md` actually contains plus direct inference from the user's
   own description of who it's for:
   - Pains, desires, beliefs, objections — each one either a direct quote
     from `deepresearch.md` (attributed) or explicitly marked
     `(inferred, not sourced)` if it's a reasonable inference with no direct
     quote behind it. Never state an inferred pain/desire as if it were a
     sourced fact.
   - Verbatim language: pull actual phrases from `deepresearch.md`'s
     customer-language section — do not paraphrase them here.

4. **Write `offerbrief.md`** — product, promise, unique mechanism, proof,
   pricing, built from the user's own input about their own product (this is
   self-reported, not something you need to externally source — the user
   describing their own mechanism is not a claim requiring proof) plus the
   competitive contrast from `deepresearch.md`:
   - Product / promise / mechanism: from the user's description.
   - Proof: only real, checkable claims (from the user's input or
     `deepresearch.md`) — no invented stats or results.
   - Pricing: only if the user actually stated a price or model. If they
     didn't, write "Not yet specified" — never invent a number, tier, or
     price point.

5. **Write `necessary-beliefs.md`** — the 4-6 things someone must accept
   before they buy, as "I believe that..." statements, each one traceable to
   a specific line in `offerbrief.md` or `avatar-sheet.md`. These aren't
   claims about the market — they're the beliefs the copy/website/brief work
   will need to earn, so keep them specific to this offer (e.g. "I believe
   that a coffee subscription CAN be timed to my actual consumption, not a
   calendar" — not "I believe good coffee matters").

6. Now reason through the core brand decisions — same bar as before, do not
   accept the first generic answer for any of these:
   - **Positioning**: what is this, for whom, and why not the obvious
     alternative? A positioning a competitor could paste onto their own
     business unchanged has failed. Use `deepresearch.md` — if every
     competitor already says "durable" or "premium," that word is dead,
     find the actual gap.
   - **Audience**: one real person (from `avatar-sheet.md`), not a
     demographic.
   - **Tone**: how it sounds, and explicitly what it never sounds like.
   - **Visual pillars** (3-6): concrete, checkable rules.
   - **Avoid**: the visual/tonal cliches this brand explicitly refuses —
     prefer cliches actually observed in `deepresearch.md` over generic
     guesses.

7. **Write `project-knowledge.md`** — the synthesis, with two explicit,
   clearly headed sections:
   - `## VERIFIED` — every claim used anywhere in this foundation that
     traces to a cited source in `deepresearch.md`, or to the user's own
     stated facts about their own product/pricing/mechanism.
   - `## UNVERIFIED` — every claim, assumption, or inference that has no
     source: market-size guesses, assumed customer behavior beyond what
     `deepresearch.md` actually found, pricing not yet set, any competitor
     detail you couldn't confirm. **This is where an unsourced claim goes —
     it must not appear as fact anywhere else in these seven files.** If
     nothing is genuinely unverified, say so explicitly rather than leaving
     the section thin without comment.

8. Write `brand_foundation.json` matching **exactly** the schema at
   `schema/brand_foundation.schema.json` (resolve from the repo root) — this
   schema is unchanged from before.
   - `brand_id`: slugify the brand/business name.
   - `created_at`: current ISO 8601 timestamp.
   - Save to `records/brands/<brand_id>/brand_foundation.json`.

9. Validate immediately:
   `python3 scripts/validate_brief.py records/brands/<brand_id>/brand_foundation.json --schema brand_foundation`
   Fix and re-run until it prints `VALID`. Never hand off an unvalidated
   foundation.

10. **Write `brand-book.md`** last — the readable brand book, same content
    as the JSON in prose, the way a real brand book reads. Reference
    `deepresearch.md` at the top (e.g. "grounded in: `deepresearch.md`").
    This must not contradict the JSON — it's the same reasoning, prose form.

11. Tell the user it's ready. Print all seven file paths (in the order
    above) and the `VALID` line. Tell them: from now on, `aphrodite-direction`
    will automatically use `brand_foundation.json` for every brief unless
    told otherwise, and `brand-website` will read `necessary-beliefs.md` if
    present.

## How this connects to the rest of the loop

Every other skill in this repo resolves the brand directory as
`records/brands/<brand_id>/` and reads `brand_foundation.json` from inside
it — never a bare `records/brands/<brand_id>.json` (that flat-file layout is
retired). `aphrodite-direction` folds `positioning`, `audience`, `tone`,
`visual_pillars`, and `avoid` into every brief. `brand-website` additionally
reads `necessary-beliefs.md` to build one section per belief when present.
`design-tokens` and `brand-guide` read the full directory for research and
the VERIFIED/UNVERIFIED split. If more than one brand directory exists, ask
the user which `brand_id` applies before writing anything.

## Boundaries — never do these

- Never write a brand foundation from a one-word input ("make my brand
  cool") — push back and ask what the business actually is first if the
  input is too thin to reason about.
- Never accept an `avoid` list that's empty — every real brand has refused
  something. If the user can't name one, ask "what does everyone else in
  this space do that you don't want to look like?"
- Never skip validation.
- Never overwrite an existing `records/brands/<brand_id>/` directory
  silently — if one exists, tell the user and ask whether to version it or
  replace it.
- Never invent a price, stat, or claim with no source — file it under
  `project-knowledge.md`'s UNVERIFIED section instead, and never let an
  unsourced claim surface as fact in any of the other six files.
- Never write `deepresearch.md` after reasoning about positioning has
  already started — research always lands first.
