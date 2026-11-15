"""Calculus of Exponential Function (II) — from worksheet PDF 20261107203845."""

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


def exp_calculus_2_blocks() -> list[str]:
    sketch = "/year12/media/exp2_ex3_q1.png"
    return [
        '<h1 class="section">Calculus of Exponential Function (II)</h1>',
        p(
            r"<em>Source: Year 12 (A1) Mathematics Extension 1 — Optional Challenging Questions "
            r"(Level 3).</em>"
        ),
        # ---------- Exercise 1 ----------
        '<h2 class="question">Exercise 1 — Question 1</h2>',
        question_box(
            p(
                r"Show that "
                r"$\displaystyle\int\dfrac{e^x+1}{e^{x/2}+e^{-x/2}}\,dx=2e^{x/2}+C$."
            )
        ),
        '<h3 class="solution">Solution</h3>',
        p(r"Multiply numerator and denominator by $e^{x/2}$:"),
        eq(
            r"\dfrac{e^x+1}{e^{x/2}+e^{-x/2}}"
            r"=\dfrac{(e^x+1)\,e^{x/2}}{(e^{x/2}+e^{-x/2})\,e^{x/2}}"
            r"=\dfrac{(e^x+1)\,e^{x/2}}{e^x+1}"
            r"=e^{x/2}"
        ),
        eq(r"\int e^{x/2}\,dx=2e^{x/2}+C"),
        '<h2 class="question">Exercise 1 — Question 2</h2>',
        question_box(
            p(
                r"If $y=\dfrac{1}{2}\bigl(e^{ax}-e^{-ax}\bigr)$ where $a$ is a positive constant,"
            ),
            p(
                r"(a) Show that $x=\dfrac{1}{a}\ln\bigl(y+\sqrt{1+y^2}\bigr)$."
            ),
            p(r"(b) Show that $\left(\dfrac{dy}{dx}\right)^2-a^2 y^2=a^2$."),
            p(
                r"(c) Hence deduce that "
                r"$\displaystyle\int\dfrac{dy}{\sqrt{1+y^2}}"
                r"=\ln\bigl(y+\sqrt{1+y^2}\bigr)+C$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        eq(r"2y=e^{ax}-e^{-ax}"),
        p(r"Multiply by $e^{ax}$:"),
        eq(r"2y\,e^{ax}=e^{2ax}-1\quad\Rightarrow\quad e^{2ax}-2y\,e^{ax}-1=0"),
        p(r"Quadratic in $e^{ax}$ (take the positive root):"),
        eq(
            r"e^{ax}=y+\sqrt{y^2+1}"
            r"\quad\Rightarrow\quad "
            r"x=\dfrac{1}{a}\ln\bigl(y+\sqrt{1+y^2}\bigr)"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        eq(
            r"\dfrac{dy}{dx}=\dfrac{a}{2}\bigl(e^{ax}+e^{-ax}\bigr)"
        ),
        eq(
            r"\left(\dfrac{dy}{dx}\right)^2-a^2 y^2"
            r"=\dfrac{a^2}{4}\bigl(e^{ax}+e^{-ax}\bigr)^2"
            r"-a^2\cdot\dfrac{1}{4}\bigl(e^{ax}-e^{-ax}\bigr)^2"
        ),
        eq(
            r"=\dfrac{a^2}{4}\Bigl["
            r"(e^{2ax}+2+e^{-2ax})-(e^{2ax}-2+e^{-2ax})"
            r"\Bigr]"
            r"=\dfrac{a^2}{4}\cdot 4=a^2"
        ),
        '<h3 class="solution">Solution (c)</h3>',
        p(r"From (b), $\dfrac{dy}{dx}=a\sqrt{1+y^2}$ (since $\dfrac{dy}{dx}>0$)."),
        eq(
            r"\dfrac{dx}{dy}=\dfrac{1}{a\sqrt{1+y^2}}"
            r"\quad\Rightarrow\quad"
            r"\int\dfrac{dy}{\sqrt{1+y^2}}=a\int dx=ax+C'"
        ),
        p(r"Using (a), $ax=\ln\bigl(y+\sqrt{1+y^2}\bigr)$, so"),
        eq(r"\int\dfrac{dy}{\sqrt{1+y^2}}=\ln\bigl(y+\sqrt{1+y^2}\bigr)+C"),
        # ---------- Exercise 2 ----------
        '<h2 class="question">Exercise 2 — Question 1</h2>',
        question_box(
            p(r"(a) (i) Differentiate $y=x^2 e^{-x^2}$."),
            p(
                r"(ii) Hence show that "
                r"$\displaystyle\int x^3 e^{-x^2}\,dx"
                r"=-\dfrac{e^{-x^2}}{2}(x^2+1)+C$, "
                r"and calculate $\displaystyle\int_1^2 x^3 e^{-x^2}\,dx$."
            ),
            p(
                r"(b) Given that "
                r"$I=\displaystyle\int_{-1}^{1}\dfrac{x^2 e^x}{e^x+1}\,dx$ and "
                r"$J=\displaystyle\int_{-1}^{1}\dfrac{x^2}{e^x+1}\,dx$:"
            ),
            p(r"(i) Use the substitution $u=-x$ to show that $I=J$."),
            p(r"(ii) Hence evaluate $I$ and $J$."),
        ),
        '<h3 class="solution">Solution (a)(i)</h3>',
        eq(
            r"\dfrac{dy}{dx}=2x e^{-x^2}+x^2 e^{-x^2}(-2x)"
            r"=2x e^{-x^2}(1-x^2)"
        ),
        '<h3 class="solution">Solution (a)(ii)</h3>',
        p(r"From (i), $\dfrac{dy}{dx}=2x e^{-x^2}-2x^3 e^{-x^2}$, so"),
        eq(
            r"x^3 e^{-x^2}=x e^{-x^2}-\dfrac{1}{2}\dfrac{dy}{dx}"
        ),
        eq(
            r"\int x^3 e^{-x^2}\,dx"
            r"=\int x e^{-x^2}\,dx-\dfrac{1}{2}y+C"
            r"=-\dfrac{1}{2}e^{-x^2}-\dfrac{1}{2}x^2 e^{-x^2}+C"
            r"=-\dfrac{e^{-x^2}}{2}(x^2+1)+C"
        ),
        eq(
            r"\int_1^2 x^3 e^{-x^2}\,dx"
            r"=\left[-\dfrac{e^{-x^2}}{2}(x^2+1)\right]_1^2"
            r"=-\dfrac{5}{2}e^{-4}+\dfrac{2}{2}e^{-1}"
            r"=e^{-1}-\dfrac{5}{2}e^{-4}"
        ),
        p(r"<strong>Answer:</strong> $e^{-1}-\dfrac{5}{2}e^{-4}$."),
        '<h3 class="solution">Solution (b)(i)</h3>',
        p(r"Put $u=-x$ in $I$. Then $dx=-du$; when $x=-1$, $u=1$; when $x=1$, $u=-1$."),
        eq(
            r"I=\int_{1}^{-1}\dfrac{(-u)^2 e^{-u}}{e^{-u}+1}(-du)"
            r"=\int_{-1}^{1}\dfrac{u^2 e^{-u}}{e^{-u}+1}\,du"
        ),
        p(r"Multiply numerator and denominator by $e^{u}$:"),
        eq(
            r"I=\int_{-1}^{1}\dfrac{u^2}{1+e^{u}}\,du=J"
        ),
        '<h3 class="solution">Solution (b)(ii)</h3>',
        p(r"Add the two integrals:"),
        eq(
            r"I+J=\int_{-1}^{1}\dfrac{x^2 e^x+x^2}{e^x+1}\,dx"
            r"=\int_{-1}^{1}x^2\,dx"
            r"=\left[\dfrac{x^3}{3}\right]_{-1}^{1}"
            r"=\dfrac{2}{3}"
        ),
        p(r"Since $I=J$, we have $I=J=\dfrac{1}{3}$."),
        p(r"<strong>Answer:</strong> $I=J=\dfrac{1}{3}$."),
        '<h2 class="question">Exercise 2 — Question 2</h2>',
        question_box(
            p(
                r"(a) (i) Evaluate "
                r"$\displaystyle\int_{\delta}^{1}\dfrac{e^{\sqrt{x}}}{\sqrt{x}}\,dx$."
            ),
            p(r"(ii) What happens to the integral as $\delta\to 0^+$?"),
            p(
                r"(b) (i) Differentiate $xe^{-x}$ and hence find "
                r"$\displaystyle\int_0^{N} xe^{-x}\,dx$."
            ),
            p(r"(ii) Determine the limit of the integral as $N\to\infty$."),
            p(
                r"(iii) Differentiate $x^2 e^{-x}$, and hence find "
                r"$\displaystyle\int_0^{\infty} x^2 e^{-x}\,dx$."
            ),
        ),
        '<h3 class="solution">Solution (a)(i)</h3>',
        p(r"Put $u=\sqrt{x}$, so $x=u^2$ and $dx=2u\,du$."),
        p(r"When $x=\delta$, $u=\sqrt{\delta}$; when $x=1$, $u=1$."),
        eq(
            r"\int_{\delta}^{1}\dfrac{e^{\sqrt{x}}}{\sqrt{x}}\,dx"
            r"=\int_{\sqrt{\delta}}^{1}\dfrac{e^{u}}{u}\cdot 2u\,du"
            r"=2\int_{\sqrt{\delta}}^{1}e^{u}\,du"
            r"=2\bigl(e-e^{\sqrt{\delta}}\bigr)"
        ),
        '<h3 class="solution">Solution (a)(ii)</h3>',
        p(r"As $\delta\to 0^+$, $e^{\sqrt{\delta}}\to e^{0}=1$, so the integral tends to $2(e-1)$."),
        p(r"(The improper integral $\displaystyle\int_0^{1}\dfrac{e^{\sqrt{x}}}{\sqrt{x}}\,dx$ converges.)"),
        '<h3 class="solution">Solution (b)(i)</h3>',
        eq(r"\dfrac{d}{dx}\bigl(xe^{-x}\bigr)=e^{-x}-xe^{-x}=e^{-x}(1-x)"),
        p(r"Rearrange: $xe^{-x}=e^{-x}-\dfrac{d}{dx}(xe^{-x})$."),
        eq(
            r"\int xe^{-x}\,dx=-e^{-x}-xe^{-x}+C=-e^{-x}(x+1)+C"
        ),
        eq(
            r"\int_0^{N} xe^{-x}\,dx"
            r"=\bigl[-e^{-x}(x+1)\bigr]_0^{N}"
            r"=-e^{-N}(N+1)-(-1)"
            r"=1-e^{-N}(N+1)"
        ),
        '<h3 class="solution">Solution (b)(ii)</h3>',
        eq(
            r"\lim_{N\to\infty}\int_0^{N} xe^{-x}\,dx"
            r"=1"
            r"\quad\bigl(\text{since }e^{-N}(N+1)\to 0\bigr)"
        ),
        '<h3 class="solution">Solution (b)(iii)</h3>',
        eq(
            r"\dfrac{d}{dx}\bigl(x^2 e^{-x}\bigr)=2x e^{-x}-x^2 e^{-x}=e^{-x}(2x-x^2)"
        ),
        p(r"So $x^2 e^{-x}=2x e^{-x}-\dfrac{d}{dx}(x^2 e^{-x})$."),
        eq(
            r"\int x^2 e^{-x}\,dx"
            r"=2\int xe^{-x}\,dx-x^2 e^{-x}+C"
            r"=-e^{-x}(x^2+2x+2)+C"
        ),
        eq(
            r"\int_0^{\infty} x^2 e^{-x}\,dx"
            r"=\lim_{N\to\infty}\bigl[-e^{-x}(x^2+2x+2)\bigr]_0^{N}"
            r"=0-(-2)=2"
        ),
        p(r"<strong>Answer:</strong> $2$."),
        # ---------- Exercise 3 ----------
        '<h2 class="question">Exercise 3 — Question 1</h2>',
        question_box(
            p(
                r"The sketch shows the curve "
                r"$y=\dfrac{e^{2x}-1}{e^{2x}+1}$ and its asymptotes $y=\pm 1$, "
                r"and the line $x=k$ where $k>0$."
            ),
            figure(sketch, "Curve y=(e^{2x}-1)/(e^{2x}+1) with shaded area A"),
            p(
                r"(a) Using the substitution $u=e^{2x}$, or otherwise, show that the area "
                r"in the first quadrant bounded by the curve and the lines $x=0$, $y=1$ and "
                r"$x=k$ is given by "
                r"$A=\ln 2+2k-\ln(e^{2k}+1)$."
            ),
            p(r"(b) Explain why this area is always less than $\ln 2$."),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        eq(
            r"A=\int_0^{k}\left(1-\dfrac{e^{2x}-1}{e^{2x}+1}\right)\,dx"
            r"=\int_0^{k}\dfrac{2}{e^{2x}+1}\,dx"
        ),
        p(r"Put $u=e^{2x}$, so $du=2e^{2x}\,dx=2u\,dx$ and $dx=\dfrac{du}{2u}$."),
        p(r"When $x=0$, $u=1$; when $x=k$, $u=e^{2k}$."),
        eq(
            r"A=\int_1^{e^{2k}}\dfrac{2}{u+1}\cdot\dfrac{du}{2u}"
            r"=\int_1^{e^{2k}}\dfrac{1}{u(u+1)}\,du"
            r"=\int_1^{e^{2k}}\left(\dfrac{1}{u}-\dfrac{1}{u+1}\right)\,du"
        ),
        eq(
            r"=\bigl[\ln u-\ln(u+1)\bigr]_1^{e^{2k}}"
            r"=\ln\dfrac{e^{2k}}{e^{2k}+1}-\ln\dfrac{1}{2}"
            r"=2k-\ln(e^{2k}+1)+\ln 2"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        eq(
            r"A=\ln 2+2k-\ln(e^{2k}+1)"
            r"=\ln 2-\ln\bigl(1+e^{-2k}\bigr)"
        ),
        p(
            r"For $k>0$, $e^{-2k}>0$, so $\ln(1+e^{-2k})>0$. "
            r"Hence $A<\ln 2$."
        ),
    ]
