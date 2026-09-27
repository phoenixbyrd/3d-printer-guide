---
title: Visible lines on the sides — Z-banding / inconsistent layers
category: Surface Quality
keywords: z banding, banding, layer lines, horizontal lines, inconsistent layers, ribbed sides
check_first: Check that both Z lead screws are clean, lubed, and at the same height. Regularly-spaced bands = mechanical Z issue; irregular = temperature or extrusion.
hw_sw: Mostly hardware (Z axis), sometimes slicer/temp
---

## What it looks like

Horizontal bands or ridges repeating up the sides of the print. If the spacing matches the lead screw pitch (regular, repeating), it's mechanical. If irregular, it's extrusion/temperature variation.

## Causes

1. **Z lead screw issues** — bent screw, debris in the threads, dry screws, or the brass nut binding. The SV01's dual Z means *both* screws must move freely and stay synchronized.
2. **Gantry not level** — one Z side higher than the other, so layers wedge.
3. **Temperature fluctuation** (bad PID) changing flow layer to layer.
4. **Inconsistent extrusion** from a partial clog or varying filament diameter.
5. **Over-tightened lead screw couplers** or misaligned Z motors causing binding.

## Fixes

1. **Clean and lubricate both Z screws** (wipe old grease off first), then re-level the gantry side to side.
2. Check the lead screws for visible bends by rolling them on a flat surface; check couplers are snug but not crushing.
3. **PID tune** the hotend to rule out temperature swing.
4. Make sure the X gantry moves smoothly by hand (power off) through the full Z range — any tight spot is a binding point.
5. Rule out extrusion causes via the Inconsistent extrusion guide.
