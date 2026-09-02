# Design Tokens — signal-roasters

## Palette

- `#14151A` — ink (primary text, primary UI fill; near-black, cool not warm — avoids any brown/charcoal-coffee tint)
- `#F3F1EC` — bone (background; warm-neutral off-white — the only "warm" value in the system, and it's a neutral, not a golden-hour tone)
- `#6B6D73` — steel (secondary text, hairline borders, field labels on the schedule/data elements — the "spec sheet" gray)
- `#E8232A` — signal red (accent only: CTAs, and the timing/schedule element required in every image — roast date, days-remaining, delivery window. Never body text, never a background fill, never more than one accent use per layout)

No other colors. No gradients. If a build needs a fifth color, it's not derived from this foundation — stop and ask rather than picking one.

## Typography

- Display/headlines: grotesk sans — `-apple-system, "Helvetica Neue", Arial, sans-serif`. Never a serif, never a script (foundation explicitly bans anything reading as "craft" branding).
- Body: same grotesk family, regular weight, sentence case — never smaller than 15px, 1.5 line-height minimum.
- Data/timing values (roast date, days-remaining countdown, delivery window): monospace — `ui-monospace, "SF Mono", "Roboto Mono", monospace`. This is the one place monospace is required, not optional — pillar 4 requires the schedule mechanism to be legible in every image, and monospace is what makes a date or countdown read as a readout instead of a caption.
- Never pair a third typeface in. Two families total: grotesk + monospace.

## Voice

USE: plain, operational, roast date, delivery window, days remaining, on-schedule, consumption-matched, equipment, workday, status

AVOID: cozy, artisanal, hand-crafted, curated, small-batch (unless paired with a specific checkable number), surprise, discover, journey, delight, hygge

Rule: state a fact (a date, a count, a window) instead of an adjective wherever one is available. If a sentence has no fact to state, it's probably not a sentence Signal needs.

## Components

- Buttons: solid fill (ink or signal red), 0–2px corner radius, no gradient, no shadow, no pill shapes.
- Cards/sections: 1px hairline border at 8–12% opacity, never a drop shadow, aligned to a grid — no floating/shadowed cards.
- Every product image or hero section includes a legible monospace timing element (roast date / days-remaining / delivery window) — this is not decorative, it's required per visual pillar 4. A layout without one is incomplete.
- Layout: grid-based and symmetrical, like a spec sheet or dashboard — no asymmetric flat-lay compositions, no scattered props, no artful negative space for its own sake.
- Photography direction (for any generated imagery): flat, even lighting, plain surface, no hands, no steam, no window light. Signal red never used as a background wash — it appears only as a small, precise mark (a button, a status dot, a countdown digit).
- Spacing: functional, not generous-for-its-own-sake — spacing should read as alignment to a grid, not as breathing room for a lifestyle layout.

## Mood

A finished asset should feel like glancing at an equipment status panel, not opening a care package — exact, quiet, and slightly clinical, the way a shipment tracker or a machine's readout is trusted precisely because it doesn't try to charm you. Nothing on the page should ask to be admired; every element either states a fact (roast date, days remaining, delivery window) or does a job (button, label, boundary). If a layout would look at home on a travel postcard or a hygge mood board, it has failed, no matter how polished it looks.
