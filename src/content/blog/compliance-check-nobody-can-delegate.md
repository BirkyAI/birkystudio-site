---
title: "The Compliance Check Nobody Can Delegate"
description: "A first-pass building code check runs three to six hours per project, with no junior to hand it to. What an AI agent can take off that sweep."
date: 2026-11-11
image: "/images/blog/ai-generated/compliance-check-nobody-can-delegate.jpg"
tags: ["Birky Studio", "AI Agent", "Small Business", "Compliance"]
lang: "en"
author: "Luna Jerney"
---

## The clause in the middle of the sentence

> "From the independent BCIN designers I've talked to, it's often 3 to 6 hours per project, and with no junior to delegate to, it all lands on you... Has anyone tried software for a first-pass check, and how did it go?"

A designer working in Ontario wrote that in r/RealEstateTechnology. Most people reading it stop at the hours. Three to six hours is most of one working day per project, and if you run four packages a month, that is four days gone before anything has been sent anywhere.

The clause that matters is the short one: **no junior to delegate to.**

Here is the thing about this particular step. You can hand off almost everything else. Someone else can draft, model, document, schedule, answer the phone. You cannot hand off verification, because verification is the thing your seal is sitting on. A junior can draw a stair. A junior cannot carry the risk of a stair that is three centimetres short. So the check stays exactly where the liability is, with the one person in the business who has the least time to spare and the most to lose by rushing it.

*What follows is a composite. The code items are the ones I watch come back on real drawing packages. The review wording is mine.*

## What a first pass actually hands back

A designer asking "has anyone tried software for this" is usually picturing a black box that stamps a drawing. That is not what a first pass looks like. It looks like a list.

```
FIRST-PASS CHECK, drawing package 24-117
Checked against: provincial building code, Part 9

 1. Rear bedroom window opening 0.31 m2          under 0.35 m2 CONFIRM
 2. Basement stair headroom    1.87 m           under 1.95 m  CONFIRM
 3. Rear deck guard height     0.98 m           meets 0.90 m  CLEAR
 4. Garage fire separation     absent from plan               CONFIRM
 5. Smoke alarm locations      noted            rooms missing CONFIRM
 6. Attic insulation value     R-40 stated      meets minimum CLEAR
 7. Window schedule            2 of 9 types     missing       CONFIRM
 8. Main entry door landing    no issue found                 CLEAR
 9. Second-floor living room   no changes                     DESIGN
```

Nine lines instead of a full read of the set. Five items to confirm, three cleared outright, and one that was never a code question in the first place.

Read the last column again, because the value is not in the five. **The value is in the three.**

- **Items 1, 2, 4, 5 and 7 to confirm.** Each one needs a human eye for about two minutes. The numbers are computed and the decision is not. Item 4 is worth pausing on: the garage fire separation is not wrong on the drawing, it is absent from it, and an absence is the hardest thing for a tired reader to notice at hour three.
- **Items 3, 6 and 8 cleared.** This is the part nobody expects to matter, and it is the part that returns the hours. Deleting a confirmed item from your mental stack is the whole product.
- **Item 9 is a design choice.** Whether the living room moves is your client's call. A first pass that flagged it as a code defect would be wrong, and you would stop trusting the next one it sent you.

## The honest arithmetic

I am not going to tell you this turns six hours into forty minutes. I have not measured your projects, and neither has anyone selling you a version of this. When a number like that appears in a demo with no documented measurement attached, it was invented for the slide.

What I can describe is the shape of the change. The sweep stops being one long read in which attention is the only tool, and becomes a short list you work, most of whose lines are already answered.

## The tools that survive are the boring ones

There is a reason this kind of software rarely demos well. It is not exciting. It does not add a dashboard, or a workflow, or a place to type. It reads a document and hands back a shorter document.

That is exactly the profile of the technology that actually stays in a professional's week. E-signature replaced print, sign and scan. A shared calendar replaced the paper diary. A digital lockbox replaced the drive across town. None of them were interesting, and all of them quietly removed a step that used to be somebody's afternoon. I wrote about that pattern in [The AI You Forget You're Using](https://birkystudio.com/blog/the-ai-you-forget-youre-using/), and a compliance first pass belongs in the same category.

## What the agent does on a package

- **Reads the drawing set you already have.** PDF, plan set, schedules, notes. Nothing gets redrawn and nothing gets retyped.
- **Checks the items that are checkable.** Egress openings, stair and guard dimensions, headroom, insulation and seal values, fire separation, smoke alarm placement, schedule completeness.
- **Returns a triaged list, not a verdict.** Confirm, clear, or design call, with the number each line was checked against so you can verify the check itself.
- **Shows its reasoning.** If an item reads clear, you can see what it was compared to. A first pass you cannot audit is a first pass you will not use twice.
- **Keeps the checklist current.** Code editions change, and a checklist that was right in 2023 is a liability in 2026. That upkeep is the part of the work that maintenance covers, and I wrote about why that half never makes it into a demo in [What Happens After Your AI Agent Goes Live](https://birkystudio.com/blog/what-happens-after-your-ai-agent-goes-live/).
- **Logs what was flagged and what you decided.** When the same item comes back on the next package, you can see whether it is your detail or your client's habit.

This is the Base Agent doing document work, and it starts at $1,297 one time for a solo practice, including the Notion workspace and 30 days of support while you get it bedded in. The full scope is on [The Base Agent](https://birkystudio.com/products/ai-agent-setup/).

If you want the simpler question answered first, whether this step is even worth automating, run it through the four questions in [What Deserves Automation (And What Doesn't)](https://birkystudio.com/blog/what-deserves-automation/). A first pass on a drawing package passes all four, which is why it is on this list at all.

## What it will not do

- It will not seal, stamp, certify or sign anything. Ever. The judgment stays with the professional, and the seal stays with you.
- It will not tell you the code is satisfied when a plan is silent. An absence comes back as a question, which is the honest answer.
- It will not make a design decision. Item 9 exists to show you what a tool looks like when it knows the edge of its own job.
- It will not replace your own read on a high-risk package. If something in the set worries you, that worry outranks the list.
- It will not quote you an hours-saved figure. I refuse to invent that one when the only projects I can honestly measure are my own.

## Try it

Start with the free piece. The [Quick Log template](https://birkystudio.com/quick-log-template/) is the same running record I use to keep one project's decisions in one place, and it takes about four minutes to set up.

If you would rather hear a version of this working, call [Elliot, our AI voice agent demo](https://birkystudio.com/voice-demo/). It answers, asks the qualifying questions and books itself, with no login needed. Then try the [WhatsApp AI agent](https://wa.me/50234775110) with something awkward from your own business and watch where it lands.

And if the leak is not the check but the quotes sitting unanswered in your inbox, that is a different job: the [Outreach Engine](https://birkystudio.com/products/outreach-engine/) runs the follow-up on the inquiries you meant to get back to, $797 one time.

Want to talk through what a first pass would look like on your own drawings? [Send me a note](https://birkystudio.com/contact/) and describe one package.
