---
title: Setup & Calibration
description: From unboxing to first perfect print on the Sovol SV01 — assembly checks, bed leveling, Z-offset, e-steps, flow, PID, temperature and retraction tuning.
---

## Unboxing & assembly checks

The SV01 arrives mostly assembled: the gantry bolts to the base with four long Allen screws, then you mount the screen, spool holder, filament sensor, and Z endstop. Before your first print:

- **Square the frame.** With the gantry loosely bolted, stand the printer on a flat table and make sure both Z uprights sit flat and the X gantry is level (measure from the gantry to the base on both sides). Tighten in a star pattern.
- **Check the eccentric nuts.** The V-wheels on the X carriage, both Z carriages, and the bed should roll without wobble but not be cranked down. Spin each wheel with a finger — it should turn with slight resistance, not spin freely or lock up.
- **Belt tension.** X and Y belts should twang like a low guitar string, not flap. The SV01 uses fixed mounts with tensioners — snug, not stretched.
- **Dual Z sync.** Both Z lead screws should start at the same height. Manually turn one coupler until the X gantry is level side to side (measure from gantry to frame on each side), then never grab just one side again.
- **Wiring check.** Make sure the hotend wires, thermistor wires, and bed wires have slack at full travel and nothing rubs the lead screws. The bed cable should have a strain-relief loop.
- **Voltage selector.** Confirm the red voltage switch on the MeanWell PSU matches your mains (115V in the US) before first power-on.

## Slicer setup

No built-in SV01 profile ships in most slicers, so add it as a custom printer:

**Machine settings (all slicers):** X 280, Y 240, Z 300 mm. Nozzle 0.4 mm, filament 1.75 mm. Heated bed enabled. G-code flavor: Marlin.

- **Cura:** Settings → Printer → Add → Custom FFF printer. Name it "Sovol SV01", enter the dimensions above. Start G-code (after heatup): `G28` (home all), then a purge line. A common purge: `G1 Z2.0 F3000`, `G1 X10 Y20 Z0.3 F1500`, `G92 E0`, `G1 X10 Y200 E15 F500`, `G92 E0`. Profiles also floated around the Sovol Facebook user group and the SD card that shipped with early units — usable as a starting point, but verify temperatures.
- **PrusaSlicer / SuperSlicer:** Configuration → Printer Settings → Custom. Same dimensions. Note: early Sovol manuals had the X/Y dimensions swapped (280/240) — the correct order is **X 280, Y 240, Z 300**.
- **OrcaSlicer:** No built-in SV01 profile (as of 2026). Create a custom printer with the same dimensions, or import a community profile from the Sovol user groups and sanity-check it before printing.

**Sensible starting profile (PLA, 0.4 mm nozzle):** 0.2 mm layer height, 3 walls, 4 top/bottom layers, 15–20% infill, print speed 50 mm/s, first layer 20 mm/s, nozzle 200–210°C, bed 60°C, fan 100% after layer 2, retraction 1.5 mm at 30 mm/s (direct drive — tune this, don't copy Bowden values).

## Bed leveling (manual, the paper method)

The SV01 has no stock probe — four knobs under a glass bed. Do this with the bed and nozzle at printing temperature (heat soaks the bed; a "cold level" lies to you).

1. Home all axes, then disable steppers (or use the menu to move the nozzle manually).
2. Slide a standard sheet of paper under the nozzle at the front-left corner. Adjust the knob until you feel light, even drag — the paper moves but you feel the nozzle gripping it.
3. Repeat at front-right, back-right, back-left. Then repeat the whole loop at least twice — adjusting one corner changes the others.
4. Finish with a center check. If the center drags differently than the corners, your glass may have a slight bow; a small Z-offset tweak or a mesh (with an added probe, see upgrades) handles it.

**Live-Z fine tuning:** Print a large single-layer square (a "first layer test"). While it prints, babystep Z down until the lines merge into a smooth sheet with no gaps between them, but stop before the nozzle plows ridges. The finished square should be smooth, uniform, and hard to peel apart.

## E-steps calibration

This fixes under/over-extrusion at the source. Heat the nozzle to your normal PLA temp.

1. Send `M503` and note the current `M92 E` value (or check Configuration → Advanced on the LCD).
2. Mark the filament 120 mm above the extruder entry with tape or a marker.
3. Command 100 mm of extrusion (`G1 E100 F100`, or use the LCD: Move → Extruder → 100 mm).
4. Measure from the extruder entry to your mark. If exactly 20 mm remains, you're perfect. Otherwise: `new E-steps = old E-steps × 100 / actually extruded`.
5. Set with `M92 E<new value>`, then `M500` to save. Re-test to confirm.

Do this once per extruder hardware change — not per filament. Flow rate (below) is the per-filament tweak.

## Flow rate (extrusion multiplier)

1. Print a 20 mm hollow cube in **vase mode** (spiralize, 1 wall, no top, no infill).
2. Measure the wall thickness in several spots with calipers and average.
3. `new flow % = old flow % × (nozzle diameter / measured thickness)`. Example: 0.4 mm nozzle, measured 0.44 mm at 100% flow → set 91%.
4. Set it in the slicer filament profile (not firmware), since it varies slightly per spool.

## PID tuning

If your nozzle or bed temperature swings more than ±2°C on the graph, tune PID. Send over USB (Pronterface, OctoPrint terminal) or use the LCD if the firmware menu exposes it:

- Hotend: `M303 E0 S200 C8` (8 cycles at 200°C — use your normal PLA temp)
- Bed: `M303 E-1 S60 C8`
- Save: `M500`

Re-tune after changing the hotend, fans, sock, or firmware.

## Temperature tower

Every spool is different. Print a temperature tower (Teaching Tech's calibration site generates the G-code for you: search "Teaching Tech calibration") ranging ~10°C above to ~10°C below the filament's rated range. Pick the lowest temperature that still gives clean bridges, no stringing, and strong layer adhesion. Write it on the spool with a marker.

## Retraction tuning (direct drive!)

The SV01's Titan-style direct drive needs **much less** retraction than Bowden printers. Bowden values (4–6 mm) will jam a direct drive. Start at **1.0–2.0 mm distance, 25–40 mm/s speed**, then print a retraction tower:

- Too little → stringing and oozing between parts.
- Too much → clogs, gaps at layer starts, extruder clicking.
- Also enable "retract on layer change" off for testing, and keep Z-hop small (0.2 mm) or off — big Z-hop causes blobs.

A widely reported sweet spot for the stock SV01 hotend is around 1.5 mm at 30 mm/s, but verify on your machine — every hotend is a little different.

## First-print checklist

1. Bed leveled hot, first-layer test square looks smooth.
2. E-steps verified, flow calibrated for this spool.
3. Temperature tower done, temp written on spool.
4. Retraction tower done, no stringing.
5. Print a 20 mm calibration cube: measure X/Y/Z — all should be within ±0.1 mm. If not, check belt tension and flow before touching step values.
6. Print something fun. A benchy is traditional — and genuinely useful as a benchmark you can compare against later.
