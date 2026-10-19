---
title: "The Published List Is Not the Truth"
description: "Official lists are incomplete more often than they are wrong. Here is how to verify a published record before you plan a week around it."
date: 2026-10-19
image: "/images/blog/ai-generated/published-list-is-not-the-truth.jpg"
tags: ["Birky Studio", "AI Agents", "Data", "Automation"]
lang: "en"
author: "Birky Studio"
---

An agent on r/RealEstateTechnology put it better than any vendor deck could:

> *"My county publishes upcoming foreclosure sales but the list isn't always accurate. Sometimes I'll show up to auctions and they will announce sales that weren't included on their published calendar."*

Read that again, because the interesting part is not that a government website is imperfect. The interesting part is that the list was **official**, and that is exactly why he trusted it.

He planned his week around it. He lost the week.

## Official is not the same word as accurate

I have spent enough years in operations to know how these lists get made. Somebody at the county maintains a spreadsheet. A sale gets added, a date moves, a filing gets pulled at the last minute, and the public page updates when someone remembers to update it. Nobody is lying. The list is simply a summary of a process that keeps moving after the summary was written.

The same shape shows up everywhere in this business. The MLS status says active on Tuesday, and the seller signed something on Monday. The permit list says a project is under review, and the hearing already happened. The showings calendar says the unit is available, and it rented over the weekend. Every one of those is a published list that is *mostly* right, and mostly right is the most expensive kind of wrong there is, because it looks trustworthy enough that you stop checking.

Missing information makes you careful. Incomplete information makes you confident. Confidence is what costs you the trip.

## What the list says versus what the record says

Here is the same week, in the two versions you can actually get. I have simplified the entries. The pattern is real.

| What the published list says | What the source record says | What it costs you |
|:--|:--|:--|
| Sale scheduled Thursday 10:00am, parcel 04-113-022 | Notice of postponement filed Monday, new date in November | A morning, a drive, and a slot you told a client you would hold |
| Three sales this week in the county | Five dockets opened, two never made the calendar | The two you never knew to look at |
| Property is one address, one parcel | Same house under three address formats and two APN versions | A CMA that pulls the house twice, a follow-up that goes to the wrong file |
| "Under review" | Hearing concluded, approval recorded six days ago | The window where the useful call could have been made |

That last row is the quiet one. By the time a list catches up to reality, the part where knowing earlier was worth money is already gone.

## The duplicate problem sits under the missing-data problem

There is a second layer, and it is worse, because you cannot see it by checking one source at a time.

The same property does not look the same in three systems. MLS writes `123 N Main St Unit 4`. The assessor writes `123 NORTH MAIN ST #4`. The recorded deed writes `123 N Main #4`. Parcel numbers do not rescue you either, because APN formats differ by county, some drop leading zeros, and parcels get split or merged until last year's identifier simply does not exist.

I wrote a full teardown of that in [One House, Three Records](/blog/duplicate-property-records-cost-you-deals/), so I will not repeat it here. The point for today is this: a verification layer is not one check. It is a check against a source *and* a way of knowing that the thing you verified is the same thing you already have on file.

## What verification actually looks like

Not a new dashboard. A short, boring loop that runs whether or not you remember it:

1. Pull the record from the source, not from the summary.
2. Match it to the one canonical record you already hold for that property or person.
3. Compare it to what you had yesterday and surface only what **changed**.
4. When two sources disagree, flag the conflict and keep the link back to each original, do not silently pick a winner.

Step three is the one everybody skips, and it is the only step that saves you a trip. A list you have to re-read from scratch every morning is not verification, it is homework. What you want is the difference: this one moved, that one was cancelled, this one is new since yesterday.

Step four is where most tools quietly do damage. Fuzzy matching a conflict away feels clean and produces a record that is confidently wrong, which is a worse outcome than a duplicate. I would rather see a flag than a guess.

## Where this fits in a real stack

The agent I build for a client does this on a schedule rather than on memory. It watches the sources you name, keeps one record per property and per person, notes what changed since the last pass, and puts a short list in front of you each morning instead of a wall of new rows.

For prospect data the same principle runs through the [Lead Generation Pack](/products/lead-generation-pack/): one record per person, deduplicated before it reaches your file, with the source kept so you can check it yourself. A list you cannot trace is not an asset, it is a liability with good formatting.

And for the outreach that follows, the [Outreach Engine](/products/outreach-engine/) runs off that single clean record, so the same person does not get emailed twice from two slightly different names.

None of this makes a county publish better data. It makes you the person who checked.

## What this will not do

I am not going to pretend the system fixes the source. Four honest limits:

- If a county never publishes the change, no tool can invent it. A sale announced at the podium is announced at the podium.
- If a parcel was split and no feed reported the split, the link between old and new records is a judgment call, and it gets flagged for a human.
- It cannot verify what it was never connected to. A list living in someone's head or a printed handout is outside the loop.
- I will not quote you a match-accuracy percentage. Your match rate depends on the quality of your county's records, not on my software. Anyone giving you a clean number for that has not looked at your county.

What it will do is narrower and more useful: it will stop you from planning a week around a list that changed on Monday, and it will tell you which of your records are not the same record.

## The cheapest habit in this whole business

Check the source before you plan the week. Not because the published list is a lie, but because it is a summary, and summaries go stale at the exact moment they matter most.

If you are doing that by hand across four sources and two spreadsheets, that is the first thing I would automate, before anything else in the stack.

## Try it, or just test the thinking

**Start free:** the [Quick Log template](https://birkystudio.com/quick-log-template/) is the one-page structure I use to keep a running record per client and per property. No sales call, no login.

**Call the voice demo:** [Elliot answers on this page](https://birkystudio.com/voice-demo/) and books a showing like a real receptionist. It is the fastest way to hear what a live agent sounds like before you spend anything.

**Or message the WhatsApp bot:** [wa.me/50234775110](https://wa.me/50234775110) runs the same logic over text. Ask it something awkward on purpose and see what it does when it does not know.

If you want the version that watches your sources and hands you the difference each morning, [tell me which lists you plan your week around](https://birkystudio.com/contact/). That conversation is free, and it usually takes one call to find out whether it is worth building at all.
