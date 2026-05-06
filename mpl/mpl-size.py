import matplotlib.pyplot as plt
import numpy as np

plt.style.use("physics_plot.pp_base")

x = np.linspace(0, 10, 1000)
y = np.sin(5 * x)

fig, ax = plt.subplots(figsize=(4, 2), constrained_layout=True)
ax.plot(x, y, label=r"$y = \sin(5x)$")
ax.set_ylabel(r"$y(x)$")
ax.set_xlabel(r"$x$")
ax.legend(loc="upper right")
fig.suptitle(r"Small Figure Size (4x2 inches), i.e., \texttt{figsize=(4, 2)}")
fig.savefig("mpl-size-sm.png")

fig, ax = plt.subplots(figsize=(8, 4), constrained_layout=True)
ax.plot(x, y, label=r"$y = \sin(5x)$")
ax.set_ylabel(r"$y(x)$")
ax.set_xlabel(r"$x$")
ax.legend(loc="upper right")
fig.suptitle(r"Large Figure Size (8x4 inches), i.e., \texttt{figsize=(8, 4)}")
fig.savefig("mpl-size-lg.png")
