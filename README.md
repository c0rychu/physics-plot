# physics-plot

`physics-plot` is a lightweight Matplotlib add-on that ships a publication-friendly plotting style and a few helper utilities. 

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
  
  ![Bode plot](examples/bode-plot@2x.png)

- **Violin plot** (`examples/violin-plot.ipynb`) demonstrates how to pair `Handles` with `Axes.violinplot` so the legend of the violin plot can be created, which is absent in Matplotlib.

  ![Violin plot](examples/violin-plot@2x.png)

Feel free to start from either example when styling your own figures.

## Development

- Coming soon

## License

[MIT](LICENSE)
