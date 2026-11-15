"""Build Year 12 pages from structured chapter content."""

from __future__ import annotations

import runpy
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "public" / "year12"
MEDIA_OUT = OUT_DIR / "media"
CONTENT = ROOT / "content" / "year12"
SCRIPTS = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS))
from site_common import enhance_blocks, escape, page  # noqa: E402
from log_calculus_1_content import log_calculus_1_blocks  # noqa: E402
from log_calculus_2_content import log_calculus_2_blocks  # noqa: E402
from exp_calculus_1_content import exp_calculus_1_blocks  # noqa: E402
from exp_calculus_2_content import exp_calculus_2_blocks  # noqa: E402
from trig_calculus_1_content import trig_calculus_1_blocks  # noqa: E402

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


def vector_geometry_1_blocks() -> list[str]:
    img1 = "/year12/media/vg1_q1_associative.png"
    img2 = "/year12/media/vg1_q2_planes.png"
    return [
        '<h1 class="doc-title">Year 12 — Questions and Solutions</h1>',
        '<h1 class="section">Vector Geometry (1)</h1>',
        '<h2 class="question">Question 1</h2>',
        question_box(
            p(
                r"Use vector geometry to prove that "
                r"$(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$."
            )
        ),
        '<h3 class="solution">Solution</h3>',
        p(
            "We prove the result geometrically by showing that both sides represent "
            "the same directed segment from a common starting point."
        ),
        p(
            r"Let $O$ be an origin in the plane (or in space). Represent the vectors "
            r"by directed segments:"
        ),
        p(
            r"$\overrightarrow{OA} = \mathbf{u}$, then $\overrightarrow{AB} = \mathbf{v}$, "
            r"then $\overrightarrow{BC} = \mathbf{w}$."
        ),
        p("By the triangle law of vector addition,"),
        eq(r"\overrightarrow{OB} = \overrightarrow{OA} + \overrightarrow{AB} = \mathbf{u} + \mathbf{v}"),
        eq(
            r"\overrightarrow{OC} = \overrightarrow{OB} + \overrightarrow{BC}"
            r" = (\mathbf{u} + \mathbf{v}) + \mathbf{w}"
        ),
        p(
            r"On the other hand, the single directed segment from $A$ to $C$ is "
            r"$\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{BC} = \mathbf{v} + \mathbf{w}$."
        ),
        p("Applying the triangle law again from $O$ to $C$ via $A$,"),
        eq(
            r"\overrightarrow{OC} = \overrightarrow{OA} + \overrightarrow{AC}"
            r" = \mathbf{u} + (\mathbf{v} + \mathbf{w})"
        ),
        p(
            r"Therefore both $(\mathbf{u} + \mathbf{v}) + \mathbf{w}$ and "
            r"$\mathbf{u} + (\mathbf{v} + \mathbf{w})$ equal the same vector "
            r"$\overrightarrow{OC}$."
        ),
        eq(r"(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})"),
        p("<strong>Hence vector addition is associative.</strong>"),
        figure(img1, "Geometric proof of associativity of vector addition"),
        p(
            "The same argument works in three dimensions: the construction uses only "
            "the triangle law along a broken line of directed segments, which is valid in space."
        ),
        # ---- Question 2 ----
        '<h2 class="question">Question 2</h2>',
        question_box(
            p(
                r"(a) Use a diagram to show that the distances from the vector "
                r"$\mathbf{u} = (x_0, y_0, z_0)$ to the $x$-$y$, $y$-$z$ and $x$-$z$ planes "
                r"are $z_0$, $x_0$ and $y_0$ respectively."
            ),
            p(
                r"(b) If $\alpha$, $\beta$, $\gamma$ are the angles that the vector "
                r"$\mathbf{u} = (x_0, y_0, z_0)$ makes with the positive $x$, $y$ and $z$-axes "
                r"respectively, prove that "
                r"$\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(
            r"Identify the tip of $\mathbf{u}$ with the point $P(x_0,y_0,z_0)$ in "
            r"$xyz$-space (taking the common initial point of position vectors as the origin $O$)."
        ),
        p("The coordinate planes and the perpendicular distances from $P$ to them are:"),
        p(
            r"• $x$-$y$ plane: $z = 0$. The foot of the perpendicular from $P$ is "
            r"$(x_0,y_0,0)$, so the distance is $|z_0|$. "
            r"(In the usual first-octant diagram one writes this as $z_0$.)"
        ),
        p(
            r"• $y$-$z$ plane: $x = 0$. The foot is $(0,y_0,z_0)$, so the distance is $|x_0|$ "
            r"(shown as $x_0$)."
        ),
        p(
            r"• $x$-$z$ plane: $y = 0$. The foot is $(x_0,0,z_0)$, so the distance is $|y_0|$ "
            r"(shown as $y_0$)."
        ),
        figure(img2, "Distances from u to the coordinate planes"),
        p(
            r"Thus the distances from $\mathbf{u} = (x_0,y_0,z_0)$ to the $x$-$y$, $y$-$z$ and "
            r"$x$-$z$ planes are $z_0$, $x_0$ and $y_0$ respectively."
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(
            r"Let $|\mathbf{u}| = r = \sqrt{x_0^2 + y_0^2 + z_0^2}$ "
            r"(assume $\mathbf{u} \neq \mathbf{0}$)."
        ),
        p(
            r"By definition of the direction angles,"
        ),
        eq(r"\cos\alpha = \dfrac{x_0}{r},\qquad \cos\beta = \dfrac{y_0}{r},\qquad \cos\gamma = \dfrac{z_0}{r}"),
        p("Therefore"),
        eq(
            r"\cos^2\alpha + \cos^2\beta + \cos^2\gamma"
            r" = \dfrac{x_0^2}{r^2} + \dfrac{y_0^2}{r^2} + \dfrac{z_0^2}{r^2}"
            r" = \dfrac{x_0^2 + y_0^2 + z_0^2}{r^2}"
            r" = \dfrac{r^2}{r^2} = 1"
        ),
        p(
            r"<strong>Hence $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$.</strong>"
        ),
        # ---- Question 1 (Level 3) ----
        '<h2 class="question">Question 1 (Level 3)</h2>',
        question_box(
            p(
                r"The points $A$, $B$, $C$ and $D$ form a parallelogram, where "
                r"$A = \begin{pmatrix}-1\\2\\1\end{pmatrix}$, "
                r"$B = \begin{pmatrix}-3\\5\\2\end{pmatrix}$ and "
                r"$C = \begin{pmatrix}1\\3\\4\end{pmatrix}$. "
                r"Find the possible position vectors of $D$."
            )
        ),
        '<h3 class="solution">Solution</h3>',
        p(
            r"The order of the vertices is not specified, so any one of $A$, $B$ or $C$ "
            r"may be opposite $D$. Equivalently, the midpoint of one of the segments "
            r"$AB$, $AC$ or $BC$ is also the midpoint of the other diagonal."
        ),
        p(r"<strong>Case 1:</strong> $AB$ and $CD$ are diagonals (so $C$ and $D$ complete with midpoint of $AB$)."),
        eq(r"\dfrac{A+B}{2} = \dfrac{C+D}{2} \Rightarrow D = A + B - C"),
        eq(
            r"D = \begin{pmatrix}-1\\2\\1\end{pmatrix}"
            r" + \begin{pmatrix}-3\\5\\2\end{pmatrix}"
            r" - \begin{pmatrix}1\\3\\4\end{pmatrix}"
            r" = \begin{pmatrix}-5\\4\\-1\end{pmatrix}"
        ),
        p(r"<strong>Case 2:</strong> $AC$ and $BD$ are diagonals."),
        eq(r"\dfrac{A+C}{2} = \dfrac{B+D}{2} \Rightarrow D = A + C - B"),
        eq(
            r"D = \begin{pmatrix}-1\\2\\1\end{pmatrix}"
            r" + \begin{pmatrix}1\\3\\4\end{pmatrix}"
            r" - \begin{pmatrix}-3\\5\\2\end{pmatrix}"
            r" = \begin{pmatrix}3\\0\\3\end{pmatrix}"
        ),
        p(r"<strong>Case 3:</strong> $BC$ and $AD$ are diagonals."),
        eq(r"\dfrac{B+C}{2} = \dfrac{A+D}{2} \Rightarrow D = B + C - A"),
        eq(
            r"D = \begin{pmatrix}-3\\5\\2\end{pmatrix}"
            r" + \begin{pmatrix}1\\3\\4\end{pmatrix}"
            r" - \begin{pmatrix}-1\\2\\1\end{pmatrix}"
            r" = \begin{pmatrix}-1\\6\\5\end{pmatrix}"
        ),
        p(
            r"<strong>Answer:</strong> the possible position vectors of $D$ are "
            r"$\begin{pmatrix}-5\\4\\-1\end{pmatrix}$, "
            r"$\begin{pmatrix}3\\0\\3\end{pmatrix}$ and "
            r"$\begin{pmatrix}-1\\6\\5\end{pmatrix}$."
        ),
        # ---- Question 2 (Level 3) ----
        '<h2 class="question">Question 2 (Level 3)</h2>',
        question_box(
            figure(
                "/year12/media/vg1_q2_level3.png",
                "Quadrilateral OAYB with diagonals AB and OY meeting at X",
            ),
            p(r"In the diagram, $\overrightarrow{OA} = 3\mathbf{a}$, $\overrightarrow{OB} = 6\mathbf{b}$ and $\overrightarrow{YB} = 5\mathbf{a} - \mathbf{b}$."),
            p(r"(a) Express $\overrightarrow{AB}$ and $\overrightarrow{OY}$ in terms of $\mathbf{a}$ and $\mathbf{b}$."),
            p(r"(b) Find the ratio in which $X$ divides $AB$ and $OY$."),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"Take $O$ as the origin, so the position vectors are $\mathbf{A} = 3\mathbf{a}$ and $\mathbf{B} = 6\mathbf{b}$."),
        p(r"Since $\overrightarrow{YB} = \mathbf{B} - \mathbf{Y} = 5\mathbf{a} - \mathbf{b}$,"),
        eq(r"\mathbf{Y} = \mathbf{B} - (5\mathbf{a} - \mathbf{b}) = 6\mathbf{b} - 5\mathbf{a} + \mathbf{b} = -5\mathbf{a} + 7\mathbf{b}"),
        eq(r"\overrightarrow{AB} = \mathbf{B} - \mathbf{A} = 6\mathbf{b} - 3\mathbf{a} = -3\mathbf{a} + 6\mathbf{b}"),
        eq(r"\overrightarrow{OY} = \mathbf{Y} = -5\mathbf{a} + 7\mathbf{b}"),
        p(
            r"<strong>Answer:</strong> $\overrightarrow{AB} = -3\mathbf{a} + 6\mathbf{b}$, "
            r"$\overrightarrow{OY} = -5\mathbf{a} + 7\mathbf{b}$."
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"Let $X$ divide $AB$ in the ratio $\lambda : 1$, so $\overrightarrow{AX}:\overrightarrow{XB} = \lambda:1$. Then"),
        eq(r"\mathbf{X} = \dfrac{\mathbf{A} + \lambda\mathbf{B}}{\lambda + 1} = \dfrac{3\mathbf{a} + 6\lambda\mathbf{b}}{\lambda + 1}"),
        p(r"Let $X$ also divide $OY$ in the ratio $\mu : 1$, so $\overrightarrow{OX}:\overrightarrow{XY} = \mu:1$. Then"),
        eq(r"\mathbf{X} = \dfrac{\mu\mathbf{Y}}{\mu + 1} = \dfrac{\mu(-5\mathbf{a} + 7\mathbf{b})}{\mu + 1}"),
        p(r"Equating coefficients of $\mathbf{a}$ and $\mathbf{b}$ (assuming $\mathbf{a}$, $\mathbf{b}$ independent),"),
        eq(r"\dfrac{3}{\lambda + 1} = \dfrac{-5\mu}{\mu + 1}, \qquad \dfrac{6\lambda}{\lambda + 1} = \dfrac{7\mu}{\mu + 1}"),
        p(r"From the second equation,"),
        eq(r"6\lambda(\mu + 1) = 7\mu(\lambda + 1) \Rightarrow 6\lambda - 7\mu = \lambda\mu"),
        eq(r"\lambda = \dfrac{7\mu}{6 - \mu}"),
        p(r"Substitute into the first equation:"),
        eq(r"3(\mu + 1) = -5\mu(\lambda + 1)"),
        eq(r"3 + 8\mu = -5\lambda\mu"),
        eq(r"3 + 8\mu = -5\mu\cdot\dfrac{7\mu}{6 - \mu} = \dfrac{-35\mu^2}{6 - \mu}"),
        eq(r"(3 + 8\mu)(6 - \mu) = -35\mu^2"),
        eq(r"18 + 48\mu - 3\mu - 8\mu^2 = -35\mu^2"),
        eq(r"27\mu^2 + 45\mu + 18 = 0"),
        eq(r"3\mu^2 + 5\mu + 2 = 0 \Rightarrow (3\mu + 2)(\mu + 1) = 0"),
        p(r"So $\mu = -1$ (invalid, since $\mu + 1 = 0$) or $\mu = -\dfrac{2}{3}$."),
        eq(r"\lambda = \dfrac{7(-\tfrac{2}{3})}{6 - (-\tfrac{2}{3})} = \dfrac{-\tfrac{14}{3}}{\tfrac{20}{3}} = -\dfrac{7}{10}"),
        p(
            r"Hence $X$ divides $AB$ in the ratio $\overrightarrow{AX}:\overrightarrow{XB} = -7:10$ "
            r"(i.e. externally in the ratio $7:10$), and divides $OY$ in the ratio "
            r"$\overrightarrow{OX}:\overrightarrow{XY} = -2:3$ (externally in the ratio $2:3$)."
        ),
        p(
            r"<strong>Answer:</strong> $X$ divides $AB$ in the ratio $7:10$ externally, "
            r"and divides $OY$ in the ratio $2:3$ externally."
        ),
        # ---- Question 2 (Projections) ----
        '<h2 class="question">Question 2 (Projections)</h2>',
        question_box(
            p(
                r"Given nonzero vectors $\mathbf{u}$ and $\mathbf{v}$ in $\mathbb{R}^2$, "
                r"prove the following identities using a geometric argument:"
            ),
            p(r"(i) $\mathrm{proj}_{\mathbf{u}}(-\mathbf{v}) = -\mathrm{proj}_{\mathbf{u}}(\mathbf{v})$"),
        ),
        '<h3 class="solution">Solution (i)</h3>',
        figure(
            "/year12/media/vg1_q2_proj.png",
            "Geometric comparison of proj_u(v) and proj_u(-v)",
        ),
        p(
            r"Recall that $\mathrm{proj}_{\mathbf{u}}(\mathbf{v})$ is the vector along the line "
            r"through $\mathbf{u}$ obtained by dropping a perpendicular from the tip of "
            r"$\mathbf{v}$ onto that line."
        ),
        p(
            r"Replace $\mathbf{v}$ by $-\mathbf{v}$. The tip of $-\mathbf{v}$ is the point "
            r"diametrically opposite the tip of $\mathbf{v}$ through the common initial point. "
            r"The perpendicular from the tip of $-\mathbf{v}$ to the line of $\mathbf{u}$ "
            r"therefore meets that line at the point opposite "
            r"$\mathrm{proj}_{\mathbf{u}}(\mathbf{v})$ with respect to the origin."
        ),
        p(
            r"Hence the projected vector is exactly the negative of "
            r"$\mathrm{proj}_{\mathbf{u}}(\mathbf{v})$:"
        ),
        eq(r"\mathrm{proj}_{\mathbf{u}}(-\mathbf{v}) = -\mathrm{proj}_{\mathbf{u}}(\mathbf{v})"),
        p(
            r"(Algebraically the same conclusion follows from "
            r"$\mathrm{proj}_{\mathbf{u}}(\mathbf{v})=\dfrac{\mathbf{v}\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\mathbf{u}$, "
            r"since $(-\mathbf{v})\cdot\mathbf{u}=-(\mathbf{v}\cdot\mathbf{u})$, but the question asks for a geometric argument.)"
        ),
        # ---- Question 3 (Pythagoras) ----
        '<h2 class="question">Question 3</h2>',
        question_box(
            p(r"Use vector methods to prove Pythagoras' theorem.")
        ),
        '<h3 class="solution">Solution</h3>',
        figure(
            "/year12/media/vg1_q3_pythagoras.png",
            "Right triangle with vectors a, b, c for Pythagoras proof",
        ),
        p(
            r"Let $\triangle ABC$ be right-angled at $C$. Write "
            r"$\mathbf{a}=\overrightarrow{CA}$ and $\mathbf{b}=\overrightarrow{CB}$, "
            r"and let $\mathbf{c}=\overrightarrow{AB}$."
        ),
        p(r"Then $\mathbf{c}=\mathbf{b}-\mathbf{a}$, and since $\angle C=90^\circ$ the sides $CA$ and $CB$ are perpendicular, so"),
        eq(r"\mathbf{a}\cdot\mathbf{b}=0"),
        p(r"Now expand $|\mathbf{c}|^2=\mathbf{c}\cdot\mathbf{c}$:"),
        eq(
            r"|\mathbf{c}|^2 = (\mathbf{b}-\mathbf{a})\cdot(\mathbf{b}-\mathbf{a})"
            r" = |\mathbf{b}|^2 - 2\mathbf{a}\cdot\mathbf{b} + |\mathbf{a}|^2"
        ),
        p(r"Using $\mathbf{a}\cdot\mathbf{b}=0$,"),
        eq(r"|\mathbf{c}|^2 = |\mathbf{a}|^2 + |\mathbf{b}|^2"),
        p(
            r"But $|\mathbf{a}|=CA$, $|\mathbf{b}|=CB$ and $|\mathbf{c}|=AB$, so"
        ),
        eq(r"AB^2 = CA^2 + CB^2"),
        p(r"<strong>Hence Pythagoras' theorem holds.</strong>"),
        p(
            r"(Equivalently: if $\mathbf{u}$ and $\mathbf{v}$ are orthogonal, then "
            r"$|\mathbf{u}+\mathbf{v}|^2=|\mathbf{u}|^2+|\mathbf{v}|^2$, since the cross term "
            r"$2\mathbf{u}\cdot\mathbf{v}$ vanishes.)"
        ),
    ]


def main() -> None:
    runpy.run_path(str(SCRIPTS / "render_vg1_q1.py"))
    runpy.run_path(str(SCRIPTS / "render_vg1_q2.py"))
    runpy.run_path(str(SCRIPTS / "render_vg1_q2_level3.py"))
    runpy.run_path(str(SCRIPTS / "render_vg1_proj.py"))
    runpy.run_path(str(SCRIPTS / "render_vg1_pythagoras.py"))
    runpy.run_path(str(SCRIPTS / "render_log1_ex3_q2.py"))
    runpy.run_path(str(SCRIPTS / "render_log1_ex3_q1c.py"))

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MEDIA_OUT.mkdir(parents=True, exist_ok=True)

    src_media = CONTENT / "media"
    if src_media.exists():
        for f in src_media.glob("*"):
            if f.is_file():
                shutil.copy2(f, MEDIA_OUT / f.name)

    blocks = (
        vector_geometry_1_blocks()
        + log_calculus_1_blocks()
        + log_calculus_2_blocks()
        + exp_calculus_1_blocks()
        + exp_calculus_2_blocks()
        + trig_calculus_1_blocks()
    )
    enhanced, toc = enhance_blocks(blocks)
    html = page(
        title="Year 12 — Questions and Solutions",
        active_year=12,
        toc=toc,
        body="\n".join(enhanced),
        math_script=MATH_SCRIPT,
    )
    (OUT_DIR / "index.html").write_text(html, encoding="utf-8")
    print(f"Built {OUT_DIR / 'index.html'} ({len(enhanced)} blocks)")


if __name__ == "__main__":
    main()
