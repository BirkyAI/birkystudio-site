#!/usr/bin/env python3
"""Fix the retired copy still rendered by the product data + the ES homepage.

Found on 28 Sep 2026 while regenerating the live-copy snapshot: the product data
files still carried copy the earlier site pass had already fixed on the pages.
- EN + ES still claimed a "2 to 3 hour" setup session (Doc 2/3 say about 15 min of build).
- EN product data was fixed for property search, the ES data was NOT.
- ES still sold the RETIRED support tier as "Q373/mes" (that is the old $49 tier).

ES support mentions follow the convention already used on the ES partners page:
USD figures with the Spanish tier names from Doc 3.

Each rule carries an expected match count, so a rule that stops matching fails loudly.
"""
import pathlib, sys

SITE = pathlib.Path.home() / "websites" / "birkystudio-site" / "src"
EN = SITE / "data" / "products.js"
ES = SITE / "data" / "products-es.js"
ES_HOME = SITE / "pages" / "es" / "index.astro"

RULES = [
    (EN, "in one 2 to 3 hour screen-sharing session.",
         "on one guided screen-sharing call, with about 15 minutes of build on her side.", 1),
    (EN, "A live 2 to 3 hour setup and training session, plus 30 days of free support after",
         "A live setup and training session, about 15 minutes of build plus a guided walkthrough, and 30 days of free support after", 1),
    (EN, "One 2\u20133 hour remote session, live within 2\u20133 days.",
         "Live within 2\u20133 days. The build takes about 15 minutes, on a guided screen-sharing call.", 1),
    (ES, "en una sola sesi\u00f3n de 2 a 3 horas compartiendo pantalla, con el entrenamiento completo incluido.",
         "en una sola llamada guiada compartiendo pantalla, con unos 15 minutos de instalaci\u00f3n de su parte y el entrenamiento completo incluido.", 1),
    (ES, "Busca propiedades por ti y escribe las descripciones de tus anuncios",
         "Atiende y califica cada consulta por ti", 1),
    (ES, "Se instala en vivo en una sesi\u00f3n de 2 a 3 horas, con entrenamiento y 30 d\u00edas de soporte gratis",
         "Se instala en vivo en una llamada guiada, con unos 15 minutos de instalaci\u00f3n, entrenamiento y 30 d\u00edas de soporte gratis", 1),
    (ES, "Una sesi\u00f3n remota de 2\u20133 horas, en vivo en 2\u20133 d\u00edas.",
         "En vivo en 2\u20133 d\u00edas. La instalaci\u00f3n toma unos 15 minutos, en una llamada guiada compartiendo pantalla.", 1),
    (ES, "configuraci\u00f3n \u00b7 soporte opcional Q373/mes",
         "configuraci\u00f3n \u00b7 soporte opcional desde $97/mes", 1),
    (ES, "El mantenimiento y los ajustes continuos de sus respuestas son opcionales, por Q373 al mes.",
         "El mantenimiento y los ajustes continuos de sus respuestas son opcionales, desde $97/mes (Cuidado y Mantenimiento) o $197/mes (Socio de IA para Negocios).", 1),
    (ES, "La ayuda opcional es de Q373 al mes.",
         "La ayuda opcional es $97/mes (Cuidado y Mantenimiento) o $197/mes (Socio de IA para Negocios).", 1),
    (ES_HOME, "El soporte opcional es Q373/mes, sin contrato.",
         "El soporte opcional es $97/mes (Cuidado y Mantenimiento) o $197/mes (Socio de IA para Negocios), sin contrato.", 1),
]

apply = "--apply" in sys.argv
texts = {p: p.read_text(encoding="utf-8") for p in {r[0] for r in RULES}}

ok = True
for path, old, new, expect in RULES:
    n = texts[path].count(old)
    if n != expect:
        print(f"  FAIL {path.name}: expected {expect} of {old[:60]!r}, found {n}")
        ok = False
        continue
    texts[path] = texts[path].replace(old, new)
    print(f"  ok   {path.name}: {old[:60]!r}")

if apply and ok:
    for p, t in texts.items():
        p.write_text(t, encoding="utf-8")
print(f"{'APPLIED' if (apply and ok) else 'DRY RUN'}, {len(RULES)} rules")
sys.exit(0 if ok else 2)