import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def arrow(ax, start, vec, color, lw=2):
    ax.annotate(
        "",
        xy=(start[0] + vec[0], start[1] + vec[1]),
        xytext=start,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=14),
    )


fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.8))

# Left: proj_u(v)
ax = axes[0]
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-0.3, 4.2)
ax.set_ylim(-0.5, 2.6)
O = np.array([0.2, 0.2])
u = np.array([3.2, 0.0])
v = np.array([1.8, 1.8])
# projection scalar
t = np.dot(v, u) / np.dot(u, u)
p = t * u
arrow(ax, O, u, "#1f77b4")
arrow(ax, O, v, "#d62728")
arrow(ax, O, p, "#2ca02c", lw=2.4)
ax.plot([O[0] + v[0], O[0] + p[0]], [O[1] + v[1], O[1] + p[1]], "--", color="#666", lw=1.2)
ax.text(O[0] + u[0] + 0.05, O[1] + 0.1, r"$\mathbf{u}$", color="#1f77b4", fontsize=12)
ax.text(O[0] + v[0] + 0.05, O[1] + v[1], r"$\mathbf{v}$", color="#d62728", fontsize=12)
ax.text(O[0] + p[0] * 0.45, O[1] - 0.28, r"$\mathrm{proj}_{\mathbf{u}}(\mathbf{v})$", color="#2ca02c", fontsize=11)
ax.set_title(r"$\mathrm{proj}_{\mathbf{u}}(\mathbf{v})$", fontsize=12)

# Right: proj_u(-v)
ax = axes[1]
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-2.5, 3.8)
ax.set_ylim(-2.3, 1.2)
O = np.array([1.6, 0.2])
u = np.array([2.0, 0.0])
mv = -v
t2 = np.dot(mv, u) / np.dot(u, u)
p2 = t2 * u  # = -p direction along u axis; with this u length different
# use same geometry scaled
u = np.array([3.2, 0.0])
mv = np.array([-1.8, -1.8])
t2 = np.dot(mv, u) / np.dot(u, u)
p2 = t2 * u
arrow(ax, O, u, "#1f77b4")
arrow(ax, O, mv, "#d62728")
arrow(ax, O, p2, "#2ca02c", lw=2.4)
ax.plot(
    [O[0] + mv[0], O[0] + p2[0]],
    [O[1] + mv[1], O[1] + p2[1]],
    "--",
    color="#666",
    lw=1.2,
)
ax.text(O[0] + u[0] + 0.05, O[1] + 0.1, r"$\mathbf{u}$", color="#1f77b4", fontsize=12)
ax.text(O[0] + mv[0] - 0.55, O[1] + mv[1] - 0.15, r"$-\mathbf{v}$", color="#d62728", fontsize=12)
ax.text(
    O[0] + p2[0] * 0.35 - 0.2,
    O[1] + 0.2,
    r"$\mathrm{proj}_{\mathbf{u}}(-\mathbf{v})$",
    color="#2ca02c",
    fontsize=11,
)
ax.set_title(r"$\mathrm{proj}_{\mathbf{u}}(-\mathbf{v})=-\mathrm{proj}_{\mathbf{u}}(\mathbf{v})$", fontsize=12)

fig.tight_layout()
out = r"D:\source codes\04-other-code\math\content\year12\media\vg1_q2_proj.png"
import pathlib

pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=160, bbox_inches="tight", facecolor="white")
print("saved", out)
