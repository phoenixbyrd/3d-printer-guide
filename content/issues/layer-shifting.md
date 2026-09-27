---
title: Layer shifting — layers misaligned
category: Strength & Structure
keywords: layer shift, shifted layers, misaligned, skewed print, layers offset
check_first: Check belt tension and make sure nothing physically blocked the toolhead or bed mid-print. One big sudden shift = collision or skipped steps; gradual drift = loose mechanicals.
hw_sw: Mostly hardware (belts, pulleys, collisions)
---

## What it looks like

The print looks like a deck of cards that slid — one or more layers are offset sideways from the rest, sometimes dramatically, sometimes just a step.

## Causes

1. **Loose belts.** The #1 cause. A belt that can be deflected more than a few mm lets the motor turn without moving the axis exactly.
2. **Loose pulley grub screws.** The pulley spins on the motor shaft — mark the shaft and pulley with a marker line to catch this.
3. **Nozzle collision.** A curled overhang or blob caught the nozzle and the motors skipped steps. (Fix the underlying blob/curl too.)
4. **Printing too fast** with accelerations the motors can't follow, especially with the heavy direct-drive toolhead.
5. **Overheating stepper drivers** cutting out momentarily (feel the motors — burning hot is bad).
6. **Obstruction** — a cable, binder clip, or the spool holder physically blocking bed/toolhead travel.

## Fixes

1. **Tension belts** so they twang; tighten **pulley grub screws** (one must sit on the flat of the motor shaft).
2. Clear the full travel path of both axes — no clips, cables, or debris.
3. **Slow down** and reduce acceleration/jerk if shifts happen on direction-heavy prints.
4. Check for the collision source: curled corners (cooling), blobs (retraction) — layer shift is often a *symptom* of another issue.
5. Improve electronics cooling if drivers run hot; verify motor currents aren't set absurdly low in firmware.
