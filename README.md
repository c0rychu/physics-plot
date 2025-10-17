# physics-plot

[![PyPI - Version](https://img.shields.io/pypi/v/physics-plot)](https://pypi.org/project/physics-plot/)

`physics-plot` is a lightweight python package shipping a [Matplotlib style sheet](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html) called [`pp_base.mplstyle`](https://github.com/c0rychu/physics-plot/blob/main/src/physics_plot/pp_base.mplstyle) and a few helper functions to create publication-quality plots with minimal effort.

- [Documentation](https://c0rychu.github.io/physics-plot/)
- [PyPI](https://pypi.org/project/physics-plot/)

## Features

- **Matplotlib style sheet** — `physics_plot.pp_base` enforces serif fonts, LaTeX math, minimalist grids, and high-resolution exports out of the box.
- **Legend utilities** — `physics_plot.Handles` makes it easy to build custom legend entries for artists (e.g., violin plots) that don’t expose a `label` argument.

## Installation

```bash
pip install physics-plot
```

## Quick Start

```python
import matplotlib.pyplot as plt

plt.style.use("physics_plot.pp_base")
```

## Examples

- **Bode plot** (`examples/bode-plot.py`) generates a two-panel magnitude/phase plot for a first-order low-pass filter.
  
  ![Bode plot](https://raw.githubusercontent.com/c0rychu/physics-plot/main/examples/bode-plot%402x.png)

- **Violin plot** (`examples/violin-plot.ipynb`) demonstrates how to pair `Handles` with `Axes.violinplot` so the legend of the violin plot can be created, which is absent in Matplotlib.

  ![Violin plot](https://raw.githubusercontent.com/c0rychu/physics-plot/main/examples/violin-plot%402x.png)

Feel free to start from either example when styling your own figures.

## Development

- Coming soon

## License

[MIT](LICENSE)
