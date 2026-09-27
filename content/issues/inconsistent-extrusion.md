---
title: Inconsistent extrusion — lines vary in width
category: Extrusion Problems
keywords: inconsistent extrusion, varying line width, pulsing, uneven extrusion, wavy lines
check_first: Watch the extruder gear during a slow print — rhythmic variation points to the extruder/hotend, random variation points to filament or temperature.
hw_sw: Both
---

## What it looks like

Wall lines visibly swell and thin along their length, or the surface has a subtle pulsing texture. Not the regular pattern of ringing — this is irregular.

## Causes

1. **Temperature swinging** (bad PID tune) — plastic viscosity follows temperature directly.
2. **Partial clog** intermittently restricting flow.
3. **Filament diameter varying** along the spool (cheap filament) — measure several meters.
4. **Extruder gear slipping intermittently** — dust-packed teeth or marginal idler tension.
5. **Wet filament** — steam bubbles make extrusion sputter (listen for popping).
6. **Spool drag varying** as the spool rotates (tangled or tight-wound spool).

## Fixes

1. **PID tune** the hotend (M303 + M500) and watch the temp graph for flatness.
2. Cold pull to rule out a partial clog.
3. Measure filament diameter at several points; if it varies more than ±0.05 mm, the spool is the problem.
4. Clean the extruder gear, set idler tension, and make sure the spool unwinds freely.
5. Dry the spool if there's any popping or frosty texture.
