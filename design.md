# Design Tokens — quiet-desk

## Palette

- `#121316` — matte black (primary background / instrument casing; deliberately not pure `#000` — pure black reads as default UI, this reads as machined material)
- `#E9E9EA` — cool off-white (primary text on dark, or light-mode base — never warm/cream, this is lab-panel white not lifestyle white)
- `#8A8D93` — instrument grey (secondary text, axis labels, dividers, unit labels like "dB" / "WPM" — the "fine print on a spec sheet" tone)
- `#FFC800` — calibration yellow (the single accent, standing in for the foundation's "safety yellow or orange" test-equipment marking; used only for: the decibel figure itself, primary CTA, tick marks/axis highlights — never decorative, never a gradient, never fills more than one element per layout)

No RGB gradients, no soft pastels, no beige/cream lifestyle tones — any warm neutral is out of bounds per the foundation's explicit refusal of both gamer-RGB and minimalist-desk-Instagram palettes.

## Typography

- Numerals, headlines, and every decibel/WPM figure: `"IBM Plex Mono", "JetBrains Mono", ui-monospace, monospace` — tabular-nums on at all times; this carries the "spec-sheet numerals" requirement, so a figure like `38 dB` must never fall back to a proportional face
- Body copy, labels, UI chrome: `"IBM Plex Sans", -apple-system, Helvetica, sans-serif` — technical grotesk only, never below 14px, never italic (spec sheets don't italicize for emphasis — use the yellow accent or the mono face instead)

Exactly these two families, total. No display, script, or hand-lettered face anywhere, including on packaging or one-off promo assets.

## Voice

USE: measured, dB, WPM, tested, published, calibrated, spec, rig, quarterly
AVOID: whisper-quiet, buttery, thocky, unleash, dominate, cozy, curated, aspirational, artisanal

Every sentence that claims quiet must carry a number and a test condition (switch name, WPM, distance from mic) in the same breath — a bare adjective like "quiet" or "whisper-quiet" with no figure attached is not shippable copy, it's the exact gap the brand exists to close.

## Components

- Data display: any sound claim renders as figure + unit + test condition together, e.g. `38 dB @ 60 WPM · 30cm` — never the number alone, never the adjective alone
- Buttons: flat calibration-yellow fill on dark, or yellow outline on light — 0-2px radius, no shadow, no gradient, no hover-glow
- Cards/panels: hairline border (1px, instrument grey, 10-15% opacity) on the matte-black or off-white base — no drop shadow, no soft rounded corners (max 4px radius, functional not decorative)
- Layout motifs: tick marks, axis labels, waveform or dB-meter graphics are allowed and encouraged; Instagram-square crops, mood-board collage grids, and rounded "app card" layouts are not
- Photography: product shots are top-down or instrument-angle, on a rig or plain surface, with a visible scale/ruler reference — no flat-lay staging, no plants, no coffee, no warm ambient window light

## Mood

A finished asset should feel like it was pulled off a calibration bench, not a mood board — the kind of confidence that comes from stating a measurement and letting it stand, not from styling. Nothing here is trying to look impressive; it's trying to look correct, the way a multimeter readout doesn't need adjectives to be convincing. The one hit of calibration yellow should read like a warning light or a dial marking earning its place, not a brand color chosen for warmth. If a page could be mistaken for a keyboard-hobbyist storefront or a desk-aesthetic Instagram grid, it has failed, regardless of how clean it looks.
