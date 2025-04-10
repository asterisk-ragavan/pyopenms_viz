from __future__ import annotations

from typing import TYPE_CHECKING
from ..constants import IS_SPHINX_BUILD

from .core import (
    PLOTLYLinePlot,
    PLOTLYVLinePlot,
    PLOTLYScatterPlot,
    PLOTLYChromatogramPlot,
    PLOTLYMobilogramPlot,
    PLOTLYSpectrumPlot,
    PLOTLYPeakMapPlot,
)

if TYPE_CHECKING:
    from .core import PLOTLYPlot

if IS_SPHINX_BUILD:
    from .core import PLOTLY_MSPlot, PLOTLYPlot

PLOT_CLASSES: dict[str, type[PLOTLYPlot]] = {
    "line": PLOTLYLinePlot,
    "vline": PLOTLYVLinePlot,
    "scatter": PLOTLYScatterPlot,
    "chromatogram": PLOTLYChromatogramPlot,
    "mobilogram": PLOTLYMobilogramPlot,
    "spectrum": PLOTLYSpectrumPlot,
    "peakmap": PLOTLYPeakMapPlot,
}


def plot(data, kind, **kwargs):
    plot_obj = PLOT_CLASSES[kind](data, **kwargs)
    if plot_obj.show_plot:
        plot_obj.show()

    return plot_obj.fig


__all__ = ["plot"]
