---
title: Under-extrusion — gaps, thin walls, weak prints
category: Extrusion Problems
keywords: under extrusion, underextrusion, gaps, thin walls, missing layers, weak print, sparse
check_first: Raise nozzle temp 5–10°C and check that e-steps are calibrated. Most under-extrusion is temperature, a partial clog, or uncalibrated e-steps.
hw_sw: Both — start with slicer/temp, then hardware (clogs, extruder)
---

## What it looks like

Gaps between perimeters and infill, visibly thin or broken wall lines, layers that don't quite touch, prints that feel light and crush easily. Infill looks sparse even at normal percentages.

## Causes

1. **Nozzle temperature too low.** The plastic can't melt fast enough to keep up — the most common cause.
2. **Partial clog.** Debris or heat-degraded filament narrowing the nozzle.
3. **E-steps not calibrated.** The extruder pushes less filament than commanded.
4. **Flow rate set too low** in the slicer for this spool.
5. **Printing too fast** for the hotend's melt capacity (volumetric flow limit exceeded).
6. **Filament diameter wrong in slicer** (e.g. 2.85 mm setting with 1.75 mm filament, or a spool that actually measures 1.68 mm).
7. **Extruder slipping** — weak idler tension, worn gear, or grinding (see those issues).
8. **Wet filament** can mimic under-extrusion with rough, inconsistent lines.

## Fixes

1. **Calibrate e-steps**, then **flow rate** (Setup guide) — do these once properly and rule them out forever.
2. **Raise temp 5–10°C** and/or **slow down** 20%. If it clears up, you were exceeding the hotend's melt rate.
3. **Measure your filament** in several spots with calipers; enter the real average in the slicer.
4. **Cold pull** to clear a partial clog (see Clogged nozzle).
5. Check extruder idler tension and gear cleanliness — tighten until the gear bites without deforming the filament.
6. Dry the spool if you hear popping or see frosty, rough extrusion.
