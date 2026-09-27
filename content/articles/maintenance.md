---
title: Maintenance Schedule
description: Daily, weekly, and monthly checklists to keep the Sovol SV01 printing reliably — cleaning, lubrication, belt checks, and wear parts.
---

Most "random" print failures are maintenance failures wearing a costume. A ten-minute routine prevents the majority of clogs, shifts, and adhesion mysteries.

## Every print (30 seconds)

- **Glance at the first layer.** Stay for the first 2–3 layers of any print. If it's not sticking or looks wrong, cancel now — filament is cheaper than a 9-hour spaghetti sculpture.
- **Clear the bed.** Remove all skirt/brim remnants and debris before starting. A stray blob under the next print's first layer ruins adhesion.

## Weekly (or every ~20 print hours)

- **Clean the bed.** Wash the glass with warm water and dish soap, rinse well, air dry. For quick touch-ups between washes, wipe with isopropyl alcohol (90%+). Touch the print surface as little as possible — finger oils kill adhesion.
- **Check belt tension.** X and Y belts should twang, not flap. If a belt has stretched, re-tension at the mounts.
- **Wiggle test.** With steppers engaged, grab the hotend carriage and the bed and try to rock them. Any play means an eccentric nut needs a quarter-turn.
- **Inspect the nozzle.** Look for plastic baked onto the outside (a sign of a gap between nozzle and heat break, or oozing from too-hot temps). Brass nozzles are wear items — if the tip looks rounded or prints have lost fine detail, swap it (they're cheap).
- **Check the extruder gear.** Open the extruder idler and look for ground-up filament dust in the gear teeth. Brush it out. Dust here means the gear is chewing — check idler tension and for partial clogs.
- **Fan check.** Both the hotend fan (always on) and part-cooling fan should spin freely and quietly. A dying hotend fan causes heat creep (see troubleshooting).

## Monthly (or every ~100 print hours)

- **Lubricate the Z lead screws.** Wipe them clean with a dry cloth first (old grease collects dust and becomes grinding paste), then apply a thin film of PTFE/silicone grease or light machine oil. **Dual Z on the SV01:** do both screws, then re-check that the gantry is level side to side.
- **Check all frame bolts.** Vibration loosens things. Go over the gantry bolts, bed knobs area, and spool holder with the Allen keys — snug, not gorilla-tight.
- **Inspect wiring.** Look for chafing where the bed cable flexes and where hotend wires pass the frame. Catching a worn wire beats a short.
- **Check the PTFE liner.** Even direct-drive hotends have a short PTFE tube inside. If you're getting mysterious jams with PLA, a heat-deformed liner is a suspect — it should be cut perfectly square and seated firmly against the nozzle.
- **Clean the lead screw brass nuts.** Brush out dust, re-lube lightly.

## Wear parts to keep on hand

These are cheap and will fail eventually. Having spares turns a week of downtime into a 15-minute fix:

- Brass nozzles, 0.4 mm (5-pack)
- One spare PTFE tube + tube cutter (or a pre-cut liner for the SV01 hotend)
- A spare thermistor and heater cartridge (wiring is the usual failure, not the part itself)
- Silicone socks for the hotend
- GT2 belt (a meter is plenty) and a couple of spare V-wheels

## What NOT to do

- Don't use WD-40 on lead screws or rails — it's a solvent, not a lubricant, and it strips existing grease.
- Don't overtighten the nozzle cold and then heat it — always do the final nozzle snug at printing temperature, holding the heat block with a wrench so you don't snap the heat break.
- Don't oil the V-wheels themselves — they ride dry on the extrusion. Oil attracts dust and makes them slip.
