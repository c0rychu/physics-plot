import matplotlib.pyplot as plt
import numpy as np


def sine_gaussian(t, f0, sigma, t0=0, A=1):
    return (
        A
        * np.exp(-((t - t0) ** 2) / (2 * sigma**2))
        * np.sin(2 * np.pi * f0 * (t - t0))
    )


t = np.linspace(-0.01, 0.01, 2000)
y = sine_gaussian(t, f0=300, t0=-0.002, sigma=0.002)

with plt.style.context("physics_plot.pp_base"):
    plt.figure()
    plt.plot(t, y, label="offset = 0")
    plt.plot(t, y - 0.5, label="offset = -0.5")
    plt.plot(t, y - 1, label="offset = -1")
    plt.legend(loc="upper right")
    plt.title(r"$\texttt{physics_plot}$ style")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.savefig("with-pp@2x.png")

plt.figure()
plt.plot(t, y, label="offset = 0")
plt.plot(t, y - 0.5, label="offset = -0.5")
plt.plot(t, y - 1, label="offset = -1")
plt.legend(loc="upper right")
plt.title("Matplotlib default style")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.savefig("without-pp@2x.png", dpi=600)
