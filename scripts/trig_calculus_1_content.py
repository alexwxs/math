"""Calculus of Trigonometric Functions (I) — from worksheet PDF 20261113194042."""

from __future__ import annotations


def p(text: str) -> str:
    return f"<p>{text}</p>"


def eq(latex: str) -> str:
    return f'<p class="display-math">$${latex}$$</p>'


def question_box(*parts: str) -> str:
    return f'<aside class="question-box">{"".join(parts)}</aside>'


def figure(src: str, alt: str) -> str:
    from html import escape

    return (
        f'<figure class="figure"><img src="{escape(src)}" alt="{escape(alt)}" '
        'loading="lazy" /></figure>'
    )


def trig_calculus_1_blocks() -> list[str]:
    lim_fig = "/year12/media/trig1_ex1_q1.png"
    poly_fig = "/year12/media/trig1_ex1_q2.png"
    return [
        '<h1 class="section">Calculus of Trigonometric Functions (I)</h1>',
        p(
            r"<em>Source: Year 12 (A1) Mathematics Extension 1 — Optional Challenging Questions "
            r"(Level 3).</em>"
        ),
        # ---------- Exercise 1 ----------
        '<h2 class="question">Exercise 1 — Question 1</h2>',
        question_box(
            p(
                r"Explain the geometrical significance of both "
                r"$\displaystyle\lim_{\theta\to 0}\dfrac{\sin\theta}{\theta}=1$ and "
                r"$\displaystyle\lim_{\theta\to 0}\dfrac{\tan\theta}{\theta}=1$."
            ),
            figure(lim_fig, "Unit circle with chord, arc and tangent for small θ"),
        ),
        '<h3 class="solution">Solution</h3>',
        p(
            r"On the unit circle, let $\angle AOB=\theta$ (radians), with arc $AB$ of length "
            r"$\theta$, chord $AB$, perpendicular $AP=\sin\theta$, and tangent segment "
            r"$BT=\tan\theta$."
        ),
        p(r"Comparing lengths (for $0<\theta<\tfrac{\pi}{2}$):"),
        eq(r"\sin\theta < \theta < \tan\theta"),
        p(r"Divide through by $\theta>0$:"),
        eq(r"\dfrac{\sin\theta}{\theta}<1<\dfrac{\tan\theta}{\theta}"),
        p(
            r"As $\theta\to 0^+$, the chord, arc and tangent segment all become "
            r"indistinguishable, so both ratios tend to $1$. Geometrically:"
        ),
        p(
            r"$\dfrac{\sin\theta}{\theta}\to 1$ means the vertical rise $\sin\theta$ is "
            r"asymptotically the same as the arc length $\theta$;"
        ),
        p(
            r"$\dfrac{\tan\theta}{\theta}\to 1$ means the tangent length $\tan\theta$ is "
            r"likewise asymptotically equal to the arc length."
        ),
        p(
            r"(Equivalently: for small angles in radians, $\sin\theta\approx\theta\approx\tan\theta$.)"
        ),
        '<h2 class="question">Exercise 1 — Question 2</h2>',
        question_box(
            p(
                r"The diagram shows a regular $n$-sided polygon inscribed in a circle of "
                r"radius $r$. Each side subtends an angle of $\alpha$ radians at the centre."
            ),
            figure(poly_fig, "Regular polygon inscribed in a circle with central angle α"),
            p(r"(a) Prove that the perimeter of the polygon is $2nr\sin\dfrac{\pi}{n}$."),
            p(
                r"(b) Prove that the area of the polygon is "
                r"$\dfrac{1}{2}nr^2\sin\dfrac{2\pi}{n}$."
            ),
            p(
                r"(c) Also prove that the corresponding area of the circumscribed polygon "
                r"(sides tangent to the circle) is $nr^2\tan\dfrac{\pi}{n}$."
            ),
            p(r"(d) Hence deduce the area of the circle by using an inequality and limits."),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"The central angle is $\alpha=\dfrac{2\pi}{n}$."),
        p(r"Each side is a chord of angular width $\alpha$, so its length is"),
        eq(r"2r\sin\dfrac{\alpha}{2}=2r\sin\dfrac{\pi}{n}"),
        eq(r"\text{Perimeter}=n\cdot 2r\sin\dfrac{\pi}{n}=2nr\sin\dfrac{\pi}{n}"),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"The polygon is made of $n$ isosceles triangles of two sides $r$ and included angle $\alpha$:"),
        eq(
            r"\text{Area}=n\cdot\dfrac{1}{2}r^2\sin\alpha"
            r"=\dfrac{1}{2}nr^2\sin\dfrac{2\pi}{n}"
        ),
        '<h3 class="solution">Solution (c)</h3>',
        p(
            r"For the circumscribed polygon, each side is tangent to the circle. "
            r"Half a side forms a right triangle with opposite side $r\tan\dfrac{\pi}{n}$, "
            r"so each full side is $2r\tan\dfrac{\pi}{n}$."
        ),
        p(r"Area of one triangle from the centre to a side:"),
        eq(r"\dfrac{1}{2}\cdot\bigl(2r\tan\dfrac{\pi}{n}\bigr)\cdot r=r^2\tan\dfrac{\pi}{n}"),
        eq(r"\text{Total area}=nr^2\tan\dfrac{\pi}{n}"),
        '<h3 class="solution">Solution (d)</h3>',
        p(r"The inscribed polygon lies inside the circle, which lies inside the circumscribed polygon:"),
        eq(
            r"\dfrac{1}{2}nr^2\sin\dfrac{2\pi}{n}"
            r"\le \pi r^2"
            r"\le nr^2\tan\dfrac{\pi}{n}"
        ),
        p(r"Divide by $r^2>0$:"),
        eq(
            r"n\sin\dfrac{\pi}{n}\cos\dfrac{\pi}{n}"
            r"\le \pi"
            r"\le n\tan\dfrac{\pi}{n}"
        ),
        p(
            r"Let $\theta=\dfrac{\pi}{n}$. As $n\to\infty$, $\theta\to 0^+$, and using "
            r"$\dfrac{\sin\theta}{\theta}\to 1$ and $\dfrac{\tan\theta}{\theta}\to 1$:"
        ),
        eq(
            r"n\sin\dfrac{\pi}{n}\cos\dfrac{\pi}{n}"
            r"=\pi\cdot\dfrac{\sin\theta}{\theta}\cdot\cos\theta\to\pi\cdot 1\cdot 1=\pi"
        ),
        eq(r"n\tan\dfrac{\pi}{n}=\pi\cdot\dfrac{\tan\theta}{\theta}\to\pi"),
        p(
            r"By the squeeze theorem the area of the circle is $\pi r^2$."
        ),
        # ---------- Exercise 2 ----------
        '<h2 class="question">Exercise 2 — Question 1</h2>',
        question_box(
            p(
                r"If $f(x)=\cos^2 x+\cos^2\!\left(x+\dfrac{2\pi}{3}\right)"
                r"+\cos^2\!\left(x-\dfrac{2\pi}{3}\right)$, "
                r"prove that $f'(x)=0$ for all real $x$. "
                r"Hence show that $f(x)=\dfrac{3}{2}$ for all real $x$."
            )
        ),
        '<h3 class="solution">Solution</h3>',
        eq(
            r"f'(x)=-\sin 2x-\sin\!\left(2x+\dfrac{4\pi}{3}\right)"
            r"-\sin\!\left(2x-\dfrac{4\pi}{3}\right)"
        ),
        p(
            r"The three angles $2x$, $2x+\dfrac{4\pi}{3}$, $2x-\dfrac{4\pi}{3}$ are equally "
            r"spaced by $\dfrac{4\pi}{3}$. Their sines sum to zero:"
        ),
        eq(
            r"\sin\theta+\sin\!\left(\theta+\dfrac{4\pi}{3}\right)"
            r"+\sin\!\left(\theta-\dfrac{4\pi}{3}\right)"
            r"=2\sin\theta\cos\dfrac{4\pi}{3}+\sin\theta"
            r"=\sin\theta\bigl(1+2\cdot(-\tfrac{1}{2})\bigr)=0"
        ),
        p(r"with $\theta=2x$. Hence $f'(x)=0$ for all $x$, so $f$ is constant."),
        eq(
            r"f(0)=1+\cos^2\dfrac{2\pi}{3}+\cos^2\!\left(-\dfrac{2\pi}{3}\right)"
            r"=1+\left(-\dfrac{1}{2}\right)^2+\left(-\dfrac{1}{2}\right)^2"
            r"=1+\dfrac{1}{4}+\dfrac{1}{4}=\dfrac{3}{2}"
        ),
        p(r"Therefore $f(x)=\dfrac{3}{2}$ for all real $x$."),
        # ---------- Exercise 3 ----------
        '<h2 class="question">Exercise 3 — Question 1</h2>',
        question_box(
            p(
                r"Let $f(t)=\sin(a+nt)\sin b-\sin a\sin(b-nt)$, where $a$, $b$ and $n$ are "
                r"constants with $a>0$, $b>0$, $a+b<\pi$ and $n\neq 0$."
            ),
            p(r"(a) Prove that $f''(t)=-n^2 f(t)$ and $f(0)=0$."),
            p(r"(b) Prove that $f(t)=\sin(a+b)\sin(nt)$."),
            p(
                r"(c) Find all values of $t$ for which "
                r"$\dfrac{\sin(a+nt)}{\sin(b-nt)}=\dfrac{\sin a}{\sin b}$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        eq(r"f(0)=\sin a\sin b-\sin a\sin b=0"),
        eq(
            r"f'(t)=n\cos(a+nt)\sin b+n\sin a\cos(b-nt)"
        ),
        eq(
            r"f''(t)=-n^2\sin(a+nt)\sin b+n^2\sin a\sin(b-nt)"
            r"=-n^2\bigl(\sin(a+nt)\sin b-\sin a\sin(b-nt)\bigr)"
            r"=-n^2 f(t)"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"Expand using angle formulae:"),
        eq(
            r"\sin(a+nt)\sin b"
            r"=(\sin a\cos(nt)+\cos a\sin(nt))\sin b"
        ),
        eq(
            r"\sin a\sin(b-nt)"
            r"=\sin a\bigl(\sin b\cos(nt)-\cos b\sin(nt)\bigr)"
        ),
        eq(
            r"f(t)"
            r"=(\cos a\sin b+\sin a\cos b)\sin(nt)"
            r"=\sin(a+b)\sin(nt)"
        ),
        '<h3 class="solution">Solution (c)</h3>',
        p(
            r"The given equation is equivalent to "
            r"$\sin(a+nt)\sin b=\sin a\sin(b-nt)$, i.e. $f(t)=0$, "
            r"provided $\sin(b-nt)\neq 0$."
        ),
        eq(r"\sin(a+b)\sin(nt)=0"),
        p(
            r"Since $a>0$, $b>0$ and $a+b<\pi$, we have $\sin(a+b)\neq 0$. "
            r"Thus $\sin(nt)=0$, so $nt=k\pi$ for $k\in\mathbb{Z}$."
        ),
        eq(r"t=\dfrac{k\pi}{n},\quad k\in\mathbb{Z}"),
        p(
            r"Exclude values where $\sin(b-nt)=0$, i.e. where "
            r"$b-\dfrac{k\pi}{n}=m\pi$ for some integer $m$. "
            r"(In particular $t=0$ is always a solution.)"
        ),
        '<h2 class="question">Exercise 3 — Question 2</h2>',
        question_box(
            p(
                r"(a) If $y=Ae^{\lambda x}\sin x+Be^{\lambda x}\cos x$, show that "
                r"$y''-2\lambda y'+(\lambda^2+1)y=0$."
            ),
            p(
                r"(b) A function satisfies $y''-2\lambda y'+(\lambda^2+1)y=0$, and "
                r"$y(0)=y'(0)=1$. Evaluate $A$ and $B$ and hence find the equation of "
                r"the function."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"Write $y=e^{\lambda x}u$ where $u=A\sin x+B\cos x$, so $u'=A\cos x-B\sin x$ and $u''=-u$."),
        eq(r"y'=e^{\lambda x}(\lambda u+u')"),
        eq(r"y''=e^{\lambda x}\bigl(\lambda^2 u+2\lambda u'+u''\bigr)=e^{\lambda x}(\lambda^2 u+2\lambda u'-u)"),
        eq(
            r"y''-2\lambda y'+(\lambda^2+1)y"
            r"=e^{\lambda x}\bigl[(\lambda^2 u+2\lambda u'-u)-2\lambda(\lambda u+u')+(\lambda^2+1)u\bigr]"
            r"=e^{\lambda x}\cdot 0=0"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"From (a), $y=e^{\lambda x}(A\sin x+B\cos x)$."),
        eq(r"y(0)=B=1"),
        eq(
            r"y'(0)=\lambda B+A=1"
            r"\quad\Rightarrow\quad "
            r"A+\lambda=1"
            r"\quad\Rightarrow\quad "
            r"A=1-\lambda"
        ),
        eq(r"y=e^{\lambda x}\bigl[(1-\lambda)\sin x+\cos x\bigr]"),
        p(
            r"<strong>Answer:</strong> $A=1-\lambda$, $B=1$, and "
            r"$y=e^{\lambda x}\bigl[(1-\lambda)\sin x+\cos x\bigr]$."
        ),
    ]
