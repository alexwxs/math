"""Calculus of Logarithmic Function (II) — from worksheet PDF 20261023212349."""

from __future__ import annotations


def p(text: str) -> str:
    return f"<p>{text}</p>"


def eq(latex: str) -> str:
    return f'<p class="display-math">$${latex}$$</p>'


def question_box(*parts: str) -> str:
    return f'<aside class="question-box">{"".join(parts)}</aside>'


def log_calculus_2_blocks() -> list[str]:
    return [
        '<h1 class="section">Calculus of Logarithmic Function (II)</h1>',
        p(
            r"<em>Source: Year 12 (A1) Mathematics Extension 1 — Optional Challenging Questions "
            r"(Level 3).</em>"
        ),
        # ---------- Exercise 1 ----------
        '<h2 class="question">Exercise 1 — Question 1</h2>',
        question_box(
            p(
                r"(a) Show that "
                r"$\dfrac{d}{dx}\left[\dfrac{1}{2a}\ln\left|\dfrac{x-a}{x+a}\right|\right]"
                r"=\dfrac{1}{x^2-a^2}$ for $a>0$. "
                r"Hence find $\displaystyle\int\dfrac{1}{x^2-a^2}\,dx$."
            ),
            p(
                r"(b) Hence, by using the substitution $x=u^2$ or otherwise, find "
                r"$\displaystyle\int\dfrac{\sqrt{x}}{x-1}\,dx$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        eq(
            r"\dfrac{1}{2a}\ln\left|\dfrac{x-a}{x+a}\right|"
            r"=\dfrac{1}{2a}\bigl(\ln|x-a|-\ln|x+a|\bigr)"
        ),
        p(r"Differentiate:"),
        eq(
            r"\dfrac{d}{dx}"
            r"=\dfrac{1}{2a}\left(\dfrac{1}{x-a}-\dfrac{1}{x+a}\right)"
            r"=\dfrac{1}{2a}\cdot\dfrac{(x+a)-(x-a)}{(x-a)(x+a)}"
            r"=\dfrac{1}{2a}\cdot\dfrac{2a}{x^2-a^2}"
            r"=\dfrac{1}{x^2-a^2}"
        ),
        p(r"Therefore, integrating both sides,"),
        eq(
            r"\int\dfrac{1}{x^2-a^2}\,dx"
            r"=\dfrac{1}{2a}\ln\left|\dfrac{x-a}{x+a}\right|+C"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"Put $x=u^2$ (so $u=\sqrt{x}$ for $x>0$), giving $dx=2u\,du$."),
        eq(
            r"\int\dfrac{\sqrt{x}}{x-1}\,dx"
            r"=\int\dfrac{u}{u^2-1}\cdot 2u\,du"
            r"=\int\dfrac{2u^2}{u^2-1}\,du"
            r"=\int\left(2+\dfrac{2}{u^2-1}\right)\,du"
        ),
        p(r"Using part (a) with $a=1$:"),
        eq(
            r"\int\dfrac{2}{u^2-1}\,du"
            r"=2\cdot\dfrac{1}{2}\ln\left|\dfrac{u-1}{u+1}\right|"
            r"=\ln\left|\dfrac{u-1}{u+1}\right|"
        ),
        eq(
            r"\int\dfrac{\sqrt{x}}{x-1}\,dx"
            r"=2u+\ln\left|\dfrac{u-1}{u+1}\right|+C"
            r"=2\sqrt{x}+\ln\left|\dfrac{\sqrt{x}-1}{\sqrt{x}+1}\right|+C"
        ),
        p(
            r"<strong>Answer:</strong> "
            r"$2\sqrt{x}+\ln\left|\dfrac{\sqrt{x}-1}{\sqrt{x}+1}\right|+C$."
        ),
        # ---------- Exercise 2 ----------
        '<h2 class="question">Exercise 2 — Question 1</h2>',
        question_box(
            p(
                r"Evaluate "
                r"$\displaystyle\int_{1}^{27}\dfrac{3}{\bigl(x^{1/3}+1\bigr)\,x^{2/3}}\,dx$."
            )
        ),
        '<h3 class="solution">Solution</h3>',
        p(r"Let $u=x^{1/3}$, so $x=u^3$ and $dx=3u^2\,du$."),
        p(r"When $x=1$, $u=1$; when $x=27$, $u=3$."),
        eq(
            r"\int_{1}^{27}\dfrac{3}{(x^{1/3}+1)\,x^{2/3}}\,dx"
            r"=\int_{1}^{3}\dfrac{3}{(u+1)\,u^2}\cdot 3u^2\,du"
            r"=\int_{1}^{3}\dfrac{9}{u+1}\,du"
        ),
        eq(r"=9\ln|u+1|\Big|_{1}^{3}=9\bigl(\ln 4-\ln 2\bigr)=9\ln 2"),
        p(r"<strong>Answer:</strong> $9\ln 2$."),
        '<h2 class="question">Exercise 2 — Question 2</h2>',
        question_box(
            p(
                r"(a) Using the substitution $u=\dfrac{1}{x}$, show that "
                r"$\displaystyle\int_{1/2}^{1}\dfrac{\ln x}{1+x^2}\,dx"
                r"=\int_{2}^{1}\dfrac{\ln u}{1+u^2}\,du$."
            ),
            p(
                r"(b) Deduce the value of "
                r"$\displaystyle\int_{1/2}^{2}\dfrac{\ln x}{1+x^2}\,dx$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(r"Let $u=\dfrac{1}{x}$, so $x=\dfrac{1}{u}$ and $dx=-\dfrac{1}{u^2}\,du$."),
        p(r"When $x=\dfrac{1}{2}$, $u=2$; when $x=1$, $u=1$."),
        eq(
            r"\int_{1/2}^{1}\dfrac{\ln x}{1+x^2}\,dx"
            r"=\int_{2}^{1}\dfrac{\ln(1/u)}{1+1/u^2}\left(-\dfrac{1}{u^2}\right)\,du"
        ),
        eq(
            r"=\int_{2}^{1}\dfrac{-\ln u}{(u^2+1)/u^2}\left(-\dfrac{1}{u^2}\right)\,du"
            r"=\int_{2}^{1}\dfrac{\ln u}{1+u^2}\,du"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"Write"),
        eq(
            r"I=\int_{1/2}^{2}\dfrac{\ln x}{1+x^2}\,dx"
            r"=\int_{1/2}^{1}\dfrac{\ln x}{1+x^2}\,dx"
            r"+\int_{1}^{2}\dfrac{\ln x}{1+x^2}\,dx"
        ),
        p(r"From (a), the first integral equals $\displaystyle\int_{2}^{1}\dfrac{\ln u}{1+u^2}\,du"
        r"=-\int_{1}^{2}\dfrac{\ln x}{1+x^2}\,dx$."),
        eq(r"I=-\int_{1}^{2}\dfrac{\ln x}{1+x^2}\,dx+\int_{1}^{2}\dfrac{\ln x}{1+x^2}\,dx=0"),
        p(r"<strong>Answer:</strong> $0$."),
        # ---------- Exercise 3 ----------
        '<h2 class="question">Exercise 3 — Question 1</h2>',
        question_box(
            p(r"Consider the area under $y=\dfrac{1}{x}$ between $x=n$ and $x=n+1$, where $n>0$."),
            p(
                r"(a) Show that "
                r"$\dfrac{1}{n+1}<\displaystyle\int_{n}^{n+1}\dfrac{1}{x}\,dx<\dfrac{1}{n}$."
            ),
            p(
                r"(b) Hence show that "
                r"$\dfrac{n}{n+1}<\ln\left(1+\dfrac{1}{n}\right)^{n}<1$."
            ),
            p(
                r"(c) Take the limit as $n\to\infty$ to show that "
                r"$\displaystyle\lim_{n\to\infty}\left(1+\dfrac{1}{n}\right)^{n}=e$."
            ),
            p(
                r"(d) Repeat the above, replacing $n+1$ with $n+m$, to show that "
                r"$\displaystyle\lim_{n\to\infty}\left(1+\dfrac{m}{n}\right)^{n}=e^{m}$."
            ),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        p(
            r"On $[n,n+1]$, the function $y=\dfrac{1}{x}$ is decreasing, so its graph lies "
            r"between the horizontal lines $y=\dfrac{1}{n+1}$ and $y=\dfrac{1}{n}$."
        ),
        p(r"Comparing areas of rectangles of width $1$ with the area under the curve:"),
        eq(r"\dfrac{1}{n+1}\cdot 1<\int_{n}^{n+1}\dfrac{1}{x}\,dx<\dfrac{1}{n}\cdot 1"),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"The middle expression is $\ln(n+1)-\ln n=\ln\left(1+\dfrac{1}{n}\right)$."),
        eq(r"\dfrac{1}{n+1}<\ln\left(1+\dfrac{1}{n}\right)<\dfrac{1}{n}"),
        p(r"Multiply through by $n>0$:"),
        eq(
            r"\dfrac{n}{n+1}<n\ln\left(1+\dfrac{1}{n}\right)<1"
            r"\quad\Leftrightarrow\quad"
            r"\dfrac{n}{n+1}<\ln\left(1+\dfrac{1}{n}\right)^{n}<1"
        ),
        '<h3 class="solution">Solution (c)</h3>',
        p(r"Let $L_n=\left(1+\dfrac{1}{n}\right)^{n}$. From (b),"),
        eq(r"\dfrac{n}{n+1}<\ln L_n<1"),
        p(r"As $n\to\infty$, $\dfrac{n}{n+1}\to 1$, so by the squeeze theorem $\ln L_n\to 1$."),
        p(r"Hence $L_n\to e^{1}=e$."),
        eq(r"\lim_{n\to\infty}\left(1+\dfrac{1}{n}\right)^{n}=e"),
        '<h3 class="solution">Solution (d)</h3>',
        p(
            r"Comparing areas under $y=\dfrac{1}{x}$ from $n$ to $n+m$ (width $m$) with "
            r"rectangles of heights $\dfrac{1}{n+m}$ and $\dfrac{1}{n}$ gives"
        ),
        eq(r"\dfrac{m}{n+m}<\ln\left(1+\dfrac{m}{n}\right)<\dfrac{m}{n}"),
        p(r"Multiply by $n$ and rearrange as in (b)–(c) to obtain"),
        eq(r"\dfrac{mn}{n+m}<\ln\left(1+\dfrac{m}{n}\right)^{n}<m"),
        p(
            r"As $n\to\infty$, $\dfrac{mn}{n+m}\to m$, so "
            r"$\ln\left(1+\dfrac{m}{n}\right)^{n}\to m$, and therefore"
        ),
        eq(r"\lim_{n\to\infty}\left(1+\dfrac{m}{n}\right)^{n}=e^{m}"),
        '<h2 class="question">Exercise 3 — Question 2</h2>',
        question_box(
            p(
                r"(a) Using differentiation from first principles, show that if $y=\ln x$, then "
                r"$y'=\displaystyle\lim_{h\to 0}\ln\left(1+\dfrac{h}{x}\right)^{1/h}$."
            ),
            p(
                r"(b) Using the result $y'=\dfrac{1}{x}$, show that "
                r"$\displaystyle\lim_{h\to 0}\ln\left(1+\dfrac{h}{x}\right)^{1/h}=\dfrac{1}{x}$."
            ),
            p(
                r"(c) Substitute $n=\dfrac{1}{h}$ and $m=\dfrac{1}{x}$ to prove "
                r"$\displaystyle\lim_{n\to\infty}\left(1+\dfrac{m}{n}\right)^{n}=e^{m}$."
            ),
            p(
                r"(d) Hence, using your calculator with the following values of $n$, find the "
                r"approximate value of $e$ to 9 decimal places:"
            ),
            p(r"(i) $n=10^{6}$"),
            p(r"(ii) $n=10^{10}$"),
        ),
        '<h3 class="solution">Solution (a)</h3>',
        eq(
            r"y'=\lim_{h\to 0}\dfrac{\ln(x+h)-\ln x}{h}"
            r"=\lim_{h\to 0}\dfrac{1}{h}\ln\left(\dfrac{x+h}{x}\right)"
            r"=\lim_{h\to 0}\ln\left(1+\dfrac{h}{x}\right)^{1/h}"
        ),
        '<h3 class="solution">Solution (b)</h3>',
        p(r"Since $y=\ln x$ has derivative $\dfrac{1}{x}$, part (a) gives"),
        eq(r"\lim_{h\to 0}\ln\left(1+\dfrac{h}{x}\right)^{1/h}=\dfrac{1}{x}"),
        '<h3 class="solution">Solution (c)</h3>',
        p(r"Put $n=\dfrac{1}{h}$ and $m=\dfrac{1}{x}$. As $h\to 0^+$, we have $n\to\infty$."),
        p(r"The limit in (b) becomes"),
        eq(
            r"\lim_{n\to\infty}\ln\left(1+\dfrac{m}{n}\right)^{n}=m"
            r"\quad\Rightarrow\quad"
            r"\lim_{n\to\infty}\left(1+\dfrac{m}{n}\right)^{n}=e^{m}"
        ),
        '<h3 class="solution">Solution (d)</h3>',
        p(r"With $m=1$, compute $\left(1+\dfrac{1}{n}\right)^{n}$:"),
        p(r"(i) $n=10^{6}$: $\left(1+10^{-6}\right)^{10^{6}}\approx 2.718280469$"),
        p(r"(ii) $n=10^{10}$: $\left(1+10^{-10}\right)^{10^{10}}\approx 2.718281828$"),
        p(r"(For comparison, $e\approx 2.718281828$ to 9 d.p.)"),
    ]
