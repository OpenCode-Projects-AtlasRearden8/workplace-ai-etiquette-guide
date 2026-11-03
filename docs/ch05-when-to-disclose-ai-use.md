# Chapter 5: When to Disclose AI Use

Somewhere between "I never mention the AI" and "I narrate every prompt" there is a comfortable, professional middle. This chapter maps that middle ground.

## The honest principle

If AI use would change a decision someone makes about your work, disclose it. If it's just spellcheck-with-a-thesis, you don't need to open every email with "drafted by GPT."

Ask: *would the reader want to know before relying on this?*

## Times disclosure is usually expected

- **Client-facing or published work:** a report, proposal, or article that a client will rely on. A short note in the footer or cover email is enough.
- **Catalogued or reviewable deliverables:** meeting minutes, knowledge-base entries — many workplaces want an "assisted by AI" tag.
- **When your employer's policy says so.** This is the override. If the policy from [Chapter 1](ch01-reading-employer-policy.html) requires disclosure, disclosure wins, full stop.
- **If someone asks.** "Did you use AI for this?" gets a straightforward, unbothered yes.

## Times it's usually fine to skip

- Brainstorming an outline for your own thinking
- Fixing grammar in your own prose
- Summarizing something only you will read
- Asking a tool to reword one sentence you drafted

The work product is yours either way. What matters to other people is the accuracy and confidentiality, not the tooling.

## What good disclosure sounds like

Short and unapologetic beats long and defensive:

> "Drafted with AI assistance, then reviewed and edited by me."
>
> "Used AI to summarize the raw notes; I verified action items with each owner."
>
> "The data chart AI produced had the axis labels wrong; I've fixed them."

Notice the pattern: name the tool's role, name what *you* did. It reads as competence, not confession.

## Keep a log for when it matters

For anything client-facing, keep a tiny log file of what you used AI for and what you verified. One tested command builds it and one shows it (your date will differ, and `>` creates or overwrites the file):

```console
$ printf '%s | grant-proposal.md | drafted with AI; verified budget math manually\n' "$(date +%F)" > ai-use-log.txt
$ cat ai-use-log.txt
2026-11-03 | grant-proposal.md | drafted with AI; verified budget math manually
```

Once the file exists, use `>>` instead of `>` so you append instead of overwrite:

```console
$ printf '%s | meeting-summary.md | AI-polished notes; verified action items\n' "$(date +%F)" >> ai-use-log.txt
$ tail -2 ai-use-log.txt
2026-11-03 | grant-proposal.md | drafted with AI; verified budget math manually
2026-11-03 | meeting-summary.md | AI-polished notes; verified action items
```

Sixty seconds now saves you an awkward deposition-style interview later, if a client ever asks what was human.

## Answering the question directly

When someone asks "did you use AI?", any of these work:

- "Yes — I drafted it with AI and checked every number myself."
- "Partially. The structure came from AI; the recommendations are mine."
- "No, I wrote this one from scratch."

All three are respected answers. What isn't respected is being caught in a shrug, because the follow-up question in every workplace is about *everything else you did*.

---

*Education only, not legal advice. The Workplace AI Etiquette Guide, by Asdale Dynamics, LLC.*
