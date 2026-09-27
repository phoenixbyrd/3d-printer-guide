---
title: Nozzle too close — first layer squished or scraping
category: First Layer & Bed Adhesion
keywords: too close, scraping, squished, nozzle dragging, rough first layer, filament curling, z offset too low
check_first: Raise Z (babystep up) in 0.05 mm steps while printing a first-layer test until the lines lay flat without ridges.
hw_sw: Hardware/setup (Z-offset, leveling)
---

## What it looks like

The first layer is translucent-thin, the nozzle visibly plows through just-laid plastic leaving ridges, or you hear scraping. Sometimes filament curls up around the nozzle instead of sticking, because there's no gap for it to exit into. The extruder may click from the backpressure.

## Causes

1. **Z-offset too low.** The nozzle is starting below the correct first-layer height.
2. **Bed leveled with too much paper drag.** "Light drag" means the paper moves freely with slight resistance — not pinned.
3. **Warped bed high spot.** Glass beds can bow; one area prints fine while a high spot scrapes.
4. **First layer height set too low in the slicer** combined with an aggressive "squish" — e.g. 0.1 mm first layer with 150% width.

## Fixes

1. **Babystep Z up** during a first-layer test print, 0.05 mm at a time, until lines are smooth and separate slightly rather than ridged.
2. **Re-level with lighter paper drag**, hot, two full loops.
3. **Set a sane first layer:** 0.2 mm height at 100–120% width is forgiving; don't go below 0.15 mm until everything else is dialed in.
4. If one spot always scrapes while the rest is fine, that's a bed warp — a probe with mesh leveling (see Upgrades) compensates for it, or avoid that bed region for critical prints.
