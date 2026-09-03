---
description: "Build Your Brand — Lesson 10: Grow. Ads, emails, and content — the three engines that make the brand show up, all gated and grounded."
---

# /build:10-grow

```ansi
     ██  █████  ██  ██████  ██████  ██████
     ██ ██   ██ ██ ██      ██    ██ ██   ██
     ██ ███████ ██ ██      ██    ██ ██████
██   ██ ██   ██ ██ ██      ██    ██ ██   ██
 █████  ██   ██ ██  ██████  ██████  ██████

          T H E   C R E A T I V E   A R C H I T E C T
```

```
──────────────────────────────────────────────────
LESSON 10 · GROW
THE ENGINES
──────────────────────────────────────────────────
```

> **Timing**     ~30-45 minutes (pick one engine or run all three)
> **Goal**       A launch-ready ad set, a belief-mapped email sequence, and a 2-week content calendar — whichever you choose, grounded and gated
> **Progress**   `[██████████] 9/9 done · post-course utilities`

---

## The brand exists. Now make it show up.

Lessons 1-9 built the brand. This lesson runs the engines that put
it in front of people. Three of them, each reading the same
foundation everything else reads — the angles in your ads come from
the same research your site came from:

| Engine | What you get | Spend |
|--------|-------------|-------|
| **Ads** | 5-8 researched angles, a Meta-ready copy bank, static ads, video scripts | Image plates cost credits (gated); copy is free |
| **Email** | A 5-7 email welcome/launch arc, belief-mapped, A/B subjects, HTML templates | No credits — just your review |
| **Content** | 4-5 pillars, 15-20 sourced ideas, 3-4 rendered carousels, captions, a 2-week calendar | No credits — headless Chrome renders |

Run one, two, or all three — each works standalone once the
foundation and `design.md` exist.

One rule runs through all of them: **every claim sourced, every
generation gated.** If an engine needs a number the research doesn't
have, it flags it — it doesn't invent it. That's the difference
between marketing a real brand and impersonating one.

---

## ENGINE 1 — Ads (`ad-factory`)

### Why ads fail the naive way

Two ways AI ads go wrong: the angles are generic ("quality matters")
because they were imagined, not mined from research. And the image
model renders the text — garbled headlines, fake logos, the trash
look. This engine fixes both: angles mined from YOUR research, and
all type overlaid in post as brand-locked HTML, never generated.

### STEP 1 — Angles and the copy bank (free, your review)

```
claude -p "Use ad-factory to mine ad angles for <brand_id>"
```

It reads your avatar's pains/fears/objections verbatim, your
necessary beliefs, and the competitor teardown, then writes 5-8
concepts to `records/ads/<brand_id>/ad-concepts.md` — each mapped to
one belief, three distinct hooks each, every line with its source.
**The kill rule: any angle a competitor could run unchanged is cut.**

Read and edit this file. It's your campaign's source of truth.

> **ACTION:** `ad-concepts.md` read, cut/sharpened where needed,
> `copy-bank.md` looks ready. Type `1` when the angles are locked.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Angles mined from research, not imagination     │
└─────────────────────────────────────────────────┘
```

### STEP 2 — Static ads: plate through the gate, overlay in post (gated)

For each concept you approve for production:

```
claude -p "Use ad-factory to produce a static ad for concept N of <brand_id>"
```

Two layers, and this is the anti-trash trick:
1. **The plate** — a text-free background in your exact
   `design.md` palette, built through the approval gate (real
   credits — check cost before `y`). Briefs carry
   `asset_type: ad-plate`; the build prompt explicitly forbids any
   text, logos, or fabricated characters.
2. **The overlay** — your hook, headline, and CTA rendered on top
   as brand-locked HTML (your exact fonts, your exact colours),
   screenshotted to PNG. Crisp type every time.

**Then judge it:** copy legible, palette exact, no garbled text.
Weak plate = new plate brief, not a patched overlay.

> **ACTION:** Statics judged — every one legible and on-palette.
> Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Launch-ready statics — crisp type, zero garble   │
└─────────────────────────────────────────────────┘
```

### STEP 3 — Video scripts (optional)

Beat scripts per concept (hook → problem → mechanism → CTA, timed)
written to `records/ads/<brand_id>/video/`. Plates gated as above;
motion/VO/caption assembly runs only when you say go — the skill
provides exact commands and naming, spends nothing uninvited.

---

## ENGINE 2 — Email (`email-sequence`)

### The arc before the emails

```
claude -p "Use email-sequence to plan a welcome sequence for <brand_id>"
```

It maps a 5-7 email arc to your beliefs in funnel order —
`sequence-plan.md` for your review BEFORE any body is written.
Day-7 urgency only if your offer actually has a real deadline; fake
urgency is banned and would cost trust you can't buy back.

> **ACTION:** Arc reviewed and approved. Type `1` to write the
> emails.

### The emails

Bodies in `records/email/<brand_id>/emails.md` — subject A/B pairs,
preview text, hook in the customer's verbatim words, one belief and
one CTA per email. Plus brand-locked HTML templates (table layout,
inline styles, 600px — email clients strip everything else),
screenshot-verified by actually rendering them.

You paste the sequence into your ESP (Klaviyo/Mailchimp/Beehiiv/
ConvertKit) — the skill gives exact instructions but never touches
your account.

> **ACTION:** Emails read and tweaked, HTML renders verified.
> Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Belief-mapped sequence ready to ship            │
└─────────────────────────────────────────────────┘
```

---

## ENGINE 3 — Content (`content-engine`)

### Pillars, then carousels as finished files

```
claude -p "Use content-engine to build a content batch for <brand_id>"
```

1. **Plan** — 4-5 pillars + 15-20 post ideas in
   `records/content/<brand_id>/content-plan.md`, each idea mapped
   to a belief with its source line. Ideas with no source are cut.
   Your review first.
2. **Carousels** — the best 3-4 built as slide-by-slide HTML in
   your EXACT design tokens and rendered to PNG at 1080×1350.
   These aren't instructions — they're finished, postable images.
   Fonts-actually-loaded is verified by looking at the render, not
   assumed.
3. **Captions + calendar** — per-asset captions and a balanced
   2-week calendar that starts with assets that already exist.

> **ACTION:** Carousels rendered and looked at, calendar confirmed.
> Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Two weeks of content, done and on-brand          │
└─────────────────────────────────────────────────┘
```

---

## DONE

**What you have now (whichever engines you ran):**
- **Ads:** research-mined angles, a Meta-ready copy bank, gated
  statics with crisp overlaid type, timed video scripts
- **Email:** a belief-mapped welcome arc, verified HTML templates,
  ready to paste into your ESP
- **Content:** pillars, rendered carousels, captions, a 2-week
  calendar

All three read the same foundation your site was built on. Same
claims, same voice, same palette — the whole surface area of the
brand is one argument, delivered in three paces: seconds (ads),
days (email), weeks (content).

**The flywheel:** publish, see what lands, re-run the engine — the
plan steps regenerate against what you've learned. Ads that win get
new hooks on the same bodies. Content that lands becomes a pillar.
The foundation doesn't change; the delivery sharpens.
