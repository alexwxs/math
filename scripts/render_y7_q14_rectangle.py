"""Diagram for Year 7 Q14: shaded triangle in a rectangle."""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Rectangle

# D(0,0), C(13,0), B(13,11), A(0,11)
# E on DC with DE=5 => E(5,0); EC=8
# F on BC with BF=3, FC=8 => F(13,8)
A, B, C, D = (0, 11), (13, 11), (13, 0), (0, 0)
E, F = (5, 0), (13, 8)

fig, ax = plt.subplots(figsize=(5.4, 4.4))

ax.add_patch(Rectangle((0, 0), 13, 11, fill=False, edgecolor="#111", lw=2.0, zorder=2))

# Extra construction lines as in the worksheet
ax.plot([A[0], E[0]], [A[1], E[1]], color="#333", lw=1.2, zorder=3)
ax.plot([A[0], F[0]], [A[1], F[1]], color="#333", lw=1.2, zorder=3)
ax.plot([B[0], E[0]], [B[1], E[1]], color="#333", lw=1.0, zorder=3)
ax.plot([D[0], F[0]], [D[1], F[1]], color="#333", lw=1.0, zorder=3)
ax.plot([E[0], F[0]], [E[1], F[1]], color="#333", lw=1.2, zorder=3)

# Shade triangle AEF with hatch (vertical lines, matching worksheet)
tri = Polygon(
    [A, E, F],
    closed=True,
    facecolor="#cfe3f7",
    edgecolor="#1e4e8c",
    lw=1.5,
    hatch="||",
    zorder=4,
    alpha=0.9,
)
ax.add_patch(tri)

# Length labels
ax.annotate("5", xy=(2.5, 0), xytext=(0, -14), textcoords="offset points", ha="center", fontsize=11)
ax.annotate("8", xy=(9.0, 0), xytext=(0, -14), textcoords="offset points", ha="center", fontsize=11)
ax.annotate("3", xy=(13, 9.5), xytext=(10, 0), textcoords="offset points", va="center", fontsize=11)
ax.annotate("8", xy=(13, 4.0), xytext=(10, 0), textcoords="offset points", va="center", fontsize=11)

labels = {
    "A": (A, (-12, 8)),
    "B": (B, (8, 8)),
    "C": (C, (8, -14)),
    "D": (D, (-12, -14)),
    "E": (E, (0, -16)),
    "F": (F, (12, 0)),
}
for name, ((x, y), (dx, dy)) in labels.items():
    ax.plot([x], [y], "o", color="#111", ms=3.6, zorder=5)
    ax.annotate(name, xy=(x, y), xytext=(dx, dy), textcoords="offset points", fontsize=11)

ax.set_aspect("equal")
ax.set_xlim(-2.2, 16.2)
ax.set_ylim(-2.5, 13.2)
ax.axis("off")

media = pathlib.Path(__file__).resolve().parents[1] / "content" / "year7" / "media"
pub = pathlib.Path(__file__).resolve().parents[1] / "public" / "year7" / "media"
media.mkdir(parents=True, exist_ok=True)
pub.mkdir(parents=True, exist_ok=True)
out = media / "y7_q14_rectangle.png"
for dest in (out, pub / out.name):
    fig.savefig(dest, dpi=150, facecolor="white")
    print("saved", dest)
