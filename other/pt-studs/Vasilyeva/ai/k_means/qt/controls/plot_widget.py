from PySide6 import QtWidgets as qtw
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from kmeans import Point


# noinspection PyTypeChecker,PyUnresolvedReferences
class PlotWidget(qtw.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.plot_action = ''
        self.points = []
        self.layout = qtw.QVBoxLayout(self)
        self.figure = Figure()
        self.facecolor = (240 / 255, 240 / 255, 240 / 255)
        self.figure.subplots_adjust(left=0.15, right=0.95, top=0.98, bottom=0.08)
        self.figure.patch.set_facecolor(self.facecolor)
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)

        self.update_method = self.update_plot

        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.update_method()

    def on_click(self, event):
        if event.inaxes is not None:
            if self.plot_action == 'add':
                self.points.append(Point(event.xdata, event.ydata))
            elif self.plot_action == 'delete':
                self.points = [p for p in self.points if not (abs(p.x - event.xdata) < 3 and abs(p.y - event.ydata) < 3)]
            self.update_method()

    def update_plot(self):
        self.ax.clear()
        if self.points:
            xs, ys = zip(*[p.astuple() for p in self.points])
            self.ax.scatter(xs, ys, s=8)
        self.ax.set_xlim(-100, 100)
        self.ax.set_ylim(-100, 100)
        self.canvas.draw()
        try:
            self.parent.update_points_list()
        except:
            pass
