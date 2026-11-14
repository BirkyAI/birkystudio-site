---
title: "AI Audit Trail: Who Approved the Message?"
description: "The ARA wants a licensed human accountable for AI-sent messages. Here is the audit trail a typical lead-response stack is not keeping, and why it matters."
date: 2026-11-14
image: "/images/blog/ai-generated/ai-audit-trail-who-approved-the-message.jpg"
tags: ["Birky Studio", "AI Agent", "Compliance", "Workflow"]
lang: "en"
author: "Luna Jerney"
---

## The rule is not the hard part

On November 12 someone posted this to r/RealEstateTechnology:

> "The rule only works if someone defines 'licensed work.' Answering a buyer's question about a listing, booking a showing, and discussing price all sit at different points on that line. For anyone building lead-response or assistant tools, the practical side is the audit trail. You'd need a record of which messages the AI sent, which a licensee approved, and what the agent could see when they signed off."

The headline is the proposal: the American Real Estate Association (ARA) wants licensee-in-the-loop language, a licensed human staying accountable for AI that performs licensed work. There is no federal license, so the plan is model language taken to state legislatures one at a time.

Read the quote again, though. Two problems fall out of it, and only one of them is about law.

The first is that "licensed work" is undefined. Answering a question about a listing, booking a showing and discussing price are three different things sitting at three different points on the same line, and nobody has drawn the line yet. The second problem is that the record does not exist. A rule that says a licensee must approve the message is unenforceable, and unprovable, if no system can show which messages went out and who saw them before they did.

The first problem will be solved by somebody with a committee and a legal department. The second one is yours, in your own inbox, this week.

## One normal week

*The list below is a composite, built from message threads I have read and written in my own lead flow. The names change. The pattern does not.*

```
One week of messages from a lead-response stack

Mon 08:12  Is the house on Elm still available?      [assistance]        sent, no approval on file
Mon 09:40  Can we see it Saturday morning?           [assistance]        sent, no approval on file
Mon 14:05  How much would you offer for it?          [needs a licensee]  sent, no approval on file
Tue 11:20  What are the HOA dues on this one?        [assistance]        sent, no approval on file
Tue 16:48  Do you think it will appraise at list?    [needs a licensee]  sent, no approval on file
Wed 10:02  Has the seller had other offers?          [needs a licensee]  sent, no approval on file
Thu 13:30  Can you send me the floor plan?           [assistance]        sent, no approval on file
Fri 09:15  Should I waive the inspection?            [licensed activity] sent, no approval on file
Fri 17:44  What would you do if you were me?         [licensed activity] sent, no approval on file
```

Nine messages in five days. Four of them are pure logistics: availability, a time, a document, a fee that is written in the listing notes and can be looked up in ten seconds. Three sit in the middle, where the honest answer starts to lean on your read of the deal. Two are advice on a decision the buyer owns and a licensee has to stand behind.

Now read the last column again, top to bottom. It says the same thing nine times.

That is the failure, and it is not a failure of the AI. The tool answered all nine, quickly, which is exactly what it was bought for. The failure is that after the fact, nobody in that chain can answer two very ordinary questions. What did it send? And who approved that?

Ask those two questions of a typical stack and the answers are: you can probably scroll far enough to find some of them, and nobody knows. If a broker asks you to show your work on a Friday message, you would be reading a chat thread out loud and hoping the timestamps line up.

## What the record actually has to carry

A message record is not a transcript. A transcript tells you what was said. The thing a licensee-in-the-loop rule needs is five facts attached to every message that leaves in your name:

1. **Which message it was**, and whether it went out unedited or as a draft.
2. **Who or what sent it**, meaning the agent or the human, by name.
3. **Which licensee approved it**, if a human approval was required.
4. **What that person could see when they signed off**: the customer's question, the notes the answer was drawn from, and the reply itself.
5. **When all of that happened**, in one timeline.

Four of those five are cheap. The one that nobody's stack has is the fourth, because "what the agent could see at sign-off" is a design decision, not a field you can bolt on later. If the AI hands a human a draft with no source attached, the human approves a sentence, not a decision, and there is no record that distinguishes the two.

## What ours writes

When the agent routes a message to a human, this is the record it keeps. This is one real message from the same kind of week, shortened:

