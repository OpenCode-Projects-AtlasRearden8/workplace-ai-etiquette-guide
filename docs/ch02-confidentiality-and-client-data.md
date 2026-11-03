# Chapter 2: Confidentiality and Client Data

This is the chapter that prevents the biggest AI-at-work disasters. Everything here is about one idea: **what you type into a tool can leave your control.** Say that to yourself once. It's the whole chapter in a sentence.

## The mental model: the AI is a stranger you're talking to

Think of a generic, consumer-grade AI chat tool as a public blog post you're about to publish. Would you put that client's name on a blog? Their invoice number? Their health details? If not, don't put it in the chat.

Some business tools have agreements that change this picture (Chapter 1 will tell you what your company allows). But the default, safe assumption for a free public tool is: **anything you paste could be stored, reviewed, or trained on.**

## The three kinds of information

1. **Public** — things anyone could find (already-published docs, general knowledge). Generally fine for any tool.
2. **Internal** — company-only things (project names, internal emails, drafts). Only use tools your company has approved. [See Chapter 1](ch01-reading-employer-policy.html).
3. **Restricted** — client data, personal data, health data, financial records, credentials, anything with names attached. **Treat as off-limits unless your employer's policy and your tool agreement both explicitly allow it.**

When in doubt, it's restricted.

## Before you paste: the redaction habit

Most "I need AI's help" moments don't actually need real names or numbers. AI is great at "a customer had a billing dispute" — it doesn't need to know who. Get in the habit of scrubbing before you paste.

Here is the pattern, applied to a sample `notes.md` that holds an SSN, an email address, and a phone number. It was tested and works — the original file is untouched, and the cleaned copy is written to a *different* file:

```console
$ cat notes.md
Contact: Jane Doe, SSN 123-45-6789
Email jane.doe@example.com, phone (555) 010-1234
Notes: dispute call on 2026-10-14 went well, follow up Monday

$ sed -E 's/[[:alnum:]._%+-]+@[[:alnum:].-]+/[REDACTED-EMAIL]/g; s/[0-9]{3}-[0-9]{2}-[0-9]{4}/XXX-XX-XXXX/g; s/[0-9]{4,6}/0000/g' notes.md > notes-clean.md
$ cat notes-clean.md
Contact: Jane Doe, SSN XXX-XX-XXXX
Email [REDACTED-EMAIL], phone (555) 010-0000
Notes: dispute call on 0000-10-14 went well, follow up Monday
```

Three patterns, one pass: emails, SSN-style numbers, and any 4-to-6 digit runs (the date's year got zeroed too — that's the trade-off; verify anything numeric after redacting). Paste only from `notes-clean.md`.

A quick keyword check confirms the sensitive tokens are gone (works on macOS, Linux, and Windows with Git Bash):

```console
$ grep -E "(REDACTED-EMAIL|XXX-XX-XXXX)" notes-clean.md
Contact: Jane Doe, SSN XXX-XX-XXXX
Email [REDACTED-EMAIL], phone (555) 010-0000

$ grep -inE "client|patient|social security|invoice|confidential" notes-clean.md
$
```

The second command returning nothing is the clean scan you want. (Only useful for the words you list; it can't catch everything, which is exactly why the habit of summarizing matters more than the tool.)

## The summarizing move

When redacting feels like too much work, summarize instead. Compare:

- **Risky paste:** "Client Jane Doe, invoice #48291, dispute over $12,340 charge dated 2026-10-14..."
- **Safe version:** "A client is disputing a significant invoice charge from mid-October and wants a refund. Draft three calm, professional response options."

You lose nothing. The AI produces better output when it has *structure*, not secrets.

## One-time and ongoing rules of thumb

- Never paste credentials, API keys, or tokens into any AI tool. Anything typed as a password-style secret should be considered burned and rotated. (This guide contains no such examples on purpose.)
- Watch for attachments: uploading a file uploads everything inside it, including things you didn't scroll to.
- Screenshots count. A screenshot of a spreadsheet is a spreadsheet-shaped leak.
- If a workflow turns out to need real client data, that's a Chapter 7 conversation with your employer, not a solo judgment call.

## The pre-paste checklist

Ask these four questions before every paste:

1. Is this information public, internal, or restricted?
2. Would I be comfortable if this text appeared in a public archive?
3. Have I removed names, numbers, and identifiers?
4. Is this tool on my employer's approved list?

Four yes-or-NA answers, then paste.

---

*Education only, not legal advice. The Workplace AI Etiquette Guide, by Asdale Dynamics, LLC.*
