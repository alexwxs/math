"""Diagram for Calculus of Exponential Function (II) Exercise 3."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "content" / "year12" / "media"


def render_area_sketch(k: float = 1.2) -> None:
    x = np.linspace(-2.2, 2.8, 500)
    y = (np.exp(2 * x) - 1) / (np.exp(2 * x) + 1)

    fig, ax = plt.subplots(figsize=(5.0, 3.6))
    ax.plot(x, y, color="#1a1a1a", lw=1.8)
    ax.axhline(1, color="#666", ls="--", lw=0.9)
    ax.axhline(-1, color="#666", ls="--", lw=0.9)
    ax.axhline(0, color="#888", lw=0.6)
    ax.axvline(0, color="#888", lw=0.6)
    ax.axvline(k, color="#666", ls="--", lw=0.9)

    xs = np.linspace(0, k, 120)
    ys = (np.exp(2 * xs) - 1) / (np.exp(2 * xs) + 1)
    poly = np.column_stack(
        [np.concatenate([xs, xs[::-1]]), np.concatenate([ys, np.ones_like(xs)])]
    )
    ax.add_patch(Polygon(poly, closed=True, facecolor="#c8c8c8", edgecolor="none", alpha=0.85))

    ax.text(k + 0.08, -0.18, r"$k$", fontsize=11)
    ax.text(0.08, 1.08, r"$1$", fontsize=10)
    ax.text(0.08, -1.22, r"$-1$", fontsize=10)
    ax.text(1.5, 0.55, r"$y=\dfrac{e^{2x}-1}{e^{2x}+1}$", fontsize=10)
    ax.set_xlim(-2.2, 2.8)
    ax.set_ylim(-1.5, 1.45)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    dest = OUT / "exp2_ex3_q1.png"
    fig.savefig(dest, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", dest)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    render_area_sketch()
