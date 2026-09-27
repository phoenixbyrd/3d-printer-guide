---
title: Heating errors — thermal runaway, mintemp, bed won't reach temp
category: Printer Errors
keywords: thermal runaway, heating failed, mintemp, maxtemp, thermal error, printer halted, bed not heating, nozzle not heating
check_first: STOP and inspect. Thermal runaway means the printer detected heating it couldn't control — check the thermistor and heater cartridge wiring before resetting and continuing.
hw_sw: Hardware — treat with respect, this is the fire-safety system working
---

## What it looks like

The printer halts mid-print (or on heatup) with an error: THERMAL RUNAWAY, HEATING FAILED, MINTEMP, or MAXTEMP. Or the bed/nozzle heats very slowly or never reaches the target.

## Causes

1. **Thermistor loose or damaged.** If the temp sensor isn't reading the real block temp, the printer either overheats blindly (dangerous — the firmware caught it) or reads wrong and errors out. MINTEMP usually means the thermistor circuit is open/broken; MAXTEMP means shorted.
2. **Heater cartridge failing** — heats slowly or not at all.
3. **Wiring break** where cables flex (bed cable chain area, hotend cable bundle). Intermittent errors that come and go with movement = broken wire.
4. **Part-cooling fan blasting the nozzle/block** (missing silicone sock + 100% fan on a cold day) can outpace the heater — "heating failed" on an otherwise fine printer.
5. **Bed won't reach high temps:** the stock bed draws a lot of power; 100°C for ABS is near its limit, worse in a cold room. Insulating under the bed helps.

## Fixes

1. **Power off and inspect.** Look at the thermistor (tiny glass bead in the heat block) — is it seated? Wires intact? Check the heater cartridge wires too. Do not bypass thermal runaway protection in firmware, ever.
2. **Wiggle test:** with the printer on but cold, gently flex the wire bundles while watching the temp display. Jumping readings = broken wire — replace the thermistor/cartridge (they're cheap; keep spares).
3. **Reseat or replace the thermistor**, making sure it's fully inserted and secured (not crushed — overtightening the screw breaks them).
4. Keep the **silicone sock on** the block and don't aim the part-cooling fan at the nozzle itself.
5. For slow beds: **insulate under the bed** (cork/foil foam), enclose drafts, and accept that 100°C takes a while — preheat the bed 10 minutes before the print.
6. If errors persist with new thermistor + cartridge, the board's MOSFET or ADC may be failing — board replacement time.
