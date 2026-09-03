---
name: email-sequence
description: Use when the student wants a welcome/launch email sequence — a belief-mapped 5-7 email arc in the brand voice, with A/B subjects, plus optional brand-locked HTML email templates rendered and screenshot-verified.
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

Map a **5-7 email sequence** to the beliefs, in the order they're
sequenced in `necessary-beliefs.md` (problem-aware → ready-to-buy).
One belief per email, one CTA per email. Typical arc:

| # | Day | Email | Installs | CTA strength |
|---|-----|-------|----------|-------------|
| 1 | 0 | Welcome — who we are, the one promise | the frame | soft |
| 2 | 1 | The problem, in their words | Belief 1 | low |
| 3 | 2 | Why the usual fixes fail + the mechanism | Beliefs 2-3 | medium |
| 4 | 4 | Proof, sourced — how it works | Belief 3/5 | medium |
| 5 | 5 | The offer + price | Belief 4 | strong |
| 6 | 6 | Objection-killer — the #1 objection head-on | Belief 5 | strong |
| 7 | 7 | Earned-urgency close (real scarcity only) | Belief 6 | hard |

Collapse to 5 if the offer is simple. **Day 7's urgency must be
real** — an actual deadline, cap, or season from the offer brief. No
real scarcity? The close earns the buy on the argument alone; fake
urgency is forbidden everywhere and would cost the brand trust it
can't buy back.

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

Subject patterns to draw from: the customer's pain verbatim · a
bold-but-sourced claim · "the real reason [pain]" · a number (only
if sourced). Never a clickbait curiosity gap the body doesn't pay
off.

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
- Logo header (hosted URL or base64 — clients can't read local
  files), one big button CTA, generous padding, dark-mode-friendly.
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

Provide exact instructions for the ESP the student uses (Klaviyo /
Mailchimp / Beehiiv / ConvertKit): create a signup-triggered flow,
one message per email, send delays from the arc, paste subject +
preview + body or import the HTML. **The student pastes it — the
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
