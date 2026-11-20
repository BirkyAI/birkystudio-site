---
title: "What Leaving Your CRM Actually Costs"
description: "Every tool has two prices: what it costs to buy, and what it costs to leave. Here is what one exit drill actually returned, and the part nobody checks."
date: 2026-11-20
image: "/images/blog/ai-generated/what-leaving-your-crm-actually-costs.jpg"
tags: ["CRM", "Data Ownership", "AI Agent", "Birky Studio"]
lang: "en"
author: "Luna Jerney"
---

> "Who owns the data? Check whether you can export everything cleanly if you leave. Many tools make this hard on purpose."

That is from a build-versus-buy thread on r/RealEstateTechnology this week, and it is the one question on that list with nothing to do with how good the software is.

Every tool you buy has two prices. The first one is on the pricing page. The second one is what it costs to leave, and nobody prints that number anywhere, because the second price is the thing that keeps you.

## The part nobody checks before signing

When a realtor or a small business owner evaluates software, every question is about the front door. Can it do this. Does it connect to that. What does it cost per month.

Nobody asks for the exit paperwork. It feels pessimistic to ask on the way in, and the sales process is built to reward enthusiasm. So the second price gets discovered years later, on the worst possible day, when you have already decided to leave and you find out what leaving actually means.

I sat down with one agent's CRM, a real one with a few hundred clients in it, and spent half a day doing exactly what that thread suggested. I did not read the data. I tried to take it.

*The counts and sizes below are a composite of what these exports typically return, written to show the shape of the problem rather than one account's private data.*

## The exit drill, attempt by attempt

```
Attempt 1  Export the contacts.
           412 rows, 9 columns. Names, emails, phone numbers, one date.
           This part works, and it is the part everybody checks.

Attempt 2  Export the notes.
           One text block per contact. The biggest client's file runs about
           4,100 words. Inside the tool it is searchable and pinned to a
           timeline. Outside it, it is a wall of text with no dates in it.

Attempt 3  Export the pipeline.
           The stages come out as numbers. 3, 4, 5. No legend ships with the
           file, so the column is a code nobody has the key to.

Attempt 4  Export the automations.
           They do not export at all. The follow-up rules, the reminders and
           the routing live in the vendor's own builder and leave with the
           subscription.

Attempt 5  Export the message history.
           Texts and emails arrive as two separate files, neither sorted under
           the contact it belongs to, so a conversation with one client is now
           a page in each file and a person to guess at.

Attempt 6  Export the tags and the merge history.
           Gone. Every duplicate decision made over three years, which record
           was kept and which one was folded into it, is in no file at all.

Attempt 7  Ask for a full account export.
           This one works. Format on request, five to ten business days. Free.
```

Seven attempts, and the honest result is not that the software refuses to let you go. Most modern tools will hand you a file. The result is that the file is a skeleton. You get the names and the numbers, and you leave behind the context that made them worth keeping: the dates inside the notes, the meaning of the stages, the rules that were doing the work, and the history that told you which duplicate to trust.

## What you own, and what you rent

This is the sentence worth keeping: you can export the records, and you cannot export the context.

The records are rows in a table. The context is the thing that made the table worth having. The vendor almost never has to hide the export button, because the skeleton on its own is not worth the move. You open the file, work out that rebuilding the context is a two-week job nobody has time for, and stay another year.

That is the lock. It is not a password and it is not a contract clause. It is the gap between what leaves and what it would cost to rebuild what stayed.

## Why the gap is so wide

The gap is wide because your client's history was never in one place to begin with. The contact sits in the CRM. The conversation sits in a text thread and an inbox. The dates sit on a calendar that belongs to a phone. The documents sit in cloud storage under a surname spelled two different ways. Even a perfect export out of one tool hands you a quarter of a person, and the other three quarters are exactly where they always were.

That is [the integration problem](https://birkystudio.com/blog/integration-hell-real-estate-ai-agent/) seen from the exit instead of the entrance. You were the only thing ever holding the four pieces together, and that is why leaving is a project rather than a click.

## What we do differently, and where it shows

The Base Agent takes the opposite position on purpose: the records it keeps are designed to survive us.

- **It runs on your own server, not ours.** You are not renting a seat inside our application. The machine doing the work is yours, and so is everything on it.
- **The CRM is a Notion workspace built for your business.** Notion exports a workspace natively, so contacts, notes and pipeline come back out in a form a human can still read. Your records are yours in the plain sense of the word.
- **The follow-up rules are written down for you, not sealed inside a builder.** You should be able to see what is doing the work, which also means you can carry it somewhere else if you ever want to.
- **The context gets captured at the source.** Exports feel hollow because the detail was never written down anywhere. A system that logs the call and the message as they happen is the only thing that makes an exit file worth having.

If the honest picture of your week is four tools and one person holding them together, the [Base Agent](https://birkystudio.com/products/ai-agent-setup/) is the product that fixes it at the root, and a clean exit file is a side effect of doing that properly. It is **$1,297 one-time** including the Notion CRM and 30 days of support, from **$2,997** for a business with staff.

## Five things this will not fix

- **It will not clean up another vendor's export.** If your data is trapped in a tool that only ships a skeleton, we cannot un-trap it from here. Some of that rebuild is manual, and I will tell you so before you pay us anything.
- **It will not turn old records into new ones.** Cleaning a three-year-old database is a job of its own, and it is better done before the move than after, [which is a whole post of its own](https://birkystudio.com/blog/crm-database-rot-what-to-keep/).
- **Notion is still a third party.** Your workspace is yours and it exports natively, which is the point, but it is a hosted service like any other and it can change its terms. Owning your data is not the same as running your own database, and I am not going to pretend otherwise.
- **It cannot recover what was never recorded.** No system returns a record that was never written. It stops the loss from here forward.
- **I will not quote you a switching cost.** Every stack is different, and anyone who tells you the move will take "two days" without opening your files is guessing out loud.

## What it costs

The Base Agent is **$1,297 one-time** for a solo operator and from **$2,997** for a business with staff, with the Notion CRM and 30 days of support included rather than sold as extras. Care & Maintenance is **$97/mo** if you want us keeping it running and tuned, and the Business AI Partner is **$197/mo** for ongoing work.

[Book the free 15-minute audit](https://birkystudio.com/contact/) and bring the tool you are currently stuck inside. We will look at what it will actually give you on the way out, and if the honest answer is that you should stay where you are, we will say so.

## Try it

**Start with the free one.** The [Quick Log template](https://birkystudio.com/quick-log-template/) is a plain one-page format for writing down what happened with a client in under a minute. Free, it takes an email, and it is the smallest version of the record that makes any export worth having later.

**Then hear what catching the detail sounds like.** The [voice demo](https://birkystudio.com/voice-demo/) connects you to Elliot, our AI receptionist, in one click. No login, no form, no sales call. Ask him what a client would ask.

**And if you would rather keep your own system than rent one,** [THE REAL ESTATE SYSTEM](https://notionforrealestate.gumroad.com/l/ocuwss) is the Notion build we sell as a one-time download. It lands in your own workspace, which is the whole argument of this post in a single purchase.

**Where the same idea applies to your website,** [Self-Editing CMS](https://birkystudio.com/products/self-editing-cms/) ($130 one-time) lets you change the text and swap the photos on your own site, with no ticket and no waiting on us. Your property should not need a gatekeeper either.
