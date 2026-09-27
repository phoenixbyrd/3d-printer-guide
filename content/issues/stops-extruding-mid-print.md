---
title: Stops extruding mid-print
category: Extrusion Problems
keywords: stops extruding, stops mid print, air printing, extrusion stopped halfway
check_first: Check whether the extruder gear is still turning against unmoving filament (jam/grind) or the filament snapped — each points to a different fix.
hw_sw: Hardware
---

## What it looks like

The print was going fine, then the nozzle starts moving with nothing coming out — "printing air." The part is incomplete from some layer upward.

## Causes

1. **Heat creep** — the most common mid-print stoppage. The heat break warms up over time, filament softens too high, and forms a plug. Prints fail at roughly the same height/time repeatedly.
2. **Filament tangle on the spool** — the spool binds, the extruder can't pull, filament strips or the extruder skips until it gives up.
3. **Filament runout sensor false trigger or actual runout.** (The SV01 has a runout sensor — check it's not triggering on a dusty sensor or a thin spot.)
4. **Extruder overheating** — the stepper driver overheats and shuts down intermittently, resuming later. Feels random.
5. **Partial clog that finally sealed**, or the PTFE liner deforming as the print went on.
6. **Slicer issue:** a corrupt model or bad G-code (rare — re-slice if nothing mechanical explains it).

## Fixes

1. If it always dies at a similar time in: **heat creep.** Verify the hotend fan runs at full speed whenever hot, reduce retraction, lower temp 5°C, and make sure the silicone sock is on (it keeps heat where it belongs).
2. **Unspool and rewind** the filament neatly; make sure the spool spins freely with no drag — direct-drive extruders are sensitive to spool resistance.
3. Check the runout sensor: clean it, verify the filament path through it is smooth.
4. Feel the extruder motor after a failure — if it's too hot to touch comfortably, improve cooling/airflow around the electronics.
5. Cold pull, check the PTFE liner, and re-slice the model if all else fails.
