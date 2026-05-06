import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 100)
y = np.sin(t)

with plt.style.context("physics_plot.pp_base"):
    fig, ax = plt.subplots(figsize=(4, 2.5), constrained_layout=True)
    ax.plot(t, y - 0.0, "r", label="r (red)")
    ax.plot(t, y - 0.3, "k", label="k (black)")
    ax.plot(t, y - 0.6, "b", label="b (blue)")
    ax.plot(t, y - 0.9, "g", label="g (green)")
    ax.plot(t, y - 1.2, "c", label="c (cyan)")
    ax.plot(t, y - 1.5, "m", label="m (magenta)")

    ax.set_ylabel(r"$y(t)$")
    ax.set_xlabel(r"Time $t$ [s]")
    ax.legend(loc="upper right")
    fig.suptitle(r"Named colors (from Matplotlib)")
    fig.savefig("color-named.png")
