---
title: Heat creep — jams that start after the first hour
category: Extrusion Problems
keywords: heat creep, jam after hours, progressive clogging, gets worse over time
check_first: Confirm the hotend fan spins at full speed whenever the nozzle is hot. A dead or slow fan is the #1 heat creep cause.
hw_sw: Hardware (cooling), sometimes slicer (retraction)
---

## What it looks like

Prints start perfectly and degrade over time — extrusion gets spotty, the extruder starts clicking an hour or two in, and eventually it jams completely. Short prints are fine; long prints always fail. The jammed filament, when pulled, has a thickened "mushroom" end above where the melt zone should be.

## Causes

1. **Hotend fan failing, slow, or wired wrong.** The fan must run at 100% whenever the hotend is above ~50°C. Even a fan at 70% can cause creep over hours.
2. **Excessive retraction** dragging molten plastic up into the heat break repeatedly, where it solidifies into a plug.
3. **High ambient temperature** (hot room, enclosure with PLA) reducing the temperature gradient the heat break needs.
4. **Missing or damaged silicone sock**, letting heat radiate onto the heat break area.
5. **Printing PLA too hot** (above ~220°C) increases the creep risk.

## Fixes

1. **Verify the hotend fan.** Watch it at print start — full blast, no hesitation. Replace it at the first sign of bearing noise or slow spin; it's a cheap part that causes expensive failures.
2. **Cut retraction** to 1 mm or less temporarily — if long prints suddenly succeed, retraction was contributing.
3. **Keep the silicone sock on** and intact.
4. Print at the cool end of the filament's good range (use your temperature tower result).
5. In hot rooms, point a small external fan at the printer's hotend area (not at the print — that causes warping).
