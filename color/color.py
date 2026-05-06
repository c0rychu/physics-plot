import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 100)
y = np.sin(t)

with plt.style.context("physics_plot.pp_base"):
    fig, ax = plt.subplots(figsize=(4, 2), constrained_layout=True)
    for i, offset in enumerate(np.linspace(0, 2, 5)):
        ax.plot(t, y - offset, label=f"C{i}")
    ax.set_ylabel(r"$y(t)$")
    ax.set_xlabel(r"Time $t$ [s]")
    ax.legend(loc="upper right")
    fig.suptitle(r"Default color (from Matplotlib)")
    fig.savefig("color-default.png")


with plt.style.context(["physics_plot.pp_base", "physics_plot.colors.ggplot"]):
    fig, ax = plt.subplots(figsize=(4, 2), constrained_layout=True)
    for i, offset in enumerate(np.linspace(0, 2, 5)):
        ax.plot(t, y - offset, label=f"C{i}")
    ax.set_ylabel(r"$y(t)$")
    ax.set_xlabel(r"Time $t$ [s]")
    ax.legend(loc="upper right")
    fig.suptitle(r"\texttt{ggplot} - color (from Matplotlib)")
    fig.savefig("color-ggplot.png")


with plt.style.context(["physics_plot.pp_base", "physics_plot.colors.colorblind"]):
    fig, ax = plt.subplots(figsize=(4, 2), constrained_layout=True)
    for i, offset in enumerate(np.linspace(0, 2, 5)):
        ax.plot(t, y - offset, label=f"C{i}")
    ax.set_ylabel(r"$y(t)$")
    ax.set_xlabel(r"Time $t$ [s]")
    ax.legend(loc="upper right")
    fig.suptitle(r"\texttt{colorblind} - color (from Seaborn)")
    fig.savefig("color-colorblind.png")
