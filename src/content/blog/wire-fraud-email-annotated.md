---
title: "Wire Fraud Email: Annotated Line by Line"
description: "A fake wiring-instructions email, printed and annotated line by line. Five of its six tells prove nothing, and the only decisive check is a phone call."
date: 2026-10-30
image: "/images/blog/ai-generated/wire-fraud-email-annotated.jpg"
tags: ["Birky Studio", "AI Agents", "Real Estate", "Closing Security"]
lang: "en"
author: "Luna Jerney"
---

There is a line from the r/RealEstateTechnology thread on closing security that has stayed with me since September: *wire fraud barely comes up, despite losses running into the hundreds of millions annually.*

Ask why, and the first answer is always the same: because most people do not know what the fake looks like.

I do not believe that any more. I think the problem is that everyone has been taught to spot a fake wiring email by **reading** it, and this generation of fakes cannot be caught by reading. So let me print one and go through it line by line, because the annotations are the argument.

*The email below is a composite. The wording, the amounts and the timing are illustrative. The pattern is not.*

```
From: Maria Alvarez, Escrow Officer <escrow@firstcap-title-closings.com>
To: Daniel Reeves, Buyer
Cc: Listing Agent, Loan Officer
Subject: UPDATED wiring instructions, please confirm receipt today

Hi Daniel,

Following a system migration at the title company, our escrow account
number has changed. Please use the details below for the funds due
Friday. The previous account is closed, and any transfer sent there
will be returned, which could delay your closing.

Bank: First Capital Bank
Account name: First Capital Title Escrow Services LLC
Routing: 021000021
Account: 4417 8092 1136 44
Wire amount: $68,400.00

Please confirm receipt of this email today so we can release the file.
If you have questions, reply here and I will pick it up.

Thank you,
Maria Alvarez
Escrow Officer, First Capital Title
(555) 214-8890
```

## Six tells, and five of them prove nothing

Here is what a careful person notices, in the order they notice it. I will be straight with you about what each one is worth.

**1. The domain does not match the title company's website.** `firstcap-title-closings.com` is not `firstcapitaltitle.com`. Inconclusive on its own. Small businesses run on hyphenated marketing domains, third-party sending platforms, and CRM systems that send on a vendor's behalf every single day. A lookalike domain costs less than lunch.

**2. The urgency.** "Please confirm receipt today." "So we can release the file." Inconclusive. Closing week is urgent. Every escrow officer in the country sounds like this on a Thursday.

**3. The reason given for the change.** "A system migration." Inconclusive, and slightly comforting, because it is plausible. Migrations happen. Title companies get bought, change banks and move software.

**4. The completeness of the details.** Full account name, routing number, account number, exact amount, no formatting oddities. Inconclusive. A genuine email contains exactly the same fields. A fake that got the format wrong would be spotted by an eight-year-old, which is why the fakes do not get the format wrong.

**5. The signature block.** Real name, real title, direct line, spelled correctly, matching the person the buyer has already spoken to. Inconclusive. A signature block is copy and paste.

**6. The line that does the actual work.** "The previous account is closed, and any transfer sent there will be returned, which could delay your closing." Read it as an instruction and it says: the safe thing is also the risky thing. It is the sentence that turns a two-minute phone call into a decision about whether you are the reason the closing slips.

That is the whole email. Five items that a careful reader would flag and then talk themselves out of, and one sentence that punishes them for slowing down.

## The only test that cannot be copied

Every identifier in that message is copyable: the display name, the signature, the bank, the account name, the tone, the reply-to, and the history itself if the thread was compromised three weeks earlier. That is what changed. The fake is no longer written by someone guessing at how a closing sounds. It is copied from the real thing, because copying is easier than inventing.

So the test cannot live inside the email. The one thing a fraudster cannot answer is a question asked on a phone line you already had:

**Call the title company on the number in your own contact record. Ask a question only they could answer. Confirm the account ending. Then write down the time, the name of the person you spoke to, and what they said.**

That is it. Two minutes, and the scam collapses, because nobody can spoof the sound of the actual escrow officer answering her own desk phone.

Here is the honest part. Almost everyone reading this already knew that. The reason it still fails is not ignorance. It is that the check has no owner, no deadline, and it lands in the worst week of the month, which is exactly the week it needs to happen. I wrote the process version of this in [the five-minute closing rule](/blog/wire-fraud-five-minute-closing-rule/): who is assumed to own each step of a closing, and the one step with nobody's name on it. This post is about something narrower. Even when the check happens, the answer usually dies on the phone.

