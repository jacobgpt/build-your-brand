---
description: "Build Your Brand — Lesson 2: Interview + deep research. Real competitor and customer research, sourced, before any brand decisions."
---

# /build:02-research

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
LESSON 2 · DEEP RESEARCH
THE FOUNDATION
──────────────────────────────────────────────────
```

> **Timing**     ~30-40 minutes (most of it Claude searching the web)
> **Goal**       Your interview answers on file, and a sourced competitor dossier you have actually read
> **Progress**   `[█░░░░░░░░░] 1/9 · starting`

---

## Why this is the most important lesson

Every weak brand skips this. Every strong one starts here.

Generic AI output comes from the same place: a prompt with nothing
behind it. The model fills the gaps with the average of everything
it's seen — and the average looks like everything else.

Research is what stops that. Not vibes about your market — real
competitors taken apart properly: their visual language, their type,
their palette, their positioning, and where they're weak. Plus the
language customers actually use, and the gap nobody's filling.

Everything in the next seven lessons is built on what this lesson
produces. Get it wrong and everything downstream is confidently wrong.

---

## STEP 1 — The interview

Before any research happens, Claude asks you questions. Real ones —
answer in your own words, as much or as little as you like:

1. **Who are you?** Your background — what you've done, built, or sold
   before, and what you want to be known for.
2. **What are you building?** What it is, who it's for, why it's
   different, what it refuses to look like. Two to four sentences —
   don't over-polish it.
3. **Who exactly is it for?** The ideal customer.
4. **What does it cost?** Price, range, or model — genuinely unset is
   fine too.
5. **Existing sales page, site, or ads?** A URL gets audited before
   research starts.
6. **Top 2-3 competitors** you already know of.
7. **The biggest result your customer wants, and their biggest
   fear or frustration** — plus anything else worth knowing
   (founder story, testimonials, press).

   Also: **how do you want it to feel?** Colour and type preferences,
   and any look you hate — Lesson 4's design options will use these.

Don't have perfect answers? Good enough is fine — the research fills
the gaps. Your answers are written to
`records/brands/<brand_id>/intake.md` before anything else happens:
every later step reads what YOU said, not a guess.

> **ACTION:** Answer the four questions. When `intake.md` exists with
> your answers in it, type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Interview complete — intake.md written          │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[█░░░░░░░░░] 1/9 · Step 1/3`

---

## STEP 2 — Run the research

Now the real work:

```bash
claude -p "Use brand-foundation to build a brand foundation for the brand I described in intake.md"
```

Real web search first — this is a proper dossier, not a quick pass:
a ~3,000-word deepresearch.md with a per-competitor teardown (visual
language, type, palette, positioning, pricing, weaknesses), the
category landscape and its openings, 20+ verbatim customer quotes
with failed solutions and fears, proof points, and mechanism
opportunities. If you gave it a sales page URL, that gets audited
first. Later lessons offer you real choices instead of defaulting
because of this step. It writes nine files, in order, to
`records/brands/<brand_id>/`:

```
intake.md               your interview answers (written first)
copywriter-prompt.md    a ready-to-paste AI copywriter prompt, tuned
                        to your brand, that flags gaps instead of
                        inventing claims
deepresearch.md         the dossier, sourced — lands before anything else
avatar-sheet.md         the customer, in their own words
offerbrief.md           product, promise, mechanism, proof, pricing
necessary-beliefs.md    what someone must accept before they buy
project-knowledge.md    the synthesis, VERIFIED vs UNVERIFIED
brand-book.md           the readable brand book
brand_foundation.json   the structured contract
```

This takes the longest — the research is doing real work across the
web. Let it cook.

> **ACTION:** Run the command. When all nine files exist, type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Research complete — nine files written         │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[█░░░░░░░░░] 1/9 · Step 2/3`

---

## STEP 3 — Read it before you move

This is the step people skip and regret. Open `deepresearch.md` and
read it in full — especially the competitor teardown. A wrong
assumption about your customer, a competitor you didn't know about, a
claim with nothing behind it — this is where it shows up, and it's
cheap to fix here and expensive later.

Then open `project-knowledge.md` and check the UNVERIFIED section
specifically — those claims stay out of everything you build. Not
because it's cautious — a brand that only says what it can prove is
the one people believe.

> **ACTION:** Read `deepresearch.md` and sanity-check it against what
> you know. Check the UNVERIFIED section. Type `1` when it holds up.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Foundation researched and reviewed              │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[██░░░░░░░░] 2/9 · Lesson 2 complete`

---

## DONE

**What you have now:**
- Your interview answers on record (`intake.md`)
- A ready-to-paste AI copywriter prompt (`copywriter-prompt.md`) —
  drop it into any AI assistant and every piece of copy it writes is
  grounded in your brand, not generic AI copy
- A ~3,000-word sourced dossier: competitor teardown (visual +
  strategic), category landscape, 20+ verbatim customer quotes, proof
  points, mechanism opportunities
- The customer's exact language, the offer with a named mechanism,
  beliefs with bridges, and a VERIFIED/UNVERIFIED split

**Next lesson:** `/build:03-foundation` — validate the contract your
research produced and make it yours. Quick one.
