#!/usr/bin/env python3
"""Build the static HTML site from the Markdown docs.

Uses only the Python standard library. Markdown features supported are the
subset used by docs/*.md: ATX headings, paragraphs, bullet/numbered lists,
blockquotes, fenced code blocks, horizontal rules, bold, italics and inline
code. Escaping is handled before formatting so no HTML can leak through.
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
TITLE = "The Workplace AI Etiquette Guide"
FOOTER = (
    "The Workplace AI Etiquette Guide &mdash; by Asdale Dynamics, LLC. "
    "Educational content only; not legal advice."
)

CSS = """\
:root {
  --ink: #1d2229;
  --muted: #5c6672;
  --accent: #2a5a8c;
  --rule: #d8dee6;
  --code-bg: #f2f4f7;
  --quote-bg: #f7f9fb;
}
* { box-sizing: border-box; }
html { font-size: 17px; }
body {
  margin: 0;
  background: #ffffff;
  color: var(--ink);
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.65;
}
main {
  max-width: 46rem;
  margin: 0 auto;
  padding: 2rem 1.25rem 4rem;
}
h1, h2, h3 {
  font-family: "Helvetica Neue", Arial, sans-serif;
  line-height: 1.25;
  color: #10141a;
}
h1 { font-size: 2rem; margin: 0 0 .4rem; }
h2 { font-size: 1.35rem; margin-top: 2.2rem; }
h3 { font-size: 1.05rem; margin-top: 1.6rem; }
p { margin: 0.9rem 0; }
a { color: var(--accent); }
code, pre {
  font-family: "SF Mono", Consolas, Menlo, monospace;
  font-size: 0.86em;
}
pre {
  background: var(--code-bg);
  border: 1px solid var(--rule);
  border-radius: 6px;
  padding: 0.9rem 1rem;
  overflow-x: auto;
}
code { background: var(--code-bg); padding: 0.1em 0.35em; border-radius: 4px; }
pre code { background: none; padding: 0; }
blockquote {
  margin: 1.2rem 0;
  padding: 0.5rem 1.1rem;
  border-left: 4px solid var(--accent);
  background: var(--quote-bg);
  color: var(--muted);
}
blockquote p { margin: 0.4rem 0; }
ul, ol { padding-left: 1.4rem; }
li { margin: 0.35rem 0; }
hr { border: 0; border-top: 1px solid var(--rule); margin: 2rem 0; }
.site-header {
  border-bottom: 1px solid var(--rule);
  background: #fafbfc;
}
.site-header .inner {
  max-width: 46rem;
  margin: 0 auto;
  padding: 1rem 1.25rem;
}
.site-title {
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-weight: 700;
  font-size: 1.05rem;
  text-decoration: none;
  color: #10141a;
  display: inline-block;
}
.site-title span { color: var(--accent); }
.site-nav {
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 0.8rem;
  margin-top: 0.4rem;
}
.site-nav a { text-decoration: none; margin-right: 0.9rem; white-space: nowrap; }
.site-nav a:hover, .site-title:hover { text-decoration: underline; }
.disclaimer {
  font-size: 0.85rem;
  color: var(--muted);
  font-style: italic;
}
p.subtitle { color: var(--muted); margin-top: 0; font-size: 1rem; }
.pager {
  font-family: "Helvetica Neue", Arial, sans-serif;
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  margin-top: 3rem;
  padding-top: 1rem;
  border-top: 1px solid var(--rule);
  font-size: 0.9rem;
}
.pager a { text-decoration: none; }
.pager a:hover { text-decoration: underline; }
footer.site-footer {
  border-top: 1px solid var(--rule);
  color: var(--muted);
  font-size: 0.85rem;
}
footer.site-footer .inner {
  max-width: 46rem;
  margin: 0 auto;
  padding: 1rem 1.25rem 2rem;
}
li .cmd-result {
  display: block;
  color: var(--muted);
  font-style: italic;
}

