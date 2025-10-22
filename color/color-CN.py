import matplotlib.pyplot as plt
import numpy as np

plt.style.use(["physics_plot.pp_base", "physics_plot.colors.ggplot"])

t = np.linspace(0, 10, 100)
y = np.sin(t)

fig, ax = plt.subplots(figsize=(4, 2), constrained_layout=True)
ax.plot(t, y, "C0", label="C0")
ax.plot(t, y + 1, "C4", label="C4")
ax.set_ylabel(r"$y(t)$")
ax.set_xlabel(r"Time $t$ [s]")
ax.legend(loc="upper right")
fig.suptitle(r"\texttt{ggplot} - color (from Matplotlib)")
fig.savefig("color-CN.png")
