#!/usr/bin/env python3
"""
Migrate the old site palette to the Doc 5 single-accent palette.

Luna, 27 Sep 2026: "I would like the whole website to be like the top
section with the grid. On all pages." That means one page colour, one
accent, no indigo / cyan / slate bands left over from the old theme.

Order matters and each rule is property-aware, because the SAME hex can be
a surface in one place and text in another (example: #0f172a is a navy
panel on one page and article body text on the blog).

Deliberately KEPT brand colours: #10b981 (green), #f472b6 (pink),
#25d366 (WhatsApp green), #ef4444/#eab308 (traffic-light dots).
hero.css is skipped, it is already on palette.

Usage: python3 tools/migrate-palette.py [--apply]
"""
import re
import sys
import pathlib

ROOT = pathlib.Path("/Users/macminim4/websites/birkystudio-site")
APPLY = "--apply" in sys.argv
SKIP_NAMES = {"hero.css"}

# 1. surface hexes -> raised panel
SURFACE = {
    "0f172a", "1e1b4b", "312e81", "1e293b", "1e1e2e", "1e1e30", "151520",
    "0a1628", "0d2818", "1a3a2a", "111827", "1f2937", "f8fafc",
}
SURFACE_NAMED = {"white", "#fff", "#ffffff"}
SURFACE_TO = "var(--bs-bg-raised)"

# 2. text hexes -> palette text token
TEXT_MAP = {
    "cbd5e1": "var(--bs-text)",
    "e2e8f0": "var(--bs-text)",
    "f8fafc": "var(--bs-text)",
    "0f172a": "var(--bs-text)",
    "1e293b": "var(--bs-text)",
    "1e1b4b": "var(--bs-text)",
    "312e81": "var(--bs-text)",
    "065f46": "var(--bs-text)",
    "111827": "var(--bs-text)",
    "1f2937": "var(--bs-text)",
    "94a3b8": "var(--bs-text-muted)",
    "64748b": "var(--bs-text-muted)",
    "475569": "var(--bs-text-muted)",
    "334155": "var(--bs-text-muted)",
}

# 3. everything else (borders, gradient stops, shadows, icons)
FLAT = {
    "818cf8": "var(--bs-accent)",
    "a5b4fc": "var(--bs-accent)",
    "6366f1": "var(--bs-accent)",
    "4f46e5": "var(--bs-accent)",
    "8b5cf6": "var(--bs-accent)",
    "7c3aed": "var(--bs-accent)",
    "ec4899": "var(--bs-accent)",
    "06b6d4": "var(--bs-accent)",
    "22d3ee": "var(--bs-accent)",
}
for h in SURFACE:
    FLAT.setdefault(h, SURFACE_TO)

RGBA_MAP = [
    (r"rgba\(\s*99\s*,\s*102\s*,\s*241\s*,", "rgba(255,45,149,"),
    (r"rgba\(\s*129\s*,\s*140\s*,\s*248\s*,", "rgba(255,45,149,"),
    (r"rgba\(\s*236\s*,\s*72\s*,\s*153\s*,", "rgba(255,45,149,"),
    (r"rgba\(\s*79\s*,\s*70\s*,\s*229\s*,", "rgba(255,45,149,"),
]

files = []
for sub in ("src/pages", "src/components", "src/layouts", "src/styles"):
    d = ROOT / sub
    if d.exists():
        files += [p for p in d.rglob("*")
                  if p.suffix in {".astro", ".css", ".js", ".ts"} and p.name not in SKIP_NAMES]

counts = {}


def bump(kind, key, n=1):
    counts[(kind, key)] = counts.get((kind, key), 0) + n


for path in sorted(files):
    txt = path.read_text()
    original = txt

    # 1. surfaces: background / background-color
    def bg_repl(m):
        prop, val = m.group(1), m.group(2).strip().lower()
        key = val.lstrip("#")
        if val in SURFACE_NAMED or key in SURFACE:
            bump("surface", val)
            return f"{prop}:{SURFACE_TO}"
        return m.group(0)

    txt = re.sub(r"\b(background(?:-color)?)\s*:\s*(#[0-9a-fA-F]{3,6}|white)\b", bg_repl, txt)

    # 2. light borders -> palette border
    txt, n = re.subn(r"(border(?:-[a-z]+)?\s*:\s*[^;\"']*?)#e2e8f0",
                     lambda m: m.group(1) + "var(--bs-border)", txt)
    if n:
        bump("border", "e2e8f0", n)

    # 3. text colours -> palette text tokens
    def color_repl(m):
        prop, hexv = m.group(1), m.group(2).lower()
        if hexv in TEXT_MAP:
            bump("text", hexv)
            return f"{prop}:{TEXT_MAP[hexv]}"
        return m.group(0)

    txt = re.sub(r"\b(color)\s*:\s*#([0-9a-fA-F]{6})\b", color_repl, txt)

    # 4. flat swaps everywhere else
    def hex_repl(m):
        key = m.group(1).lower()
        if key in FLAT:
            bump("flat", key)
            return FLAT[key]
        return m.group(0)

    txt = re.sub(r"#([0-9a-fA-F]{6})\b", hex_repl, txt)

    # 5. rgba accent shadows
    for pat, rep in RGBA_MAP:
        txt, n = re.subn(pat, rep, txt)
        if n:
            bump("rgba", pat, n)

    if txt != original and APPLY:
        path.write_text(txt)

print("mode:", "APPLY" if APPLY else "DRY RUN")
print("files scanned:", len(files))
print()
for (kind, key), n in sorted(counts.items(), key=lambda x: -x[1]):
    print(f"  {n:5d}  {kind:8s} {key}")
print()
print("total replacements:", sum(counts.values()))