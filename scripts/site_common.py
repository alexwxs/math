"""Shared HTML helpers for Year 11 / Year 12 pages."""

from __future__ import annotations

import re


def escape(s: str) -> str:
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", "", html).strip()


def slugify(text: str, used: dict[str, int]) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "section"
    n = used.get(base, 0) + 1
    used[base] = n
    return base if n == 1 else f"{base}-{n}"


HEADING_RE = re.compile(
    r"^<(?P<tag>h[123])(?P<attrs>[^>]*)>(?P<inner>.*)</(?P=tag)>$",
    re.DOTALL,
)


def enhance_blocks(blocks: list[str]) -> tuple[list[str], str]:
    """Add heading ids, wrap solutions in <details>, build left-panel TOC."""
    used_slugs: dict[str, int] = {}
    toc_sections: list[dict] = []
    current_section: dict | None = None
    out: list[str] = []
    i = 0

    while i < len(blocks):
        block = blocks[i]
        m = HEADING_RE.match(block.strip())
        if not m:
            out.append(block)
            i += 1
            continue

        tag = m.group("tag")
        attrs = m.group("attrs")
        inner = m.group("inner")
        text = strip_tags(inner)
        classes = ""
        cm = re.search(r'class="([^"]*)"', attrs)
        if cm:
            classes = cm.group(1)

        if tag == "h1" and "section" in classes:
            sid = slugify(text, used_slugs)
            out.append(f'<{tag} class="{classes}" id="{sid}">{inner}</{tag}>')
            current_section = {"id": sid, "title": text, "questions": []}
            toc_sections.append(current_section)
            i += 1
            continue

        if tag == "h2" and "question" in classes:
            qid = slugify(text, used_slugs)
            if current_section is not None:
                current_section["questions"].append({"id": qid, "title": text})
            else:
                toc_sections.append(
                    {"id": qid, "title": text, "questions": [], "is_question": True}
                )
            out.append(f'<{tag} class="{classes}" id="{qid}">{inner}</{tag}>')
            i += 1
            continue

        if tag == "h3" and "solution" in classes:
            summary = text or "Solution"
            body_parts: list[str] = []
            i += 1
            while i < len(blocks):
                nxt = blocks[i]
                nm = HEADING_RE.match(nxt.strip())
                if nm and nm.group("tag") in {"h1", "h2", "h3"}:
                    break
                body_parts.append(nxt)
                i += 1
            body_html = "\n".join(body_parts)
            out.append(
                '<details class="solution-block">'
                f'<summary><span class="solution-label">{escape(summary)}</span>'
                '<span class="solution-hint">Show</span></summary>'
                f'<div class="solution-body">{body_html}</div>'
                "</details>"
            )
            continue

        hid = slugify(text or tag, used_slugs)
        out.append(f"<{tag}{attrs} id=\"{hid}\">{inner}</{tag}>")
        i += 1

    toc_items: list[str] = []
    for sec in toc_sections:
        if sec.get("is_question"):
            toc_items.append(
                f'<li class="toc-q"><a href="#{sec["id"]}">{escape(sec["title"])}</a></li>'
            )
            continue
        kids = "".join(
            f'<li><a href="#{q["id"]}">{escape(q["title"])}</a></li>'
            for q in sec["questions"]
        )
        nested = f"<ul>{kids}</ul>" if kids else ""
        toc_items.append(
            f'<li class="toc-section"><a href="#{sec["id"]}">{escape(sec["title"])}</a>{nested}</li>'
        )

    toc = (
        '<nav class="toc" aria-label="Index">'
        '<div class="toc-head">'
        "<strong>Index</strong>"
        '<div class="toc-actions">'
        '<button type="button" class="btn-text" data-action="expand-all">Expand solutions</button>'
        '<button type="button" class="btn-text" data-action="collapse-all">Collapse</button>'
        "</div></div>"
        f'<ol class="toc-list">{"".join(toc_items)}</ol>'
        "</nav>"
    )
    return out, toc


def page(
    *,
    title: str,
    active_year: int,
    toc: str,
    body: str,
    math_script: str,
    app_script: str = "/app.js",
) -> str:
    y7 = ' aria-current="page"' if active_year == 7 else ""
    y11 = ' aria-current="page"' if active_year == 11 else ""
    y12 = ' aria-current="page"' if active_year == 12 else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{escape(title)}</title>
  <link rel="stylesheet" href="/styles.css" />
  {math_script}
  <script defer src="{app_script}"></script>
</head>
<body class="has-toc">
  <header class="top">
    <a class="brand" href="/">Math</a>
    <nav>
      <button type="button" class="toc-toggle" aria-controls="toc-panel" aria-expanded="false">Index</button>
      <a href="/year7/"{y7}>Year 7</a>
      <a href="/year11/"{y11}>Year 11</a>
      <a href="/year12/"{y12}>Year 12</a>
    </nav>
  </header>
  <div class="layout">
    <aside id="toc-panel" class="toc-panel">
{toc}
    </aside>
    <main class="page year-content">
{body}
    </main>
  </div>
</body>
</html>
"""
