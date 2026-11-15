import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure(figsize=(7.2, 6.2))
ax = fig.add_subplot(111, projection="3d")

# Point / vector tip
x0, y0, z0 = 2.2, 1.6, 1.8
O = np.array([0.0, 0.0, 0.0])
P = np.array([x0, y0, z0])

# Axes
L = 2.8
ax.plot([0, L], [0, 0], [0, 0], color="#444", lw=1.2)
ax.plot([0, 0], [0, L], [0, 0], color="#444", lw=1.2)
ax.plot([0, 0], [0, 0], [0, L], color="#444", lw=1.2)
ax.text(L, 0, 0, "x", fontsize=11)
ax.text(0, L, 0, "y", fontsize=11)
ax.text(0, 0, L, "z", fontsize=11)

# Light plane patches near origin
xy = Poly3DCollection(
    [[[0, 0, 0], [2.5, 0, 0], [2.5, 2.0, 0], [0, 2.0, 0]]],
    alpha=0.12,
    facecolor="#1f77b4",
    edgecolor="none",
)
yz = Poly3DCollection(
    [[[0, 0, 0], [0, 2.0, 0], [0, 2.0, 2.2], [0, 0, 2.2]]],
    alpha=0.12,
    facecolor="#2ca02c",
    edgecolor="none",
)
xz = Poly3DCollection(
    [[[0, 0, 0], [2.5, 0, 0], [2.5, 0, 2.2], [0, 0, 2.2]]],
    alpha=0.12,
    facecolor="#d62728",
    edgecolor="none",
)
ax.add_collection3d(xy)
ax.add_collection3d(yz)
ax.add_collection3d(xz)

# Vector u
ax.quiver(0, 0, 0, x0, y0, z0, color="#0f4c5c", arrow_length_ratio=0.08, lw=2)
ax.scatter([x0], [y0], [z0], color="#0f4c5c", s=30, zorder=5)
ax.text(x0 + 0.1, y0 + 0.1, z0 + 0.1, r"$u=(x_0,y_0,z_0)$", fontsize=10)

# Feet of perpendiculars to planes
# to xy-plane (z=0): (x0,y0,0), distance z0
# to yz-plane (x=0): (0,y0,z0), distance x0
# to xz-plane (y=0): (x0,0,z0), distance y0
Fxy = np.array([x0, y0, 0.0])
Fyz = np.array([0.0, y0, z0])
Fxz = np.array([x0, 0.0, z0])

for F, color, label, mid in [
    (Fxy, "#1f77b4", r"$z_0$", (x0 + 0.15, y0 + 0.15, z0 / 2)),
    (Fyz, "#2ca02c", r"$x_0$", (x0 / 2, y0 + 0.15, z0 + 0.1)),
    (Fxz, "#d62728", r"$y_0$", (x0 + 0.15, y0 / 2, z0 + 0.1)),
]:
    ax.plot([P[0], F[0]], [P[1], F[1]], [P[2], F[2]], color=color, lw=1.8, ls="--")
    ax.scatter([F[0]], [F[1]], [F[2]], color=color, s=22, zorder=5)
    ax.text(*mid, label, color=color, fontsize=11)

ax.scatter([0], [0], [0], color="black", s=18)
ax.text(-0.15, -0.15, -0.1, "O", fontsize=11)

ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_zlim(0, L)
ax.set_box_aspect([1, 1, 1])
ax.view_init(elev=22, azim=35)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_title("Distances from $u$ to the coordinate planes", fontsize=12, pad=8)

fig.tight_layout()
out = r"D:\source codes\04-other-code\math\content\year12\media\vg1_q2_planes.png"
import pathlib

pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=160, bbox_inches="tight", facecolor="white")
print("saved", out)
