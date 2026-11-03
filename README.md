# The Workplace AI Etiquette Guide

A plain-English manual for using AI tools at work without getting yourself — or your employer — into trouble. Written like a friend would explain it: warm, step by step, never condescending.

**By [Asdale Dynamics, LLC](https://dylanasdale.github.io)** — Dylan Asdale's beginner-friendly AI education shop. Education only; **not legal advice**. Your workplace, your policies, and your local laws always win.

## What's inside

Seven short chapters, each ending with a checklist:

1. **Reading Your Employer's Policy** — find the rules before you use the tools
2. **Confidentiality and Client Data** — the redaction habit, and what never goes in
3. **Drafting Emails and Reports** — get good drafts fast and verify them properly
4. **Meetings and Notes** — capture rough, polish smart, share safely
5. **When to Disclose AI Use** — the honest middle ground between silence and narrating
6. **Saying No Gracefully** — three-part refusals that keep everyone's dignity intact
7. **Escalation Red Flags** — what to report same-day, and exactly what to say

## Repository layout

```
docs/    Markdown chapters (the source of truth)
site/    Generated static HTML site with print-friendly styling
build/   build.py — the stdlib-only Markdown → HTML converter
build.sh One-line wrapper that runs the build
```

## How to run it

Build the site (works on macOS, Linux, and Windows with Python 3 or Git Bash):

```sh
./build.sh
```

Read the HTML in any browser, or serve it locally:

```sh
python3 -m http.server 8000 --directory site
```

Then open `http://localhost:8000`. To print or save a chapter as PDF, open it in a browser and print — the print styles collapse navigation, tighten spacing, and keep code blocks from splitting across pages.

To regenerate the site after editing any file in `docs/`, just run `./build.sh` again. The converter uses only the Python standard library; nothing to install, no network calls, no keys.

## Testing the command examples

Every shell command shown in the chapters was tested against sample files (policy documents, drafts, notes, and logs with dummy data). No confidential data, credentials, or API keys appear anywhere in this repository, and none are needed to verify the examples.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.

## More from Asdale Dynamics

Books and guides including *The Massive AI Manual*, plus beginner-friendly tools and templates, at <https://dylanasdale.github.io>.
