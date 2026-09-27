---
title: Layer separation / splitting (delamination)
category: Strength & Structure
keywords: layer separation, delamination, splitting, layers splitting apart, layers separate
check_first: Raise nozzle temp 10°C and cut part-cooling fan in half. Layers split when they didn't bond — that's temperature and cooling, almost always.
hw_sw: Mostly slicer/material (temp, cooling); material choice matters
---

## What it looks like

The print splits apart between layers — cracks running horizontally, sometimes the whole part delaminates into sheets. Common in tall ABS/ASA prints, occasional in PETG, rare in PLA.

## Causes

1. **Nozzle too cold** — layers don't fuse properly.
2. **Too much cooling** — the fan chills each layer before the next bonds (classic ABS killer).
3. **Drafts** cooling the part unevenly.
4. **Wet filament** — steam bubbles weaken the layer bond.
5. **Printing too fast** — less time for the new layer to melt into the previous one.

## Fixes

1. **Raise temp 10°C** (stay in the filament's safe range) and **reduce fan** (ABS/ASA: 0–25%; PETG: 30%; PLA rarely delaminates — if it does, something else is very wrong).
2. **Eliminate drafts**; for ABS/ASA use an enclosure.
3. **Slow down** 20–30% so each layer bonds properly.
4. Dry the filament.
5. If a specific tall ABS part keeps splitting no matter what, consider PETG or ASA instead — some geometries just fight ABS.
