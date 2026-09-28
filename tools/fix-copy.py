#!/usr/bin/env python3
"""
Doc 4 Part B: retire the stale product claims and prices from the live site copy.

Every rule is an EXACT string replacement with an expected match count, so a rule that
silently stops matching fails loudly instead of quietly doing nothing. Dry-run by default.

Groups (Doc 4):
  B1  retired support tiers $29/mo and $49/mo -> $97 Care & Maintenance / $197 Business AI Partner
  B2  "Notion Real Estate System" as a product name -> "Notion CRM, built for agents"
  B3  listing-description claims -> deleted outright
  B4  property search presented as included -> deleted from inclusion lists
  B7  retired website prices $195/$390/$780 -> $499/$999/$1,999 (NEW, found during this pass)
  B8  retired AI Agent price $549-$799 -> $1,297 (NEW, found during this pass)
  B6  the same sweep on the Spanish pages, in voseo, using Doc 3 ES tier names

Deliberately NOT touched:
  - competitor prices that happen to be $29/$49/$780 (Shopify, Calendly, Real Geeks' Geek AI Text,
    Guatemala receptionist salaries, generic market budgets)
  - the generic "$250 to $1,100 first year" budget in the website-cost post, that is market data
  - the blog that says "search listings" about Google, that is search-engine listings

Usage: python3 tools/fix-copy.py [--apply]
"""
import sys
import pathlib

ROOT = pathlib.Path("/Users/macminim4/websites/birkystudio-site")
APPLY = "--apply" in sys.argv

SUP_SHORT = "from $97/month"
SUP_FULL = "$97/month (Care & Maintenance) or $197/month (Business AI Partner)"

