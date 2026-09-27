---
title: Blobs and zits on the surface
category: Surface Quality
keywords: blobs, zits, bumps, pimples, dots on surface
check_first: These happen at layer starts/stops — tune retraction and enable wipe. If blobs sit exactly on the Z-seam line, align the seam to a corner first.
hw_sw: Mostly slicer
---

## What it looks like

Small round bumps scattered on the print's surface, often in a vertical line (that's the Z-seam) or at corners where the print head paused.

## Causes

1. **Pressure buildup released at layer change.** The extruder stops, pressure oozes a blob, then it starts the next layer.
2. **Retraction settings off** — too little retraction before the travel, or too slow a "retract on layer change."
3. **Z-seam placed randomly**, scattering the start/stop blobs across the surface instead of hiding them.
4. **Over-extrusion** making every imperfection bigger.
5. **Too-high temperature** increasing ooze.

## Fixes

1. **Align the Z-seam** to the sharpest corner or the back of the model (slicer: "seam position: aligned" / "rear").
2. **Tune retraction** (see Stringing) — blobs and strings share a root cause.
3. **Enable wipe** (nozzle wipes while retracting) and a small **coast** distance so pressure bleeds off before the layer ends.
4. **Lower temp 5°C** and verify flow isn't over 100%.
5. If blobs appear at the *same* spots as travel endpoints, "avoid crossing perimeters" helps keep ooze inside the part.
