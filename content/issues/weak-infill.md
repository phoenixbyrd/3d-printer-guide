---
title: Weak, stringy infill
category: Strength & Structure
keywords: weak infill, stringy infill, thin infill, infill not bonding
check_first: Slow down infill speed and raise temp 5°C. Infill is usually printed fastest and hottest-demand — it's where under-extrusion shows first.
hw_sw: Mostly slicer
---

## What it looks like

Inside the print, the infill is wispy, broken, or doesn't connect to itself or the walls. The part feels hollow-weak even at 20%+ infill.

## Causes

1. **Infill speed too high** — infill often prints at 2x wall speed, exceeding the hotend's melt rate.
2. **Under-extrusion** showing up first where it's least visible.
3. **Infill temp effectively lower** — some slicers drop temp for infill; combined with speed, it can't bond.
4. **Infill pattern with long bridges** (e.g. sparse lines) that can't span.

## Fixes

1. **Cap infill speed** at ~60–80 mm/s and raise temp 5°C.
2. Rule out general under-extrusion (e-steps, flow, partial clog).
3. Switch to a self-supporting pattern (gyroid, cubic) at 15–20% — stronger per gram than sparse lines.
4. If the part needs real strength, add walls instead of infill — 4–5 walls beats 40% infill for most functional parts.