RULES = [
    # ------------------------------------------------------------------ B1 data
    ("B1", "src/data/products.js",
     "'one-time · optional support $29/month'", "'one-time · optional support from $97/month'", 1),
    ("B1", "src/data/products.js",
     "'Optional $29/month for ongoing support and tweaks (not required)'",
     "'Optional from $97/month for ongoing support and tweaks (not required)'", 1),
    ("B1", "src/data/products.js",
     "'No, it is optional at $29/month for ongoing tweaks and priority help.'",
     "'No, it is optional. Care & Maintenance is $97/month, and Business AI Partner is $197/month for ongoing tweaks and priority help.'", 1),
    ("B1", "src/data/products.js",
     "'setup · optional support $49/month'", "'setup · optional support from $97/month'", 1),
    ("B1", "src/data/products.js",
     "'Optional $49/month for ongoing upkeep and fine-tuning'",
     "'Optional from $97/month for ongoing upkeep and fine-tuning'", 1),
    ("B1", "src/data/products.js",
     "Optional support is $49/month.",
     "Optional support is $97/month (Care & Maintenance) or $197/month (Business AI Partner).", 1),

    # ------------------------------------------------------------------ B1 index + partners
    ("B1", "src/pages/index.astro",
     "Ongoing maintenance & prompt tweaks ($49/mo optional)",
     "Ongoing maintenance & prompt tweaks (from $97/mo optional)", 1),
    ("B1", "src/pages/partners.astro",
     ">$29 - $49/mo<", ">$97 - $197/mo<", 1),
    ("B1", "src/pages/partners.astro",
     "optional support retainer ($197/mo for AI Agent with training, or $29-49/mo basic)",
     "optional support retainer ($197/mo Business AI Partner, or $97/mo Care & Maintenance)", 1),

    # ------------------------------------------------------------------ B1 comparison pages
    ("B1", "src/pages/best-ai-receptionists-real-estate.astro",
     "Optional support: $49/month (voice) / $29/month (text)", "Optional support from $97/month", 1),
    ("B1", "src/pages/birkystudio-vs-dialpad.astro",
     "Optional support: $49/month (voice) / $29/month (text)", "Optional support from $97/month", 1),
    ("B1", "src/pages/birkystudio-vs-goodcall.astro",
     "Optional support: $49/month (voice) / $29/month (text)", "Optional support from $97/month", 1),
    ("B1", "src/pages/birkystudio-vs-loman.astro",
     "Optional support: $49/month (voice) / $29/month (text)", "Optional support from $97/month", 1),
    ("B1", "src/pages/birkystudio-vs-smithai.astro",
     "Optional support: $49/month (voice) / $29/month (text)", "Optional support from $97/month", 1),
    ("B1", "src/pages/birkystudio-vs-wix-squarespace.astro",
     "AI Agent support $49/month (optional)", "AI Agent support from $97/month (optional)", 1),

    # gohighlevel  (also carries B2 and B3/B4)
    ("B1", "src/pages/birkystudio-vs-gohighlevel.astro",
     "with optional support from $29/month", "with optional support from $97/month", 1),
    ("B1", "src/pages/birkystudio-vs-gohighlevel.astro",
     "Over 12 months, BirkyStudio costs roughly $1,297-$1,645/year.",
     "Over 12 months, BirkyStudio costs roughly $1,297-$2,461/year.", 1),
    ("B1", "src/pages/birkystudio-vs-gohighlevel.astro",
     "· Optional support from $29/month", "· Optional support from $97/month", 1),
    ("B1", "src/pages/birkystudio-vs-gohighlevel.astro",
     "~$1,645 (setup + $29/mo support)", "~$2,461 (setup + $97/mo support)", 1),
    ("B2", "src/pages/birkystudio-vs-gohighlevel.astro",
     "(includes Notion Real Estate System)", "(includes a Notion CRM built for agents)", 1),
    ("B3", "src/pages/birkystudio-vs-gohighlevel.astro",
     "automates property searches, manages your email inbox, drafts listing descriptions, follows up with past clients",
     "manages your email inbox, follows up with past clients", 1),
    ("B4", "src/pages/birkystudio-vs-gohighlevel.astro",
     "handles lead conversations, property searches, follow-ups, and task automation, but uses Notion as a lightweight CRM layer",
     "handles lead conversations, follow-ups, and task automation, but uses Notion as a lightweight CRM layer", 1),
    ("B4", "src/pages/birkystudio-vs-gohighlevel.astro",
     "handles lead conversations, property searches, follow-ups, email management, and task automation",
     "handles lead conversations, follow-ups, email management, and task automation", 1),
    ("B4", "src/pages/birkystudio-vs-gohighlevel.astro",
     "wants AI to handle lead conversations, property searches, email follow-ups, and daily task automation",
     "wants AI to handle lead conversations, email follow-ups, and daily task automation", 1),
    ("B4", "src/pages/birkystudio-vs-gohighlevel.astro",
     "<td style=\"padding:14px 12px;color:white;font-weight:600;\">✅ AI can search listings</td>",
     "<td style=\"padding:14px 12px;color:white;font-weight:600;\">⚠️ Separate paid research service</td>", 1),
    ("B4", "src/pages/birkystudio-vs-gohighlevel.astro",
     "conversations, property searches, email management, task automation",
     "conversations, email management, task automation", 1),
    ("B4", "src/pages/birkystudio-vs-gohighlevel.astro",
     "The AI agent handles lead conversations, property searches, and follow-ups",
     "The AI agent handles lead conversations and follow-ups", 1),

    # human-va
    ("B1", "src/pages/birkystudio-vs-human-va.astro",
     "with optional support at $29-$49/month", "with optional support at $97-$197/month", 1),
    ("B1", "src/pages/birkystudio-vs-human-va.astro",
     "That's roughly $645-$1,618 in year one, a fraction of one month of a human VA.",
     "That's roughly $1,461-$2,194 in year one, against $24,000-$42,000 for a human VA.", 1),
    ("B1", "src/pages/birkystudio-vs-human-va.astro",
     "plus optional support at $49/month. The AI Text Receptionist for WhatsApp is $297 one-time with optional support at $29/month.",
     "plus optional support at $97/month. The AI Text Receptionist for WhatsApp is $297 one-time with optional support at $97/month.", 2),
    ("B1", "src/pages/birkystudio-vs-human-va.astro",
     "~$30-$50/mo Vapi usage + optional $29-$49/mo support",
     "~$30-$50/mo Vapi usage + optional $97-$197/mo support", 1),
    ("B1", "src/pages/birkystudio-vs-human-va.astro",
     "Optional support runs $29-$49 a month.", "Optional support runs $97-$197 a month.", 1),
    ("B1", "src/pages/birkystudio-vs-human-va.astro",
     "+ optional support $49/mo · AI Text Receptionist (WhatsApp) $297 one-time + optional support $29/mo · AI Agent Setup $1,297 (includes Notion Real Estate System) · Optional Support &amp; Maintenance $197/mo",
     "+ optional support from $97/mo · AI Text Receptionist (WhatsApp) $297 one-time + optional support from $97/mo · AI Agent Setup $1,297 (includes a Notion CRM built for agents) · Optional support $97/mo Care &amp; Maintenance or $197/mo Business AI Partner", 1),
    ("B1", "src/pages/birkystudio-vs-human-va.astro",
     "~$645 ($297 + $29/mo support)", "~$1,461 ($297 + $97/mo support)", 1),
    ("B1", "src/pages/birkystudio-vs-human-va.astro",
     "~$1,618 ($550 + ~$40/mo Vapi + $49/mo support)",
     "~$2,194 ($550 + ~$40/mo Vapi + $97/mo support)", 1),
    ("B1", "src/pages/birkystudio-vs-human-va.astro",
     "with optional support at $29-$49/mo. That's roughly $645-$1,618 in year one.",
     "with optional support at $97-$197/mo. That's roughly $1,461-$2,194 in year one.", 1),
    ("B1", "src/pages/birkystudio-vs-human-va.astro",
     "+ optional support $49/mo; AI Text Receptionist $297 one-time + optional support $29/mo; AI Agent Setup $1,297; Support &amp; Maintenance $197/mo",
     "+ optional support from $97/mo; AI Text Receptionist $297 one-time + optional support from $97/mo; AI Agent Setup $1,297; Support $97/mo Care &amp; Maintenance or $197/mo Business AI Partner", 1),

    # side
    ("B1", "src/pages/birkystudio-vs-side.astro",
     "(includes Notion Real Estate System), with optional support from $29/month",
     "(includes a Notion CRM built for agents), with optional support from $97/month", 1),
    ("B1", "src/pages/birkystudio-vs-side.astro",
     "($1,297 one-time plus optional $29/month support)",
     "($1,297 one-time plus optional support from $97/month)", 1),
    ("B1", "src/pages/birkystudio-vs-side.astro",
     "Optional support from $29/month", "Optional support from $97/month", 1),
    ("B1", "src/pages/birkystudio-vs-side.astro",
     "~$1,645 (setup + $29/mo support)", "~$2,461 (setup + $97/mo support)", 1),
    ("B1", "src/pages/birkystudio-vs-side.astro",
     "~$2,435 (setup + voice + $29/mo + Vapi ~$40/mo)",
     "~$3,491 (setup + voice + $97/mo support + Vapi ~$40/mo)", 1),
    ("B1", "src/pages/birkystudio-vs-side.astro",
     "optional $29/month support. No surprises", "optional support from $97/month. No surprises", 1),
    ("B3", "src/pages/birkystudio-vs-side.astro",
     "qualifies leads, schedules showings, searches properties, manages your email inbox, drafts listing descriptions, and follows up with past clients",
     "qualifies leads, schedules showings, manages your email inbox, and follows up with past clients", 1),

    # traditional-agency  (B1 + B7-adjacent B8 retired AI agent price)
    ("B1", "src/pages/birkystudio-vs-traditional-agency.astro",
     "and $549-$799 one-time for a custom AI agent", "and $1,297 one-time for a custom AI agent", 1),
    ("B8", "src/pages/birkystudio-vs-traditional-agency.astro",
     "BirkyStudio costs $297-$3,797 total.", "BirkyStudio costs $297-$3,846 total.", 1),
    ("B1", "src/pages/birkystudio-vs-traditional-agency.astro",
     "BirkyStudio's optional support is $29/month for receptionists and $49/month for AI agents, both optional and cancellable any time.",
     "BirkyStudio's optional support is $97/month (Care & Maintenance) or $197/month (Business AI Partner), both optional and cancellable any time.", 1),
    ("B8", "src/pages/birkystudio-vs-traditional-agency.astro",
     "✅ $549-$799 one-time", "✅ $1,297 one-time", 1),
    ("B1", "src/pages/birkystudio-vs-traditional-agency.astro",
     "$0 or $29-$49/mo optional", "$0 or from $97/mo optional", 1),
    ("B1", "src/pages/birkystudio-vs-traditional-agency.astro",
     "optional support at $49/month if you want it", "optional support from $97/month if you want it", 1),
    ("B1", "src/pages/birkystudio-vs-traditional-agency.astro",
     "AI Agent $549-$799 one-time · Optional support $29-$49/mo",
     "AI Agent $1,297 one-time · Optional support from $97/mo", 1),
    ("B1", "src/pages/birkystudio-vs-traditional-agency.astro",
     "Ongoing support ($29-$49/month)", "Ongoing support (from $97/month)", 1),
    ("B1", "src/pages/birkystudio-vs-traditional-agency.astro",
     "optional support plan ($29-$49/month)", "optional support plan (from $97/month)", 1),

    # wix / squarespace  (B4 website-capability claims we cannot deliver)
    ("B4", "src/pages/birkystudio-vs-wix-squarespace.astro",
     "BirkyStudio builds real estate websites with property listings, IDX integration, lead capture, and AI receptionist built in, all from the start",
     "BirkyStudio builds real estate websites with property listings, lead capture, and AI receptionist built in, all from the start", 1),
    ("B4", "src/pages/birkystudio-vs-wix-squarespace.astro",
     "(IDX integration, property search, lead capture, blog)",
     "(lead capture, blog, booking forms)", 1),
    ("B4", "src/pages/birkystudio-vs-wix-squarespace.astro",
     "with property search, lead capture, and AI-powered follow-up built in from day one",
     "with lead capture and AI-powered follow-up built in from day one", 1),
    ("B4", "src/pages/birkystudio-vs-wix-squarespace.astro",
     "BirkyStudio includes all of this out of the box. IDX, property listings, lead capture, and AI receptionist, because it's built specifically for real estate agents from the ground up.",
     "BirkyStudio includes property listings, lead capture, and an AI receptionist out of the box, because it's built specifically for real estate agents from the ground up.", 1),

    # ------------------------------------------------------------------ B2 / B3 / B4 others
    ("B2", "src/pages/ai-readiness-quiz.astro",
     'name: "Notion Real Estate System", price: "FREE included"',
     'name: "Notion CRM, built for agents", price: "FREE included"', 1),
    ("B4", "src/pages/ai-readiness-quiz.astro",
     "handles lead follow-ups, property searches, and after-hours inquiries",
     "handles lead follow-ups and after-hours inquiries", 1),
    ("B2", "src/pages/birkystudio-vs-realgeeks.astro",
     "✅ Notion Real Estate System (in $1,297 AI Agent Setup)",
     "✅ Notion CRM, built for agents (in $1,297 AI Agent Setup)", 1),
    ("B2", "src/pages/portfolio.astro",
     "Includes Notion Real Estate System with CRM, automated property search, listing description generator, email management with follow-ups, Google Business Profile content automation, and bilingual WhatsApp + Telegram.",
     "Includes a Notion CRM built for agents, email management with follow-ups, Google Business Profile content automation, and bilingual WhatsApp + Telegram.", 1),
    ("B3", "src/data/products.js",
     "'Searches properties and writes listing descriptions for you',",
     "'Catches and qualifies every enquiry for you',", 1),
    ("B4", "src/pages/tools/ai-savings-calculator.astro",
     'style="font-size:14px;color:var(--bs-text-muted);$1,297">Drafts emails, manages CRM, searches properties, writes listings, posts to GBP, and more.',
     'style="font-size:14px;color:var(--bs-text-muted);">Drafts emails, manages your CRM, posts to Google Business Profile, and more.', 1),

    # ------------------------------------------------------------------ B1 blogs
    ("B1", "src/content/blog/ai-agent-vs-hiring-va.md",
     "| Optional monthly support & maintenance | $29/month |",
     "| Optional monthly support & maintenance | $97/month (or $197/month Business AI Partner) |", 1),
    ("B1", "src/content/blog/ai-agent-vs-hiring-va.md",
     "| Monthly cost | **$2,000 – $3,500** | $29 (optional) |",
     "| Monthly cost | **$2,000 – $3,500** | $97 (optional) |", 1),
    ("B1", "src/content/blog/ai-agents-vs-diy-chatbots.md",
     "($0 for 30 days, then $49/mo optional)", "($0 for 30 days, then $97/mo optional)", 1),
    ("B1", "src/content/blog/ai-voice-receptionist-books-clients-while-you-sleep.md",
     "that is $29/month optional", "that is $97/month optional", 1),
    ("B1", "src/content/blog/ai-voice-receptionist-vs-monthly.md",
     "the optional $29/month support package", "the optional $97/month support package", 2),
    ("B1", "src/content/blog/ai-voice-receptionist-vs-monthly.md",
     "## The Optional Support Package ($29/month)", "## The Optional Support Package ($97/month)", 1),
    ("B1", "src/content/blog/clients-remember-what-you-forget.md",
     "it includes three months of support. The text receptionist starts at $297 and the voice receptionist at $550 with an optional $29 a month support package",
     "it includes 30 days of support. The text receptionist starts at $297 and the voice receptionist at $550 with an optional $97 a month support package", 1),
    ("B1", "src/content/blog/what-1297-buys-ai-agent-setup.md",
     "Optional support after the first three months is $49/month for voice, $29/month for text.",
     "Optional support after the first 30 days is $97/month (Care & Maintenance) or $197/month (Business AI Partner).", 1),

    # ------------------------------------------------------------------ B7 retired website prices
    ("B7", "src/content/blog/small-business-website-cost-2026.md",
     "our Starter plan at $195 fits right here", "our Starter plan at $499 fits right here", 1),
    ("B7", "src/content/blog/small-business-website-cost-2026.md",
     "Our Professional plan at $390 covers this with room to spare.",
     "Our Professional plan at $999 covers this with room to spare.", 1),
    ("B7", "src/content/blog/small-business-website-cost-2026.md",
     "Our E-commerce plan at $780 includes online store setup, payment integration, and product management.\n\n",
     "", 1),
    ("B7", "src/content/blog/small-business-website-cost-2026.md",
     "If a $390 website brings in even one new customer", "If a $999 website brings in even one new customer", 1),
    ("B7", "src/content/blog/website-redesign-small-business.md",
     "our Starter plan at $195 works well", "our Starter plan at $499 works well", 1),
    ("B7", "src/content/blog/website-redesign-small-business.md",
     "Our Professional plan at $390 covers", "Our Professional plan at $999 covers", 1),
    ("B7", "src/content/blog/bilingual-website-design-guatemala.md",
     "Our Professional plan at $390 includes", "Our Professional plan at $999 includes", 1),
    ("B7", "src/content/blog/why-every-small-business-needs-a-website-2026.md",
     "Professional websites for small businesses start at $195.",
     "Professional websites for small businesses start at $499.", 1),

    # ------------------------------------------------------------------ B6 Spanish pages
    ("B6", "src/pages/es/partners.astro",
     ">$29 - $49/mes<", ">$97 - $197/mes<", 1),
    ("B6", "src/pages/es/partners.astro",
     "nuestro plan de soporte opcional ($197/mes para Agente IA con entrenamiento, o $29-49/mes básico)",
     "nuestro plan de soporte opcional ($197/mes Socio de IA para Negocios, o $97/mes Cuidado y Mantenimiento)", 1),
    ("B6", "src/pages/es/portafolio.astro",
     "Incluye Sistema Notion de Bienes Raíces con CRM, búsqueda automatizada de propiedades, generador de descripciones, gestión de correo con seguimientos, automatización de Google Business Profile y WhatsApp + Telegram bilingüe.",
     "Incluye un CRM de Notion hecho para agentes, gestión de correo con seguimientos, automatización de Google Business Profile y WhatsApp + Telegram bilingüe.", 1),

    # ------------------------------------------------------------------ B9 setup time
    # Doc 4 Part C flagged the demo bubble claiming a "2-3 hour remote session"; Doc 2 and Doc 3
    # both say the build is about 15 minutes on Luna's side plus a guided call. The same stale
    # claim was on the homepage FAQ (visible and schema) and three comparison pages.
    ("B9", "src/pages/birkystudio-vs-gohighlevel.astro",
     "Setup takes 2-3 hours with Luna guiding you via screen share.",
     "Setup takes about 15 minutes of build, with Luna guiding you on a screen share call.", 1),
    ("B9", "src/pages/birkystudio-vs-gohighlevel.astro",
     '<td style="padding:14px 12px;color:var(--bs-text);">2-3 hours (guided screen share)</td>',
     '<td style="padding:14px 12px;color:var(--bs-text);">~15 min build + guided call</td>', 1),
    ("B9", "src/pages/birkystudio-vs-gohighlevel.astro",
     "set up in a single 2-3 hour screen share session.",
     "set up in a single guided screen share session of about 15 minutes of build.", 1),
    ("B9", "src/pages/birkystudio-vs-gohighlevel.astro",
     "A 2-3 hour setup session and you're done.",
     "A guided session with about 15 minutes of build, and you're done.", 1),
    ("B9", "src/pages/birkystudio-vs-side.astro",
     "is set up in 2-3 hours.",
     "is set up in a guided session with about 15 minutes of build.", 1),
    ("B9", "src/pages/birkystudio-vs-side.astro",
     '<td style="padding:14px 12px;color:var(--bs-text);">2-3 hours (guided screen share)</td>',
     '<td style="padding:14px 12px;color:var(--bs-text);">~15 min build + guided call</td>', 1),
    ("B9", "src/pages/birkystudio-vs-side.astro",
     "Setup takes 2-3 hours in a guided screen share session, and the",
     "Setup takes about 15 minutes of build in a guided screen share session, and the", 1),
    ("B9", "src/pages/birkystudio-vs-side.astro",
     "BirkyStudio takes 2-3 hours in a guided screen share session. Your AI is trained on your specific listings and processes in one afternoon.",
     "BirkyStudio takes about 15 minutes of build in a guided screen share session. Your AI is trained on your specific listings and processes in that same session.", 1),
    ("B9", "src/pages/index.astro",
     "for you via a screen-sharing session that takes 2-3 hours, including full training.",
     "with you on a screen-sharing call. The build takes about 15 minutes on her side, and the call covers connecting your accounts and a full walkthrough.", 1),
    ("B9", "src/pages/index.astro",
     "AI agent setup takes one 2-3 hour remote session.",
     "AI agent setup is about 15 minutes of build plus a call to connect your accounts.", 1),
    ("B9", "src/pages/birkystudio-vs-traditional-agency.astro",
     "BirkyStudio costs $297-$3,797 total for the same core services.",
     "BirkyStudio costs $297-$3,846 total for the same core services.", 1),
]


