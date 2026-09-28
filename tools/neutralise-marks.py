#!/usr/bin/env python3
"""Neutralise comparison-table status marks in birkystudio-site.

- "Pros"/"Cons" headings: drop the emoji entirely (symmetric, toned down).
- Warn triangle (caveat/partial) -> soft grey cross.
- Red cross (not available)    -> white cross.
- Green check stays untouched (meaningful, user-approved).
Idempotent: safe to re-run.
"""
import pathlib, re, sys

ROOT = pathlib.Path.home() / "websites" / "birkystudio-site" / "src"
WARN = "\u26a0\ufe0f"   # ⚠️
CROSS = "\u274c"        # ❌
NEW = "\u2715"          # ✕
SOFT = '<span class="mark-soft">\u2715</span>'

changed_files, n_head, n_warn, n_cross = 0, 0, 0, 0

for p in sorted(ROOT.rglob("*")):
    if p.suffix not in (".astro", ".md", ".mdx"):
        continue
    txt = p.read_text(encoding="utf-8")
    orig = txt

    # 1. headings first so their emoji does not become a cross
    txt, a = re.subn(rf"{WARN}\s+Pros\b", "Pros", txt)
    txt, b = re.subn(rf"{WARN}\s+Cons\b", "Cons", txt)
    txt, c = re.subn(rf"\u2705\s+Pros\b", "Pros", txt)
    txt, d = re.subn(rf"\u2705\s+Cons\b", "Cons", txt)
    n_head += a + b + c + d

    # 2. remaining caveat triangles -> soft grey cross
    txt, e = re.subn(WARN, SOFT, txt)
    n_warn += e

    # 3. remaining red crosses -> white cross
    txt, f = re.subn(CROSS, NEW, txt)
    n_cross += f

    if txt != orig:
        p.write_text(txt, encoding="utf-8")
        changed_files += 1

print(f"files changed: {changed_files}")
print(f"headings normalised: {n_head}")
print(f"caveat triangles -> grey cross: {n_warn}")
print(f"red crosses -> white cross: {n_cross}")