#!/usr/bin/env python3
"""Regenerate the live-copy snapshot from the product data files.

The snapshot is Luna's mark-up sheet: every product page, English then Spanish,
exactly as it is on the site. It was generated 25 Sep 2026 and went stale the moment
the copy fixes landed (it still said "2 to 3 hour session", still listed property
search and listing descriptions, still showed the retired support tiers).

Source of truth is src/data/products.js and src/data/products-es.js, which is what the
product pages actually render, so regenerating from them cannot drift from the site.

usage: regenerate-copy-snapshot.py /tmp/products-en.json /tmp/products-es.json OUT.md
"""
import json, sys, pathlib

en = json.loads(pathlib.Path(sys.argv[1]).read_text())
es = json.loads(pathlib.Path(sys.argv[2]).read_text())
out = pathlib.Path(sys.argv[3])

WORD_TO_ES_CATEGORY = {
    "Assistant": "Asistente",
    "Lead Generation": "Generación de Prospectos",
    "Website": "Sitio Web",
    "Website Add-on": "Complemento de Sitio Web",
    "Receptionist": "Recepcionista",
}

HEADER = """# BirkyStudio - All Product Page Copy (for review)

Every product page, English then Spanish, exactly as it is on the site.
Mark anything you want changed directly in this file: strike it out, or write the
replacement underneath. Anything you do not touch, I leave exactly as is.

Regenerated 28 Sep 2026 from the live product data (`src/data/products.js` and
`src/data/products-es.js`). The date in this filename is the original creation date.
Prices and copy now match Doc 1 (FROZEN 27 Sep 2026).

Live pages: https://birkystudio.com/products/  ·  https://birkystudio.com/es/products/
"""


def bullets(items):
    return "\n".join(f"- {i}" for i in items) if items else "_(none)_"


def faq(items):
    return "\n".join(f"- **{f['q']}** {f['a']}" for f in items) if items else "_(none)_"


es_by_slug = {p["slug"]: p for p in es}
lines = [HEADER]
current_cat = None
n = 0

for p in en:
    if p["category"] != current_cat:
        current_cat = p["category"]
        lines.append(f"\n## {current_cat}\n")
    n += 1
    e = es_by_slug.get(p["slug"], {})
    lines.append(f"### {n}. {p['name']} / {e.get('name', '?')}\n")
    lines.append(f"- Slug: `{p['slug']}`  (never changes)")
    price_note = f" {p['priceNote']}" if p.get("priceNote") else ""
    lines.append(f"- Price: {p.get('price', '?')}{price_note}\n")

    for lang, d, L in (("ENGLISH", p, {
            "h": "*Heading:*", "t": "*Tagline:*", "w": "*What it is:*",
            "i": "*What you get:*", "b": "*What it doesn't include:*",
            "d": "*Delivery:*", "bf": "*Best for:*", "q": "*Questions:*"}),
        ("ESPAÑOL", e, {
            "h": "*Título:*", "t": "*Frase corta:*", "w": "*Qué es:*",
            "i": "*Qué recibes:*", "b": "*Qué no incluye:*",
            "d": "*Entrega:*", "bf": "*Ideal para:*", "q": "*Preguntas:*"})):
        if not d:
            continue
        lines.append(f"**{lang}**\n")
        lines.append(f"{L['h']} {d.get('name', '?')}\n")
        if d.get("tagline"):
            lines.append(f"{L['t']} {d['tagline']}\n")
        if d.get("whatItIs"):
            lines.append(f"{L['w']} {d['whatItIs']}\n")
        if d.get("included"):
            lines.append(f"{L['i']}\n{bullets(d['included'])}\n")
        if d.get("boundaries"):
            lines.append(f"{L['b']}\n{bullets(d['boundaries'])}\n")
        if d.get("delivery"):
            lines.append(f"{L['d']} {d['delivery']}\n")
        if d.get("bestFor"):
            lines.append(f"{L['bf']} {d['bestFor']}\n")
        if d.get("faqs"):
            lines.append(f"{L['q']}\n{faq(d['faqs'])}\n")

    lines.append("---\n")

out.write_text("\n".join(lines).replace("\n\n\n", "\n\n"), encoding="utf-8")
print(f"wrote {out} with {n} product sections ({out.stat().st_size} bytes)")