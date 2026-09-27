---
title: Dimensional inaccuracy — parts don't fit
category: Strength & Structure
keywords: dimensional accuracy, parts don't fit, holes too small, tolerance, wrong size
check_first: Print a 20 mm calibration cube and measure with calipers. If X/Y/Z are off, it's steps or flow; if only holes are small, it's the classic hole-shrinkage slicer compensation.
hw_sw: Both — calibrate first, then compensate in slicer
---

## What it looks like

A 20 mm cube measures 20.4 mm. Holes print smaller than designed. Pins don't fit holes. Assemblies that should slot together don't.

## Causes

1. **Flow rate too high** — every wall slightly too thick adds up (most common).
2. **Hole shrinkage** — holes print ~0.2–0.4 mm smaller than modeled because the plastic pulls inward as the circular toolpath cools. This is normal physics, not a malfunction.
3. **E-steps / flow uncalibrated** (see Setup).
4. **Elephant's foot** making the base oversized.
5. **Thermal expansion differences** between materials (ABS shrinks ~1–2% overall).

## Fixes

1. **Calibrate e-steps and flow** first — measure the 20 mm cube on all axes.
2. **Horizontal expansion compensation:** most slicers offer "hole horizontal expansion" — try +0.1 to +0.2 mm on holes, and slight negative overall expansion if everything runs big.
3. **Design for FDM:** clearance of 0.2–0.3 mm per side for sliding fits; drill/ream critical holes after printing.
4. For ABS/ASA, apply a **shrinkage factor** (scale the model 100.5–101%) — or better, print a test piece and measure the actual shrinkage of your spool.
5. Fix elephant's foot separately if the base is the only oversized part.
