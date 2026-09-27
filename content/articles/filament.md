---
title: Filament Guide
description: PLA, PETG, ABS/ASA, and TPU on the Sovol SV01 — temperatures, bed temps, enclosure needs, gotchas, storage and drying.
---

## Quick reference

| Filament | Nozzle | Bed | Fan | Enclosure | Notes |
|---|---|---|---|---|---|
| PLA | 200–220°C | 60°C | 100% | No | Easiest. Start here. |
| PLA+ / Tough PLA | 205–225°C | 60°C | 100% | No | Stronger, slightly hotter. |
| PETG | 230–250°C | 80–90°C | 30–50% | Helpful | Sticky — use glue stick on glass as a *release* agent. |
| TPU (95A) | 220–240°C | 50–60°C | 50–100% | No | Print slow (20–30 mm/s). Direct drive shines here. |
| ABS | 240–260°C | 100–110°C | 0–25% | Strongly recommended | Warps badly in drafts. SV01 is open-frame — hard mode. |
| ASA | 240–260°C | 100–110°C | 0–25% | Strongly recommended | Like ABS but UV-stable. Same warping battle. |

**Hard limits of the SV01:** 250°C max nozzle and 100°C max bed (per spec). That rules out polycarbonate, nylon (needs 250–270°C+ and a dry box), and anything exotic. Stick to the table above.

Always run a temperature tower for each new spool — the ranges above are starting points, and brands vary by ±10°C.

## PLA — the default

PLA is forgiving, odorless, and needs no enclosure. It is also brittle (thin parts snap) and softens around 55–60°C, so don't use it for car parts or anything near heat. On the SV01's glass bed, 60°C with a clean bed usually sticks perfectly and releases when cool. If PLA pops and crackles while printing, it's wet — dry it (see below).

## PETG — strong and a little fussy

PETG is tougher than PLA and handles ~80°C, great for functional parts. Its quirks:

- **It bonds to glass permanently.** Always put down glue stick (or blue tape) on the SV01's glass bed as a release layer, or you'll chip the glass prying a part off.
- **It oozes and strings.** Dry the spool, lower temp to the cool end of the range, and increase retraction slightly vs your PLA value.
- **First layer:** print it a touch higher (bigger Z gap) than PLA — squishing PETG too hard makes a mess that welds to the nozzle.
- **Cooling:** 30–50% fan. Full fan makes layer adhesion worse; no fan makes overhangs droop.

## ABS / ASA — experts only on an open printer

ABS warps because it shrinks as it cools, and any draft makes it worse. The SV01 has no enclosure, so ABS is genuinely difficult: expect curled corners and split layers unless you build or buy an enclosure (even a large cardboard box or a cheap tent enclosure helps enormously). If you try it: 100–110°C bed, brim or raft, zero part cooling for the first layers, and keep the room warm and draft-free. ASA behaves the same but survives sunlight — the right pick for outdoor parts.

**Safety:** ABS/ASA fumes (styrene) are unpleasant. Ventilate the room or vent the enclosure outside.

## TPU — the direct-drive payoff

Bowden printers fight flexible filament; the SV01's direct drive extruder eats it for breakfast. Still, respect the rules:

- Print **slow**: 20–30 mm/s for 95A TPU. Speed is the #1 cause of TPU jams.
- **Minimal retraction**: 0.5–1.0 mm. Long retractions with soft filament cause jams above the heat break.
- Disable or minimize Z-hop. Keep the filament path constrained — no gaps for the soft filament to buckle into.
- Softer TPUs (85A and below) are much harder; 95A is the sweet spot for a stock extruder.

## Wet filament: the invisible problem

Filament absorbs moisture from the air — PLA in weeks, PETG and TPU in days, nylon in hours. Symptoms: popping/crackling sounds while printing, rough frosty surfaces, stringing that won't tune away, weak layer bonds, brittle PLA that snaps when you bend it.

**Fix:** dry the spool. A food dehydrator or a dedicated filament dryer at 50–60°C for 4–6 hours (check the filament's max — don't melt PLA at 70°C+). The print-during-drying dryers that feed the printer directly are the convenient endgame.

**Storage:** fresh spools go into sealed bags or bins with desiccant. Toss a cheap hygrometer in the bin — if it reads over ~30% RH, recharge or replace the desiccant. For humid climates (or if you print PETG/TPU often), a dry box you print *from* is worth building: a sealed tub with a desiccant and a PTFE tube outlet.

## Nozzle compatibility

Brass nozzles (stock) are fine for PLA, PETG, TPU, ABS. **Abrasive filaments** — glow-in-the-dark, carbon fiber, glass fiber, wood-fill, marble — will chew through a brass nozzle in a single print, widening it and ruining tolerances. Use a hardened steel nozzle for those (and bump temps ~5–10°C since steel conducts heat worse).
