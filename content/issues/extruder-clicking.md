---
title: Extruder clicking / skipping steps
category: Extrusion Problems
keywords: clicking, skipping, extruder skipping, thunk, knocking sound, stepper skipping
check_first: Raise the nozzle temp 5–10°C. Clicking is the extruder motor stalling against backpressure — usually the plastic isn't melting fast enough.
hw_sw: Hardware symptom, often slicer/temp cause
---

## What it looks like

A rhythmic *thunk-thunk* from the extruder, sometimes with the extruder gear visibly jumping backward. Print shows under-extrusion or gaps corresponding to the skips.

## Causes

1. **Temperature too low** for the speed/material — the #1 cause.
2. **Partial clog** creating backpressure.
3. **Printing too fast** — exceeding the hotend's volumetric melt rate.
4. **Nozzle too close to the bed** on the first layer — nowhere for plastic to go.
5. **Idler tension wrong** — too loose slips, too tight deforms filament and increases friction.
6. **Retraction too aggressive** chewing the filament so the gear can't grip.
7. **Heat creep** softening filament above the melt zone, increasing friction.

## Fixes

1. **Raise temp 5–10°C** and/or **slow down 20%**. If clicking stops, you found it.
2. On the first layer only? Raise Z slightly — the nozzle is too close.
3. **Clear any partial clog** (cold pull).
4. Adjust idler tension: tight enough that the gear teeth bite visibly but the filament isn't flattened.
5. Reduce retraction distance/speed to sane direct-drive values (1–2 mm, 25–40 mm/s).
6. Verify the hotend fan is running — heat creep causes progressive clicking that gets worse over time.
