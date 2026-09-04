---
name: email-sequence
description: Use when the student wants a welcome or launch email sequence — five to seven emails, one belief each, in the brand voice, two subject lines apiece, with optional HTML templates in the brand's tokens, rendered and checked by eye.
---

# Email Sequence

You write the sequence that turns a new subscriber into a buyer —
paced over days, mapped to the necessary beliefs, every email in the
brand's voice, every claim sourced.

## Prerequisites

- `records/brands/<brand_id>/` with `necessary-beliefs.md`,
  `offerbrief.md`, `project-knowledge.md`.
- `design.md` at the repo root (for the HTML templates and voice
  USE/AVOID).
- The brand's CTA destination (a real link, a waitlist, a store —
  whatever the site uses). If none exists, stop and ask — never
  invent a link.

## What you do

### Step 1 — The arc

Five to seven emails, one per belief, in the order
`necessary-beliefs.md` gives them. One belief and one ask per email.
The default shape, adjusted to the beliefs on file:

1. **Day 0, the frame.** Who this is and the one thing it promises.
   Ask nothing yet.
2. **Day 1, the problem.** In the customer's own words from the avatar
   sheet. First belief.
3. **Day 3, why the usual fixes fail, and the mechanism.** Second and
   third beliefs.
4. **Day 5, the proof.** Only what the offer brief and the dossier can
   back. Third or fifth belief.
5. **Day 6, the offer and its price.** Fourth belief. The first firm
   ask.
6. **Day 8, the top objection, answered directly.** Fifth belief.
7. **Day 9, the close.** Sixth belief. A deadline only if the offer
   brief holds a real one.

Five emails if the offer is simple. **The closing deadline has to
exist**: a date, a cap or a season from the offer brief. Without one,
the close rests on the argument. Manufactured urgency is banned
throughout; it spends trust the brand cannot earn back.

Write the plan to `records/email/<brand_id>/sequence-plan.md` for the
student to review BEFORE any email body gets written.

### Step 2 — The emails

For each email, write to `records/email/<brand_id>/emails.md`:

```
## Email N — [purpose] (Belief #X, Day Y)
Subject A: [≤45 chars]
Subject B: [A/B variant, different pattern]
Preview: [extends the subject, never repeats it]
---
[Hook line — their words, from the avatar's verbatim language]
[2-4 short paragraphs: problem → mechanism/proof → the turn.
 Brand voice, argument-first, no hype.]
[One CTA line] → [destination]
[Sign-off, in the brand's tone]
```

Subject lines come from four places: a pain phrase lifted from the
avatar sheet, a strong claim the dossier backs, the cause behind the
pain, or a sourced figure. Never a tease the body doesn't deliver on.

**Proof discipline:** every number, result, or testimonial in any
body must trace to `offerbrief.md` or `deepresearch.md`. Anything
UNVERIFIED stays out — no exceptions for "it's just email."

### Step 3 — Brand-locked HTML (optional but recommended)

Build `records/email/<brand_id>/html/email-N.html` per email:

- **600px max width, table layout, ALL styles inline** — email
  clients strip `<style>` blocks; inline is the only reliable CSS.
- Brand colours and fonts from `design.md`; note that most clients
  fall back to system fonts — design for that degradation, don't
  fight it.
- A logo at the top as a hosted URL or base64, since mail clients
  won't load a local file; one prominent button; room around
  everything; readable in dark mode.
- Keep the plain-text version alongside — it lands in more inboxes
  than any HTML.

Then **verify by rendering** — screenshot each with headless Chrome
at 700×1000 and actually look: button renders, spacing holds, no
broken table. A template that looks right in the editor and wrong in
Gmail has failed.

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --hide-scrollbars \
  --window-size=700,1000 --screenshot=email-N.png \
  "file://$PWD/records/email/<brand_id>/html/email-N.html"
```

### Step 4 — Ship (the student's hands)

Give exact steps for whichever email platform the student uses: a
flow triggered on signup, one message per email, the waits from the
arc, each subject, preview and body pasted in or the HTML imported. **The student pastes it — the
skill never touches an ESP account itself.**

## Output layout

```
records/email/<brand_id>/
  sequence-plan.md    the arc, for review before writing
  emails.md           full bodies, subjects, previews
  html/               brand-locked templates + screenshots
```

## Boundaries — never do these

- Never invent a CTA destination, a stat, a testimonial, or urgency.
- Never use an UNVERIFIED claim in a subject or body.
- Never write the bodies before the student approves the arc.
- Never touch the student's ESP account — provide instructions,
  they execute.
- Never skip the render-verification on HTML templates.

## How this connects

Reads the same foundation every other skill reads; voice USE/AVOID
and palette from `design.md`; pain language verbatim from
`avatar-sheet.md`; proof only from `offerbrief.md`/
`deepresearch.md`.
