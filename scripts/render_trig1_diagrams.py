"""Diagrams for Calculus of Trigonometric Functions (I)."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Polygon, Wedge

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "content" / "year12" / "media"


def render_limits_geometry() -> None:
    """Unit-circle picture for lim sinθ/θ and tanθ/θ."""
    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    theta = 0.85  # radians for illustration
    ax.add_patch(Circle((0, 0), 1, fill=False, color="#1a1a1a", lw=1.4))
    ax.plot([0, 1.6], [0, 0], color="#888", lw=0.7)
    ax.plot([0, 0], [0, 1.35], color="#888", lw=0.7)

    # radii to A=(cosθ,sinθ) and to tangent point suggestion
    A = (np.cos(theta), np.sin(theta))
    # vertical from A to x-axis foot P=(cosθ,0); chord from (1,0) wait standard:
    # O origin, point B=(1,0) on circle, A on circle, tangent at B meets OA at T
    B = (1.0, 0.0)
    # tangent at B is x=1; OA line intersects x=1 at T=(1, tanθ)
    T = (1.0, np.tan(theta))
    P = (np.cos(theta), 0.0)  # foot for sin length from A? actually height is sin

    ax.plot([0, A[0]], [0, A[1]], color="#1a1a1a", lw=1.3)
    ax.plot([0, T[0]], [0, T[1]], color="#1a1a1a", lw=1.0, ls="--")
    ax.plot([A[0], A[0]], [0, A[1]], color="#444", lw=1.0)  # sin θ
    ax.plot([B[0], T[0]], [B[1], T[1]], color="#1a1a1a", lw=1.3)  # tan θ
    ax.plot([A[0], B[0]], [A[1], B[1]], color="#1a1a1a", lw=1.1)  # chord

    arc = Arc((0, 0), 2, 2, theta1=0, theta2=np.degrees(theta), color="#1a1a1a", lw=1.5)
    ax.add_patch(arc)

    ax.plot(*A, "o", color="#1a1a1a", ms=4)
    ax.plot(*B, "o", color="#1a1a1a", ms=4)
    ax.plot(*T, "o", color="#1a1a1a", ms=4)
    ax.plot(0, 0, "o", color="#1a1a1a", ms=4)

    ax.text(-0.12, -0.12, r"$O$", fontsize=11)
    ax.text(B[0] + 0.06, -0.14, r"$B$", fontsize=11)
    ax.text(A[0] - 0.18, A[1] + 0.06, r"$A$", fontsize=11)
    ax.text(T[0] + 0.06, T[1] - 0.02, r"$T$", fontsize=11)
    ax.text(0.55, 0.12, r"$\theta$", fontsize=11)
    ax.text(A[0] - 0.28, A[1] / 2, r"$\sin\theta$", fontsize=9, rotation=90)
    ax.text(1.08, T[1] / 2, r"$\tan\theta$", fontsize=9)
    ax.text(0.72, 0.38, r"arc $\theta$", fontsize=9)

    ax.set_xlim(-0.35, 1.55)
    ax.set_ylim(-0.35, 1.45)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    dest = OUT / "trig1_ex1_q1.png"
    fig.savefig(dest, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", dest)


def render_polygon() -> None:
    """Regular polygon sector with central angle α."""
    fig, ax = plt.subplots(figsize=(4.2, 4.0))
    r = 1.0
    alpha = 2 * np.pi / 6  # illustrative hexagon sector
    ax.add_patch(Circle((0, 0), r, fill=False, color="#1a1a1a", lw=1.3))

    a0, a1 = -alpha / 2, alpha / 2
    p0 = (r * np.cos(a0), r * np.sin(a0))
    p1 = (r * np.cos(a1), r * np.sin(a1))
    ax.plot([0, p0[0]], [0, p0[1]], color="#1a1a1a", lw=1.3)
    ax.plot([0, p1[0]], [0, p1[1]], color="#1a1a1a", lw=1.3)
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="#1a1a1a", lw=1.5)

    # light rest of hexagon
    verts = [
        (r * np.cos(-np.pi / 2 + k * alpha), r * np.sin(-np.pi / 2 + k * alpha))
        for k in range(6)
    ]
    # use standard orientation: start at angle
    verts = [(r * np.cos(k * alpha + a0), r * np.sin(k * alpha + a0)) for k in range(6)]
    ax.add_patch(Polygon(verts, closed=True, fill=False, edgecolor="#888", lw=1.0, ls="--"))

    ax.plot(0, 0, "o", color="#1a1a1a", ms=4)
    mid = ((p0[0] + p1[0]) / 2 * 0.35, (p0[1] + p1[1]) / 2 * 0.35)
    ax.text(mid[0] - 0.05, mid[1] - 0.02, r"$\alpha$", fontsize=12)
    ax.text(0.35, -0.08, r"$r$", fontsize=11)
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    dest = OUT / "trig1_ex1_q2.png"
    fig.savefig(dest, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", dest)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    render_limits_geometry()
    render_polygon()
