---
title: Poor surface above supports
category: Strength & Structure
keywords: support surface, rough above supports, support interface, supports stuck, supports fused
check_first: Set the support Z-gap to one layer height (0.2 mm) and enable 2–3 dense interface layers. The gap is the whole game: too small fuses, too big droops.
hw_sw: Mostly slicer
---

## What it looks like

The surface that printed on top of supports is rough, scarred, or droopy — noticeably worse than the rest of the print. Or the opposite: supports welded on and won't come off.

## Causes

1. **Support Z-gap wrong.** Zero gap = fused supports; huge gap = drooping surface.
2. **No dense interface layers** — sparse support tops leave the surface spanning wide gaps.
3. **Support pattern too sparse** overall.
4. **Printing the interface too hot/fast** to bridge cleanly.

## Fixes

1. **Z-gap = one layer height** (0.2 mm at 0.2 mm layers). For easy-removal materials like PLA this is the sweet spot.
2. **Enable 2–3 interface layers** at 80–100% density on top of the supports.
3. **Slow down** interface layers and keep cooling high so they bridge crisply.
4. For PETG (which loves to fuse), increase the gap slightly or use a different support material strategy; for PLA, a 0.1–0.15 mm gap can give near-perfect undersides if you don't mind firmer removal.
5. Orient the model to minimize supported area in the first place — the best support is no support.
