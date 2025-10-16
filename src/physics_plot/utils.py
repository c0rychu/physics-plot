class Handles(list):
    def __init__(self, *args):
        super().__init__(*args)

    def append_violinplot(self, violinplot, label):
        self.append(self._create_patch_from_violinplot(violinplot, label))

    def _create_patch_from_violinplot(self, violinplot, label):
        from matplotlib.patches import Patch

        body = violinplot["bodies"][0]
        color = body.get_facecolor()[0]
        return Patch(color=color, label=label)
