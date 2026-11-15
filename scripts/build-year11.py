"""Convert Questions_and_Solutions.docx → public/year11/index.html (MathML)."""

from __future__ import annotations

import re
import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "content" / "Questions_and_Solutions.docx"
OUT_DIR = ROOT / "public" / "year11"
MEDIA_DIR = OUT_DIR / "media"

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def text_of(el: ET.Element | None) -> str:
    if el is None:
        return ""
    return "".join(el.itertext())


def el(name: str, attrs: dict | None = None, kids: list[str] | None = None) -> str:
    attrs = attrs or {}
    kids = kids or []
    attr = "".join(f' {k}="{escape(v)}"' for k, v in attrs.items())
    if not kids:
        return f"<{name}{attr} />"
    return f"<{name}{attr}>{''.join(kids)}</{name}>"


def convert_omml(node: ET.Element) -> str:
    name = local(node.tag)

    def kids(tag: str | None = None) -> list[ET.Element]:
        if tag is None:
            return [c for c in list(node) if isinstance(c.tag, str)]
        return [c for c in node if local(c.tag) == tag]

    def first(tag: str) -> ET.Element | None:
        found = kids(tag)
        return found[0] if found else None

    def conv_children(parent: ET.Element | None) -> str:
        if parent is None:
            return ""
        return "".join(convert_omml(c) for c in parent if isinstance(c.tag, str))

    if name in {"oMath", "oMathPara", "e", "den", "num", "sub", "sup", "deg", "fName"}:
        return "".join(convert_omml(c) for c in kids())

    if name == "r":
        raw = text_of(first("t"))
        if not raw:
            return ""
        if re.fullmatch(r"[0-9.]+", raw):
            return el("mn", {}, [escape(raw)])
        if re.fullmatch(r"[=+\-−×·÷<>≤≥≠≈∈∘↦⇒⇐⇔±∪∩]", raw) or re.fullmatch(
            r"[,:;|()\[\]{}]", raw
        ):
            return el("mo", {}, [escape(raw)])
        if len(raw) == 1 and raw.isalpha():
            return el("mi", {}, [escape(raw)])
        return el("mrow", {}, [el("mtext", {}, [escape(raw)])])

    if name == "rad":
        deg = first("deg")
        e = first("e")
        body = conv_children(e)
        deg_content = conv_children(deg).strip()
        if not deg_content:
            return el("msqrt", {}, [body])
        return el("mroot", {}, [body, deg_content])

    if name == "sSup":
        return el(
            "msup",
            {},
            [
                el("mrow", {}, [conv_children(first("e"))]),
                el("mrow", {}, [conv_children(first("sup"))]),
            ],
        )

    if name == "sSub":
        return el(
            "msub",
            {},
            [
                el("mrow", {}, [conv_children(first("e"))]),
                el("mrow", {}, [conv_children(first("sub"))]),
            ],
        )

    if name == "sSubSup":
        return el(
            "msubsup",
            {},
            [
                el("mrow", {}, [conv_children(first("e"))]),
                el("mrow", {}, [conv_children(first("sub"))]),
                el("mrow", {}, [conv_children(first("sup"))]),
            ],
        )

    if name == "f":
        return el(
            "mfrac",
            {},
            [
                el("mrow", {}, [conv_children(first("num"))]),
                el("mrow", {}, [conv_children(first("den"))]),
            ],
        )

    if name == "d":
        e = first("e")
        inner = conv_children(e) if e is not None else "".join(convert_omml(c) for c in kids())
        return el("mfenced", {}, [inner])

    if name == "func":
        return el(
            "mrow",
            {},
            [
                el("mrow", {}, [conv_children(first("fName"))]),
                el("mfenced", {}, [conv_children(first("e"))]),
            ],
        )

    if name in {"box", "borderBox"}:
        return "".join(convert_omml(c) for c in kids())

    if name == "t":
        return el("mtext", {}, [escape(text_of(node))])

    if name.endswith("Pr"):
        return ""

    return "".join(convert_omml(c) for c in kids())


