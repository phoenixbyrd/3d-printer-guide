---
title: Filament grinding / stripped filament
category: Extrusion Problems
keywords: grinding, stripped filament, chewed filament, extruder eating filament, dust in extruder
check_first: Loosen the extruder idler slightly and clear any partial clog — grinding means the gear is spinning against filament that isn't moving.
hw_sw: Hardware
---

## What it looks like

Plastic dust around the extruder gears, and a section of filament with a flat chewed spot where the gear dug in. Once stripped, the gear can't grip at all and extrusion stops.

## Causes

1. **Filament not moving but gear keeps turning** — the root is always downstream resistance: a clog, printing too cold, or nozzle too close.
2. **Idler tension too tight**, deforming the filament so it wedges in the path.
3. **Retraction-heavy prints** (lots of small moves) chewing one spot repeatedly.
4. **Worn extruder gear** with dull teeth.

## Fixes

1. **Fix the downstream blockage first** (see Clogged nozzle / Extruder clicking) — otherwise it'll grind again immediately.
2. Cut away the chewed section, reload fresh filament.
3. Set idler tension so the gear bites without flattening the filament.
4. Clean the gear teeth with a brass brush — packed dust reduces grip.
5. Reduce retraction count: enable "limit retractions per mm of filament" type settings if your slicer offers them.
