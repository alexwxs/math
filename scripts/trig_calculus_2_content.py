"""Calculus of Trigonometric Functions (II) — from worksheet PDF 20261117214004."""

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


def trig_calculus_2_blocks() -> list[str]:
    fig_ln = "/year12/media/trig2_ex2_q1.png"
    fig_sinc = "/year12/media/trig2_ex3_q1.png"
    fig_quad = "/year12/media/trig2_ex3_q2.png"
    return [
        '<h1 class="section">Calculus of Trigonometric Functions (II)</h1>',
        p(
            r"<em>Source: Year 12 (A1) Mathematics Extension 1 — Optional Challenging Questions "
            r"(Level 3).</em>"
        ),
        # ---------- Exercise 1 ----------
        '<h2 class="question">Exercise 1 — Question 1</h2>',
        question_box(
            p(
                r"The curves $y=\cos x$ and $y=\tan x$ intersect at a point $P$ whose "
                r"$x$-coordinate is $\alpha$."
            ),
            p(r"(a) Show that the curves intersect at right angles at $P$."),
            p(r"(b) Show that $\sec^2\alpha=\dfrac{1+\sqrt{5}}{2}$."),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"At $P$, $\cos\alpha=\tan\alpha$, so $\cos^2\alpha=\sin\alpha$ (and $\cos\alpha\neq 0$)."),
        eq(r"\dfrac{d}{dx}(\cos x)=-\sin x,\qquad \dfrac{d}{dx}(\tan x)=\sec^2 x"),
        p(r"The product of the gradients at $x=\alpha$ is"),
        eq(
            r"(-\sin\alpha)\sec^2\alpha"
            r"=-\dfrac{\sin\alpha}{\cos^2\alpha}"
            r"=-1"
        ),
        p(
            r"using $\sin\alpha=\cos^2\alpha$. Hence the tangents are perpendicular, so the "
            r"curves intersect at right angles at $P$."
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"From $\sin\alpha=\cos^2\alpha$ and $\sin^2\alpha+\cos^2\alpha=1$,"),
        eq(r"\cos^4\alpha+\cos^2\alpha-1=0"),
        p(r"Put $u=\cos^2\alpha=\dfrac{1}{\sec^2\alpha}$. Then $u^2+u-1=0$, so"),
        eq(
            r"u=\dfrac{-1+\sqrt{5}}{2}"
            r"\quad\Rightarrow\quad "
            r"\sec^2\alpha=\dfrac{1}{u}=\dfrac{2}{\sqrt{5}-1}=\dfrac{1+\sqrt{5}}{2}"
        ),
        # ---------- Exercise 1 Q2 ----------
        '<h2 class="question">Exercise 1 — Question 2</h2>',
        question_box(
            p(
                r"A curve is defined by $x=\cos^3\theta$ and $y=\sin^3\theta$ for "
                r"$0<\theta<\dfrac{\pi}{4}$."
            ),
            p(
                r"(a) Show that the equation of the normal at "
                r"$P(\cos^3\theta,\sin^3\theta)$ is "
                r"$x\cos\theta-y\sin\theta=\cos 2\theta$."
            ),
            p(
                r"(b) The normal at $P$ cuts the $x$-axis at $A$ and the $y$-axis at $B$. "
                r"Show that $AB=2\cot 2\theta$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        eq(
            r"\dfrac{dx}{d\theta}=-3\cos^2\theta\sin\theta,"
            r"\quad "
            r"\dfrac{dy}{d\theta}=3\sin^2\theta\cos\theta"
        ),
        eq(
            r"\dfrac{dy}{dx}"
            r"=\dfrac{3\sin^2\theta\cos\theta}{-3\cos^2\theta\sin\theta}"
            r"=-\tan\theta"
        ),
        p(r"So the gradient of the normal is $\cot\theta$."),
        eq(
            r"y-\sin^3\theta=\cot\theta\bigl(x-\cos^3\theta\bigr)"
        ),
        p(r"Multiply through by $\sin\theta$:"),
        eq(
            r"y\sin\theta-\sin^4\theta=x\cos\theta-\cos^4\theta"
        ),
        eq(
            r"x\cos\theta-y\sin\theta=\cos^4\theta-\sin^4\theta=\cos 2\theta"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"At $A$ ($y=0$): $x=\dfrac{\cos 2\theta}{\cos\theta}$."),
        p(r"At $B$ ($x=0$): $y=-\dfrac{\cos 2\theta}{\sin\theta}$."),
        eq(
            r"AB^2"
            r"=\left(\dfrac{\cos 2\theta}{\cos\theta}\right)^2"
            r"+\left(\dfrac{\cos 2\theta}{\sin\theta}\right)^2"
            r"=\cos^2 2\theta\cdot\dfrac{1}{\sin^2\theta\cos^2\theta}"
        ),
        eq(
            r"AB"
            r"=\dfrac{\cos 2\theta}{\sin\theta\cos\theta}"
            r"=\dfrac{2\cos 2\theta}{\sin 2\theta}"
            r"=2\cot 2\theta"
        ),
        # ---------- Exercise 2 ----------
        '<h2 class="question">Exercise 2 — Question 1</h2>',
        question_box(
            p(
                r"Consider $f(x)=\ln(1+\cos x)$ for $-2\pi\le x\le 2\pi$ where "
                r"$x\neq\pm\pi$."
            ),
            p(
                r"(a) Show that the function is even and is concave down for all values of "
                r"$x$ in its domain."
            ),
            p(r"(b) Sketch a graph of the curve $y=f(x)$."),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        eq(r"f(-x)=\ln\bigl(1+\cos(-x)\bigr)=\ln(1+\cos x)=f(x)"),
        p(r"so $f$ is even. Differentiating,"),
        eq(r"f'(x)=-\dfrac{\sin x}{1+\cos x}"),
        eq(
            r"f''(x)"
            r"=\dfrac{-\cos x(1+\cos x)-\sin x\cdot\sin x}{(1+\cos x)^2}"
            r"=\dfrac{-\cos x-\cos^2 x-\sin^2 x}{(1+\cos x)^2}"
            r"=\dfrac{-(1+\cos x)}{(1+\cos x)^2}"
            r"=-\dfrac{1}{1+\cos x}"
        ),
        p(
            r"For $x\neq\pm\pi$ in the given interval, $\cos x\neq -1$, so $1+\cos x>0$ and "
            r"$f''(x)<0$. Hence $f$ is concave down on its domain."
        ),
        '<h3 class="solution">Solution (b)</h3>',
        figure(fig_ln, "Graph of y=ln(1+cos x)"),
        p(
            r"Vertical asymptotes at $x=\pm\pi$; local maxima at $x=0,\pm 2\pi$ with "
            r"$f=\ln 2$; even symmetry about the $y$-axis."
        ),
        # ---------- Exercise 3 ----------
        '<h2 class="question">Exercise 3 — Question 1</h2>',
        question_box(
            p(r"(a) Show that the line $y=x$ is tangent to the curve $y=\tan x$ at $(0,0)$."),
            p(r"(b) Show that $\tan x>x$ for $0<x<\dfrac{\pi}{2}$."),
            p(
                r"(c) Let $f(x)=\dfrac{\sin x}{x}$ for $0<x<\dfrac{\pi}{2}$. Find $f'(x)$ and "
                r"show that $f'(x)<0$ in the given domain."
            ),
            p(
                r"(d) Sketch $y=f(x)$ over the given domain and explain why "
                r"$\sin x>\dfrac{2x}{\pi}$ for $0<x<\dfrac{\pi}{2}$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"Both curves pass through $(0,0)$. Also"),
        eq(r"\left.\dfrac{d}{dx}(\tan x)\right|_{x=0}=\sec^2 0=1"),
        p(r"which equals the gradient of $y=x$. Hence $y=x$ is the tangent at $(0,0)$."),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"Let $g(x)=\tan x-x$. Then $g(0)=0$ and"),
        eq(r"g'(x)=\sec^2 x-1=\tan^2 x>0\quad\text{for }0<x<\tfrac{\pi}{2}"),
        p(r"so $g(x)>g(0)=0$, i.e. $\tan x>x$."),
        '<h3 class="solution">Solution (c)</h3>',
        eq(
            r"f'(x)=\dfrac{x\cos x-\sin x}{x^2}"
        ),
        p(r"Let $h(x)=x\cos x-\sin x$. Then $h(0)=0$ and $h'(x)=-x\sin x<0$ for $0<x<\tfrac{\pi}{2}$."),
        p(r"Thus $h(x)<0$, so $f'(x)<0$ on the domain."),
        p(r"(Equivalently: $x\cos x-\sin x<0\Leftrightarrow\tan x>x$, by part (b).)"),
        '<h3 class="solution">Solution (d)</h3>',
        figure(fig_sinc, "Graph of y=(sin x)/x on (0, π/2)"),
        p(
            r"As $x\to 0^+$, $f(x)\to 1$; at $x=\dfrac{\pi}{2}$, "
            r"$f=\dfrac{2}{\pi}$. Since $f$ is continuous and strictly decreasing on "
            r"$\bigl(0,\tfrac{\pi}{2}\bigr)$,"
        ),
        eq(
            r"\dfrac{\sin x}{x}>\dfrac{2}{\pi}"
            r"\quad\Rightarrow\quad "
            r"\sin x>\dfrac{2x}{\pi}"
        ),
        '<h2 class="question">Exercise 3 — Question 2</h2>',
        question_box(
            p(
                r"The sides of quadrilateral $PQRS$ have fixed lengths $a$, $b$, $c$ and $d$, "
                r"as shown. Angles $\angle PQR=\alpha$ and $\angle PSR=\beta$ (radians), "
                r"with $0<\alpha<\pi$ and $0<\beta<\pi$."
            ),
            figure(fig_quad, "Quadrilateral PQRS with angles alpha and beta"),
            p(
                r"(a) Use the cosine rule to find two expressions for $(PR)^2$ and hence, "
                r"by differentiating both with respect to $\alpha$, show that "
                r"$\dfrac{d\beta}{d\alpha}=\dfrac{ab\sin\alpha}{cd\sin\beta}$."
            ),
            p(
                r"(b) Find an expression for the area of $PQRS$ in terms of $\sin\alpha$ and "
                r"$\sin\beta$, and hence prove that the area is a maximum when "
                r"$\alpha+\beta=\pi$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        eq(
            r"PR^2=a^2+b^2-2ab\cos\alpha=c^2+d^2-2cd\cos\beta"
        ),
        p(r"Differentiate both expressions with respect to $\alpha$:"),
        eq(
            r"2ab\sin\alpha=2cd\sin\beta\cdot\dfrac{d\beta}{d\alpha}"
            r"\quad\Rightarrow\quad "
            r"\dfrac{d\beta}{d\alpha}=\dfrac{ab\sin\alpha}{cd\sin\beta}"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        eq(
            r"A=\dfrac{1}{2}ab\sin\alpha+\dfrac{1}{2}cd\sin\beta"
        ),
        p(r"Differentiate with respect to $\alpha$:"),
        eq(
            r"\dfrac{dA}{d\alpha}"
            r"=\dfrac{1}{2}ab\cos\alpha+\dfrac{1}{2}cd\cos\beta\cdot\dfrac{d\beta}{d\alpha}"
        ),
        p(r"Set $\dfrac{dA}{d\alpha}=0$ and substitute part (a):"),
        eq(
            r"ab\cos\alpha+cd\cos\beta\cdot\dfrac{ab\sin\alpha}{cd\sin\beta}=0"
        ),
        eq(
            r"\cos\alpha\sin\beta+\sin\alpha\cos\beta=0"
            r"\quad\Rightarrow\quad "
            r"\sin(\alpha+\beta)=0"
        ),
        p(
            r"Since $0<\alpha,\beta<\pi$, we have $0<\alpha+\beta<2\pi$, so "
            r"$\alpha+\beta=\pi$. The second-derivative / endpoint check confirms this "
            r"critical point gives the maximum area (cyclic quadrilateral)."
        ),
    ]
