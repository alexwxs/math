import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(7, 5.2))

# Points: O, A = u, B = u+v, C = u+v+w, and D = v from O? 
# Standard geometric associativity:
# Start at O
# Path 1: O --u--> A --v--> B --w--> C
# Path 2: O --u--> A, and from A do (v+w): or O --u--> P, then show 
# Classic diagram:
# O -> A (u), A -> B (v), B -> C (w) so OC = (u+v)+w
# Also A -> E (v+w) where E = C, and O -> F (v) then F -> C? 
# Better parallelogram style:
# O, U tip of u, V tip of v from O, UV parallelogram tip is u+v
# Then from u+v add w to get tip T
# From tip of v, add w get tip, then from tip of u add (v+w)

O = (0.0, 0.0)
u = (2.8, 0.4)
v = (1.2, 1.8)
w = (-0.6, 1.5)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

A = add(O, u)          # tip of u
B = add(A, v)          # tip of u+v
C = add(B, w)          # tip of (u+v)+w
E = add(A, add(v, w))  # tip of u+(v+w) — same as C
V = add(O, v)
VW = add(V, w)         # tip of v+w from O? from V
# From A, vector (v+w) goes to C

def arrow(p, q, color, label=None, label_pos=0.5, offset=(0, 0), lw=2):
    arr = FancyArrowPatch(
        p,
        q,
        arrowstyle="-|>",
        mutation_scale=14,
        lw=lw,
        color=color,
        shrinkA=0,
        shrinkB=0,
    )
    ax.add_patch(arr)
    if label:
        mx = p[0] + (q[0] - p[0]) * label_pos + offset[0]
        my = p[1] + (q[1] - p[1]) * label_pos + offset[1]
        ax.text(mx, my, label, color=color, fontsize=12)


# Path for (u+v)+w
arrow(O, A, "#1f77b4", r"$u$", 0.5, (0, -0.25))
arrow(A, B, "#2ca02c", r"$v$", 0.45, (0.1, 0.12))
arrow(B, C, "#d62728", r"$w$", 0.5, (0.12, 0.05))

# Show v+w from A as alternate path coinciding at C
arrow(A, C, "#9467bd", r"$v+w$", 0.55, (-0.35, 0.05), lw=1.6)

# Points
for p, name, off in [
    (O, "O", (-0.25, -0.15)),
    (A, "A", (-0.15, -0.25)),
    (B, "B", (0.1, 0.1)),
    (C, "C", (0.1, 0.05)),
]:
    ax.plot(*p, "o", color="black", ms=5, zorder=5)
    ax.text(p[0] + off[0], p[1] + off[1], name, fontsize=11)

ax.text(
    0.02,
    0.98,
    r"$OC=(u+v)+w=u+(v+w)$",
    transform=ax.transAxes,
    fontsize=11,
    va="top",
)

ax.set_aspect("equal")
ax.axis("off")
pad = 0.6
xs = [O[0], A[0], B[0], C[0]]
ys = [O[1], A[1], B[1], C[1]]
ax.set_xlim(min(xs) - pad, max(xs) + pad)
ax.set_ylim(min(ys) - pad, max(ys) + pad)
fig.tight_layout()
out = r"D:\source codes\04-other-code\math\content\year12\media\vg1_q1_associative.png"
import pathlib

pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=160, bbox_inches="tight", facecolor="white")
print("saved", out)
