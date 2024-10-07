import mplcursors
from PySide6 import QtWidgets as qtw
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import sympy as sp
import chromosome as ch
import visualizer as v


class GeneticAlgorithmPlotWidget(qtw.QWidget, v.BaseGeneticAlgorithmVisualizer):
    def __init__(self):
        super().__init__()
        self.func = None
        self.z_func = None
        self.bounds = None
        self.layout = qtw.QVBoxLayout(self)
        self.figure = Figure()
        self.facecolor = (45 / 255, 45 / 255, 45 / 255)
        self.figure.patch.set_facecolor(self.facecolor)
        self.figure.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.1)
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def set_v_data(self, func: sp.Expr, bounds: dict[sp.Symbol, (float, float)]):
        self.func = func
        self.bounds = {str(s): b for s, b in bounds.items()}

    def visualize_population(self, population: list):
        sample = population[0]
        if len(sample.kw_dict) != 2:
            raise NotImplementedError('Доступна визуализация только двумерных сущностей')

        self.figure.clear()

        xs, ys = zip(*[[c[attr] for attr in c.attrs] for c in population])

        ax = self.figure.add_subplot(111, facecolor=self.facecolor)
        scatter = ax.scatter(xs, ys, color='white', s=10)
        ax.set_xlim(*self.bounds[sample.attrs[0]])
        ax.set_ylim(*self.bounds[sample.attrs[1]])

        cursor = mplcursors.cursor(scatter, hover=True)

        @cursor.connect('add')
        def on_add(sel):
            index = sel.index
            x, y = xs[index], ys[index]
            result = self.func.subs({sample.attrs[0]: x, sample.attrs[1]: y})
            ax.set_title(f'f({x:.2f}, {y:.2f}) = {result:.2f}')
            sel.annotation.set(visible=False)

        self.canvas.draw()

    def visualize_health(self, population: list[ch.Chromosome], health: list[float]):
        pass
