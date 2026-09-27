---
title: Gaps or holes in top layers (pillowing)
category: Surface Quality
keywords: gaps in top, holes top layer, pillowing, top surface holes, sparse top
check_first: Add more top layers (5–6 at 0.2 mm) and bump infill to 20%+. Pillowing is almost always too few top layers over too-sparse infill.
hw_sw: Mostly slicer
---

## What it looks like

The top surface has small holes, dips, or a "pillow" texture where the top layers sagged between infill lines instead of bridging them.

## Causes

1. **Too few top layers.** 2–3 top layers at 0.2 mm can't bridge infill gaps cleanly.
2. **Infill too sparse** — the spans between infill lines are too wide to bridge.
3. **Under-extrusion** making the top layers thinner than intended.
4. **Too much cooling too fast** on the top layers, freezing them before they bond across the gap.

## Fixes

1. **Use 5–6 top layers** (about 1–1.2 mm total) and **≥15–20% infill**.
2. **Slow down** the top layers and reduce fan slightly so they bond and bridge.
3. Verify flow calibration — under-extrusion shows up worst on top surfaces.
4. Infill patterns with shorter spans (gyroid, cubic) pillow less than straight lines at the same percentage.
