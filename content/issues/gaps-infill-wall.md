---
title: Gaps between infill and walls
category: Strength & Structure
keywords: gaps between infill and outline, infill not touching walls, perimeter gap
check_first: Increase infill overlap to 20–30% and slow down. This is the slicer not quite joining two toolpaths — overlap and speed fix it.
hw_sw: Mostly slicer, sometimes under-extrusion
---

## What it looks like

A visible gap between the outer walls and where the infill meets them — you can see daylight between the perimeter and the interior on top layers or in cross-section.

## Causes

1. **Infill overlap too low** (default 10–15% sometimes isn't enough).
2. **Printing infill too fast** to bond to the wall.
3. **Under-extrusion** shrinking both toolpaths away from each other.
4. **Infill printed before walls** in some orders, with the wall laid over a gap.

## Fixes

1. **Raise infill/perimeter overlap** to 20–30%.
2. **Slow infill** and verify flow calibration.
3. Try printing **walls before infill** (slicer ordering option) so the infill butts into an existing wall.
4. Rule out general under-extrusion if gaps appear everywhere, not just at the wall junction.
