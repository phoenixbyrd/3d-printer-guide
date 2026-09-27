---
title: Ringing / ghosting — ripples echoing from edges
category: Surface Quality
keywords: ringing, ghosting, ripples, echoes, vibration artifacts, wavy walls near corners
check_first: Slow down outer walls to 30–40 mm/s. If the ripples shrink, it's ringing (vibration) — then tighten belts and reduce acceleration.
hw_sw: Hardware (belts, frame) + slicer (speed/accel)
---

## What it looks like

Faint ripples on flat walls that echo the shape of a nearby corner, hole, or detail — like a reflection. They're perfectly regular and fade with distance from the feature.

## Causes

1. **Printer vibration.** The heavy direct-drive toolhead on the SV01 changes direction at a corner and the whole gantry rings like a bell. Loose belts make it worse.
2. **High acceleration / jerk** on direction changes.
3. **High outer-wall speed** giving the vibration more energy.
4. **Loose frame or wobbly table** amplifying the resonance.

## Fixes

1. **Slow the outer wall** to 30–40 mm/s — the single biggest lever, since visible walls are what matter.
2. **Tension X/Y belts** properly and check the frame bolts are snug.
3. **Reduce acceleration** (try 500–800 mm/s² for outer walls) and jerk settings.
4. **Stiffen the setup:** printer on a solid surface (not a wobbly table), consider a concrete paver under it to absorb vibration.
5. **Input shaping** (firmware feature, needs a 32-bit board upgrade on the SV01) cancels resonance in software — the advanced fix after mechanics are sound.
