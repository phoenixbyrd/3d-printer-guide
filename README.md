# 3D Printer Troubleshooting Guide

A comprehensive, searchable, mobile-friendly troubleshooting and operations guide for FDM 3D printers — built around the Sovol SV01, useful for any FDM printer.

**Live site:** https://phoenixbyrd.github.io/3d-printer-guide/

## Contents

- 34 symptom-first troubleshooting issues (first layer & adhesion, extrusion, surface quality, strength & structure, printer errors)
- Setup & calibration (bed leveling, Z-offset, e-steps, flow, PID, temperature/retraction towers)
- Filament guide (PLA, PETG, ABS/ASA, TPU, storage/drying)
- Maintenance schedule (daily/weekly/monthly)
- SV01 upgrades: worth it vs. skip it
- Sources & credits

## Building

Content lives in `content/` as Markdown (issues in `content/issues/`, articles in `content/articles/`). Static assets in `static/`.

```bash
python3 build.py   # generates docs/
```

`docs/` is the GitHub Pages source. Client-side search runs off `docs/search.json` — no server needed.

## Editing

Edit the Markdown, re-run `build.py`, commit, push. Pages redeploys automatically.
