---
title: Visible Z-seam line
category: Surface Quality
keywords: z seam, seam line, vertical line, layer start line
check_first: Set the seam to "aligned" and put it on the sharpest corner or the back of the model. A seam is unavoidable — the goal is hiding it.
hw_sw: Slicer
---

## What it looks like

A faint vertical line or row of tiny bumps running up the print where each layer started and stopped.

## Causes

1. **Every layer has a start/stop point** — a tiny imperfection there is physically unavoidable.
2. **Seam set to "random"**, scattering the marks across the whole surface.
3. **Retraction/wipe not tuned**, making each seam point blob.

## Fixes

1. **Seam position: aligned** (or "rear") so all layer starts stack in one line, placed on the least visible face or sharpest corner.
2. **"Smart hiding" / "nearest"** seam modes in modern slicers tuck it into concave corners automatically.
3. Tune retraction + wipe + coast so each start point is as clean as possible (see Blobs and zits).
4. For display pieces, plan light sanding on the seam line — 5 minutes with fine sandpaper erases it.
