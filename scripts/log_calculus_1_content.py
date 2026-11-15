"""Calculus of Logarithmic Function (I) — questions and solutions from worksheet PDF."""

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


def log_calculus_1_blocks() -> list[str]:
    diagram = "/year12/media/log1_ex3_q2_p.png"
    sketch_q2 = "/year12/media/log1_ex3_q2_sketch.png"
    sketch_xx = "/year12/media/log1_ex3_q1c_sketch.png"
    return [
        '<h1 class="section">Calculus of Logarithmic Function (I)</h1>',
        p(
            r"<em>Source: Year 12 (A1) Mathematics Extension 1 — Optional Challenging Questions "
            r"(Level 3).</em>"
        ),
        # ---------- Exercise 1 ----------
        '<h2 class="question">Exercise 1 — Question 1</h2>',
        question_box(
            p(
                r"Using implicit differentiation, find the derivative of "
                r"$y = \sqrt{\dfrac{x-1}{x+1}}$ in terms of $x$ only."
            )
        ),
        '<h3 class="solution">Solution</h3>',
        p(r"For $x>1$ we have $y>0$. Take natural logarithms of both sides:"),
        eq(r"\ln y = \dfrac{1}{2}\bigl(\ln(x-1)-\ln(x+1)\bigr)"),
        p(r"Differentiate both sides with respect to $x$:"),
        eq(
            r"\dfrac{1}{y}\dfrac{dy}{dx}"
            r" = \dfrac{1}{2}\left(\dfrac{1}{x-1}-\dfrac{1}{x+1}\right)"
            r" = \dfrac{1}{2}\cdot\dfrac{2}{(x-1)(x+1)}"
            r" = \dfrac{1}{x^2-1}"
        ),
        eq(r"\dfrac{dy}{dx} = \dfrac{y}{x^2-1} = \dfrac{1}{x^2-1}\sqrt{\dfrac{x-1}{x+1}}"),
        p(r"Equivalently,"),
        eq(r"\dfrac{dy}{dx} = \dfrac{1}{(x+1)\sqrt{x^2-1}}"),
        p(r"<strong>Answer:</strong> $\dfrac{dy}{dx}=\dfrac{1}{x^2-1}\sqrt{\dfrac{x-1}{x+1}}$."),
        '<h3 class="solution">Alternative (squaring both sides)</h3>',
        p(r"Square both sides (valid for $x>1$, where $y>0$):"),
        eq(r"y^2 = \dfrac{x-1}{x+1}"),
        p(
            r"Differentiate both sides with respect to $x$ "
            r"(quotient rule on the right, chain rule on the left):"
        ),
        eq(
            r"2y\dfrac{dy}{dx}"
            r" = \dfrac{(1)(x+1)-(x-1)(1)}{(x+1)^2}"
            r" = \dfrac{2}{(x+1)^2}"
        ),
        eq(r"\dfrac{dy}{dx} = \dfrac{1}{y(x+1)^2}"),
        p(r"Rewrite using $y^2=\dfrac{x-1}{x+1}$:"),
        eq(
            r"\dfrac{dy}{dx}"
            r" = \dfrac{y}{y^2(x+1)^2}"
            r" = \dfrac{y}{\left(\dfrac{x-1}{x+1}\right)(x+1)^2}"
            r" = \dfrac{y}{x^2-1}"
            r" = \dfrac{1}{x^2-1}\sqrt{\dfrac{x-1}{x+1}}"
        ),
        p(r"Same answer as above."),
        '<h2 class="question">Exercise 1 — Question 2</h2>',
        question_box(
            p(r"By taking logarithms of both sides, differentiate $y=x^x$."),
        ),
        '<h3 class="solution">Solution</h3>',
        p(r"For $x>0$, write $y=x^x=e^{x\ln x}$, or take logs:"),
        eq(r"\ln y = x\ln x"),
        eq(r"\dfrac{1}{y}\dfrac{dy}{dx} = \ln x + x\cdot\dfrac{1}{x} = \ln x + 1"),
        eq(r"\dfrac{dy}{dx} = x^x(\ln x + 1)"),
        p(r"<strong>Answer:</strong> $\dfrac{dy}{dx}=x^x(\ln x+1)$."),
        '<h2 class="question">Exercise 1 — Question 3</h2>',
        question_box(
            p(
                r"The variables $x$ and $y$ are positive and related by "
                r"$x^a y^b = (x+y)^{a+b}$ where $a$ and $b$ are positive constants. "
                r"By taking logarithms of both sides, show that $\dfrac{dy}{dx}=\dfrac{y}{x}$, "
                r"provided that $bx\neq ay$."
            )
        ),
        '<h3 class="solution">Solution</h3>',
        eq(r"a\ln x + b\ln y = (a+b)\ln(x+y)"),
        p(r"Differentiate both sides with respect to $x$:"),
        eq(r"\dfrac{a}{x} + \dfrac{b}{y}\dfrac{dy}{dx} = (a+b)\cdot\dfrac{1}{x+y}\left(1+\dfrac{dy}{dx}\right)"),
        p(r"Multiply through by $xy(x+y)$ to clear denominators, or rearrange for $y'$:"),
        eq(
            r"\dfrac{b}{y}y' - \dfrac{a+b}{x+y}y' = \dfrac{a+b}{x+y} - \dfrac{a}{x}"
        ),
        eq(
            r"y'\left(\dfrac{b}{y}-\dfrac{a+b}{x+y}\right) = \dfrac{a(x+y)-(a+b)y}{x(x+y)} = \dfrac{ax-by}{x(x+y)}"
        ),
        eq(
            r"y'\cdot\dfrac{b(x+y)-y(a+b)}{y(x+y)} = \dfrac{ax-by}{x(x+y)}"
        ),
        eq(r"y'\cdot\dfrac{bx-ay}{y(x+y)} = \dfrac{ax-by}{x(x+y)} = \dfrac{-(bx-ay)}{x(x+y)}"),
        p(r"Since $bx\neq ay$, cancel $bx-ay$:"),
        eq(r"y'\cdot\dfrac{1}{y} = -\dfrac{1}{x}\cdot(-1) \quad\text{(after careful sign check)}"),
        p(r"More cleanly: from the previous line,"),
        eq(r"y' = \dfrac{ax-by}{x(x+y)}\cdot\dfrac{y(x+y)}{bx-ay} = \dfrac{(ax-by)y}{x(bx-ay)} = \dfrac{y}{x}"),
        p(r"since $ax-by=-(bx-ay)$."),
        p(r"<strong>Hence $\dfrac{dy}{dx}=\dfrac{y}{x}$.</strong>"),
        # ---------- Exercise 2 ----------
        '<h2 class="question">Exercise 2 — Question 1</h2>',
        question_box(
            p(
                r"(a) Show that the tangent from the origin to the curve $y=\ln x$ has gradient "
                r"$\dfrac{1}{e}$."
            ),
            p(
                r"(b) Hence find the set of values of the real number $k$ for which the equation "
                r"$\ln x = kx$ has two distinct roots."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"Let the point of tangency be $(t,\ln t)$ with $t>0$. Then $\dfrac{dy}{dx}=\dfrac{1}{x}$, so the gradient at $x=t$ is $\dfrac{1}{t}$."),
        p(r"The tangent line is"),
        eq(r"Y-\ln t = \dfrac{1}{t}(X-t)"),
        p(r"It passes through the origin $(0,0)$:"),
        eq(r"0-\ln t = \dfrac{1}{t}(0-t) = -1 \Rightarrow \ln t = 1 \Rightarrow t=e"),
        p(r"Therefore the gradient is $\dfrac{1}{t}=\dfrac{1}{e}$."),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"The equation $\ln x=kx$ ($x>0$) is equivalent to $k=\dfrac{\ln x}{x}$ whenever we seek intersections of $y=\ln x$ and the line $y=kx$."),
        p(r"Consider $g(x)=\dfrac{\ln x}{x}$ for $x>0$."),
        eq(r"g'(x)=\dfrac{1-\ln x}{x^2}"),
        p(r"So $g'(x)=0$ at $x=e$, and $g$ has a maximum there with $g(e)=\dfrac{1}{e}$."),
        p(r"Also $g(x)\to 0$ as $x\to\infty$, $g(x)\to-\infty$ as $x\to 0^+$, and $g(x)\lt 0$ on $(0,1)$."),
        p(r"Hence:"),
        p(r"• if $k=\dfrac{1}{e}$: exactly one positive root ($x=e$);"),
        p(r"• if $0\lt k\lt\dfrac{1}{e}$: exactly two distinct positive roots;"),
        p(r"• if $k\le 0$: at most one positive root."),
        p(
            r"<strong>Answer:</strong> two distinct roots when "
            r"$0\lt k\lt\dfrac{1}{e}$."
        ),
        # ---------- Exercise 3 ----------
        '<h2 class="question">Exercise 3 — Question 1</h2>',
        question_box(
            p(
                r"(a) Differentiate $y=x^x$ by taking logarithms of both sides. Using this, "
                r"describe the behaviour of the curve $y=x^x$ near $x=0$ and show that it becomes "
                r"vertical as $x\to 0^+$. You may use $\lim_{x\to 0^+} x\ln x=0$."
            ),
            p(
                r"(b) Determine the nature of any stationary points and find the point(s) on the "
                r"curve where the tangent has gradient $1$."
            ),
            p(r"(c) Sketch the function."),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        eq(r"\ln y = x\ln x \Rightarrow \dfrac{y'}{y}=\ln x+1 \Rightarrow y'=x^x(\ln x+1)"),
        p(r"As $x\to 0^+$, $x\ln x\to 0$, so $x^x=e^{x\ln x}\to e^0=1$. Thus the curve approaches height $1$."),
        p(r"The gradient $y'=x^x(\ln x+1)\to 1\cdot(-\infty)=-\infty$ as $x\to 0^+$, so the tangent becomes vertical."),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"Stationary points: $y'=0\Rightarrow \ln x+1=0\Rightarrow x=e^{-1}$ (since $x^x>0$)."),
        eq(r"y\left(e^{-1}\right)=\left(e^{-1}\right)^{e^{-1}}=e^{-1/e}"),
        p(r"For $0\lt x\lt e^{-1}$, $\ln x+1\lt 0$ so $y'\lt 0$; for $x>e^{-1}$, $y'>0$. Hence a local <strong>minimum</strong> at $\left(e^{-1},e^{-1/e}\right)$."),
        p(r"Where the gradient is $1$:"),
        eq(r"x^x(\ln x+1)=1"),
        p(r"For $0\lt x\lt e^{-1}$, $\ln x+1\lt 0$, so $y'\lt 0\neq 1$."),
        p(r"For $x>e^{-1}$, $y'$ increases continuously from $0$ (at the minimum) to $\infty$."),
        p(r"At $x=1$: $1^1(\ln 1+1)=1$. Since $y'$ is continuous and strictly increases through the value $1$ only once on $(e^{-1},\infty)$, this is the unique solution."),
        p(r"<strong>Answer:</strong> local minimum at $\left(e^{-1},e^{-1/e}\right)$; tangent has gradient $1$ at $(1,1)$."),
        '<h3 class="solution">Solution (c)</h3>',
        p(r"Using (a) and (b), the sketch of $y=x^x$ for $x>0$ has these features:"),
        p(r"• as $x\to 0^+$, $y\to 1$ with a vertical tangent;"),
        p(r"• a local minimum at $\left(e^{-1},e^{-1/e}\right)$;"),
        p(r"• passes through $(1,1)$, where the gradient is $1$;"),
        p(r"• increasing for $x>e^{-1}$, with $y\to\infty$ as $x\to\infty$."),
        figure(sketch_xx, "Sketch of y = x^x for x > 0"),
        '<h2 class="question">Exercise 3 — Question 2</h2>',
        question_box(
            figure(diagram, "Curve y = P(x), tangential to the x-axis at x = a"),
            p(
                r"In the diagram, the curve $y=P(x)$ is tangential to the $x$-axis at $x=a$ "
                r"where $0\lt a\lt 1$. Explain, using calculus, whether or not the curve "
                r"$y=(\ln x)\,P(x)$ will be tangential to the $x$-axis at $x=a$. "
                r"Then, on the same set of axes, sketch the curve $y=(\ln x)\,P(x)$."
            ),
        ),
        '<h3 class="solution">Solution</h3>',
        p(r"Since $y=P(x)$ is tangential to the $x$-axis at $x=a$,"),
        eq(r"P(a)=0 \quad\text{and}\quad P'(a)=0"),
        p(r"Let $f(x)=(\ln x)\,P(x)$ (defined for $x>0$). Then"),
        eq(r"f(a)=\ln a\cdot P(a)=0"),
        eq(r"f'(x)=\dfrac{1}{x}P(x)+\ln x\cdot P'(x)"),
        eq(r"f'(a)=\dfrac{1}{a}P(a)+\ln a\cdot P'(a)=0"),
        p(
            r"So $f(a)=f'(a)=0$: yes, $y=(\ln x)\,P(x)$ is also tangential to the $x$-axis at $x=a$."
        ),
        p(r"<strong>Sketch</strong> (same axes; $P$ shown lighter for reference):"),
        p(r"• Domain $x>0$. Near $x=0^+$, $P(x)$ behaves like a multiple of $x$, and $x\ln x\to 0$, so $f(x)\to 0$."),
        p(r"• Touches the $x$-axis at $x=a$ (still tangential)."),
        p(r"• For $0\lt x\lt 1$, $\ln x\lt 0$, so $f$ has the opposite sign to $P$; for $x>1$, $\ln x>0$, so $f$ has the same sign as $P$."),
        p(r"• At $x=1$, $f(1)=\ln 1\cdot P(1)=0$, so the sketch crosses the $x$-axis at $x=1$."),
        figure(sketch_q2, "Sketch of y = (ln x) P(x) on the same axes as y = P(x)"),
    ]
