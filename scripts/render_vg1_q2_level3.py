import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

fig, ax = plt.subplots(figsize=(6.8, 5.2))

# Layout matching the exam sketch (not to exact vector scale)
O = (0.5, 0.8)
A = (1.2, 4.0)
B = (5.8, 0.9)
Y = (5.2, 4.2)
# Intersection X of AB and OY (approx for diagram)
# Parametric visual midpoint-ish
X = (3.2, 2.5)


def draw_seg(p, q, color="#333", lw=1.5, ls="-"):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw, ls=ls)


def arrow(p, q, color, label, label_off=(0, 0)):
    arr = FancyArrowPatch(
        p, q, arrowstyle="-|>", mutation_scale=12, lw=1.6, color=color, shrinkA=2, shrinkB=2
    )
    ax.add_patch(arr)
    mx, my = (p[0] + q[0]) / 2 + label_off[0], (p[1] + q[1]) / 2 + label_off[1]
    ax.text(mx, my, label, color=color, fontsize=11, ha="center", va="center")


draw_seg(O, A)
draw_seg(A, Y)
draw_seg(Y, B)
draw_seg(O, B)
draw_seg(A, B, color="#555", lw=1.3)
draw_seg(O, Y, color="#555", lw=1.3)

arrow(O, A, "#1f77b4", r"$3\mathbf{a}$", (-0.45, 0.1))
arrow(O, B, "#2ca02c", r"$6\mathbf{b}$", (0.15, -0.35))
arrow(Y, B, "#d62728", r"$5\mathbf{a}-\mathbf{b}$", (0.55, 0.15))

for p, name, off in [
    (O, "O", (-0.25, -0.15)),
    (A, "A", (-0.25, 0.15)),
    (B, "B", (0.2, -0.15)),
    (Y, "Y", (0.2, 0.15)),
    (X, "X", (0.2, 0.15)),
]:
    ax.add_patch(Circle(p, 0.06, color="black", zorder=5))
    ax.text(p[0] + off[0], p[1] + off[1], name, fontsize=12)

ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-0.3, 7.0)
ax.set_ylim(0.2, 5.0)
fig.tight_layout()
out = r"D:\source codes\04-other-code\math\content\year12\media\vg1_q2_level3.png"
import pathlib

pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=160, bbox_inches="tight", facecolor="white")
print("saved", out)