def main():
    by_file = {}
    for group, rel, old, new, expected in RULES:
        by_file.setdefault((group, rel), []).append((old, new, expected))

    failures = []
    changed_files = 0
    applied = 0
    already = 0

    for (group, rel), rules in by_file.items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f"MISSING FILE {rel}")
            continue
        txt = path.read_text()
        original = txt
        for old, new, expected in rules:
            found = txt.count(old)
            if found != expected:
                # idempotency: if the replacement is already in place, this rule was applied
                # by an earlier run. Not a failure, and not re-applied.
                if found == 0 and txt.count(new) >= expected:
                    already += expected
                    continue
                failures.append(f"{rel} [{group}] expected {expected} match(es), found {found}: {old[:70]!r}")
                continue
            txt = txt.replace(old, new)
            applied += found
        if txt != original:
            changed_files += 1
            if APPLY:
                path.write_text(txt)

    print("mode:", "APPLY" if APPLY else "DRY RUN")
    print(f"rules: {len(RULES)}   files touched: {changed_files}   replacements: {applied}   already in place: {already}")
    if failures:
        print("\nFAILURES (nothing was applied for these):")
        for f in failures:
            print("  ✗", f)
        sys.exit(1)
    print("\nall rules matched their expected counts")


if __name__ == "__main__":
    main()