def omml_to_mathml(omml: ET.Element, display: bool = False) -> str:
    return el(
        "math",
        {
            "xmlns": "http://www.w3.org/1998/Math/MathML",
            "display": "block" if display else "inline",
        },
        [el("mrow", {}, [convert_omml(omml)])],
    )


def parse_rels(z: zipfile.ZipFile) -> dict[str, str]:
    try:
        xml = z.read("word/_rels/document.xml.rels")
    except KeyError:
        return {}
    root = ET.fromstring(xml)
    rels: dict[str, str] = {}
    for rel in root:
        if local(rel.tag) != "Relationship":
            continue
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target", "").lstrip("/")
        if not target.startswith("word/"):
            target = "word/" + target
        if rid:
            rels[rid] = target.replace("\\", "/")
    return rels


def extract_media(z: zipfile.ZipFile, rels: dict[str, str]) -> dict[str, str]:
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)
    media_map: dict[str, str] = {}
    used = sorted({t for t in rels.values() if "media/" in t})
    for i, target in enumerate(used, start=1):
        try:
            data = z.read(target)
        except KeyError:
            continue
        ext = Path(target).suffix or ".png"
        name = f"img-{i:02d}{ext}"
        (MEDIA_DIR / name).write_bytes(data)
        # Absolute from site root so /year11 (no trailing slash) still works.
        media_map[target] = f"/year11/media/{name}"
    return media_map


def style_of(p: ET.Element) -> str:
    ppr = p.find(f"{W}pPr")
    if ppr is None:
        return ""
    ps = ppr.find(f"{W}pStyle")
    if ps is None:
        return ""
    return ps.attrib.get(f"{W}val") or ps.attrib.get("val") or ""


def is_bold(r: ET.Element) -> bool:
    rpr = r.find(f"{W}rPr")
    return rpr is not None and rpr.find(f"{W}b") is not None


def paragraph_html(p: ET.Element, rels: dict[str, str], media_map: dict[str, str]) -> str:
    style = style_of(p)
    tag = "p"
    cls = ""
    if style == "Title":
        tag, cls = "h1", "doc-title"
    elif style == "Heading1":
        tag, cls = "h1", "section"
    elif style == "Heading2":
        tag, cls = "h2", "question"
    elif style == "Heading3":
        tag, cls = "h3", "solution"

    parts: list[str] = []
    display_math = False

    for node in p:
        name = local(node.tag)
        if name == "r":
            blip = node.find(f".//{A}blip")
            if blip is not None:
                embed = blip.attrib.get(f"{R}embed") or blip.attrib.get("embed")
                if embed and embed in rels and rels[embed] in media_map:
                    src = media_map[rels[embed]]
                    parts.append(
                        f'<figure class="figure"><img src="{escape(src)}" alt="Figure" loading="lazy" /></figure>'
                    )
                continue
            t = node.find(f"{W}t")
            if t is None or not (t.text or ""):
                continue
            text = t.text
            parts.append(f"<strong>{escape(text)}</strong>" if is_bold(node) else escape(text))
            continue

        if name == "oMath":
            parts.append(omml_to_mathml(node, display=False))
            continue

        if name == "oMathPara":
            display_math = True
            inner = node.find(f"{M}oMath")
            parts.append(omml_to_mathml(inner if inner is not None else node, display=True))
            continue

        if name == "hyperlink":
            for r in node.findall(f"{W}r"):
                t = r.find(f"{W}t")
                if t is not None and t.text:
                    parts.append(escape(t.text))

    inner = "".join(parts)
    if not inner.strip():
        return ""
    classes = " ".join(x for x in (cls, "display-math" if display_math else "") if x)
    class_attr = f' class="{classes}"' if classes else ""
    return f"<{tag}{class_attr}>{inner}</{tag}>"


def table_html(tbl: ET.Element, rels: dict[str, str], media_map: dict[str, str]) -> str:
    chunks: list[str] = []
    for tr in tbl.findall(f"{W}tr"):
        for tc in tr.findall(f"{W}tc"):
            for p in tc.findall(f"{W}p"):
                html = paragraph_html(p, rels, media_map)
                if html:
                    chunks.append(html)
    return f'<aside class="question-box">{"".join(chunks)}</aside>'


