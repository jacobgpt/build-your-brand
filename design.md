# Design Tokens — signal-roasters

## Palette

- `#111214` — ink (primary text and primary UI ink; near-black, not pure
  black — pillar: "palette stays desaturated and utilitarian")
- `#EDEAE3` — bone (page/section background; warm-neutral off-white, not
  paper-white — pillar: "desaturated and utilitarian," avoids clinical
  white)
- `#6B6F76` — slate (secondary text, captions, metadata — muted, never
  used for body copy longer than a line)
- `#D63A2E` — signal red (the one accent: CTAs, live countdowns, delivery
  status indicators only — never body text, never a background fill larger
  than a button or badge, target under 5% of any layout's area — pillar:
  "one signal accent color")
- `#1F7A5C` — ready green (status-only: used exclusively for "shipped" /
  "on schedule" state indicators, never decorative)

No warm golden-hour tones, no browns/creams associated with coffee-shop
branding — directly enforced by `avoid`: "no warm golden-hour coffee-shop
tones."

## Typography

- Display / headlines: `"IBM Plex Mono", ui-monospace, "SF Mono", Consolas,
  monospace` — every H1/H2/eyebrow label, uppercase with wide letter-spacing
  (`0.04em`+). Traces to pillar: "monospace or grotesk workhorse face."
- Body: `"Inter", -apple-system, "Segoe UI", sans-serif` — sentence case,
  never smaller than 15px, 1.5 line-height minimum, never used for
  headlines.
- Never a script or serif face anywhere — explicit exclusion from the same
  pillar ("never a script or serif face associated with craft branding").
- Max two font families total (Plex Mono + Inter). If Google Fonts fails to
  load, fall back to the system stacks listed above — never fall back to a
  serif.

## Voice

```
USE:    plain, on-schedule, equipment, workday, dependable, timed, signal
AVOID:  cozy, artisanal, hand-crafted, curated, delight, journey, small-batch-as-vibe, hygge
```

`small-batch-as-vibe` (as opposed to a checkable claim like "roasted within
48 hours") is called out separately per the foundation's `avoid` rule
against "small-batch craft" claims with nothing checkable behind them —
"small batch" is fine as a fact, banned as a mood word.

## Components

- Buttons: solid signal-red fill, white text, 0-2px corner radius, no
  gradient, no drop shadow. Hover = flat opacity shift only (no lift/scale).
- Cards / sections: 1px hairline border at 10% ink opacity, flat background,
  never a drop shadow — traces to "flat lighting, no staging" (shadows read
  as staged depth, which the pillar excludes).
- Status/schedule element: every hero or product image must carry one
  legible timing element in frame (a date, a countdown, a "ships in Nd"
  badge) — this is a content rule, not just a style rule, and it is
  load-bearing per pillar 4 ("the mechanism is always visible, not
  implied").
- Spacing: generous, utilitarian — no section under 64px vertical padding,
  no dense grid-of-cards layouts (reads as e-commerce clutter, not
  equipment documentation).

## Mood

A page or asset that follows every rule above should feel like opening a
piece of dependable equipment's spec sheet, not browsing a coffee-shop
website — flat light, plain surfaces, a single red status light doing all
the emotional work, and a visible countdown proving the timing claim rather
than asserting it in copy. Nothing here should ever feel like it's trying
to be liked; it should feel like it's trying to be on time.