## The worst week of the month is also the handoff week

There is a second thread worth reading alongside that one, from an agent describing the agent-to-coordinator handoff: *almost nothing is built for the messy, context-heavy moment right after a deal goes under contract, when the most important information is still living in someone's head.*

Notice when the wiring instructions land. They land in that window. The buyer has signed, the file has moved from the agent to the transaction coordinator, the thread has been forwarded twice, and the person now holding the most risk is the one with the least context to judge it. Buyers wire money maybe twice in their lives. The people who run closings every day are the ones in a position to notice something is off, and the current process quietly hands the risk to the buyer and hopes for the best.

This is why "we called title and confirmed" is not enough on its own. Confirmed by whom, when, and where is that written? If the answer is a phone call and a memory, the next person inherits nothing, and a forged message that arrives on Friday afternoon finds a file with no verified version to compare against. The [post-contract handoff sheet](/blog/post-contract-handoff-sheet/) is the smallest version of the fix: one page, seven fields, so the stuff that lives in someone's head survives the handoff.

## Where a Birky Studio agent actually fits

I am not going to sell you an AI agent as wire fraud protection. It cannot confirm a wire. Only a person can do that, on a phone.

What the [Base Agent setup](/products/ai-agent-setup/) does is remove the three conditions that make the scam work:

- **One running record per deal.** Every call, text, email and WhatsApp message summarized into a single thread attached to the file. A message that does not match the real thread stands out, because there is a real thread to be measured against.
- **Flags on payment details.** Anything touching wiring instructions or account numbers gets pulled out of the pile and pushed to a human with the check attached, instead of sitting in an inbox where a tired person has to notice it.
- **Enforcement instead of memory.** The verification step fires every time, and the confirmation lands in the record with a timestamp, so it does not depend on the one person who remembers the rule at 10am and forgets it by 4pm.

That last point is the one that matters here. The rule was never the hard part. The record of the rule being followed is what protects you, and it is the piece that a phone call, on its own, never produces.

## What this costs next to one intercepted wire

One spoofed wire is a six-figure loss for somebody, plus legal fees, plus a client relationship, plus the referrals that buyer would have sent you for the next decade.

The tools are not six figures:

- **Text Receptionist, $297 one-time.** Answers and logs every inbound message, so nothing lives only on one person's phone.
- **Voice Receptionist, $550 one-time.** Picks up the call nobody can, captures the details, writes them down.
- **Base Agent, $1,297 one-time**, including 30 days of support and the Notion CRM. The full build: every channel in one place, automatic logging, and enforcement rules shaped around how you already run a transaction.

You do not need the most expensive option to close this gap. You need one system that writes things down where the next person can find them.

## Try It. Here's Your Next Step

**Start with the free thing.** Grab the [Quick Log template](https://birkystudio.com/quick-log-template/). It is the single-note-after-every-call habit that turns scattered channels into a record you can actually check, and it is the same habit that makes a forged message obvious. It costs you an email and nothing else.

**Then hear the verification layer out loud.** Call [Elliot, our AI voice agent demo](https://birkystudio.com/voice-demo/). One click, no login, a real conversation. Ask it anything a nervous buyer would ask, including the awkward questions, and you will hear why "it answered and wrote it down" matters more than it sounds.

**Put the closing protocol on paper.** [THE REAL ESTATE SYSTEM](https://notionforrealestate.gumroad.com/l/ocuwss) is the Notion setup we use for transaction tracking, checklist included, so the next change of wiring instructions meets a process instead of a gut feeling.

**And close the loop after the money moves.** A deal that closes well is also the moment a client decides whether to say anything about you at all. The [Review Engine](/products/review-engine/) sends the ask on day 1, day 3 and day 7 and again six months later, from your own Google Business Profile, with the detail of the deal already in the note, so the review that comes back is about your client's closing instead of a template.

Want this mapped to how your brokerage actually closes? [Book a quick call with Birky Studio](https://birkystudio.com/contact/) and we will walk your closing week and point at the exact step where ownership is missing.

---

*Related reading: [Wire Fraud: The 5-Minute Closing Rule](/blog/wire-fraud-five-minute-closing-rule/), [The Handoff Sheet Your Deals Are Missing](/blog/post-contract-handoff-sheet/), and [The Note You Didn't Write Is Costing Deals](/blog/phone-note-chaos-transaction-calls/). New to the category? Start with [Best AI Receptionists for Real Estate](/best-ai-receptionists-real-estate/).*
