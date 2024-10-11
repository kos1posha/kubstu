from PySide6 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc

import matplotlib.pyplot as plt
from point import Point, find_bounds
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backend_bases import MouseEvent
from matplotlib.figure import Figure

import numpy as np
import math as m

plot_range = 10000


class LimSpinBox(qtw.QSpinBox):

    def __init__(self, value: int = 0, *args, **kwargs) -> None:
        super(LimSpinBox, self).__init__(*args, **kwargs)
        self.setButtonSymbols(qtw.QSpinBox.ButtonSymbols.NoButtons)
        self.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.setMinimum(-plot_range)
        self.setMaximum(plot_range)
        self.setValue(value)


class PlotWidget(qtw.QWidget):
    class InteractiveMode:
        EDIT_POINTS = 'ep'
        SHOW_CLUSTERS = 'sc'

    def __init__(self, *args, **kwargs) -> None:
        super(PlotWidget, self).__init__(*args, **kwargs)
        self.centroids = []
        self.points = []

        self.xlim = (-100, 100)
        self.ylim = (-100, 100)
        self.interactive_mode = PlotWidget.InteractiveMode.EDIT_POINTS

        self.setup_ui()
        self.connect_ui()
        self.update_plot()

    @property
    def colors(self) -> np.ndarray:
        return plt.cm.rainbow(np.linspace(0, 1, len(self.points)))

    @property
    def labelsize(self) -> int:
        max_lim = max(abs(lim) for lim in self.xlim + self.ylim)
        if max_lim < 100:
            return 10
        return 10 - m.floor(m.log10(max_lim / 100))

    def setup_ui(self) -> None:
        self.figure = Figure(facecolor=(0, 0, 0, 0))
        self.figure.subplots_adjust(left=0.14, right=0.93, top=0.98, bottom=0.06)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setStyleSheet('background:transparent')
        self.ax = self.figure.add_subplot(111, facecolor=(0, 0, 0, 0))
        self.setLayout(qtw.QVBoxLayout(self))
        self.layout().addWidget(self.canvas)

    def connect_ui(self) -> None:
        self.canvas.mpl_connect('button_press_event', self.mouse_press_event)

    def update_plot(self) -> None:
        self.ax.clear()
        match self.interactive_mode:
            case PlotWidget.InteractiveMode.EDIT_POINTS:
                self.plot_points()
            case PlotWidget.InteractiveMode.SHOW_CLUSTERS:
                self.plot_clusters()
            case _:
                pass
        self.ax.tick_params('both', labelsize=self.labelsize)
        self.ax.set_xlim(*self.xlim)
        self.ax.set_ylim(*self.ylim)
        self.canvas.draw()

    def plot_points(self) -> None:
        if not self.points:
            return
        xs, ys = zip(*[p.as_tuple() for p in self.points])
        self.ax.scatter(xs, ys, s=8, color='white')

    def plot_clusters(self) -> None:
        for i, (centroid, cluster) in enumerate(zip(self.centroids, self.points)):
            marker = chr(ord('A') + i)
            cx, cy = centroid.as_tuple()
            xs, ys = zip(*[p.as_tuple() for p in cluster])
            self.ax.scatter(xs, ys, s=8, color=self.colors[i])
            self.ax.scatter(cx, cy, s=100, color='white', edgecolor=self.colors[i], linewidth=1, marker=f'${marker}$')

    def fit_bounds(self, x_min: int, x_max: int, y_min: int, y_max: int, force: bool = False) -> None:
        self.xlim = (min(self.xlim[0], x_min), max(self.xlim[1], x_max)) if not force else (x_min, x_max)
        self.ylim = (min(self.ylim[0], y_min), max(self.ylim[1], y_max)) if not force else (y_min, y_max)
        self.update_plot()

    def mouse_press_event(self, event: MouseEvent) -> None:
        if self.interactive_mode == PlotWidget.InteractiveMode.SHOW_CLUSTERS or event.inaxes is None:
            return
        ep = Point(event.xdata, event.ydata)
        if event.button == 1:
            self.points.append(ep)
        elif event.button == 3:
            near = [p for p in self.points if (p.x - ep.x) ** 2 + (p.y - ep.y) ** 2 <= 1]
            if near:
                nearest = sorted(near, key=lambda p: ep.distance(p))[0]
                self.points.remove(nearest)
        self.update_plot()

    def adjust_bounds(self) -> None:
        if not self.points:
            self.xlim, self.ylim = (-100, 100), (-100, 100)
            return
        points = self.points if self.interactive_mode == PlotWidget.InteractiveMode.EDIT_POINTS else sum(self.points, start=[])
        bounds = tuple(find_bounds(points).values())
        self.xlim, self.ylim = bounds[:2], bounds[2:]
        self.update_plot()
