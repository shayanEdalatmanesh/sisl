# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from __future__ import annotations

from sisl.messages import deprecate
from sisl.nodes import Workflow


class Plot(Workflow):
    """Base class for all plots"""

    def __getattr__(self, key):
        if key != "nodes":
            return getattr(self.nodes.output.get(), key)
        else:
            return super().__getattr__(key)

    def merge(self, *others, **kwargs):
        from .plots.merged import merge_plots

        return merge_plots(self, *others, **kwargs)

    def update_settings(self, *args, **kwargs):
        deprecate(
            "f{self.__class__.__name__}.update_settings is deprecated. Please use update_inputs.",
            "0.15",
        )
        return self.update_inputs(*args, **kwargs)

    @classmethod
    def plot_class_key(cls) -> str:
        return cls.__name__.replace("Plot", "").lower()
