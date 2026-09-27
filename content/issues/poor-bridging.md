---
title: Poor bridging — sagging strands across gaps
category: Strength & Structure
keywords: bridging, sagging bridges, droopy bridges, strands sagging
check_first: Slow bridges to 20–25 mm/s with 100% fan. Bridging is the one move where slow + cold + full air is always right.
hw_sw: Mostly slicer
---

## What it looks like

Strands spanning a gap droop, sag, or break instead of pulling straight across. Undersides of bridges look stringy.

## Causes

1. **Bridging too fast** — the strand needs to be pulled taut, not laid.
2. **Insufficient cooling** — the strand must freeze mid-air.
3. **Too hot** — runny plastic can't span.
4. **Gap too long** for the material (over ~30–40 mm even good bridging struggles).
5. **Under-extrusion** leaving strands too thin to span.

## Fixes

1. **Bridge speed 20–25 mm/s, fan 100%**, and use the cool end of the filament's range.
2. Enable the slicer's **bridge settings** (thicker bridge lines, slower bridge infill).
3. Verify flow — thin strands can't bridge.
4. For very long spans, redesign with a chamfer or add a sacrificial support — physics has limits.
5. Print a bridging test to dial in the exact settings for your spool.
