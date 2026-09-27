---
title: Elephant's foot — bottom layers flare out
category: First Layer & Bed Adhesion
keywords: elephant foot, flared base, bottom layers wider, squished bottom
check_first: Raise the nozzle slightly (Z-offset up 0.05 mm) and make sure the bed isn't running hotter than 60°C for PLA.
hw_sw: Both — usually slicer/first-layer setup, sometimes bed too hot
---

## What it looks like

The first few layers of the print splay outward like a bell bottom, making the base wider than the design. Parts that should fit together don't, because the bottom is oversized.

## Causes

1. **First layer squished too hard.** Too-low Z-offset or excessive first-layer width/height pushes extra plastic outward.
2. **Bed too hot.** A 70°C+ bed keeps the bottom layers soft so the weight above squashes them outward (common when people crank the bed to fix adhesion).
3. **Nozzle too hot on layer one**, same softening effect.
4. **Missing chamfer in the model.** Sharp 90° bottom edges show elephant's foot worst; a 0.5 mm chamfer hides it.

## Fixes

1. **Dial back the squish:** raise Z-offset slightly and use 0.2 mm / 100–120% for the first layer instead of extreme settings.
2. **Bed at 60°C for PLA** (not higher) once adhesion is otherwise working.
3. **Slicer compensation:** most slicers have an "elephant's foot compensation" / "initial layer horizontal expansion" setting — try −0.1 to −0.2 mm.
4. **Design around it:** add a small chamfer to the model's base; it hides any residual flare.
