---
title: Not extruding at the start of the print
category: Extrusion Problems
keywords: not extruding, no filament at start, prime, purge, skirt missing, first lines missing
check_first: Add a skirt or brim (3+ loops) and a purge line in your start G-code — the nozzle needs to prime before the real print starts.
hw_sw: Mostly slicer/start G-code
---

## What it looks like

The print head moves but nothing comes out for the first seconds or first lines. The skirt is patchy or missing, and the actual part starts with gaps. After a bit, plastic flows normally.

## Causes

1. **No priming.** Filament oozed out during heatup, leaving the nozzle empty when the print starts.
2. **Nozzle parked too long hot before starting**, oozing out the melt zone.
3. **Retraction at the end of the previous print** left the filament pulled back with nothing primed.
4. **Old/cold start:** the hotend wasn't fully up to temp when extrusion began.

## Fixes

1. **Add a skirt** (3 loops, 3–4 mm from the part) — it primes the nozzle and confirms bed level before the part starts.
2. **Add a purge line to start G-code** (see Setup guide) — a thick line at the bed edge that gets flow going.
3. **Preheat and wait** 1–2 minutes after reaching temp so the whole melt zone is stable.
4. Manually extrude 10–15 mm right before starting if your workflow allows.
5. If the problem persists past the first layer, it's not priming — see Under-extrusion or Clogged nozzle.
