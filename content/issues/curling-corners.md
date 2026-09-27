---
title: Curling or rough corners (overheating)
category: Surface Quality
keywords: curling corners, rough corners, overheated corners, deformed corners, melty edges
check_first: More cooling + slower on small layers. Corners curl when the plastic is still soft as the nozzle comes back around — it needs time or air to set.
hw_sw: Mostly slicer (cooling, speed)
---

## What it looks like

Sharp corners curl upward or look melted and deformed, especially on small parts or overhanging corners. The nozzle may catch the curled corner on the next pass.

## Causes

1. **Insufficient cooling** — the part-cooling fan too low or poorly aimed.
2. **Layer time too short** — on small layers the nozzle returns before the plastic sets.
3. **Printing too hot** for the geometry.
4. **Nozzle dragging** through the soft corner (too close, or over-extrusion).

## Fixes

1. **Max out part cooling** after the first couple of layers (100% for PLA).
2. **Set a minimum layer time** (10–15 s) so the slicer slows down or lifts on tiny layers. Printing two copies of a small part also buys cooling time.
3. **Slow down** outer walls on detailed sections.
4. **Lower temp** 5°C toward the cool end of the filament's range.
5. Check the part-cooling duct actually aims at the nozzle tip — a misaligned or melted duct (print ducts in PETG/ABS, not PLA) silently kills cooling.
