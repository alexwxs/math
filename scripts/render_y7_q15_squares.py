"""Diagram for Year 7 Q15: two squares ABCD and PQRS (both fully shown)."""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

# P at origin; ABCD side 10, axes-aligned
A, B, C, D = (-5.0, 5.0), (5.0, 5.0), (5.0, -5.0), (-5.0, -5.0)
P = np.array([0.0, 0.0])
# BX = 4 => X = (5, 1); 90° clockwise about P => Y = (1, -5)
X = np.array([5.0, 1.0])
Y = np.array([1.0, -5.0])

# Square PQRS: side 10, vertex P; PQ through X, PS through Y
v = X / np.linalg.norm(X) * 10.0
w = np.array([v[1], -v[0]])  # 90° clockwise
Q = P + v
S = P + w
R = P + v + w

fig, ax = plt.subplots(figsize=(6.0, 6.0))

ax.add_patch(Polygon([A, B, C, D], closed=True, fill=False, edgecolor="#111", lw=2.0, zorder=2))
ax.add_patch(Polygon([P, Q, R, S], closed=True, fill=False, edgecolor="#111", lw=1.7, zorder=2))
ax.add_patch(
    Polygon(
        [P, X, C, Y],
        closed=True,
        facecolor="#d6e8f8",
        edgecolor="#1e4e8c",
        lw=1.6,
        zorder=3,
        alpha=0.85,
    )
)

ax.annotate(
    "",
    xy=tuple(X),
    xytext=B,
    arrowprops=dict(arrowstyle="<->", color="#333", lw=0.9),
)
ax.text(5.85, 3.0, "4 cm", fontsize=9, color="#333", rotation=90, va="center")

labels = {
    "A": (A, (-12, 8)),
    "B": (B, (8, 8)),
    "C": (C, (12, -12)),
    "D": (D, (-12, -14)),
    "P": (tuple(P), (-14, 10)),
    "Q": (tuple(Q), (10, 10)),
    "R": (tuple(R), (12, -8)),
    "S": (tuple(S), (-4, -16)),
    "X": (tuple(X), (12, 2)),
    "Y": (tuple(Y), (6, -16)),
}
for name, ((x, y), (dx, dy)) in labels.items():
    ax.plot([x], [y], "o", color="#111", ms=3.8, zorder=5)
    ax.annotate(name, xy=(x, y), xytext=(dx, dy), textcoords="offset points", fontsize=11)

# Fixed limits so both full squares stay inside the image
ax.set_xlim(-8.5, 15.0)
ax.set_ylim(-13.0, 9.0)
ax.set_aspect("equal")
ax.axis("off")

media = pathlib.Path(__file__).resolve().parents[1] / "content" / "year7" / "media"
pub = pathlib.Path(__file__).resolve().parents[1] / "public" / "year7" / "media"
media.mkdir(parents=True, exist_ok=True)
pub.mkdir(parents=True, exist_ok=True)
out = media / "y7_q15_squares.png"
# Avoid bbox_inches="tight" — it was cropping square PQRS
for dest in (out, pub / out.name):
    fig.savefig(dest, dpi=150, facecolor="white")
    print("saved", dest)