/* Print styles */
@media print {
  html { font-size: 11.5pt; }
  body { color: #000; font-family: Georgia, serif; line-height: 1.5; }
  main { max-width: none; padding: 0; margin: 0; }
  a { color: #000; text-decoration: none; }
  .site-nav, .pager { display: none; }
  .site-header { border-bottom: 2px solid #000; background: none; }
  footer.site-footer { border-top: 2px solid #000; }
  h1, h2, h3 { color: #000; }
  h2 { page-break-after: avoid; }
  pre, blockquote, table { page-break-inside: avoid; }
  pre {
    border: 1px solid #000;
    background: none;
    white-space: pre-wrap;
    word-wrap: break-word;
  }
  .disclaimer { font-size: 0.8rem; font-style: italic; }
  code { background: none; border: none; padding: 0; }
  blockquote { border-left: 3px solid #000; background: none; }
}
@page { margin: 2cm 2.2cm; }
"""


def inline(md: str) -> str:
    text = html.escape(md, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  r'<a href="\2">\1</a>', text)
    return text


def render_markdown(md: str) -> str:
    lines = md.split("\n")
    out = []
    i = 0
    in_code = False
    code_lang = ""
    list_tag = None
    while i < len(lines):
        line = lines[i]
        if in_code:
            if line.strip().startswith("```"):
                out.append("</code></pre>")
                in_code = False
            else:
                out.append(html.escape(line))
            i += 1
            continue
        if line.strip().startswith("```"):
            out.append("<pre><code>")
            in_code = True
            i += 1
            continue
        m = re.match(r"^(#{1,4}) (.*)$", line)
        if m:
            level = len(m.group(1))
            # The chapter title is emitted in the page template; skip the
            # first H1 inside the body and keep deeper headings as-is.
            if level == 1 and i == 0:
                i += 1
                continue
            out.append(
                f"<h{level}>{inline(m.group(2))}</h{level}>"
            )
            i += 1
            continue
        if line.strip() == "---":
            out.append("<hr>")
            i += 1
            continue
        m = re.match(r"^<!-- (.*) -->$", line.strip())
        if m:
            out.append(f"<p>PH-{m.group(1)}-PH</p>")
            i += 1
            continue
        m = re.match(r"^>\s?(.*)$", line)
        if m:
            out.append("<blockquote><p>%s</p></blockquote>" % inline(m.group(1)))
            i += 1
            continue
        m = re.match(r"^[-*] (.*)$", line)
        if m:
            if list_tag != "ul":
                out.append("<ul>")
                list_tag = "ul"
            out.append("<li>%s</li>" % inline(m.group(1)))
            i += 1
            continue
        m = re.match(r"^\d+\. (.*)$", line)
        if m:
            if list_tag != "ol":
                out.append("<ol>")
                list_tag = "ol"
            out.append("<li>%s</li>" % inline(m.group(1)))
            i += 1
            continue
        if list_tag:
            out.append("</%s>" % list_tag)
            list_tag = None
        if line.strip():
            out.append("<p>%s</p>" % inline(line.strip()))
        i += 1
    if list_tag:
        out.append("</%s>" % list_tag)
    return "\n".join(out)


def page(title_suffix: str, body: str, nav: str, pager: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title_suffix if title_suffix else TITLE)}</title>
<meta name="description" content="Plain-English manual on using AI at work without trouble. Education only, not legal advice.">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="site-header">
  <div class="inner">
    <a class="site-title" href="index.html">The Workplace AI <span>Etiquette Guide</span></a>
    <p class="disclaimer">Education only &mdash; not legal advice.</p>
    <nav class="site-nav">{nav}</nav>
  </div>
</header>
<main>
<article>
{body}
</article>
{pager}
</main>
<footer class="site-footer">
  <div class="inner">
    <p>{FOOTER}</p>
  </div>
</footer>
</body>
</html>
"""


def main() -> int:
    SITE.mkdir(exist_ok=True)
    (SITE / "styles.css").write_text(CSS, encoding="utf-8")
    files = sorted(DOCS.glob("*.md"))
    if not files:
        print("No markdown files found in docs/", file=sys.stderr)
        return 1

    chapters = []
    for f in files:
        if f.name == "index.md":
            continue
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^# (.+)$", text, re.M)
        title = m.group(1).strip() if m else f.stem
        slug = f.stem
        chapters.append((title, slug))
    nav = " ".join(
        f'<a href="{slug}.html">{html.escape(short_title(t))}</a>'
        for t, slug in chapters
    )

    for idx, (title, slug) in enumerate(chapters):
        md = (DOCS / f"{slug}.md").read_text(encoding="utf-8")
        body = render_markdown(md)
        prev_ch = chapters[idx - 1] if idx > 0 else None
        next_ch = chapters[idx + 1] if idx < len(chapters) - 1 else None
        prev_link = (
            f'<a href="{prev_ch[1]}.html">&larr; {short_title(prev_ch[0])}</a>'
            if prev_ch
            else ""
        )
        next_link = (
            f'<a href="{next_ch[1]}.html">{short_title(next_ch[0])} &rarr;</a>'
            if next_ch
            else ""
        )
        pager = f'<nav class="pager"><span>{prev_link}</span><span>{next_link}</span></nav>'
        html_page = page(
            title + " — " + TITLE,
            body,
            nav,
            pager,
        )
        (SITE / f"{slug}.html").write_text(html_page, encoding="utf-8")
        print(f"Wrote site/{slug}.html")

    # Index page
    text = (DOCS / "index.md").read_text(encoding="utf-8")
    body = render_markdown(text)
    toc = "<ul>" + "".join(
        f'<li><a href="{slug}.html">{html.escape(t)}</a></li>'
        for t, slug in chapters
    ) + "</ul>"
    body = body.replace("<p>PH-TOC-PH</p>", toc)
    html_page = page(
        TITLE,
        body,
        nav,
        '<nav class="pager"><span></span><span>'
        f'<a href="{chapters[0][1]}.html">Start with Chapter 1 &rarr;</a>'
        "</span></nav>",
    )
    (SITE / "index.html").write_text(html_page, encoding="utf-8")
    print("Wrote site/index.html")
    return 0


def short_title(t: str) -> str:
    t = re.sub(r"^Chapter \d+[:.]?\s*", "", t)
    if ":" in t:
        return t.split(":", 1)[1].strip()
    return t


if __name__ == "__main__":
    sys.exit(main())
