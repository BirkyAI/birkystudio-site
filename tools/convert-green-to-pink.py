#!/usr/bin/env python3
"""Convert the green family to the single accent, Luna's call 28 Sep 2026.

Luna, answering the open question about green as a second colour: "Convert to pink."

Green stood for the positive/emphasis colour across about 10 files (stat cards, partner
payouts, tip callouts, portfolio badges and CTAs, product pills, links, progress bar,
success messages). The site is now one accent: neon pink.

Two things are deliberately NOT converted, and both are reported:
  1. the sanctioned gradient, green into pink, on the main buttons and the product CTA.
     Doc 5 permits green ONLY as the other end of that gradient, and it is the pair Luna
     has said she likes.
  2. the green check marks (the tick emoji in the comparison tables and the tick glyphs in
     the product lists). Luna explicitly asked for the check to stay, and a tick is a
     meaning-bearing marker, not a decorative colour.
Hero block icon colours are left alone too, on her separate instruction.

Idempotent-ish: protecting the sanctioned gradients first means a re-run converts nothing.
"""
import pathlib, re, sys, collections

SITE = pathlib.Path.home() / "websites" / "birkystudio-site" / "src"

# Sanctioned gradients, protected before the sweep so their green survives.
KEEP = [
    "linear-gradient(135deg, #10b981, #ff2d95)",
    "linear-gradient(135deg,#10b981,var(--bs-accent))",
]

TOKEN_MAP = [
    ("linear-gradient(135deg,#10b981,#059669)", "var(--bs-accent)"),
    ("linear-gradient(135deg,#10b981,#34d399)", "var(--bs-accent)"),
    ("rgba(16,185,129,0.04)", "rgba(255,45,149,0.04)"),
    ("rgba(16,185,129,0.05)", "rgba(255,45,149,0.05)"),
    ("rgba(16,185,129,0.08)", "rgba(255,45,149,0.07)"),
    ("rgba(5,150,105,0.05)", "rgba(255,45,149,0.05)"),
    ("rgba(5,150,105,0.15)", "rgba(255,45,149,0.15)"),
    ("rgba(16,185,129,0.1)", "rgba(255,45,149,0.08)"),
    ("rgba(16,185,129,0.15)", "rgba(255,45,149,0.14)"),
    ("rgba(16,185,129,0.2)", "rgba(255,45,149,0.22)"),
    ("rgba(16,185,129,0.25)", "rgba(255,45,149,0.28)"),
    ("rgba(16,185,129,0.3)", "rgba(255,45,149,0.3)"),
    ("rgba(16,185,129,0.4)", "rgba(255,45,149,0.4)"),
    ("rgba(16,185,129,0.45)", "rgba(255,45,149,0.45)"),
    ("#6ee7b7", "var(--bs-accent)"),
    ("#34d399", "var(--bs-accent)"),
    ("#059669", "var(--bs-accent)"),
    ("#10b981", "var(--bs-accent)"),
]

apply = "--apply" in sys.argv
files = [p for p in SITE.rglob("*")
         if p.suffix in (".astro", ".css", ".js") and p.name != "hero.css"]

counts = collections.Counter()
changed = 0
newtext = {}

for p in files:
    t = original = p.read_text(encoding="utf-8")
    for i, k in enumerate(KEEP):
        t = t.replace(k, f"@@KEEP{i}@@")
    for old, new in TOKEN_MAP:
        n = t.count(old)
        if n:
            counts[old] += n
            t = t.replace(old, new)
    for i, k in enumerate(KEEP):
        t = t.replace(f"@@KEEP{i}@@", k)
    if t != original:
        changed += 1
        newtext[p] = t

for old, n in counts.most_common():
    print(f"  {n:3d}  {old}")
print(f"total conversions: {sum(counts.values())} in {changed} file(s)")

if apply:
    for p, t in newtext.items():
        p.write_text(t, encoding="utf-8")
    print("APPLIED")
else:
    print("DRY RUN")