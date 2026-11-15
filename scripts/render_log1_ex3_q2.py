"""Diagrams for Log Calculus Ex3 Q2: P(x) question figure + solution sketch."""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

a = 0.5
MEDIA = pathlib.Path(__file__).resolve().parents[1] / "content" / "year12" / "media"
MEDIA.mkdir(parents=True, exist_ok=True)


def P(x):
    # Root at 0; double root (tangency / local min on axis) at a.
    # The mark "1" is a reference only (0 < a < 1), not a root.
    return 2.2 * np.asarray(x, dtype=float) * (np.asarray(x, dtype=float) - a) ** 2


def style_axes(ax, ylim):
    ax.axhline(0, color="#333", lw=1.1)
    ax.axvline(0, color="#333", lw=1.1)
    for xv in (a, 1.0):
        ax.plot([xv], [0], "o", color="#1a1a1a", ms=5, zorder=4)
    ax.annotate(r"$a$", xy=(a, 0), xytext=(0, -18), textcoords="offset points", ha="center", va="top", fontsize=13)
    ax.annotate(r"$1$", xy=(1.0, 0), xytext=(0, -18), textcoords="offset points", ha="center", va="top", fontsize=13)
    ax.text(-0.08, -0.12, "0", fontsize=12, ha="right", va="top")
    ax.set_xlim(-0.55, 1.95)
    ax.set_ylim(*ylim)
    ax.annotate(r"$x$", xy=(1.9, 0), xytext=(8, -3), textcoords="offset points", fontsize=12)
    ax.annotate(r"$y$", xy=(0, ylim[1] - 0.05), xytext=(5, 2), textcoords="offset points", fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


# ---- Question figure: y = P(x) only ----
fig, ax = plt.subplots(figsize=(6.6, 4.6))
x = np.linspace(-0.45, 1.85, 800)
ax.plot(x, P(x), color="#1a1a1a", lw=2.25, zorder=3)
style_axes(ax, (-0.4, 1.15))
ax.annotate(
    r"$y=P(x)$",
    xy=(1.35, float(P(1.35))),
    xytext=(-2, 14),
    textcoords="offset points",
    fontsize=12,
)
fig.tight_layout(pad=0.25)
out_p = MEDIA / "log1_ex3_q2_p.png"
fig.savefig(out_p, dpi=170, bbox_inches="tight", facecolor="white")
print("saved", out_p)
plt.close(fig)

# ---- Solution sketch: P and (ln x) P on the same axes ----
fig, ax = plt.subplots(figsize=(6.8, 4.8))
x_p = np.linspace(-0.45, 1.85, 800)
x_f = np.linspace(0.04, 1.85, 900)
f = np.log(x_f) * P(x_f)

ax.plot(x_p, P(x_p), color="#888888", lw=1.8, zorder=2, label=r"$y=P(x)$")
ax.plot(x_f, f, color="#1a1a1a", lw=2.35, zorder=3, label=r"$y=(\ln x)\,P(x)$")

style_axes(ax, (-0.55, 1.2))

# Labels placed to avoid overlap
ax.annotate(
    r"$y=P(x)$",
    xy=(1.45, float(P(1.45))),
    xytext=(8, -2),
    textcoords="offset points",
    fontsize=11,
    color="#666666",
)
ax.annotate(
    r"$y=(\ln x)\,P(x)$",
    xy=(1.45, float(np.log(1.45) * P(1.45))),
    xytext=(8, 10),
    textcoords="offset points",
    fontsize=11,
    color="#1a1a1a",
)

# Mark tangency at a and intercept at 1 for f
ax.plot([a], [0], "o", color="#1a1a1a", ms=5.5, zorder=5)
ax.plot([1.0], [0], "o", color="#1a1a1a", ms=5, zorder=5)

fig.tight_layout(pad=0.25)
out_s = MEDIA / "log1_ex3_q2_sketch.png"
fig.savefig(out_s, dpi=170, bbox_inches="tight", facecolor="white")
print("saved", out_s)
plt.close(fig)
