---
name: brand-foundation
description: Use when the user wants to build, define, or establish their brand from scratch before making any assets — e.g. "build my brand", "let's define my brand foundation", "I'm starting a new brand for X". Interviews the user first (who they are, what they're building, visual preferences, pricing), then does sourced competitor research, and produces a structured brand_foundation.json that aphrodite-direction reads automatically for every future brief, so all assets come out on-brand instead of generic.
---

# Brand Foundation

You do the strategic thinking a real brand book front-loads — positioning,
audience, tone, visual rules, what to refuse — compressed into one working
session instead of weeks of back-and-forth. This is not a form-fill: reason
about the input the way a strategist would, push back internally on generic
answers, and only write down what's actually specific and defensible.

## Interview first — never skip this

Before any research or reasoning, interview the user. Ask as one list or
one by one, and **wait for real answers**. Never fill in a plausible
default for them. You must get answers (or an explicit
"I don't know / undecided") to at least these seven:

1. **Who are you?** Background — what they've done, built, or sold
   before, and what they want to be known for.
2. **What are you building?** What it is, who it's for, why it's
   different, what it refuses to look like. Two to four sentences.
3. **Who exactly is it for?** One real buyer: who they are and how they
   see themselves, as far as the user knows.
4. **What does it cost?** Price, range, or model (one-time,
   subscription, bundle) — or an explicit "undecided."
5. **Do you have an existing sales page, site, or ads?** If yes, get
   the URL or have them drop the file into the repo.
6. **Which two or three competitors** do they already know about?
7. **The outcome the customer most wants, and the fear or frustration
   they most want gone.** Plus anything else worth knowing: founder
   story, unique mechanism, testimonials, press.

Plus one more that feeds Lesson 4: **how do they want it to feel?**
Colour/type preferences, and any look they hate.

**If they provided an existing sales page or site: audit it before
researching.** Read it properly and write up how it performs on six counts: the
hook, how specific its claims are, whether the mechanism is clear, what
proof it shows, how it handles objections, and what it asks the reader
to do. That write-up opens `deepresearch.md` under
`## Existing Sales Page Audit`.

If the input is under ~2 sentences or too thin to research (see
Boundaries), the interview is where you get the missing depth — extend
it, don't proceed on a thin paragraph. Push back internally on generic
answers ("premium quality" is not an answer to any of the seven).

**Write `records/brands/<brand_id>/intake.md` first**, before anything
else: the seven questions, the feel question, and the user's answers,
verbatim. Every later
step reads this file — the customer description, pricing, and design
preferences come from here, not from guessing.

## When this triggers

The user describes their business/brand and wants a brand foundation
established before (or instead of) making a specific asset. This
runs ONCE per brand, not per asset — after it exists, `aphrodite-direction`
picks it up automatically for every brief.

## Output layout

Everything for one brand lives in **one directory**:
`records/brands/<brand_id>/`, containing nine files (intake + copywriter prompt + seven):

```
records/brands/<brand_id>/
  intake.md                the user's interview answers, written first
  copywriter-prompt.md     ready-to-paste AI copywriter system prompt
  deepresearch.md          research dossier — per-competitor visual/type/
                            palette/positioning teardown, category
                            pattern, real customer language, the opening.
                            Sourced.
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

1. Read `intake.md` (written in the interview step). Everything below
   reasons from it plus real research — never from guesses about the
   user or their market.

2. **Deep research first — do not skip this, and do not reason about the
   brand before this file exists.** Use web search/fetch to actually look
   at the real market. This is the highest-leverage step in the whole
   pipeline — everything downstream inherits its quality — so do it
   properly, not as a checkbox:

   **Competitor teardown (3-5 direct competitors or category leaders).**
   For each one, actually visit or research their site/presence and
   record:
   - **Visual language** — imagery style, photography vs illustration,
     colour saturation, whitespace, overall feel
   - **Type** — serif/sans/mono, weight, any distinctive typographic move
   - **Palette** — actual dominant colours they use (approximate hex if
     you can see them), accent colour
   - **Positioning** — the promise they lead with, the words they
     overuse, who they're talking to
   - **Where they're weak** — generic, interchangeable, clichéd, or
     neglected angles. This is the map of openings you'll use to present
     the user real options later.
   - A one-line "category pattern" synthesis at the end: what everyone
     in this space looks like (e.g. "all five use warm serif + cream
     backgrounds") — patterns are what a new brand can break.

   Plus the strategic layer, not just the visual one, per competitor:
   - **What they charge** and their offer structure, where findable.
   - **What they get right** — copy, proof, mechanism — not just where
     they're weak.
   - **The category**: what everyone in it currently claims, which
     claims are crowded, which are unclaimed, and which way it is
     moving.

   **Customer language — deep, not a garnish.** Search review sites,
   forums, comment threads and communities where buyers talk
   unprompted about the problem AND about the outcome they want. Pull 20+
   actual phrases, verbatim, in blockquotes so later lessons can lift
   them directly — paraphrases are worthless here. Alongside the
   phrases, capture:
   - **What they tried before**: the fixes they already paid for, why
     each one let them down in their words, and who they hold
     responsible.
   - **Fears**: what do they secretly fear is true about themselves
     because the problem persists?
   - **The outcome they picture**: what changes about their life, and
     about who they are, once this is solved. Not the feature, the
     person.

   **Proof points.** Studies, certifications, founder credentials,
   manufacturing/sourcing facts, anything in the category that lends
   rock-solid credibility — captured, not invented.

   **Mechanisms this brand could own.** A process, an angle or a frame
   nobody else in the category is claiming, and that this brand could
   defend as its own.

   **Timing.** Anything in the news, in the rules, or in the calendar
   that makes one angle stronger this quarter than it was last.

   **Depth bar: this is a dossier, not a summary.** Minimum ~3,000
   words of dense, structured research (H2/H3 sections, customer
   quotes in blockquotes). Use web search/fetch liberally — many
   queries, many sources. Cite URLs inline for EVERY claim. A thin
   deepresearch.md fails the whole foundation: everything downstream
   inherits its quality.
   - **Write `records/brands/<brand_id>/deepresearch.md` now**, before
     doing anything else, with these sections in order: Existing Sales
     Page Audit (if one was provided), the per-competitor teardown
     (visual + strategic), the category pattern, customer language
     (verbatim blockquotes + failed solutions + fears + dream
     outcomes), proof points, mechanism opportunities, the opening you
     found. This file is the ONLY place
     external market facts get sourced — everything downstream cites
     back to it, never re-sources independently.

3. **Write `avatar-sheet.md`** — the customer, in full. Build it from
   what `deepresearch.md` actually contains plus direct inference from
   the user's own description of who it's for, covering ALL of:
   - **Identity**: archetypal name, age range, income, location/lifestyle,
     occupation, day-to-day reality.
   - **Psychographics**: core identity (how they see themselves), the
     identity they aspire to, the identity they fear becoming, top
     values, daily emotional state.
   - **The problem, three layers deep**: surface pain (what they'd say
     out loud), deeper pain (what they wouldn't admit at a dinner
     party), identity-level pain (what the problem says about who they
     are). How long they've had it, what it has cost them.
   - **Failed solutions**: what they've tried, why it didn't work (in
     their words), who they blame, what they secretly fear is true
     about themselves because it failed.
   - **Desired outcome**: surface want, deeper want, identity-level
     transformation, life 6 months after it's solved.
   - **Current beliefs** about the category, about solutions like
     this, about themselves.
   - **Objections**: top 5 ranked by likelihood, plus the single one
     most likely to kill the sale.
   - **Language patterns**: 10 verbatim phrases about the problem +
     10 about the dream outcome, from research. Words they trust,
     words they find salesy.
   - **Where they are**: platforms they live on, authorities they
     trust, communities, what they already buy in adjacent categories.

   Every pain/desire/belief must be either a direct quote from
   `deepresearch.md` (attributed) or explicitly marked `(inferred, not
   sourced)`. Never state an inferred item as if it were sourced fact.
   No section stays empty. Where the dossier is silent, go back and
   search for that specific gap before writing the section.

4. **Write `offerbrief.md`**: what is sold, what it promises, the
   mechanism behind the promise, the proof, the price. Built from the user's interview answers in `intake.md` about
   their own product (this is self-reported, not something you need to
   externally source — the user describing their own mechanism is not a
   claim requiring proof) plus the competitive contrast from
   `deepresearch.md`:
   - Product / promise / mechanism: from `intake.md`.
   - Proof: only real, checkable claims (from the user's input or
     `deepresearch.md`) — no invented stats or results.
   - **Unique mechanism**: the proprietary, ownable angle — named, in
     plain English, why it works, why it beats the category's existing
     solutions, and why competitors can't or haven't replicated it.
     Everything else in the offer points back at it. If the user's input doesn't give you
     one, propose the strongest candidate from the research's
     "mechanism opportunities" and mark it for their confirmation.
   - **Risk reversal**: guarantee terms if any, and the confidence
     story behind them. Only from user input — never invent.
   - **Bonuses**: only ones the user actually mentioned. Never invent
     a bonus or a stated value.
   - Pricing: from `intake.md`. If they answered with a price, range,
     or model, use it as stated. If they explicitly said "undecided,"
     write "Not yet specified" — never invent a number, tier, or
     price point.

5. **Write `necessary-beliefs.md`** — the 4-6 things someone must accept
   before they buy, as "I believe that..." statements, each one traceable to
   a specific line in `offerbrief.md` or `avatar-sheet.md`. These aren't
   claims about the market — they're the beliefs the copy/website/brief work
   will need to earn, so keep them specific to this offer (e.g. "I believe
   that a coffee subscription CAN be timed to my actual consumption, not a
   calendar" — not "I believe good coffee matters").

   For EACH belief, also write:
   - **Current belief**: what the prospect believes today instead.
   - **Bridge**: the argument, proof, and emotional payoff that moves
     them from current → destination. Every future piece of copy
     installs or reinforces exactly one of these beliefs.

   No more than six, and fewer is stronger. Sequence them in the order
   a stranger has to accept them: first that the problem is real, then
   that a fix exists, then that this is the fix, then that now is the
   time.

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

7. **Write `project-knowledge.md`**: the synthesis, laid out so that
   anyone writing copy or buying media for this brand, human or model,
   can work from it after one read:
   - **Snapshot** — product, promise, customer (one paragraph), unique
     mechanism, price.
   - **Customer** — the condensed avatar.
   - **Offer** — the condensed offer brief.
   - **Necessary beliefs** — just the I-believe-that statements + a
     one-line bridge each.
   - **Voice & language** — words to use, words to avoid, top 15
     customer-voice phrases.
   - **Proof inventory** — all available proof points, ranked by
     strength.
   - **Open questions / research gaps** — anything still unknown that
     would strengthen the funnel if answered.

   Then two explicit, clearly headed sections:
   - `## VERIFIED` — every claim used anywhere in this foundation that
     traces to a cited source in `deepresearch.md`, or to the user's own
     stated facts about their own product/pricing/mechanism.
   - `## UNVERIFIED` — every claim, assumption, or inference that has no
     source: market-size guesses, assumed customer behavior beyond what
     `deepresearch.md` actually found, pricing not yet set, any competitor
     detail you couldn't confirm. **This is where an unsourced claim goes —
     it must not appear as fact anywhere else in these other files.** If
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

11. **Write `copywriter-prompt.md`**: a system prompt the user pastes
    into any assistant so every future line of copy is grounded in
    this brand. Nothing in the file but the prompt itself. It must:
    - Give the assistant one job: writing for THIS brand, and no
      other.
    - Name the foundation files and treat them as the only source of
      fact.
    - Set the working order: build the argument, name the mechanism,
      pick the belief each piece serves, use the customer's words.
    - Fix the voice from the foundation's `tone` and rule out the
      tones in `avoid`.
    - Cover the work it will be asked for: ads, emails, page
      sections, hooks, angles, objection answers.
    - Make it ask which belief a piece of copy serves before it
      writes.
    - Ban any claim, number or proof that isn't in the foundation.
      Gaps get flagged, never filled.

12. Report completion. Print all nine file paths (in the order
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
- Never skip or shorten the interview — no intake.md, no foundation. If
  the user won't answer, stop and tell them why it matters.
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
- Never ship a thin dossier — if `deepresearch.md` is under ~3,000
  words or short on verbatim customer quotes, keep researching. "It
  was fast" is not a defence; everything downstream inherits this
  file's quality.
