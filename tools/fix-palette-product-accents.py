#!/usr/bin/env python3
"""Migrate the retired per-product badge gradients in products.js / products-es.js.

These 14 accent values per file still use the retired palette (indigo #6366f1,
cyan #06b6d4, the old pinks #ec4899 / #f472b6). Each rule carries an expected
match count so a stale rule fails loudly instead of silently doing nothing.

Green (#10b981) is KEPT, because it is the brand's positive colour and Luna
explicitly kept the green check. It is used only as the starting stop of the
approved gradient (green -> accent).
"""
import pathlib, sys

RULES = [
    ("linear-gradient(135deg,#f472b6,#ec4899)", "var(--bs-accent)", 1),
    ("linear-gradient(135deg,#10b981,#6366f1)", "linear-gradient(135deg,#10b981,var(--bs-accent))", 4),
    ("linear-gradient(135deg,rgba(99,102,241,0.2),rgba(236,72,153,0.2))", "rgba(255,45,149,0.16)", 1),
    ("linear-gradient(135deg,rgba(99,102,241,0.15),rgba(6,182,212,0.15))", "rgba(255,45,149,0.13)", 1),
    ("linear-gradient(135deg,rgba(16,185,129,0.2),rgba(6,182,212,0.2))", "rgba(255,45,149,0.16)", 1),
]

apply = "--apply" in sys.argv
base = pathlib.Path.home() / "websites" / "birkystudio-site" / "src" / "data"
files = [base / "products.js", base / "products-es.js"]

ok = True
for f in files:
    t = f.read_text(encoding="utf-8")
    for old, new, expect in RULES:
        n = t.count(old)
        if n != expect:
            print(f"  FAIL {f.name}: expected {expect} of {old!r} after prior rules, found {n}")
            ok = False
        t = t.replace(old, new)
    if ok and apply:
        f.write_text(t, encoding="utf-8")

print(f"{'APPLIED' if apply else 'DRY RUN'} across {len(files)} files")
if not ok:
    sys.exit(2)