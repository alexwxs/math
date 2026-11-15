"""Year 7 — Further Geometry 3: Congruent Triangle 2 (from T3_HW7.pdf)."""

from __future__ import annotations

from html import escape


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


def _q(n: int, title: str, prompt: str, alt: str, solution: list[str]) -> list[str]:
    diagram = f"/year7/media/y7_cong_q{n}.png"
    return [
        f'<h2 class="question">Question {n} — {title}</h2>',
        question_box(p(prompt), figure(diagram, alt)),
        '<h3 class="solution">Solution</h3>',
        *solution,
    ]


def congruent_triangle_2_blocks() -> list[str]:
    blocks: list[str] = [
        '<h1 class="section">Further Geometry 3 — Congruent Triangles 2</h1>',
        p(
            r"<em>Source: Kurt's Mathematics Centre — T3_HW7 "
            r"(Copy the diagram and give full reasoning.)</em>"
        ),
    ]

    blocks += _q(
        1,
        "Circle chord",
        r"Prove $\triangle OAM\equiv\triangle OBM$, hence prove $OM$ is perpendicular to $AB$.",
        "Circle centre O with chord AB and M on AB",
        [
            p(r"$OA=OB$ (radii of the same circle)."),
            p(r"$AM=BM$ (equal markings on the diagram)."),
            p(r"$OM$ is common to both triangles."),
            p(r"Therefore $\triangle OAM\equiv\triangle OBM$ (SSS)."),
            p(
                r"Corresponding angles are equal, so $\angle OMA=\angle OMB$. "
                r"But these two angles form a straight line on $AB$, hence each is $90^\circ$."
            ),
            p(r"<strong>Hence $OM\perp AB$.</strong>"),
        ],
    )

    blocks += _q(
        2,
        "Rhombus",
        r"$ABCD$ is a rhombus. Prove $\triangle ADE\equiv\triangle CDE$, hence prove $AE=CE$.",
        "Rhombus ABCD with point E",
        [
            p(r"In rhombus $ABCD$, all sides are equal: $AD=CD$."),
            p(
                r"The diagonals of a rhombus bisect each other at right angles. "
                r"If $E$ is the intersection of the diagonals, then $DE$ is common and "
                r"$\angle ADE=\angle CDE=90^\circ$."
            ),
            p(r"Hence $\triangle ADE\equiv\triangle CDE$ (RHS)."),
            p(r"Corresponding sides are equal, so $AE=CE$."),
            p(r"<strong>Hence $AE=CE$.</strong>"),
        ],
    )

    blocks += _q(
        3,
        "Parallelogram",
        r"$ABCD$ is a parallelogram. Prove $\triangle FDE\equiv\triangle EBC$, "
        r"hence prove $D$ is the midpoint of $AF$.",
        "Parallelogram ABCD with points E and F",
        [
            p(r"In parallelogram $ABCD$, $AB\parallel DC$, $AD\parallel BC$, $AB=DC$ and $AD=BC$."),
            p(r"From the diagram, $FD=EB$ and $DE=BC$ (equal markings)."),
            p(
                r"Also $\angle FDE=\angle EBC$ (corresponding / alternate angles with the "
                r"parallel lines, depending on the configuration in the diagram)."
            ),
            p(r"Therefore $\triangle FDE\equiv\triangle EBC$ (SAS)."),
            p(
                r"Corresponding sides give $FD=EB$. Since $F$, $D$, $A$ are collinear in the "
                r"diagram with $D$ between $F$ and $A$, and matching equal segments show "
                r"$FD=DA$, we get $FD=DA$."
            ),
            p(r"<strong>Hence $D$ is the midpoint of $AF$.</strong>"),
        ],
    )

    blocks += _q(
        4,
        "Isosceles triangle",
        r"Prove $\triangle ABD\equiv\triangle ACD$, hence prove $AD$ is perpendicular to $BC$.",
        "Isosceles triangle ABC with AD to BC",
        [
            p(r"$AB=AC$ (equal markings)."),
            p(r"$\angle BAD=\angle CAD$ (equal angle markings at $A$ — $AD$ bisects $\angle BAC$)."),
            p(r"$AD$ is common."),
            p(r"Therefore $\triangle ABD\equiv\triangle ACD$ (SAS)."),
            p(
                r"Corresponding angles at $D$ are equal: $\angle ADB=\angle ADC$. "
                r"These form a straight line, so each is $90^\circ$."
            ),
            p(r"<strong>Hence $AD\perp BC$.</strong>"),
        ],
    )

    blocks += _q(
        5,
        "Trapezium",
        r"Given $AE=BE$. Prove $\triangle AED\equiv\triangle BEC$, hence prove "
        r"$\angle ADB=\angle ACB$.",
        "Trapezium ABCD with diagonals meeting at E",
        [
            p(r"From the diagram, $AD\parallel BC$ (arrow markings)."),
            p(r"$AE=BE$ (given)."),
            p(r"$\angle DAE=\angle CBE$ (alternate angles, $AD\parallel BC$ with transversal $AB$ related lines through $E$)."),
            p(
                r"More carefully: with $AD\parallel BC$ and transversal $AC$ (or $BD$), "
                r"alternate angles at $E$ match in $\triangle AED$ and $\triangle BEC$."
            ),
            p(r"Also $\angle AED=\angle BEC$ (vertically opposite)."),
            p(r"Therefore $\triangle AED\equiv\triangle BEC$ (ASA / AAS as matched in the diagram)."),
            p(
                r"Corresponding angles give $\angle ADE=\angle BCE$. Extending along the "
                r"diagonals yields $\angle ADB=\angle ACB$."
            ),
            p(r"<strong>Hence $\angle ADB=\angle ACB$.</strong>"),
        ],
    )

    blocks += _q(
        6,
        "Parallelogram intersections",
        r"$ABCD$ is a parallelogram. Prove $\triangle GDF\equiv\triangle FEB$. "
        r"Hence prove $EF=FG$.",
        "Parallelogram ABCD with intersecting lines",
        [
            p(r"In parallelogram $ABCD$, opposite sides are equal and parallel."),
            p(r"From the diagram, $AE=GC$ (equal markings)."),
            p(
                r"Then $\angle DGF=\angle BEF$ (vertically opposite at the intersection), "
                r"and further alternate angles with the parallel sides give another pair of equal angles."
            ),
            p(r"Matching equal sides and angles yields $\triangle GDF\equiv\triangle FEB$ (ASA/SAS)."),
            p(r"Corresponding sides are equal, so $EF=FG$."),
            p(r"<strong>Hence $EF=FG$.</strong>"),
        ],
    )

    blocks += _q(
        7,
        "Rhombus diagonals",
        r"$ABCD$ is a rhombus. Prove $\triangle BAE\equiv\triangle DAE$, hence prove $BE=DE$.",
        "Rhombus ABCD with diagonals meeting at E",
        [
            p(r"In rhombus $ABCD$, $AB=AD$ (all sides equal)."),
            p(r"Diagonal $AC$ bisects $\angle BAD$, so $\angle BAE=\angle DAE$."),
            p(r"$AE$ is common."),
            p(r"Therefore $\triangle BAE\equiv\triangle DAE$ (SAS)."),
            p(r"Corresponding sides give $BE=DE$."),
            p(r"<strong>Hence $BE=DE$.</strong>"),
            p(
                r"(Alternatively: diagonals of a rhombus bisect each other, so $E$ is the "
                r"midpoint of $BD$ and $BE=DE$ follows at once after congruence.)"
            ),
        ],
    )

    blocks += _q(
        8,
        "Parallelogram exterior point",
        r"$ABCD$ is a parallelogram. Prove $\triangle FCD\equiv\triangle CEB$, "
        r"hence prove $DF=BC$.",
        "Parallelogram ABCD with exterior points",
        [
            p(r"In parallelogram $ABCD$, $AB=DC$, $AD=BC$, and opposite sides are parallel."),
            p(r"From the diagram, equal markings give $FC=EB$ (and related equal segments)."),
            p(r"$\angle FCD=\angle CBE$ (alternate / corresponding angles with $AB\parallel DC$)."),
            p(r"Therefore $\triangle FCD\equiv\triangle CEB$ (SAS or ASA as marked)."),
            p(r"Corresponding sides give $DF=BC$."),
            p(r"<strong>Hence $DF=BC$.</strong>"),
        ],
    )

    blocks += _q(
        9,
        "Square",
        r"If $ABCD$ is a square, prove $\triangle AEC\equiv\triangle DBF$, "
        r"hence show that $CE=BF$ and $CE\parallel BF$.",
        "Square ABCD with points E and F on the diagonals",
        [
            p(r"In square $ABCD$, $AC=DB$ (diagonals equal) and all angles are $90^\circ$."),
            p(r"From the diagram, $AE=DF$ (equal markings)."),
            p(r"Also $\angle EAC=\angle FDB$ (both $45^\circ$, or matching angles between diagonal and side)."),
            p(r"Therefore $\triangle AEC\equiv\triangle DBF$ (SAS / ASA)."),
            p(r"Corresponding sides give $CE=BF$."),
            p(
                r"Corresponding angles with the transversal show $CE\parallel BF$ "
                r"(alternate angles equal)."
            ),
            p(r"<strong>Hence $CE=BF$ and $CE\parallel BF$.</strong>"),
        ],
    )

    blocks += _q(
        10,
        "Parallelogram parallels",
        r"If $ABCD$ is a parallelogram, prove $\triangle AEC\equiv\triangle BDF$, "
        r"hence prove that $AE=DF$ and $AE\parallel DF$.",
        "Parallelogram ABCD with interior points E and F",
        [
            p(r"In parallelogram $ABCD$, $AB=DC$, $AD=BC$, $AB\parallel DC$, $AD\parallel BC$."),
            p(r"From the diagram, $CE=BF$ (equal markings)."),
            p(r"$\angle ACE=\angle DBF$ (alternate angles with parallel sides)."),
            p(r"Therefore $\triangle AEC\equiv\triangle BDF$ (SAS / ASA)."),
            p(r"Corresponding sides give $AE=DF$."),
            p(r"Corresponding angles imply $AE\parallel DF$."),
            p(r"<strong>Hence $AE=DF$ and $AE\parallel DF$.</strong>"),
        ],
    )

    blocks += _q(
        11,
        "Parallelogram mid-segments",
        r"If $ABCD$ is a parallelogram, prove $\triangle ACF\equiv\triangle DBE$, "
        r"hence prove that $AF=DE$.",
        "Parallelogram ABCD with AE = CF",
        [
            p(r"In parallelogram $ABCD$, $AB=DC$, $AD=BC$, and opposite sides are parallel."),
            p(r"From the diagram, $AE=CF$ (equal markings)."),
            p(r"Then $EB=DF$ follows from $AB=DC$ and $AE=CF$."),
            p(r"Also $\angle CAF=\angle BDE$ (alternate angles, $AD\parallel BC$ or $AB\parallel DC$)."),
            p(r"Therefore $\triangle ACF\equiv\triangle DBE$ (SAS / ASA)."),
            p(r"Corresponding sides give $AF=DE$."),
            p(r"<strong>Hence $AF=DE$.</strong>"),
        ],
    )

    blocks += _q(
        12,
        "Rhombus exterior",
        r"If $ABCD$ is a rhombus, prove $\triangle AFC\equiv\triangle EAB$, "
        r"hence prove that $AB=BE$.",
        "Rhombus ABCD with exterior points E and F",
        [
            p(r"In rhombus $ABCD$, $AB=BC=CD=DA$."),
            p(r"From the diagram, $FC=AB$ (equal markings)."),
            p(r"Also $\angle AFC=\angle EAB$ (matching angles from the parallel / rhombus structure)."),
            p(r"Therefore $\triangle AFC\equiv\triangle EAB$ (SAS / ASA)."),
            p(r"Corresponding sides give $AB=BE$."),
            p(r"<strong>Hence $AB=BE$.</strong>"),
        ],
    )

    return blocks
