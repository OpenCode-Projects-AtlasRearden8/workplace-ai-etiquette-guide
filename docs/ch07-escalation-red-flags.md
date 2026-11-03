# Chapter 7: Escalation Red Flags

Most AI mishaps are small. A few are not. This chapter is about telling the difference early — and knowing who to tell when it's the second kind.

The unifying principle: **speed and honesty beat perfection.** A promptly reported small problem is a Tuesday. A hidden one grows.

## Red flags: escalate now

Treat any of these as a same-day escalation to your manager and IT (or your named security contact):

- **Credentials in a prompt.** You pasted an API key, password, or token into any AI tool, public or internal.
- **Restricted data in a public tool.** Client records, health data, personal data, or anything marked Confidential went into a tool that isn't on your employer's approved list.
- **AI output you can't verify got shipped.** A client received numbers, claims, or a legal-sounding clause that nobody checked.
- **A policy conflict with pressure.** Someone above you is instructing you to do the thing you believe the policy forbids, and it's client data or credentials.
- **A tool you didn't sanction joined a meeting.** A third-party note-taker or transcriber appeared, especially with clients present.
- **You've been asked to hide AI use.** Editing records to *look* hand-written when it wasn't, retroactively removing "AI assisted" tags, etc.

Two of these — credentials and restricted-data — also usually trigger obligations your employer has, like breach-notice rules. That's why "tell someone today" isn't optional theater; other clocks start when the data leaves.

## The escalation script

Keep it short; details in writing afterwards:

> "I want to flag something from this morning. I pasted [what] into [which tool] before realizing it wasn't approved. I deleted the conversation and I'm rotating the credential — who else needs to know, and is there anything I should do while we wait?"

What makes this work: the situation is named in one sentence, you've already done the safe move, and you're asking for direction rather than confessing in a panic. This is exactly what good organizations want to hear early.

## Log it — lightly, for yourself

A short incident note helps you remember who you told and when, which matters more than it sounds. Tested command; writes one line per incident:

```console
$ printf '%s | client-list.xlsx pasted into public chat tool | deleted chat; told IT same day\n' "$(date +%F)" > ai-incident-log.txt
$ cat ai-incident-log.txt
2026-11-03 | client-list.xlsx pasted into public chat tool | deleted chat; told IT same day
```

Use `>>` on later entries so the log grows (same trick from the [disclosure log in Chapter 5](ch05-when-to-disclose-ai-use.html)). It becomes your own timeline *if* questions come later — keep it factual: what, which tool, what you did, who you told. Opinions and blame stay out of logs.

## Yellow flags: fix quietly, no escalation

Not everything needs a meeting:

- An AI draft had a wrong fact that you caught and fixed before sending
- You pasted internal-but-not-restricted text into an unapproved tool, then deleted it
- You used a tool outside the approved list for a public-information task

Correct, note briefly in your own log if it repeats, and carry on. Escalating trivia trains everyone to ignore escalation.

## The decision in one line

> **"Would I want my employer to hear about this from me first, or from someone else?"**

If the honest answer is "from me first" — you know what to do today.

---

*Education only, not legal advice. The Workplace AI Etiquette Guide, by Asdale Dynamics, LLC.*
