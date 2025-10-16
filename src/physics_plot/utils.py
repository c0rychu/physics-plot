class Handles(list):
    """Container for legend handles derived from Matplotlib artists."""

    def __init__(self, *args):
        """Initialize the handle list with optional starting values.

        Parameters
        ----------
        *args :
            Positional arguments forwarded to :class:`list`.
        """
        super().__init__(*args)

    def append_violinplot(self, violinplot, label):
        """Append a legend patch constructed from a violin plot.

        Parameters
        ----------
        violinplot : dict[str, list]
            Mapping returned by :meth:`matplotlib.axes.Axes.violinplot`.
        label : str
            Legend label describing the violin plot.

        Returns
        -------
        None
        """
        self.append(self._create_patch_from_violinplot(violinplot, label))

    def _create_patch_from_violinplot(self, violinplot, label):
        """Create a patch representing the first body of a violin plot.

        Parameters
        ----------
        violinplot : dict[str, list]
            Mapping returned by :meth:`matplotlib.axes.Axes.violinplot`.
        label : str
            Legend label describing the violin plot.

        Returns
        -------
        matplotlib.patches.Patch
            Patch configured with the violin plot's face color and label.
        """
        from matplotlib.patches import Patch

        body = violinplot["bodies"][0]
        color = body.get_facecolor()[0]
        return Patch(color=color, label=label)
