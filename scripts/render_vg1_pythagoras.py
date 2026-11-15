import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Arc, Rectangle
import numpy as np

fig, ax = plt.subplots(figsize=(5.5, 4.5))

C = np.array([0.8, 0.8])
A = np.array([0.8, 3.6])
B = np.array([4.2, 0.8])

ax.plot([C[0], A[0]], [C[1], A[1]], "k-", lw=1.8)
ax.plot([C[0], B[0]], [C[1], B[1]], "k-", lw=1.8)
ax.plot([A[0], B[0]], [A[1], B[1]], "k-", lw=1.8)

# right-angle mark
s = 0.28
ax.plot([C[0], C[0] + s, C[0] + s], [C[1] + s, C[1] + s, C[1]], "k-", lw=1.2)

# vectors
ax.annotate(
    "",
    xy=A,
    xytext=C,
    arrowprops=dict(arrowstyle="-|>", color="#1f77b4", lw=2, mutation_scale=14),
)
ax.annotate(
    "",
    xy=B,
    xytext=C,
    arrowprops=dict(arrowstyle="-|>", color="#2ca02c", lw=2, mutation_scale=14),
)
ax.annotate(
    "",
    xy=B,
    xytext=A,
    arrowprops=dict(arrowstyle="-|>", color="#d62728", lw=2, mutation_scale=14),
)

ax.text(C[0] - 0.25, C[1] - 0.2, "C", fontsize=12)
ax.text(A[0] - 0.25, A[1] + 0.1, "A", fontsize=12)
ax.text(B[0] + 0.1, B[1] - 0.2, "B", fontsize=12)
ax.text(C[0] - 0.55, (C[1] + A[1]) / 2, r"$\mathbf{a}$", color="#1f77b4", fontsize=12)
ax.text((C[0] + B[0]) / 2, C[1] - 0.35, r"$\mathbf{b}$", color="#2ca02c", fontsize=12)
ax.text((A[0] + B[0]) / 2 + 0.15, (A[1] + B[1]) / 2 + 0.15, r"$\mathbf{c}$", color="#d62728", fontsize=12)

ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(0, 5)
ax.set_ylim(0.2, 4.2)
ax.set_title(r"Right-angled at $C$: $\mathbf{a}\cdot\mathbf{b}=0$", fontsize=12)
fig.tight_layout()

out = r"D:\source codes\04-other-code\math\content\year12\media\vg1_q3_pythagoras.png"
import pathlib

pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=160, bbox_inches="tight", facecolor="white")
print("saved", out)
