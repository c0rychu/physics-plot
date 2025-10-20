import matplotlib.pyplot as plt
import numpy as np

plt.style.use("physics_plot.pp_base")

fig, ax = plt.subplots(figsize=(4, 2), constrained_layout=True)
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, label="Sine Wave")
ax.set_ylabel(r"$y(x)$")
ax.set_xlabel(r"$x$")
ax.legend(loc="upper right")
fig.suptitle(r"\texttt{figsize=(4, 2)}")
fig.savefig("mpl-size-sm.png")


fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, label="Sine Wave")
ax.set_ylabel(r"$y(x)$")
ax.set_xlabel(r"$x$")
ax.legend(loc="upper right")
fig.suptitle(r"\texttt{figsize=(10, 5)}")
fig.savefig("mpl-size-lg.png")
