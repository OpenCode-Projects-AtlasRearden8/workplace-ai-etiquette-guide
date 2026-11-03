# Chapter 3: Drafting Emails and Reports

Drafting is where AI genuinely shines at work. The catch: AI drafts are usually *about right and not quite right*, in subtle ways. This chapter is about getting a good draft fast and checking it well.

## The workflow that works

1. **You set the shape.** Bullet-point the key facts and the goal.
2. **AI drafts.** Give it the audience, tone, and length you want.
3. **You verify.** Every fact, date, number, and name — you check them.
4. **You make it yours.** Rewrite anything you wouldn't naturally say.

Skipping step 3 is how "the AI said it" becomes "you said it, incorrectly."

## A prompting pattern for emails

Vague prompts give vague emails. Try this shape:

> Write a warm but professional email to my manager explaining [goal] and [reason]. Keep it under 120 words. I'll supply the facts: [three bullet points]. End by asking for a short call.

The AI writes *around* your facts; it never invents between them. If it adds something you didn't give it, that's your edit queue, not a bonus.

## Quality checks before you send

Do these checks every time, in this order:

- **Facts:** names, dates, amounts, and attachments — verify each against your source.
- **Tone:** read it once out loud. Anything you'd never say in a hallway, cut.
- **Claims:** AI sometimes asserts things confidently that you never told it. Delete or verify them.

Two commands that catch real problems before sending. Both were tested and work. First, a word count to keep it tight:

```console
$ wc -w draft-email.md
121 draft-email.md
```

Second, a scan for placeholder text that AI loves to leave behind (works even if the file was pasted straight from a chat window):

```console
$ grep -inE "\[(insert|your|name|date|amount)|TBD|TODO|\{.*\}" draft-email.md
6:The replacement unit ships once accounting releases the approved [amount] to the vendor.
8:The timeline for the swap is confirmed for [date of incident], weather permitting.
```

Those bracket placeholders are exactly the things that mortify people when sent. The scan found them; now fill or cut them.

## Working from versions

Save draft versions as files so you can see what changed between AI passes. The classic `diff` tool works fine:

```console
$ diff draft-v1.md draft-v2.md
11c11
< We regret the inconvenience this may have caused.
---
> I apologize for the confusion on our end, and here's what we're doing about it:
```

Now you're reviewing a small edit instead of re-reading a whole email — and you can keep the human line and reject the AI flourish.

## Confidentiality check, every time

This chapter only works with Chapter 2's rules attached: strip client names and identifiers before pasting content into a public AI tool, and use only employer-approved tools for anything internal. An email draft is internal the moment it mentions your company's business.

## The send checklist

- Facts verified against source?
- Placeholders gone?
- Tone is yours?
- No confidential details leaked into the tool?
- Done in fewer passes than editing it yourself would have taken? (If not, do it yourself — that's a valid outcome.)

---

*Education only, not legal advice. The Workplace AI Etiquette Guide, by Asdale Dynamics, LLC.*
