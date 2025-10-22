import matplotlib.pyplot as plt
import numpy as np


# Functions for example plot
def db(x):
    return 20.0 * np.log10(x)


def model(f):
    return 10.0 / (f - 1.0j * 10)


# Plot with physics_plot style
with plt.style.context("physics_plot.pp_base"):
    fig, (ax_m, ax_p) = plt.subplots(
        nrows=2, ncols=1, figsize=(5, 3.5), constrained_layout=True
    )
    fig.suptitle(r"Low Pass Filter ($\texttt{physics_plot}$ style)")
    f = np.logspace(0, 3, 1000)

    # Magnitude
    ax_m.semilogx(f, db(np.abs(model(f))), "r", label="LPF")
    ax_m.set_xlim(1e0, 1e3)
    ax_m.set_ylabel("Magnitude [dB]")
    ax_m.grid(visible=True, which="major")
    ax_m.grid(visible=True, which="minor", linestyle=":")
    ax_m.legend(loc=1)

    # Phase
    ax_p.semilogx(f, np.angle(model(f), deg=True), "r", label="LPF")
    ax_p.set_xlim(1e0, 1e3)
    ax_p.set_ylim(0, 90)
    ax_p.set_xlabel("Frequency [Hz]")
    ax_p.set_ylabel("Phase [deg]")
    ax_p.grid(visible=True, which="major")
    ax_p.grid(visible=True, which="minor", linestyle=":")
    ax_p.legend(loc=1)

    # fig.savefig("with-pp@2x.png")
    fig.savefig("bode-plot@2x.png")


# # Plot without physics_plot style
# fig, (ax_m, ax_p) = plt.subplots(
#     nrows=2, ncols=1, figsize=(5, 3.5), constrained_layout=True
# )
# fig.suptitle("Low Pass Filter (Matplotlib default style)")
# f = np.logspace(0, 3, 1000)

# # Magnitude
# ax_m.semilogx(f, db(np.abs(model(f))), "b", label="LPF")
# ax_m.set_xlim(1e0, 1e3)
# ax_m.set_ylabel("Magnitude [dB]")
# ax_m.grid(visible=True, which="major")
# ax_m.grid(visible=True, which="minor", linestyle=":")
# ax_m.legend(loc=1)

# # Phase
# ax_p.semilogx(f, np.angle(model(f), deg=True), "b", label="LPF")
# ax_p.set_xlim(1e0, 1e3)
# ax_p.set_ylim(0, 90)
# ax_p.set_xlabel("Frequency [Hz]")
# ax_p.set_ylabel("Phase [deg]")
# ax_p.grid(visible=True, which="major")
# ax_p.grid(visible=True, which="minor", linestyle=":")
# ax_p.legend(loc=1)

# fig.savefig("without-pp@2x.png", dpi=600)