def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", "", html).strip()


def slugify(text: str, used: dict[str, int]) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "section"
    n = used.get(base, 0) + 1
    used[base] = n
    return base if n == 1 else f"{base}-{n}"


HEADING_RE = re.compile(
    r'^<(?P<tag>h[123])(?P<attrs>[^>]*)>(?P<inner>.*)</(?P=tag)>$',
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
            # Prefer section-qualified titles in TOC when possible
            title = text
            if current_section is not None:
                current_section["questions"].append({"id": qid, "title": title})
            else:
                toc_sections.append(
                    {
                        "id": qid,
                        "title": title,
                        "questions": [],
                        "is_question": True,
                    }
                )
            out.append(f'<{tag} class="{classes}" id="{qid}">{inner}</{tag}>')
            i += 1
            continue

        if tag == "h3" and "solution" in classes:
            # Gather solution body until next heading
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
                "<details class=\"solution-block\">"
                f"<summary><span class=\"solution-label\">{escape(summary)}</span>"
                "<span class=\"solution-hint\">Show</span></summary>"
                f"<div class=\"solution-body\">{body_html}</div>"
                "</details>"
            )
            continue

        # Other headings
        hid = slugify(text or tag, used_slugs)
        out.append(f'<{tag}{attrs} id="{hid}">{inner}</{tag}>')
        i += 1

    # Build TOC HTML
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
        "<div class=\"toc-head\">"
        "<strong>Index</strong>"
        '<div class="toc-actions">'
        '<button type="button" class="btn-text" data-action="expand-all">Expand solutions</button>'
        '<button type="button" class="btn-text" data-action="collapse-all">Collapse</button>'
        "</div></div>"
        f'<ol class="toc-list">{"".join(toc_items)}</ol>'
        "</nav>"
    )
    return out, toc


def page(toc: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Year 11 — Questions and Solutions</title>
  <link rel="stylesheet" href="/styles.css" />
  <script>
    window.MathJax = {{
      options: {{ renderActions: {{ addMenu: [] }} }},
      startup: {{ typeset: true }}
    }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/mml-chtml.js"></script>
  <script defer src="/app.js"></script>
</head>
<body class="has-toc">
  <header class="top">
    <a class="brand" href="/">Math</a>
    <nav>
      <button type="button" class="toc-toggle" aria-controls="toc-panel" aria-expanded="false">Index</button>
      <a href="/year7/">Year 7</a>
      <a href="/year11/" aria-current="page">Year 11</a>
      <a href="/year12/">Year 12</a>
    </nav>
  </header>
  <div class="layout">
    <aside id="toc-panel" class="toc-panel">
{toc}
    </aside>
    <main class="page year11">
{body}
    </main>
  </div>
</body>
</html>
"""


def main() -> None:
    if not DOCX.exists():
        raise SystemExit(f"Missing {DOCX}")

    if OUT_DIR.exists():
        # keep styles elsewhere; only clear year11 output
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(DOCX) as z:
        rels = parse_rels(z)
        media_map = extract_media(z, rels)
        root = ET.fromstring(z.read("word/document.xml"))

    body = root.find(f"{W}body")
    if body is None:
        raise SystemExit("No document body")

    blocks: list[str] = []
    for child in body:
        name = local(child.tag)
        if name == "p":
            html = paragraph_html(child, rels, media_map)
            if html:
                blocks.append(html)
        elif name == "tbl":
            blocks.append(table_html(child, rels, media_map))

    enhanced, toc = enhance_blocks(blocks)
    (OUT_DIR / "index.html").write_text(page(toc, "\n".join(enhanced)), encoding="utf-8")

    extras = ROOT / "content" / "images"
    if extras.exists():
        dest = OUT_DIR / "images"
        dest.mkdir(exist_ok=True)
        for f in extras.glob("*"):
            if f.is_file():
                shutil.copy2(f, dest / f.name)

    print(f"Built {OUT_DIR / 'index.html'} ({len(enhanced)} blocks)")


if __name__ == "__main__":
    main()

