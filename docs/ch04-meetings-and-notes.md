# Chapter 4: Meetings and Notes

Meeting notes are one of the least glamorous and most automatable parts of work. AI can absolutely help you capture and tidy them — as long as the same confidentiality care from [Chapter 2](ch02-confidentiality-and-client-data.html) applies to what you record and where.

## The two-step approach

1. **Capture rough.** During the meeting, write messy shorthand (or use a note-taker tool your employer has approved — many now exist).
2. **Polish with AI.** After the meeting, feed your *de-identified* rough notes to a tool and ask for a structured summary.

Never let an unsanctioned recorder or note-taking bot join a meeting without checking your employer's rules — several states require everyone's consent for recording, and several workplaces ban it outright.

## A prompting pattern for notes

Feed the tool your cleaned-up shorthand in this shape:

> These are rough notes from a meeting. Turn them into a summary with three sections: Decisions, Action items (with owners), and Open questions. Keep the wording plain. Here are the notes: [pasted, cleaned notes]

You'll get back something presentable in seconds. Then you do the human part: check that every action item still matches what people actually agreed to.

## Find and fix the action items

A quick count tells you whether the structure survived the rewrite. This command was tested and works:

```console
$ grep -c "Action:" meeting-summary.md
3
```

If the AI produced an "Actions" section but zero `Action:` lines, your export format changed — glance before you circulate.

## Sharing notes safely

Before you circulate AI-polished notes:

- Confirm the attendee list: notes for internal people can still mention things that must not reach clients.
- Run your redaction routine one more time. It's faster than an apology. This email-scrub command was tested and works:

```console
$ sed -E 's/[[:alnum:]._%+-]+@[[:alnum:].-]+/[REDACTED-EMAIL]/g' meeting-notes.md > meeting-notes-clean.md
$ diff meeting-notes.md meeting-notes-clean.md
2c2
< manager: dana.rivera@example.com
> manager: [REDACTED-EMAIL]
```

The diff shows you exactly what got scrubbed, so you're not guessing.

## The one-line script version

If you do this weekly, put your redaction pipeline in a tiny script once and stop thinking about it thereafter:

```console
$ cat > clean-notes.sh <<'EOF'
#!/bin/sh
sed -E 's/[[:alnum:]._%+-]+@[[:alnum:].-]+/[REDACTED-EMAIL]/g; s/https?:\/\/[^ )]+/[REDACTED-LINK]/g; s/[0-9]{3}-[0-9]{2}-[0-9]{4}/XXX-XX-XXXX/g' "$1" > "$2"
EOF
```

Then weekly: `sh clean-notes.sh rough-notes.md clean-notes.md`, paste only `clean-notes.md` into your tool. Keep the script with your files and you've made a habit that costs zero effort per meeting. The script is MIT-licensed along with this manual (see the LICENSE file in this project).

## Checklist from this chapter

- Rough-capture, then AI-polish, in two steps
- Strip attendee emails and any client identifiers before pasting
- Check that action items survived the rewrite
- Confirm your employer allows any note-taking bot before it joins a meeting

---

*Education only, not legal advice. The Workplace AI Etiquette Guide, by Asdale Dynamics, LLC.*
