# STATUS.md — The Workplace AI Etiquette Guide

**Project:** workplace-ai-etiquette-guide
**Owner:** Asdale Dynamics, LLC (Dylan Asdale's AI education LLC, Indiana)
**Date:** 2026-11-03

## What was built

A complete educational manual, *Using AI at Work Without Trouble*, delivered in two formats:

- **docs/** — seven Markdown chapters plus an index, the source of truth:
  1. Reading Your Employer's Policy
  2. Confidentiality and Client Data
  3. Drafting Emails and Reports
  4. Meetings and Notes
  5. When to Disclose AI Use
  6. Saying No Gracefully
  7. Escalation Red Flags
- **site/** — a generated static HTML version (one page per chapter plus `index.html` and `styles.css`) with dedicated `@media print` styles: navigation hidden in print, page-break rules for headings and code blocks, black-on-white economy, and `@page` margins for clean PDF export via the browser's print dialog.
- **build/build.py** — a dependency-free (Python stdlib only) Markdown → HTML converter supporting the subset the docs use: headings, lists, blockquotes, fenced code blocks, bold/italic/inline code, horizontal rules, and a TOC placeholder. Runs across macOS/Linux/Windows with any Python 3.
- **build.sh** — wrapper that runs the build.
- **README.md** — usage, layout, and credit to Asdale Dynamics, LLC. **LICENSE** — MIT, with the copyright line `Copyright (c) 2026 Asdale Dynamics, LLC`.

## How to run it

```sh
./build.sh                     # regenerate site/ from docs/
python3 -m http.server 8000 --directory site   # or just open site/index.html
```

Edit anything in `docs/`, rerun `./build.sh`, done. No packages to install; nothing leaves the machine.

## Verification results

All checks were run in this environment and pass:

- **Build:** `./build.sh` completes cleanly and writes 8 HTML pages into `site/`.
- **HTML validity:** every generated page parsed with an HTMLParser tag-balance checker — zero unclosed/mismatched tags, zero leftover build placeholders, zero broken internal links.
- **Print styles:** `styles.css` contains the `@media print` rules and every page links the stylesheet (validated in checks above).
- **Command examples:** every shell command shown in the chapters was executed against sample files (dummy policy documents, drafts, meeting notes, and log files) and the outputs printed in the chapters match the actual tested outputs, including:
  - `find`/`grep -riE` policy search (ch01: 13 matched lines), `grep -inE` receipt search (ch06: lines 4 and 9)
  - the `sed -E` triple redaction: emails, SSN-pattern numbers, 4–6 digit runs (ch02); the standalone email scrub + `diff` (ch04: `2c2`)
  - `wc -w` (121 words) and the placeholder scan (lines 6 and 8) (ch03); `diff` between draft versions (`11c11`) (ch03)
  - the `clean-notes.sh` redaction script — emails, links, SSN patterns (built via heredoc, exit 0, output verified) (ch04)
  - date-stamped log apps (`date +%F` → 2026-11-03) (ch05, ch07)
- **No secrets:** repository contains no API keys, tokens, credentials, or personal data; sample outputs use dummy data and RFC-style example names. Grep sweep for key/token patterns returned nothing.

## Known gaps

- The Markdown converter supports the subset of Markdown used by this manual (no tables, no images, no nested lists). Adding chapter content in that subset is safe; richer Markdown will need converter extensions.
- Sample policy text in the command examples is realistic but fictional; readers should always verify against their own employer's actual documents.
- No automated test suite is bundled for the docs content itself — command examples were verified manually in this environment (validation script referenced in the build notes above can be re-created if needed).
- Search across chapters is not implemented; there's a per-page nav instead.

## Safety posture

- Education only; not legal advice — stated on every page, in the README, and in each chapter footer.
- MIT **LICENSE** file included with the exact line: `Copyright (c) 2026 Asdale Dynamics, LLC`.
- Asdale Dynamics, LLC credited in README.md and in the site footer on every page.
