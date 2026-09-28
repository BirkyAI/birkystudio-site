#!/usr/bin/env python3
"""Fix the retired $29 support tier, quoted in quetzales as Q220/mes, on the ES pages.

Q220 is roughly $29 at the site's own implied rate (Q9,900 for $1,297), so it is the
retired tier. The EN twin of these cards already reads "$97" (USD), so the ES cards use
the same USD figure for the support line.
"""
import pathlib, sys

SITE = pathlib.Path.home() / "websites" / "birkystudio-site" / "src"
ES = SITE / "data" / "products-es.js"
ES_HOME = SITE / "pages" / "es" / "index.astro"

RULES = [
    (ES, "pago \u00fanico \u00b7 soporte opcional Q220/mes",
         "pago \u00fanico \u00b7 soporte opcional desde $97/mes", 1),
    (ES, "La ayuda y los ajustes continuos son opcionales, por Q220 al mes (no es obligatorio).",
         "La ayuda y los ajustes continuos son opcionales, desde $97/mes (Cuidado y Mantenimiento) o $197/mes (Socio de IA para Negocios), y no son obligatorios.", 1),
    (ES, "No. Es opcional por Q220 al mes, para ajustes continuos y ayuda prioritaria.",
         "No. Es opcional, desde $97/mes (Cuidado y Mantenimiento) o $197/mes (Socio de IA para Negocios), para ajustes continuos y ayuda prioritaria.", 1),
    (ES_HOME, 'font-weight:600;"> Q220</span>',
         'font-weight:600;"> $97</span>', 1),
    (ES_HOME, "(Q220/mes opcional)",
         "(soporte opcional desde $97/mes)", 1),
]

apply = "--apply" in sys.argv
texts = {p: p.read_text(encoding="utf-8") for p in {r[0] for r in RULES}}

ok = True
for path, old, new, expect in RULES:
    n = texts[path].count(old)
    if n != expect:
        print(f"  FAIL {path.name}: expected {expect} of {old[:55]!r}, found {n}")
        ok = False
        continue
    texts[path] = texts[path].replace(old, new)
    print(f"  ok   {path.name}: {old[:55]!r}")

if apply and ok:
    for p, t in texts.items():
        p.write_text(t, encoding="utf-8")
print(f"{'APPLIED' if (apply and ok) else 'DRY RUN'}, {len(RULES)} rules")
sys.exit(0 if ok else 2)