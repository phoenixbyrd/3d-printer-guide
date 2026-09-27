---
title: Scars and drag marks on the top surface
category: Surface Quality
keywords: scars, drag marks, nozzle drag, combing scars, lines on top
check_first: Enable Z-hop (0.2 mm) and check "avoid crossing perimeters." Scars are the nozzle traveling through already-printed plastic.
hw_sw: Mostly slicer
---

## What it looks like

Visible lines or gouges dragged across the top surface where the nozzle traveled between print areas, sometimes with a little blob at the end of the scar.

## Causes

1. **No Z-hop** — the nozzle drags at layer height across the print on travel moves.
2. **Combing/travel within the part** dragging the nozzle over top surfaces.
3. **Over-extrusion** leaving the surface slightly proud so the nozzle catches it.
4. **Slight over-squish on top layers** (too many top layers over extruding).

## Fixes

1. **Enable Z-hop** 0.2–0.4 mm (small — big hops cause blobs and stringing).
2. **"Avoid crossing perimeters"** / combing set to keep travels inside infill, not across top surfaces.
3. Verify flow calibration — a correctly extruded top surface sits *below* the nozzle path.
4. **Ironing** (slicer feature) can erase minor scarring on flat top surfaces as a finishing pass.
