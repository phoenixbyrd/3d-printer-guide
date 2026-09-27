---
title: Clogged nozzle / hotend jam
category: Extrusion Problems
keywords: clogged, clog, jammed, jam, blocked nozzle, no extrusion, stuck filament
check_first: Heat to 10°C above normal, try pushing filament through by hand. If it won't go, do a cold pull before disassembling anything.
hw_sw: Hardware
---

## What it looks like

Little or nothing comes out of the nozzle. The extruder clicks or grinds, filament won't load, or extrusion starts fine then chokes off. Sometimes a thin curl of plastic emerges but no real flow.

## Causes

1. **Debris in the nozzle** — burnt filament, dust, or a contaminant from a cheap spool.
2. **Heat creep** — the heat break got too hot, filament softened too high up, and solidified into a plug (see Heat creep).
3. **Gap between nozzle and heat break / PTFE liner.** Molten plastic pools in the gap and hardens into a ring that blocks flow. This is the classic cause of *recurring* clogs.
4. **Printing too cold** for the speed — the melt zone can't keep up and pressure backs up.
5. **Retraction too long** on a direct drive, pulling molten plastic up into the cold zone where it solidifies.

## Fixes

1. **The needle first:** heat to printing temp +10°C and work the acupuncture needle (came with the printer) up through the nozzle tip.
2. **Cold pull (atomic pull):** heat to ~220°C for PLA, push filament in, cool to ~90°C, then yank it out firmly. Repeat until the pulled tip comes out clean and shaped like the nozzle interior.
3. **If clogs keep returning:** disassemble the hotend hot. Check the PTFE liner end is cut perfectly square and butts firmly against the nozzle — reseat with the nozzle tightened *at temperature* against the liner/heat break, not against the heater block.
4. **Reduce retraction** to 1–2 mm (direct drive) and verify the hotend fan runs whenever the hotend is hot.
5. **Last resort:** swap the nozzle. Brass nozzles are consumables — a $1 nozzle beats an hour of fighting a stubborn clog.
