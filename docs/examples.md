# Examples

See the [examples directory on GitHub](https://github.com/c0rychu/physics-plot/tree/main/examples).


```python title="examples/bode-plot.py"
--8<-- "examples/bode-plot.py"
```
![Bode plot example](https://raw.githubusercontent.com/c0rychu/physics-plot/main/examples/bode-plot%402x.png)

<!-- Physics Plot ships with runnable demos so you can see how the style sheet and utilities behave on real data. Clone the repository locally, install the dependencies, and run the scripts from the project root.

## Bode Plot

```bash
uv run python examples/bode-plot.py
```

The script generates a two-panel magnitude/phase plot for a first-order low-pass filter:

![Bode plot example](https://raw.githubusercontent.com/c0rychu/physics-plot/main/examples/bode-plot%402x.png)

Look for the balanced serif typography, synchronised axis limits, and consistent legend placement driven by the default style.

## Violin Plot

Open `examples/violin-plot.ipynb` in JupyterLab or VS Code and execute the cells:

The notebook demonstrates using `physics_plot.Handles` to build legend entries for violin plots that otherwise omit labels.

![Violin plot example](https://raw.githubusercontent.com/c0rychu/physics-plot/main/examples/violin-plot%402x.png)

!!! tip
    Capture before/after screenshots when you tweak the style sheet or utilities. Attach them to issues or pull requests to document visual changes.

## Your Own Figures

- Swap in your data but keep the script structure to validate visual regressions quickly.
- Use the examples as smoke tests by running them after style tweaks; unexpected exceptions often reveal mismatched dependencies or missing fonts.
- Consider adding new examples that cover edge cases (e.g., log scales, multiple axes) if you find gaps. Place supporting assets under `examples/` so contributors can reproduce the output.
 -->
