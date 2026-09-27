---
title: Small features not printing / missing details
category: Surface Quality
keywords: small features missing, details not printing, tiny parts missing, holes filled in
check_first: Check the slicer preview first — if the feature is missing in the preview, it's a slicer setting, not the printer.
hw_sw: Mostly slicer
---

## What it looks like

Tiny holes print filled in, thin walls vanish, small text is unreadable, or fine details are missing entirely — while the rest of the print is fine.

## Causes

1. **Slicer filtering out small features.** "Minimum feature size" or too-coarse slicing resolution drops details smaller than the nozzle can draw.
2. **Nozzle too large** for the detail — a 0.4 mm nozzle can't resolve 0.2 mm features.
3. **Over-extrusion** filling in small gaps and holes.
4. **Too-hot printing** melting fine details before they set.
5. **Model issues** — non-manifold geometry or details below the printer's physical resolution.

## Fixes

1. **Check the sliced preview** layer by layer. If detail is missing there, adjust slicer settings: reduce minimum line width, enable "print thin walls" / "detect thin walls."
2. **Slow down** on small perimeters and enable small-feature cooling (min layer time).
3. Verify flow isn't over 100% — over-extrusion erases fine negative details first.
4. For genuinely tiny work, switch to a **0.25 mm nozzle** (and accept slower prints).
5. Run the model through a mesh repair (Windows 3D Builder, Meshmixer, or the slicer's built-in fix) — broken geometry confuses slicers into dropping features.
