---
title: Warping — corners lift off the bed
category: First Layer & Bed Adhesion
keywords: warping, warp, corners lifting, curling up, edges peel
check_first: Add a brim, raise the bed temp 5–10°C, and eliminate drafts. Warping is plastic shrinking as it cools — keep it warm and anchored.
hw_sw: Mostly slicer/environment (cooling, brim, temps); material-dependent
---

## What it looks like

Corners or edges of the print curl upward off the bed as the print progresses, sometimes dramatically. The bottom of the part ends up banana-shaped. Worst with ABS/ASA, occasional with PLA on large flat parts, rare with PETG.

## Causes

1. **Uneven cooling / drafts.** The top layers cool and shrink while the bottom stays warm — the part pulls itself up. A vent, window, or AC is the classic trigger.
2. **Bed too cool for the material.** ABS at 80°C will warp; it wants 100–110°C.
3. **No brim/raft on a large flat part.** Small contact area + shrinkage = lift.
4. **Too much part cooling too early**, especially on ABS/ASA (fan should be off or very low).
5. **Dirty or unlevel bed** reducing the grip that's fighting the shrinkage.

## Fixes

1. **Add a brim** (8–15 mm) — cheap insurance that massively increases holding area. A raft is the heavy-duty option for warp-prone materials.
2. **Raise bed temp** to the top of the material's range (PLA 60–65°C, PETG 85°C, ABS 100–110°C) and let it heat-soak 5+ minutes.
3. **Eliminate drafts.** Close windows/vents near the printer. For ABS/ASA, an enclosure isn't optional — it's the fix.
4. **Cooling:** PLA can keep its fan; ABS/ASA should run 0% fan for the first several layers, then max ~25%.
5. **Mouse ears:** small disc "ears" added at sharp corners in the slicer give extra anchor exactly where lift starts.
6. If warping persists on large ABS parts even with an enclosure, the part geometry may just be warp-prone — split it, add relief cuts, or switch to ASA/PETG.
