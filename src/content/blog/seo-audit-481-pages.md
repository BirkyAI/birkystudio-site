---
title: "481 Pages, 443 Broken Titles: SEO Audit"
description: "We audited 481 pages across two sites. 443 titles were truncated in Google, 16 orphan pages were live, 11 share images were dead. None of it was visible."
date: 2026-09-16
image: "/images/blog/ai-generated/seo-audit-481-pages.jpg"
tags: ["Birky Studio", "SEO", "Case Study", "Website Audit"]
lang: "en"
author: "Birky Studio"
---

You know how the mechanic's own car is always the worst one on the street?

That was us. Last week.

We sell SEO and website work. And when we finally ran a real audit across our own two properties — this site and our real estate development site — we found **443 broken page titles.** Out of 481 pages. Ninety-two percent of the site was quietly broken in a way nobody could see.

I want to be honest about how that felt, because I think the honesty is more useful to you than a victory lap.

## The part nobody warns you about

There is no feedback loop in this work. You publish something, and then you wait six weeks to find out if you made the right call. By the time you learn, you've made forty more decisions on top of it.

Google's documentation changes constantly. The rules that actually matter aren't in one place. To fix our own site, I had to pull from two different Google pages, two different Schema.org patterns, and our own Search Console data — and piece it together.

That's not a small-business-owner problem. That's a *nobody-has-time-for-this* problem. Agencies charge four figures a month and still ship this stuff broken.

So if you've ever looked at your website, felt vaguely uneasy, and closed the tab — you're not bad at this. You're a normal person reacting correctly to something genuinely unreasonable.

## What the audit actually found

We crawled every URL on both sites. Here's the real list, unedited:

**443 page titles were cut off in Google search results.**
Google truncates title links at roughly 60 characters, and it cuts from the *end* — exactly where your differentiator sits. Ours was the site name, repeated on almost every page. So Google was showing customers things like "AI Voice Receptionist for Small Businesses — Rea" and then nothing. Every single search result for our business looked unfinished.

**16 property pages were being actively promoted to Google.**
This one is worse than it sounds. On our real estate site, 16 listings had been marked sold or hidden. The listing pages correctly hid them. But the *detail pages* were still being built and still submitted to Google in the sitemap. So we were advertising properties that were already gone — to a site where buyers couldn't reach them from anywhere. No internal links. No menu path. Just orphan pages out there collecting dust in search results.

If you've ever wondered why a listing site feels stale, that's usually why. Nobody's checking.

**11 images that share your pages were dead.**
Every time somebody shared our pages on LinkedIn, Facebook, or WhatsApp, the preview card was blank. The link to the image file pointed to something that didn't exist. Seven weeks, on one page, before anyone noticed.

**A blog post had been live with a broken hero image.**
The file was saved as `outsourced-isa-prospecting-zero-deals.jpg`. The post pointed at `outsourced-prospecting-zero-deals.jpg`. One word difference. The image 404'd, the post looked broken, and our Facebook auto-poster had silently posted it as text-only — with no image at all.

**Our homepage had no brand signal.**
Technically: no `WebSite` schema, no `og:site_name`. Practically: nothing telling Google "this website is a business called Birky Studio." Google was guessing.

## What this costs you (and what I won't claim)

Here's where I'm going to be careful, because most agencies wouldn't be.

I can't tell you "fixing titles increased our traffic 47%." We fixed these on a Tuesday. SEO takes weeks to move, and if I quoted you a number today I'd be making it up. You'll notice a lot of marketing copy does exactly that.

What I *can* tell you is what a truncated title does, mechanically:

- Your title is your ad. It's the headline Google shows when deciding whether to click. Ours was cut off mid-word — so the decision was being made on an unfinished sentence.
- A page with no internal links is a page Google eventually stops trusting. We were asking Google to rank pages we ourselves wouldn't link to.
- A blank share card means every time a customer forwarded your link, it looked like spam.
- A missing brand signal means Google displays a guess instead of your name.

None of these are dramatic. That's the point. They don't break your site. They just quietly tax every single visitor, forever, and you'd never know.

## Why this happens to good businesses

Three reasons, and none of them are laziness:

1. **Nothing enforces it.** You can write a 97-character title and the site will publish it happily. No error, no warning. It looks fine on your screen because browsers don't truncate — only Google's results page does.
2. **It's invisible.** A broken link 404s and you notice. A truncated title renders *perfectly.* It just gets cut when a customer sees it. You are the one person who will never notice.
3. **It's spread out.** Title limits live in Google's docs. Image paths live in your code. Sitemap logic lives in your build. There is no single dashboard that says "your site is unwell."

## What we changed

We fixed all 443 titles. We rewrote the sitemap logic so sold and hidden listings exclude themselves automatically — instead of relying on someone remembering. We set hidden pages to `noindex` so they stay reachable for anyone with an old link but stop competing in search. We generated the missing images and pointed the broken references at files that actually exist. We added the brand schema.

Then we did the thing that actually matters: **we installed a watchdog.**

Every Monday morning, a script crawls all 481 pages and checks titles, descriptions, images, canonicals, and indexation. If everything's clean, it stays silent and I hear nothing. If something breaks, I get an alert.

That's the real fix. Not the 443 rewrites — those will erode. The fix is that **nobody has to remember anymore.** I've stopped being the integration between my own systems, which is the same thing I tell every client.

## The honest takeaway

You probably have some version of this on your site right now. Not because you did anything wrong — because this work is genuinely unreasonable to hold in one human head, and there is no alarm that rings when it goes wrong.

The good news: it's all fixable. All of it. It's just invisible until someone looks.

So here's a free way to start looking.

## Try it — it's free

**Grab the Quick Log template first.** It's free, it takes two minutes, and it's the exact intake tool we use to spot which leads are going cold — the same blind spot that hides SEO problems hides follow-up problems:

👉 **[Get the free Quick Log template](https://birkystudio.com/quick-log-template/)**

**Not sure how healthy your website actually is?** Take the 2-minute AI Readiness Quiz — it tells you what your site is silently missing and whether an AI agent would pay for itself:

👉 **[Take the 2-minute AI Readiness Quiz](https://birkystudio.com/ai-readiness-quiz/)**

**Want to hear what a properly built agent sounds like?** Call it. No form, no sales call, no calendar link — it answers like a real receptionist and you can ask it anything:

👉 **[Call the live AI voice demo](https://birkystudio.com/voice-demo/)**

**Or just text it.** This is the one I'd send you to if you only do one thing. It's the real thing, running in production, and it'll answer questions a chatbot has no business knowing the answers to:

👉 **[Message the AI agent on WhatsApp — +502 3477 5110](https://wa.me/50234775110)**

If you'd rather just have someone go through your site and tell you what's broken — that's what we do. **[Tell us about your business](https://birkystudio.com/contact/)** and we'll come back within the hour with a straight answer, including the parts that aren't worth paying us to fix.

Related reading: [5 simple SEO wins most small businesses miss](/blog/5-simple-seo-tips-small-business/) and [the signs your website is costing you clients](/blog/signs-website-costing-clients/).
