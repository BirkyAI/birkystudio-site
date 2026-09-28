#!/usr/bin/env python3
"""
Strip per-section background colours/gradients across the site.

Why: Luna, 27 Sep 2026. Every page should look like the top hero section,
one colour with the grid. Sections painting their own colour is exactly
what produced the "different colour sections" banding.

This removes ONLY `background:` / `background-color:` declarations from
inline styles on <section> and <footer> tags. Anything using url(...) is
left alone and reported. Divs (cards, chips, icon tiles) are never touched.

Usage: python3 tools/strip-section-bg.py [--apply]
"""
import re
import sys
import pathlib

ROOT = pathlib.Path("/Users/macminim4/websites/birkystudio-site")
APPLY = "--apply" in sys.argv

TAG_RE = re.compile(r"<(?:section|footer)\b[^>]*>", re.S)
STYLE_RE = re.compile(r'style="([^"]*)"')
BG_RE = re.compile(r"background(-color)?\s*:\s*[^;\"]+;?", re.I)

targets = sorted(list((ROOT / "src/pages").rglob("*.astro")) +
                 list((ROOT / "src/components").rglob("*.astro"))
                 if (ROOT / "src/components").exists() else
                 list((ROOT / "src/pages").rglob("*.astro")))

total_tags = 0
total_removed = 0
skipped = []
report = []


def fix_style(style: str, removed: list):
    def repl(m):
        value = m.group(0)
        if "url(" in value:
            skipped.append(value.strip())
            return value
        removed.append(value.strip().rstrip(";"))
        return ""
    out = BG_RE.sub(repl, style)
    out = re.sub(r"\s*;\s*;+", ";", out)
    out = re.sub(r";\s*$", "", out)
    return out.strip(" ;")


def fix_tag(match):
    global total_tags
    tag = match.group(0)
    if 'style="' not in tag:
        return tag
    removed = []

    def style_repl(sm):
        new_style = fix_style(sm.group(1), removed)
        if not new_style:
            return ""            # drop the whole attribute if now empty
        return 'style="%s"' % new_style

    new_tag = STYLE_RE.sub(style_repl, tag)
    if removed:
        total_tags += 1
        report.append((removed, new_tag[:110]))
    return new_tag


for path in targets:
    txt = path.read_text()
    new_txt = TAG_RE.sub(fix_tag, txt)
    if new_txt != txt:
        if APPLY:
            path.write_text(new_txt)

print("mode:", "APPLY" if APPLY else "DRY RUN")
print("files scanned:", len(targets))
print("section/footer tags whose background was removed:", total_tags)
print("values removed:", sum(len(r[0]) for r in report))
print("skipped url() backgrounds:", len(skipped))
for s in set(skipped):
    print("   SKIPPED:", s)
print()
print("sample of removals:")
for vals, tag in report[:8]:
    print("   removed", vals)
    print("     ->", tag)