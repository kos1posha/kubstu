import sympy as sp
import numpy as np
import math as m

from genetic_algorithm import symbols

from PySide6 import QtWidgets as qtw, QtCore as qtc

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.cm as cm
import mplcursors


cmap = cm.get_cmap('Reds')


class PlotWidget(qtw.QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bounds = {'x': (-100, 100), 'y': (-100, 100)}
        self.population = None
        self.function = None
        self.X, self.Y, self.C = None, None, None
        self.setup_ui()
        self.update_plot()

    @property
    def labelsize(self) -> int:
        max_b = max(abs(b) for b in self.bounds['x'] + self.bounds['y'])
        if max_b < 100:
            return 10
        return 10 - m.floor(m.log10(max_b / 100))

    def setup_ui(self) -> None:
        self.figure = Figure(facecolor=(0, 0, 0, 0))
        self.figure.subplots_adjust(left=0.14, right=0.93, top=0.98, bottom=0.06)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setStyleSheet('background:transparent')
        self.ax = self.figure.add_subplot(111, facecolor=(0, 0, 0, 0))
        self.setLayout(qtw.QVBoxLayout(self))
        self.layout().addWidget(self.canvas)

    def update_plot(self) -> None:
        self.ax.clear()
        self.update_colormesh()
        self.update_population()
        self.ax.tick_params('both', labelsize=self.labelsize)
        self.ax.set_xlim(*self.bounds['x'])
        self.ax.set_ylim(*self.bounds['y'])
        self.canvas.draw()

    def update_colormesh(self) -> None:
        if self.C is None:
            return
        self.ax.pcolormesh(self.X, self.Y, self.C, shading='gouraud', cmap=cmap)

    def update_population(self) -> None:
        if self.population is None:
            return
        xs, ys = zip(*self.population)
        scatter = self.ax.scatter(xs, ys, color='black', s=5)
        cursor = mplcursors.cursor(scatter, hover=False)

        @cursor.connect('add')
        def _(sel) -> None:
            index = sel.index
            ch, ht = self.population[index], self.health[index]
            sel.annotation.set_text(f'Хромосома ({ch[0]:.2f}, {ch[1]:.2f})\nЗдоровье: {ht:.2f}')
            sel.annotation.set_color('black')
            sel.annotation.get_bbox_patch().set(fc='lightgray', alpha=1)

    def put_function(self, func: sp.Expr, bounds: dict[str, tuple[int, int]], mesh_division: int = 50) -> None:
        self.function = func
        self.bounds = bounds
        x, y = np.linspace(*bounds['x'], mesh_division), np.linspace(*bounds['y'], mesh_division)
        self.X, self.Y = np.meshgrid(x, y)
        np_func = sp.lambdify(symbols, func, 'numpy')
        self.C = np_func(self.X, self.Y)
        self.update_plot()

    def function_data(self) -> None | tuple[sp.Expr, dict[str, tuple[int, int]]]:
        if self.function is None or self.bounds is None:
            return None
        return self.function, self.bounds


class BoundSpinBox(qtw.QSpinBox):
    def __init__(self, value: int = 0, lambda_range: int = 10000, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setButtonSymbols(qtw.QSpinBox.ButtonSymbols.NoButtons)
        self.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.setMinimum(-lambda_range)
        self.setMaximum(lambda_range)
        self.setValue(value)


class FunctionBoundsTableWidget(qtw.QTableWidget):
    def __init__(self, default_values: list[int], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setRowCount(2)
        self.setColumnCount(2)
        self.setSelectionMode(qtw.QTableWidget.SelectionMode.NoSelection)
        self.setHorizontalHeaderLabels(['min', 'max'])
        self.setVerticalHeaderLabels(['x', 'y'])
        self.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        default_values = iter(default_values)
        for r in range(2):
            for c in range(2):
                sb_bound = BoundSpinBox(value=next(default_values))
                sb_bound.setStyleSheet('border:none;background:transparent')
                self.setCellWidget(r, c, sb_bound)

    def fetch_data(self) -> dict[str, tuple[int, int]] | list[int]:
        cells = [(0, 0), (0, 1), (1, 0), (1, 1)]
        x_min, x_max, y_min, y_max = [self.cellWidget(r, c).value() for r, c in cells]
        return {'x': (x_min, x_max), 'y': (y_min, y_max)}

    def text_changed_connect(self, slot: callable) -> None:
        for r in range(2):
            for c in range(2):
                self.cellWidget(r, c).valueChanged.connect(slot)


def ask(title: str, text: str, yes_text: str, no_text: str) -> bool:
    yes, no = qtw.QPushButton(yes_text), qtw.QPushButton(no_text)
    msgbox = qtw.QMessageBox(qtw.QMessageBox.Icon.Question, title, text)
    msgbox.addButton(yes, qtw.QMessageBox.ButtonRole.YesRole)
    msgbox.addButton(no, qtw.QMessageBox.ButtonRole.NoRole)
    msgbox.exec()
    return msgbox.clickedButton() == yes
