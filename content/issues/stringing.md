---
title: Stringing / oozing — fine hairs between parts
category: Surface Quality
keywords: stringing, strings, hairs, wisps, oozing, spiderweb, spider web, cobweb
check_first: Print a retraction tower. On the SV01's direct drive, start around 1.5 mm at 30 mm/s and 5°C cooler — stringing is retraction + temperature + moisture, in that order.
hw_sw: Mostly slicer (retraction/temp), sometimes material (wet filament)
---

## What it looks like

Fine hair-like strands stretching between separate parts of the print, like spiderwebs. The surfaces themselves may be fine — the problem is only in the travel gaps.

## Causes

1. **Retraction too short or too slow.** The most common cause. (But on direct drive, "too short" means under ~1 mm — don't use Bowden values.)
2. **Nozzle too hot.** Hotter plastic oozes more during travels.
3. **Wet filament.** Moisture turns to steam and pushes plastic out during travels — stringing that won't tune away is often wetness.
4. **Travel speed too slow**, giving ooze more time to happen.
5. **Worn nozzle** with an enlarged or rough orifice oozes more.

## Fixes

1. **Print a retraction tower** varying distance (0.5–3 mm) and pick the cleanest. Then fine-tune speed (25–40 mm/s).
2. **Drop temperature 5°C** at a time — use the coolest temp that still gives good layer adhesion (from your temp tower).
3. **Dry the filament** if stringing resists tuning.
4. **Increase travel speed** (150 mm/s is reasonable on the SV01) and enable "avoid crossing perimeters" / combing settings so travels stay inside the part.
5. **Wipe/coast:** a small wipe distance or coasting can clean up the last wisps — but fix retraction and temp first.
6. Replace the nozzle if it's old — a fresh 0.4 mm brass nozzle strings less than a worn one.
