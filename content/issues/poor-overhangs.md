---
title: Rough / drooping overhangs
category: Strength & Structure
keywords: overhangs, drooping overhang, rough overhang, overhang curling
check_first: Max cooling + slow outer walls. Overhangs steeper than ~60° from vertical need support — no setting fully replaces geometry.
hw_sw: Mostly slicer (cooling, speed, orientation)
---

## What it looks like

Surfaces angled outward droop, curl, or print rough and stringy. The underside of the overhang looks melted.

## Causes

1. **Insufficient cooling** — each layer's edge has nothing under it and must freeze fast.
2. **Too fast** on the overhang perimeters.
3. **Too hot** — soft plastic droops under gravity.
4. **Overhang angle too steep** (beyond ~60–70° from vertical, or under ~45° from horizontal) — genuinely unprintable without support.
5. **Layer height too tall** — each layer sticks out further relative to its thickness.

## Fixes

1. **Fan 100%, slow outer walls** (25–35 mm/s) on overhangs; use the slicer's overhang speed settings.
2. **Lower temp** toward the cool end of the range.
3. **Orient the model** so the worst overhangs face up or become less steep; split the model if needed.
4. **Add supports** for anything beyond ~60° — with proper Z-gap and interface layers they come off cleanly (see Poor surface above supports).
5. Thinner layers (0.12–0.16 mm) handle overhangs better since each step outward is smaller.
