"""Diagrams for Calculus of Trigonometric Functions (II)."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Polygon

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "content" / "year12" / "media"


def render_ln_cos():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 2000)
    # exclude neighbourhoods of odd multiples of π
    y = np.log(1 + np.cos(x))
    mask = np.abs(np.cos(x) + 1) < 1e-3
    y = y.copy()
    y[mask] = np.nan

    fig, ax = plt.subplots(figsize=(6.2, 3.2))
    ax.plot(x, y, color="#1a1a1a", lw=1.6)
    for odd in (-np.pi, np.pi):
        ax.axvline(odd, color="#888", ls="--", lw=0.9)
    ax.axhline(0, color="#888", lw=0.6)
    ax.axvline(0, color="#888", lw=0.6)
    ax.plot([-2 * np.pi, 0, 2 * np.pi], [np.log(2)] * 3, "o", color="#1a1a1a", ms=4)
    ax.text(-np.pi - 0.15, 0.15, r"$x=-\pi$", fontsize=9, rotation=90, va="bottom")
    ax.text(np.pi + 0.05, 0.15, r"$x=\pi$", fontsize=9, rotation=90, va="bottom")
    ax.text(0.15, np.log(2) + 0.05, r"$\ln 2$", fontsize=9)
    ax.set_xlim(-2 * np.pi - 0.2, 2 * np.pi + 0.2)
    ax.set_ylim(-3.2, 1.2)
    ax.set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
    ax.set_xticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_title(r"$y=\ln(1+\cos x)$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    dest = OUT / "trig2_ex2_q1.png"
    fig.savefig(dest, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", dest)


def render_sinx_over_x():
    x = np.linspace(0.001, np.pi / 2, 400)
    y = np.sin(x) / x
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    ax.plot(x, y, color="#1a1a1a", lw=1.8)
    ax.plot([0], [1], "o", color="#1a1a1a", ms=4, fillstyle="none")
    ax.plot([np.pi / 2], [2 / np.pi], "o", color="#1a1a1a", ms=4)
    ax.axhline(2 / np.pi, color="#888", ls=":", lw=0.8)
    ax.annotate(
        r"$\left(\frac{\pi}{2},\frac{2}{\pi}\right)$",
        xy=(np.pi / 2, 2 / np.pi),
        xytext=(0.7, 0.55),
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="#444", lw=0.7),
    )
    ax.annotate(
        r"$\to 1$",
        xy=(0.05, 0.98),
        xytext=(0.35, 1.05),
        fontsize=9,
    )
    ax.set_xlim(0, np.pi / 2 + 0.1)
    ax.set_ylim(0.55, 1.12)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_title(r"$y=\dfrac{\sin x}{x}$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    dest = OUT / "trig2_ex3_q1.png"
    fig.savefig(dest, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", dest)


def render_quad():
    # Schematic PQRS with diagonal PR
    P = np.array([0.0, 2.0])
    Q = np.array([2.2, 2.3])
    R = np.array([3.0, 0.4])
    S = np.array([-0.3, 0.2])
    fig, ax = plt.subplots(figsize=(4.4, 3.6))
    poly = Polygon([P, Q, R, S], closed=True, fill=False, edgecolor="#1a1a1a", lw=1.6)
    ax.add_patch(poly)
    ax.plot([P[0], R[0]], [P[1], R[1]], color="#1a1a1a", lw=1.1, ls="--")
    for pt, lab, off in [
        (P, "P", (-0.25, 0.1)),
        (Q, "Q", (0.1, 0.1)),
        (R, "R", (0.1, -0.2)),
        (S, "S", (-0.3, -0.2)),
    ]:
        ax.plot(*pt, "o", color="#1a1a1a", ms=4)
        ax.text(pt[0] + off[0], pt[1] + off[1], lab, fontsize=11)
    ax.text(1.1, 2.35, r"$a$", fontsize=11)
    ax.text(2.75, 1.45, r"$b$", fontsize=11)
    ax.text(1.5, 0.05, r"$c$", fontsize=11)
    ax.text(-0.35, 1.1, r"$d$", fontsize=11)
    ax.text(2.35, 1.95, r"$\alpha$", fontsize=12)
    ax.text(0.55, 0.55, r"$\beta$", fontsize=12)
    ax.set_aspect("equal")
    ax.set_xlim(-0.8, 3.5)
    ax.set_ylim(-0.5, 2.8)
    ax.axis("off")
    fig.tight_layout()
    dest = OUT / "trig2_ex3_q2.png"
    fig.savefig(dest, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", dest)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    render_ln_cos()
    render_sinx_over_x()
    render_quad()
