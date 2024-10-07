import sys

from PySide6 import QtWidgets as qtw

import sympy as sp
from matplotlib import pyplot as plt

from qt.controls.main import GeneticAlgorithmControl
import visualizer as v
import genetic as g


def main_plot() -> None:
    a, b = 34, 4
    x, y = sp.symbols('x y')
    func = a * x ** 2 + (1 + b) * y
    bounds = {x: (-10, 10), y: (-10, 10)}
    visualizer = v.GeneticAlgorithmPlotVisualizer(func, bounds, True)
    g.genetic(func=func, bounds=bounds, population_size=100, max_iteration=10, visualizer=visualizer)


def main():
    plt.style.use('dark_background')
    app = qtw.QApplication(sys.argv)
    control = GeneticAlgorithmControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
