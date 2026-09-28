#!/usr/bin/env python3
"""Replace the dead pink hex #f472b6 with the approved palette token.

Doc 5 defines the single accent as #ff2d95 (var(--bs-accent)). The hex
#f472b6 is the old pink and is not part of the palette at all, so any
remaining instance is an unfinished migration. Pink to pink, so this is
visually near-identical and carries no layout risk.

Deliberately NOT touched: the green family (#10b981 #059669 #34d399
#6ee7b7 rgba(16,185,129,...)). Green here is the semantic positive /
emphasis colour, and Luna explicitly kept the green check in the
comparison tables. Changing it is a brand decision, not a migration.
"""
import pathlib, sys

OLD = "#f472b6"
NEW = "var(--bs-accent)"
EXPECTED = 36
ROOT = pathlib.Path.home() / "websites" / "birkystudio-site" / "src"

hits, files = 0, 0
for p in sorted(ROOT.rglob("*")):
    if p.suffix not in (".astro", ".css", ".md", ".mdx"):
        continue
    t = p.read_text(encoding="utf-8")
    n = t.count(OLD)
    if n:
        hits += n
        files += 1
        if "--apply" in sys.argv:
            p.write_text(t.replace(OLD, NEW), encoding="utf-8")

print(f"{'APPLIED' if '--apply' in sys.argv else 'DRY RUN'}: {hits} instance(s) of {OLD} in {files} file(s)")
if hits != EXPECTED:
    print(f"WARNING: expected {EXPECTED}, found {hits}. Stop and re-check before applying.")
    sys.exit(2)