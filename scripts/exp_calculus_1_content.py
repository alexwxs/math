"""Calculus of Exponential Function (I) — from worksheet PDF 20261105195050."""

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


def exp_calculus_1_blocks() -> list[str]:
    sketch_q1 = "/year12/media/exp1_ex3_q1.png"
    sketch_q2 = "/year12/media/exp1_ex3_q2_sketch.png"
    return [
        '<h1 class="section">Calculus of Exponential Function (I)</h1>',
        p(
            r"<em>Source: Year 12 (A1) Mathematics Extension 1 — Optional Challenging Questions "
            r"(Level 3).</em>"
        ),
        # ---------- Exercise 1 ----------
        '<h2 class="question">Exercise 1 — Question 1</h2>',
        question_box(
            p(
                r"Differentiate $y=x^x$, either by expressing it as a power of $e$, "
                r"or by taking logarithms of both sides."
            )
        ),
        '<h3 class="solution">Solution</h3>',
        p(r"<strong>Method 1 — as a power of $e$.</strong> Write $x^x=e^{x\ln x}$ for $x>0$."),
        eq(r"\dfrac{dy}{dx}=e^{x\ln x}\cdot\dfrac{d}{dx}(x\ln x)=x^x\bigl(\ln x+1\bigr)"),
        p(r"<strong>Method 2 — logarithmic differentiation.</strong> Take $\ln$ of both sides:"),
        eq(r"\ln y=x\ln x"),
        p(r"Differentiate:"),
        eq(
            r"\dfrac{1}{y}\dfrac{dy}{dx}=\ln x+1"
            r"\quad\Rightarrow\quad"
            r"\dfrac{dy}{dx}=y(\ln x+1)=x^x(\ln x+1)"
        ),
        p(r"<strong>Answer:</strong> $\dfrac{dy}{dx}=x^x(\ln x+1)$ for $x>0$."),
        '<h2 class="question">Exercise 1 — Question 2</h2>',
        question_box(
            p(
                r"(a) Prove that the derivative of $f(x)=2^x$ is "
                r"$f'(x)=(\ln 2)\,2^x$."
            ),
            p(
                r"(b) From first principles, prove that the derivative of $f(x)=2^x$ is "
                r"$f'(x)=c\cdot 2^x$ where "
                r"$c=\displaystyle\lim_{h\to 0}\dfrac{2^h-1}{h}$."
            ),
            p(r"(c) Hence, estimate the value of $\ln 2$, correct to 3 decimal places."),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"Write $2^x=e^{x\ln 2}$. Then"),
        eq(r"f'(x)=e^{x\ln 2}\cdot\ln 2=(\ln 2)\,2^x"),
        '<h3 class="solution">Solution (b)</h3>',
        eq(
            r"f'(x)=\lim_{h\to 0}\dfrac{2^{x+h}-2^x}{h}"
            r"=2^x\lim_{h\to 0}\dfrac{2^h-1}{h}"
            r"=c\cdot 2^x"
        ),
        p(r"where $c=\displaystyle\lim_{h\to 0}\dfrac{2^h-1}{h}$."),
        '<h3 class="solution">Solution (c)</h3>',
        p(r"Comparing (a) and (b), $c=\ln 2$. Estimate the limit with a small $h$, e.g. $h=0.001$:"),
        eq(r"\ln 2\approx\dfrac{2^{0.001}-1}{0.001}\approx 0.693"),
        p(r"<strong>Answer:</strong> $\ln 2\approx 0.693$ (3 d.p.)."),
        # ---------- Exercise 2 ----------
        '<h2 class="question">Exercise 2 — Question 2</h2>',
        question_box(
            p(
                r"Consider the function $f(x)=e^{x/(1+kx)}$ where $k$ is a positive constant."
            ),
            p(r"(a) Find $f'(x)$ and $f''(x)$."),
            p(
                r"(b) Show that $f(x)$ has a point of inflexion at "
                r"$\left(\dfrac{1}{2k^2}-\dfrac{1}{k},\,e^{1/k-2}\right)$."
            ),
            p(
                r"(c) Show that the tangent to $y=f(x)$ at $x=a$ passes through the origin "
                r"if and only if $k^2 a^2+(2k-1)a+1=0$."
            ),
            p(
                r"(d) Hence, show that no tangents to $y=f(x)$ pass through the origin "
                r"if and only if $k>\dfrac{1}{4}$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"Let $u=\dfrac{x}{1+kx}$. Then $f=e^u$ and"),
        eq(r"u'=\dfrac{(1+kx)-x\cdot k}{(1+kx)^2}=\dfrac{1}{(1+kx)^2}"),
        eq(r"f'(x)=e^u\cdot u'=\dfrac{e^{x/(1+kx)}}{(1+kx)^2}"),
        p(r"Differentiate again (product / quotient):"),
        eq(
            r"f''(x)=e^u\cdot u'\cdot(1+kx)^{-2}+e^u\cdot(-2)(1+kx)^{-3}\cdot k"
        ),
        eq(
            r"=e^u(1+kx)^{-3}\left(\dfrac{1}{1+kx}-2k\right)"
            r"=e^{x/(1+kx)}\,(1+kx)^{-4}\bigl(1-2k-2k^2 x\bigr)"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"Set $f''(x)=0$. Since the exponential and $(1+kx)^{-4}$ never vanish,"),
        eq(r"1-2k-2k^2 x=0\quad\Rightarrow\quad x=\dfrac{1-2k}{2k^2}=\dfrac{1}{2k^2}-\dfrac{1}{k}"),
        p(r"At this $x$-value,"),
        eq(
            r"1+kx=1+k\left(\dfrac{1}{2k^2}-\dfrac{1}{k}\right)=\dfrac{1}{2k},"
            r"\quad "
            r"u=\dfrac{x}{1+kx}=\dfrac{1}{k}-2"
        ),
        eq(r"f(x)=e^{1/k-2}"),
        p(
            r"Moreover $f''$ changes sign at this root (the factor $1-2k-2k^2 x$ is linear "
            r"with negative slope), so it is a point of inflexion."
        ),
        '<h3 class="solution">Solution (c)</h3>',
        p(r"The tangent at $x=a$ is $y-f(a)=f'(a)(x-a)$. It passes through $(0,0)$ iff"),
        eq(r"-f(a)=-a f'(a)\quad\Leftrightarrow\quad f(a)=a f'(a)"),
        p(r"Using $f'(a)=\dfrac{f(a)}{(1+ka)^2}$ and $f(a)\neq 0$,"),
        eq(
            r"1=\dfrac{a}{(1+ka)^2}"
            r"\quad\Leftrightarrow\quad "
            r"(1+ka)^2=a"
            r"\quad\Leftrightarrow\quad "
            r"k^2 a^2+(2k-1)a+1=0"
        ),
        '<h3 class="solution">Solution (d)</h3>',
        p(r"The quadratic in $a$ has discriminant"),
        eq(r"\Delta=(2k-1)^2-4k^2\cdot 1=4k^2-4k+1-4k^2=1-4k"),
        p(
            r"There is no real $a$ iff $\Delta<0$ iff $1-4k<0$ iff $k>\dfrac{1}{4}$. "
            r"Hence no tangent through the origin iff $k>\dfrac{1}{4}$."
        ),
        # ---------- Exercise 3 ----------
        '<h2 class="question">Exercise 3 — Question 1</h2>',
        question_box(
            p(r"The graph of $f(x)=x^n e^{-x}$ is shown for $x>0$."),
            figure(sketch_q1, "Graph of f(x)=x^n e^{-x} for x>0"),
            p(r"(a) Show that the maximum turning point occurs at $x=n$."),
            p(
                r"(b) By considering the relationship between the values of "
                r"$f(n)$, $f(n-1)$ and $f(n+1)$, prove that "
                r"$\left(1+\dfrac{1}{n}\right)^n < e < \left(1-\dfrac{1}{n}\right)^{-n}$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"For $x>0$, take logarithms or use the product rule:"),
        eq(
            r"f'(x)=n x^{n-1}e^{-x}-x^n e^{-x}=x^{n-1}e^{-x}(n-x)"
        ),
        p(
            r"So $f'(x)=0$ at $x=n$ (for $x>0$). Sign of $f'$: positive on $(0,n)$ and "
            r"negative on $(n,\infty)$, hence a maximum at $x=n$."
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"Since the maximum is at $x=n$, we have $f(n)>f(n+1)$ and $f(n)>f(n-1)$ (for $n>1$)."),
        p(r"From $f(n)>f(n+1)$:"),
        eq(
            r"n^n e^{-n}>(n+1)^n e^{-(n+1)}"
            r"\quad\Rightarrow\quad "
            r"e>\left(\dfrac{n+1}{n}\right)^n"
            r"=\left(1+\dfrac{1}{n}\right)^n"
        ),
        p(r"From $f(n)>f(n-1)$:"),
        eq(
            r"n^n e^{-n}>(n-1)^n e^{-(n-1)}"
            r"\quad\Rightarrow\quad "
            r"e<\left(\dfrac{n}{n-1}\right)^n"
            r"=\left(1-\dfrac{1}{n}\right)^{-n}"
        ),
        eq(r"\left(1+\dfrac{1}{n}\right)^n < e < \left(1-\dfrac{1}{n}\right)^{-n}"),
        '<h2 class="question">Exercise 3 — Question 2</h2>',
        question_box(
            p(r"The function $g$ is even, and"),
            eq(r"g(x)=4e^{-x}-6e^{-2x}\quad(x\ge 0)"),
            p(r"(with $g(x)=g(-x)$ for $x<0$)."),
            p(
                r"(a) Show that the graph of $y=g(x)$ has a maximum turning point at "
                r"$\left(\ln 3,\,\dfrac{2}{3}\right)$."
            ),
            p(
                r"(b) Sketch the curve $y=g(x)$, labelling the turning points, inflexion points, "
                r"asymptotes and points of intersection with the axes."
            ),
            p(r"(c) Discuss the behaviour of the curve $y=g(x)$ at $x=0$."),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"For $x>0$,"),
        eq(r"g'(x)=-4e^{-x}+12e^{-2x}=4e^{-2x}\bigl(3-e^{x}\bigr)"),
        p(r"So $g'(x)=0$ when $e^{x}=3$, i.e. $x=\ln 3$."),
        eq(
            r"g(\ln 3)=4e^{-\ln 3}-6e^{-2\ln 3}"
            r"=\dfrac{4}{3}-\dfrac{6}{9}"
            r"=\dfrac{4}{3}-\dfrac{2}{3}"
            r"=\dfrac{2}{3}"
        ),
        p(
            r"$g'$ changes from positive to negative at $x=\ln 3$, so this is a maximum. "
            r"(By evenness there is also a maximum at $\bigl(-\ln 3,\tfrac{2}{3}\bigr)$.)"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        figure(sketch_q2, "Sketch of y=g(x)"),
        p(r"<strong>Intercepts:</strong> $g(0)=4-6=-2$. For $x$-intercepts on $x\ge 0$, "
          r"set $4e^{-x}-6e^{-2x}=0$. With $u=e^{-x}>0$, $4u-6u^2=0\Rightarrow u=\dfrac{2}{3}$, "
          r"so $x=\ln\dfrac{3}{2}$. By evenness the curve also meets the $x$-axis at "
          r"$-\ln\dfrac{3}{2}$."),
        p(r"<strong>Turning points:</strong> "
          r"$\bigl(\pm\ln 3,\,\tfrac{2}{3}\bigr)$ (maxima)."),
        p(r"<strong>Inflexion points:</strong> for $x>0$, "
          r"$g''(x)=4e^{-x}-24e^{-2x}=0\Rightarrow e^{x}=6\Rightarrow x=\ln 6$, "
          r"and $g(\ln 6)=\dfrac{4}{6}-\dfrac{6}{36}=\dfrac{1}{2}$. "
          r"By evenness: $\bigl(\pm\ln 6,\,\tfrac{1}{2}\bigr)$."),
        p(r"<strong>Asymptote:</strong> $y\to 0$ as $x\to\pm\infty$ (horizontal asymptote $y=0$)."),
        '<h3 class="solution">Solution (c)</h3>',
        p(
            r"As $x\to 0^+$, $g'(x)\to -4+12=8$; as $x\to 0^-$, $g'(x)\to -8$ "
            r"(derivative of an even function is odd). "
            r"Thus $g$ is continuous at $x=0$ with $g(0)=-2$, but not differentiable there: "
            r"the graph has a sharp corner (a cusp-like kink) pointing downwards."
        ),
    ]
