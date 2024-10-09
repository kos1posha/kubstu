from PySide6 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc

import matplotlib.pyplot as plt
from point import Point, generate_points
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backend_bases import MouseEvent
from matplotlib.figure import Figure

import numpy as np

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

    def setup_ui(self) -> None:
        self.figure = Figure(facecolor=(0, 0, 0, 0))
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
