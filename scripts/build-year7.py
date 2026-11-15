"""Build Year 7 pages from structured question content."""

from __future__ import annotations

import runpy
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "public" / "year7"
MEDIA_OUT = OUT_DIR / "media"
CONTENT = ROOT / "content" / "year7"
SCRIPTS = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS))
from site_common import enhance_blocks, escape, page  # noqa: E402
from year7_congruent_content import congruent_triangle_2_blocks  # noqa: E402

MATH_SCRIPT = """
  <script>
    window.MathJax = {
      tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']] },
      options: { renderActions: { addMenu: [] } }
    };
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
"""


def p(text: str) -> str:
    return f"<p>{text}</p>"


def eq(latex: str) -> str:
    return f'<p class="display-math">$${latex}$$</p>'


def question_box(*parts: str) -> str:
    return f'<aside class="question-box">{"".join(parts)}</aside>'


def figure(src: str, alt: str) -> str:
    return (
        f'<figure class="figure"><img src="{escape(src)}" alt="{escape(alt)}" '
        'loading="lazy" /></figure>'
    )


def year7_blocks() -> list[str]:
    d14 = "/year7/media/y7_q14_rectangle.png"
    d15 = "/year7/media/y7_q15_squares.png"
    return [
        '<h1 class="doc-title">Year 7 — Questions and Solutions</h1>',
        '<h1 class="section">Area</h1>',
        '<h2 class="question">Question 14 — Shaded triangle in a rectangle</h2>',
        question_box(
            p(r"$ABCD$ is a rectangle. Find the area of the shaded region."),
            figure(d14, "Rectangle ABCD with area labels 5, 3, 8 and shaded triangle AEF"),
        ),
        '<h3 class="solution">Solution</h3>',
        p(
            r"In the diagram, the numbers are <strong>areas</strong> of the three unshaded "
            r"right-angled triangles:"
        ),
        p(r"• $\mathrm{Area}(\triangle ADE)=5$"),
        p(r"• $\mathrm{Area}(\triangle ABF)=3$"),
        p(r"• $\mathrm{Area}(\triangle CEF)=8$"),
        p(r"The shaded region is $\triangle AEF$. Let the area of rectangle $ABCD$ be $R$."),
        p(
            r"Triangles $\triangle ADE$ and the rectangle share the same height $AD$, so"
        ),
        eq(r"\dfrac{DE}{DC}=\dfrac{2\times 5}{R}=\dfrac{10}{R}"),
        p(r"Likewise, $\triangle ABF$ and the rectangle share height $AB$, so"),
        eq(r"\dfrac{BF}{BC}=\dfrac{2\times 3}{R}=\dfrac{6}{R}"),
        p(r"Also $\mathrm{Area}(\triangle CEF)=\dfrac{1}{2}\cdot CE\cdot CF=8$."),
        p(
            r"Writing $CE=DC\left(1-\dfrac{10}{R}\right)$ and "
            r"$CF=BC\left(1-\dfrac{6}{R}\right)$, and using $DC\cdot BC=R$,"
        ),
        eq(
            r"8=\dfrac{1}{2}\cdot R\cdot\left(1-\dfrac{10}{R}\right)\left(1-\dfrac{6}{R}\right)"
            r"=\dfrac{(R-10)(R-6)}{2R}"
        ),
        eq(r"16R=(R-10)(R-6)=R^2-16R+60"),
        eq(r"R^2-32R+60=0"),
        p(r"So $(R-30)(R-2)=0$. Since $R>10$, we get $R=30$."),
        eq(r"\mathrm{Area}(\triangle AEF)=R-5-3-8=30-16=14"),
        p(r"<strong>Answer:</strong> $14$ square units."),
        '<h2 class="question">Question 15 — Two squares</h2>',
        question_box(
            p(
                r"$ABCD$ and $PQRS$ are two squares of side $10\,\mathrm{cm}$. "
                r"$P$ is placed at the centre of square $ABCD$ and $BX=4\,\mathrm{cm}$. "
                r"Find the area of the quadrilateral $PXCY$."
            ),
            figure(d15, "Squares ABCD and PQRS with P at the centre; BX = 4 cm"),
        ),
        '<h3 class="solution">Solution</h3>',
        p(
            r"Place $P$ at the origin and align $ABCD$ with the axes. Then the vertices are "
            r"$A(-5,5)$, $B(5,5)$, $C(5,-5)$, $D(-5,-5)$ (units in cm)."
        ),
        p(
            r"Side $BC$ runs from $B(5,5)$ down to $C(5,-5)$. Since $BX=4$, point $X$ is "
            r"$4$ units below $B$:"
        ),
        eq(r"X=(5,\,1)"),
        p(
            r"Because $PQRS$ is a square with vertex at the same centre $P$, a $90^\circ$ rotation "
            r"about $P$ sends side $PQ$ to side $PS$, and sends $BC$ to $CD$. Under a "
            r"$90^\circ$ clockwise rotation about $P$, $(x,y)\mapsto(y,-x)$, so"
        ),
        eq(r"X=(5,1)\;\mapsto\; Y=(1,-5)"),
        p(r"Thus $Y$ lies on $CD$ and $CY=4\,\mathrm{cm}$ (the image of $BX$)."),
        p(r"Now find the area of quadrilateral $PXCY$ by splitting it into two triangles."),
        p(r"<strong>Triangle $PXC$</strong>: base $XC=6$ (vertical) and height $5$ (distance from $P$ to $BC$)."),
        eq(r"\mathrm{Area}(\triangle PXC)=\dfrac{1}{2}\times 6\times 5=15"),
        p(r"<strong>Triangle $PYC$</strong>: base $CY=4$ (horizontal) and height $5$ (distance from $P$ to $CD$)."),
        eq(r"\mathrm{Area}(\triangle PYC)=\dfrac{1}{2}\times 4\times 5=10"),
        eq(r"\mathrm{Area}(PXCY)=15+10=25"),
        p(r"<strong>Answer:</strong> $25\,\mathrm{cm}^2$."),
    ]


def main() -> None:
    # Q14 uses the worksheet scan in content/year7/media/y7_q14_rectangle.png
    runpy.run_path(str(SCRIPTS / "render_y7_q15_squares.py"))
    runpy.run_path(str(SCRIPTS / "_crop_t3_hw7_qs.py"))

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MEDIA_OUT.mkdir(parents=True, exist_ok=True)

    src_media = CONTENT / "media"
    if src_media.exists():
        for f in src_media.glob("y7_*.png"):
            if f.is_file():
                shutil.copy2(f, MEDIA_OUT / f.name)

    blocks = year7_blocks() + congruent_triangle_2_blocks()
    enhanced, toc = enhance_blocks(blocks)
    html = page(
        title="Year 7 — Questions and Solutions",
        active_year=7,
        toc=toc,
        body="\n".join(enhanced),
        math_script=MATH_SCRIPT,
    )
    (OUT_DIR / "index.html").write_text(html, encoding="utf-8")
    print(f"Built {OUT_DIR / 'index.html'} ({len(enhanced)} blocks)")


if __name__ == "__main__":
    main()
