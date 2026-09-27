---
title: Spaghetti — print detached mid-print (bird's nest)
category: First Layer & Bed Adhesion
keywords: spaghetti, bird nest, birdnest, detached, knocked off, print failed halfway, stringy mess, air printing
check_first: It's an adhesion failure until proven otherwise — clean and re-level the bed, add a brim, and slow down. Then check for nozzle collisions.
hw_sw: Mostly adhesion/setup; sometimes slicer (no Z-hop, supports failing)
---

## What it looks like

You come back to a tangle of loose filament strands — the print detached from the bed partway through and the nozzle kept extruding into thin air. Sometimes there's a half-printed part lying loose in the mess.

## Causes

1. **Adhesion gave up mid-print.** The first layer held weakly, then shrinkage, a tall part's leverage, or vibration worked it loose hours in.
2. **Nozzle collided with the print.** A curled-over overhang, a blob, or a warped corner sticks up; the nozzle catches it and knocks the part off. Tall thin parts are most vulnerable.
3. **Supports failed.** A support tower detached, then the nozzle dragged the whole thing around.
4. **Filament ran out / extruder jammed**, then the nozzle (printing nothing) still knocked the part loose — less common, check the extruder too.
5. **Excessive speed / acceleration** shaking a marginally-adhered part loose.

## Fixes

1. **Fix adhesion properly** (see "First layer won't stick"): clean bed, hot level, correct Z gap, brim on anything tall or small-footprint.
2. **Enable a small Z-hop** (0.2–0.4 mm) so the nozzle lifts over already-printed plastic on travel moves.
3. **Check for the collision source:** look at where the failure started — a curled overhang means cooling/speed issues; a blob means retraction/temp issues. Fix that and the spaghetti stops.
4. **Slow down** outer walls and enable "avoid printed parts on travel" if your slicer offers it.
5. **For tall thin parts:** brim is mandatory, consider printing slower, and make sure the part-cooling fan isn't blasting one side (uneven cooling warps tall parts into the nozzle path).
