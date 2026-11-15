"""Sketch of y = x^x for Log Calculus Ex3 Q1(c)."""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.02, 2.4, 800)
y = np.exp(x * np.log(x))

fig, ax = plt.subplots(figsize=(6.0, 4.2))
ax.plot(x, y, color="#1a1a1a", lw=2.0)
ax.axhline(0, color="#888", lw=0.8)
ax.axvline(0, color="#888", lw=0.8)

xmin = np.e ** -1
ymin = np.exp(xmin * np.log(xmin))
ax.plot([xmin], [ymin], "o", color="#1a1a1a", ms=5)
ax.annotate(
    r"$\left(e^{-1},\,e^{-1/e}\right)$",
    xy=(xmin, ymin),
    xytext=(18, -28),
    textcoords="offset points",
    fontsize=11,
    arrowprops=dict(arrowstyle="->", color="#555", lw=0.9),
)
ax.plot([1], [1], "o", color="#1a1a1a", ms=4)
ax.annotate(r"$(1,1)$", xy=(1, 1), xytext=(10, 8), textcoords="offset points", fontsize=11)

# asymptote hint y -> 1 as x -> 0+
ax.axhline(1, color="#aaa", lw=0.8, ls="--")
ax.annotate(r"$y\to 1$", xy=(0.08, 1), xytext=(18, 12), textcoords="offset points", fontsize=10, color="#555")

ax.set_xlim(-0.15, 2.5)
ax.set_ylim(-0.15, 2.2)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_title(r"$y=x^{x}$ $(x>0)$", fontsize=12)
ax.grid(True, alpha=0.25)

fig.tight_layout()
out = pathlib.Path(r"D:\source codes\04-other-code\math\content\year12\media\log1_ex3_q1c_sketch.png")
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=170, bbox_inches="tight", facecolor="white")
print("saved", out)
