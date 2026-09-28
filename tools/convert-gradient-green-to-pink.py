#!/usr/bin/env python3
"""
Second green pass: kill green everywhere, including inside the CTA gradient.

Why this exists
---------------
`convert-green-to-pink.py` (first pass, 27-28 Sep 2026) converted the 88 standalone
green tokens (stat cards, badges, portfolio buttons, pills, links, progress bar,
success messages) to the pink accent, but deliberately LEFT green in the button
gradients because Doc 5 then still permitted it as a "gradient partner".

Luna reviewed the live result on 28 Sep 2026 (02:30) and said:
    "Oh you already mention the green, make it pink, that was one of my comments."

So green is now retired completely. This pass replaces the green gradient stop with
a deep pink (#b0005a), which keeps the depth of the old green -> pink gradient and
keeps white button text legible, without any green left on the site.

Deliberately NOT touched (see Doc 5, "Two greens deliberately survive"):
  - .mod.m3 hero block icon green  -> Luna said "leave the hero as is"
  - #22c55e traffic-light dots     -> macOS window buttons, paired with red + amber
  - #25D366 WhatsApp brand mark, greens inside portfolio screenshots

Idempotent: safe to re-run, reports 0 changes once applied.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEEP_PINK = "#b0005a"

EDITS = [
    ("src/layouts/BaseLayout.astro",
     "linear-gradient(135deg, #10b981, #ff2d95)",
     f"linear-gradient(135deg, {DEEP_PINK}, #ff2d95)"),
    ("src/styles/hero.css",
     "--bs-accent-2: #10b981;",
     f"--bs-accent-2: {DEEP_PINK};"),
    ("src/data/products.js",
     "linear-gradient(135deg,#10b981,var(--bs-accent))",
     f"linear-gradient(135deg,{DEEP_PINK},var(--bs-accent))"),
    ("src/data/products-es.js",
     "linear-gradient(135deg,#10b981,var(--bs-accent))",
     f"linear-gradient(135deg,{DEEP_PINK},var(--bs-accent))"),
    ("src/pages/products/[slug].astro",
     "linear-gradient(135deg,#10b981,var(--bs-accent))",
     f"linear-gradient(135deg,{DEEP_PINK},var(--bs-accent))"),
    ("src/pages/es/products/[slug].astro",
     "linear-gradient(135deg,#10b981,var(--bs-accent))",
     f"linear-gradient(135deg,{DEEP_PINK},var(--bs-accent))"),
    # EN portfolio had mint (#a7f3d0) where the ES page already used pink / muted.
    ("src/pages/portfolio.astro",
     "color:#a7f3d0;font-size:0.9rem",
     "color:#f9a8d4;font-size:0.9rem"),
    ("src/pages/portfolio.astro",
     "color:#a7f3d0;max-width:600px",
     "color:var(--bs-text-muted);max-width:600px"),
]

GREEN = re.compile(
    r"#(10b981|34d399|059669|047857|065f46|6ee7b7|a7f3d0|d1fae5|ecfdf5"
    r"|22c55e|4ade80|16a34a|86efac|dcfce7)"
    r"|(16,\s*185,\s*129)|(34,\s*197,\s*94)|(22,\s*197,\s*94)|(5,\s*150,\s*105)",
    re.I,
)
ALLOWED = (".mod.m3", "background:#22c55e")


def main() -> int:
    changed = 0
    for rel, old, new in EDITS:
        p = ROOT / rel
        if not p.exists():
            print(f"MISSING  {rel}")
            continue
        text = p.read_text()
        n = text.count(old)
        if n:
            p.write_text(text.replace(old, new))
            changed += n
            print(f"changed  {rel}  ({n}x)")
        else:
            print(f"already  {rel}")

    print(f"\n{changed} replacement(s) applied.\n")

    leftovers = []
    for p in sorted((ROOT / "src").rglob("*")):
        if p.is_file() and p.suffix in {".astro", ".css", ".js", ".ts", ".json", ".html"}:
            for i, line in enumerate(p.read_text(errors="ignore").splitlines(), 1):
                if GREEN.search(line) and not any(a in line for a in ALLOWED):
                    leftovers.append(f"  {p.relative_to(ROOT)}:{i}: {line.strip()[:100]}")

    if leftovers:
        print("UNEXPECTED green remains:")
        print("\n".join(leftovers))
        return 1
    print("No unexpected green remains (hero block icon and window dots allowed).")
    return 0


if __name__ == "__main__":
    sys.exit(main())