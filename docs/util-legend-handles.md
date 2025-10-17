<!-- # Legend Utilities

Matplotlib's built-in legend machinery struggles with artists that do not expose a `label` argument. `physics_plot.Handles` provides a lightweight container that bridges the gap by wrapping custom artists (such as violin plots) in legend-friendly patches.

## Creating Handles

```python
from physics_plot import Handles

handles = Handles()
```

The class simply subclasses `list`, so you can append existing legend entries or use helper methods that ship with the package.

## Violin Plot Labels

```python
import matplotlib.pyplot as plt
from physics_plot import Handles

plt.style.use("physics_plot.pp_base")

fig, ax = plt.subplots()
violin = ax.violinplot([[1, 2, 3], [4, 5, 6]])

handles = Handles()
handles.append_violinplot(violin, label="Measurements")

ax.legend(handles=handles)
```

`append_violinplot` extracts the face colour from the first violin body and wraps it in a `matplotlib.patches.Patch`, which plays nicely with `Axes.legend`.

## Mixing Custom and Built-in Handles

Because `Handles` is just a `list`, you can freely mix values returned by Matplotlib with the custom patches:

```python
line, = ax.plot(x, y, label="Best fit")

handles.append(line)
ax.legend(handles=handles)
```

## Extending the Container

If you need to support more artist types, subclass `Handles` or add new helper methods that wrap `Handles.append`:

```python
from matplotlib.patches import Patch
from physics_plot import Handles

class CustomHandles(Handles):
    def append_patch(self, color, label):
        self.append(Patch(color=color, label=label))
```

Pull requests that generalise the container for other Matplotlib collections (e.g., `PolyCollection`) are welcome — see the [development guide](development.md) for contribution tips. -->

