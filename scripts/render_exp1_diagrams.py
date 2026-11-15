"""Diagrams for Calculus of Exponential Function (I)."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "content" / "year12" / "media"


def render_xn_exp():
    """Sketch of f(x)=x^n e^{-x} for x>0 (illustrative n=3)."""
    n = 3
    x = np.linspace(0.01, 12, 400)
    y = (x**n) * np.exp(-x)
    fig, ax = plt.subplots(figsize=(4.2, 3.0))
    ax.plot(x, y, color="#1a1a1a", lw=1.8)
    ax.plot([n], [n**n * np.exp(-n)], "o", color="#1a1a1a", ms=5)
    ax.annotate(
        r"$x=n$",
        xy=(n, n**n * np.exp(-n)),
        xytext=(n + 1.2, n**n * np.exp(-n) * 0.85),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="#444", lw=0.8),
    )
    ax.axhline(0, color="#888", lw=0.6)
    ax.axvline(0, color="#888", lw=0.6)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$f(x)$")
    ax.set_title(r"$f(x)=x^n e^{-x}$ $(n=3)$", fontsize=11)
    ax.set_xlim(0, 12)
    ax.set_ylim(bottom=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    dest = OUT / "exp1_ex3_q1.png"
    fig.savefig(dest, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", dest)


def render_g_sketch():
    """Sketch of even g(x)=4e^{-|x|}-6e^{-2|x|}."""
    x = np.linspace(-5, 5, 600)
    t = np.abs(x)
    y = 4 * np.exp(-t) - 6 * np.exp(-2 * t)

    ln3 = np.log(3)
    ln6 = np.log(6)
    ln32 = np.log(1.5)
    max_y = 2 / 3
    inf_y = 0.5

    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    ax.plot(x, y, color="#1a1a1a", lw=1.8)
    ax.axhline(0, color="#888", lw=0.7)
    ax.axvline(0, color="#888", lw=0.7)

    ax.text(4.2, 0.12, r"$y=0$", fontsize=9, color="#555")

    for sx in (ln3, -ln3):
        ax.plot([sx], [max_y], "o", color="#1a1a1a", ms=4.5)
    ax.annotate(
        r"$(\ln 3,\frac{2}{3})$",
        xy=(ln3, max_y),
        xytext=(ln3 + 0.35, max_y + 0.35),
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="#444", lw=0.7),
    )
    ax.annotate(
        r"$(-\ln 3,\frac{2}{3})$",
        xy=(-ln3, max_y),
        xytext=(-ln3 - 2.4, max_y + 0.35),
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="#444", lw=0.7),
    )

    for sx in (ln6, -ln6):
        ax.plot([sx], [inf_y], "s", color="#1a1a1a", ms=3.5, fillstyle="none")
    ax.annotate(
        r"$(\ln 6,\frac{1}{2})$",
        xy=(ln6, inf_y),
        xytext=(ln6 + 0.2, inf_y - 0.55),
        fontsize=8,
        arrowprops=dict(arrowstyle="->", color="#444", lw=0.7),
    )

    for sx in (ln32, -ln32):
        ax.plot([sx], [0], "o", color="#1a1a1a", ms=4)

    ax.plot([0], [-2], "o", color="#1a1a1a", ms=4.5)
    ax.annotate(
        r"$(0,-2)$",
        xy=(0, -2),
        xytext=(0.4, -2.35),
        fontsize=9,
    )

    ax.set_xlim(-5, 5)
    ax.set_ylim(-2.6, 1.2)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_title(r"$y=g(x)$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    dest = OUT / "exp1_ex3_q2_sketch.png"
    fig.savefig(dest, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", dest)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    render_xn_exp()
    render_g_sketch()
