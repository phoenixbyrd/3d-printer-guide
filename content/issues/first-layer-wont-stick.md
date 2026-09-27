---
title: First layer won't stick to the bed
category: First Layer & Bed Adhesion
keywords: not sticking, adhesion, first layer, bed adhesion, peeling, lifting, won't adhere
check_first: Clean the bed with dish soap and water, then re-level hot with the paper method. A dirty bed and a too-high nozzle cause the vast majority of adhesion failures.
hw_sw: Mostly hardware/setup (leveling, cleanliness), sometimes slicer (first-layer speed/temp)
---

## What it looks like

The nozzle lays down plastic but it curls up, drags around, or peels off the bed instead of staying put. Sometimes the first layer looks fine for a few lines then lifts. The print fails within the first few minutes, often turning into a blob on the nozzle.

## Causes

1. **Nozzle too far from the bed.** The single most common cause. If the first layer lines don't squash together and you can see gaps between them, the Z gap is too large.
2. **Dirty bed.** Finger oils, dust, and old adhesive residue kill adhesion on glass. Even a bed that "looks clean" often isn't.
3. **Bed not level.** One corner sticks while the opposite corner fails — classic unlevel bed.
4. **Bed too cool.** PLA below ~55°C or printing on a bed that hasn't heat-soaked won't grip. The sensor reads the heater, not the glass surface — give it 5 minutes after reaching temp.
5. **First layer printed too fast.** 60 mm/s on layer one is asking for trouble.
6. **Wrong surface for the material.** Bare glass + PETG can bond permanently; textured PEI + PLA usually just works.
7. **Drafts / cold room.** A vent or open window chilling the bed edge causes localized lifting.

## Fixes

1. **Wash the bed.** Warm water + dish soap, rinse thoroughly, air dry. Handle by the edges afterward. This alone fixes a shocking number of "adhesion problems."
2. **Re-level hot.** Heat bed to 60°C and nozzle to 200°C, then do the paper method at all four corners twice. See the Setup guide.
3. **Lower the Z gap.** Live-adjust (babystep) Z down during a first-layer test until the extruded lines merge into a smooth sheet with no gaps.
4. **Slow the first layer** to 20 mm/s and raise first-layer line width to 120% in the slicer.
5. **Raise bed temp** 5–10°C and let it soak 5 minutes before starting.
6. **Use adhesion helpers for difficult prints:** a brim (8–10 mm) for small footprints, glue stick on glass for PETG (as a release agent) or for extra PLA grip, blue painter's tape as a reliable textured surface.
7. **Kill the draft.** Close the window, move the printer away from the vent. For ABS/ASA, this means an enclosure — see the Filament guide.