```
Message record, Friday

drafted       09:15:22   AI agent, draft only, not delivered
routed        09:15:23   flagged: advice on the inspection contingency
approved      09:26:10   licensee approval on file
what they saw  the buyer's question, the listing's inspection notes, the draft reply
delivered     09:27:04   reply sent, unedited
```

Five facts, one timeline, and the line listing what they saw is the one that matters. The approval is attached to a question and a source, not to a sentence floating in a chat window.

Every product we ship publishes the rules it runs under, and the rules are usually short. The [Review Engine](https://birkystudio.com/products/review-engine/) is a fair example: it is not allowed to ask for a positive review, it is not allowed to message only the happy clients, and it will not send a text without documented consent. Those are not settings you can switch off. They are the product, $497 to set up and $97 a month.

## What the agent does

- **Sends the logistics itself.** Availability, viewing times, the fee that lives in the listing notes. Four of the nine in that week never needed a human in the first place, and they leave in seconds, at 08:12 on a Monday, when nobody is awake to approve anything.
- **Parks the grey zone and the advice.** Anything that touches price, condition, contingencies or what the buyer should do gets drafted, flagged and held, with the source notes attached.
- **Writes down what the human saw.** Not that approval happened, but which question and which notes were on the screen when it did.
- **Keeps one running record per client**, so the thread is a file you can read and not a scroll you have to reconstruct.
- **Exports on request.** If a broker, a client or a regulator asks for a week, you hand over a list rather than a memory.
- **Reports the gap.** If a message sat unanswered for two days because it was waiting on a human, the record says two days.

I have written before about the messages that never get logged at all and what those missing notes cost later ([The Note You Didn't Write Is Costing Deals](https://birkystudio.com/blog/phone-note-chaos-transaction-calls/)). This is the same problem after the fact: the note has to exist before anybody asks for it.

## What it will not do

- **It will not tell you where your state's line is.** Nobody has drawn it yet. Anyone who draws it for you during a sales call is selling certainty they do not have.
- **The log does not make you compliant.** It makes you able to show your work. Those are different claims and I am not going to blur them.
- **It cannot record the call you took yourself** on your own phone in the car. If the licensed decision happened there, it happened off the record.
- **It will not decide what may be sent.** You set the rules once, deliberately, and it holds them. If you want the agent to answer price questions on its own, that is your call to make and your name on it.
- **It refuses to quote a compliance-risk figure.** Nobody knows what a rule that has not been written yet will cost you, and anyone who gives you a number has invented it.

## The honest order of operations

Two products, and it matters which one comes first.

The Custom Assessment is $349 for a solo agent, or $999 with staff, and it credits back against whatever you build. The first thing we do in it is not a recommendation, it is a read: what your messages are made of, what your current tool sends on its own, and what your stack would be able to produce if a broker asked you about last Tuesday.

Then the build. The Base Agent starts at $1,297 one time for a solo practice, including the Notion workspace that holds the record, and from $2,997 for a business with staff, with 30 days of support while it beds in. Keeping it running is $97 a month, or $197 for a partner who keeps changing it as your rules change. If the messages are going out on text or WhatsApp, that is the $297 Text Receptionist; if you want your own line answered and logged, that is the $550 Voice Receptionist.

We have refused work before when it was the wrong purchase, and the reasoning has not changed ([Refusing to Sell You These AI Agent Mistakes](https://birkystudio.com/blog/we-refuse-to-sell-ai-agent-mistakes/)). If your volume is twelve messages a week and you answer all of them yourself, a record is still worth having and you do not need to pay for a robot to make one.

## Try it

Start with the free piece. The [Quick Log template](https://birkystudio.com/quick-log-template/) is the plain one-page record I use for exactly this, and it takes about four minutes to set up. Reading it will tell you more about your own gaps than this post can.

If you would rather hear it working, call [Elliot, our AI voice agent demo](https://birkystudio.com/voice-demo/). It answers, qualifies and books, with no login needed. Then try the [WhatsApp AI agent](https://wa.me/50234775110) with something awkward from your own business and watch what it writes down.

If you want to know what your current stack would actually hand over, the [Custom Assessment](https://birkystudio.com/products/custom-assessment/) is where that starts, $349 for a solo agent or $999 with staff, and it credits back against whatever you build afterwards.

If you would rather just show me, [send me a note](https://birkystudio.com/contact/) and describe one week of your messages. That is the conversation the assessment starts from.
