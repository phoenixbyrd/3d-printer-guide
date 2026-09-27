---
title: Over-extrusion — messy, blobby prints
category: Extrusion Problems
keywords: over extrusion, overextrusion, too much plastic, blobby, messy, fat lines
check_first: Lower flow rate 5% at a time, or re-run the single-wall flow calibration. Over-extrusion is almost always just too much plastic commanded.
hw_sw: Mostly slicer (flow rate, e-steps)
---

## What it looks like

Thick, messy lines, blobs at corners and layer starts, the nozzle dragging through excess plastic, dimensions oversized, fine details swallowed. The top surface looks lumpy instead of smooth.

## Causes

1. **Flow rate / extrusion multiplier too high** for this spool.
2. **E-steps calibrated too high** (or never calibrated — over-extrusion from the factory is common).
3. **Filament diameter set too small in the slicer** vs. reality (slicer thinks 1.70, spool is 1.78).
4. **Nozzle temperature too high**, making plastic runnier than the flow math assumes.

## Fixes

1. **Calibrate e-steps then flow** (Setup guide) — the single-wall cube method gives you the exact number for this spool.
2. **Measure filament diameter** and enter the true value.
3. **Drop temperature** 5°C if the plastic looks glossy and runny.
4. If only corners blob, that's a separate issue — see Blobs and zits (often retraction/coasting, not overall flow).
