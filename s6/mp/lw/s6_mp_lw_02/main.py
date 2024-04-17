import sys

from PySide6 import QtWidgets as qtw
from sympy import symbols

from qt.controls import StockBuyLpSolverControl
from simplex import Search, Simplex


def console_main():
    A, B = symbols('A B')
    task = {
        'search': Search.MAX,
        'obj_func': A + B,
        'constraints': [
            27 * A + 23 * B <= 930,
            A - B >= 10
        ],
    }
    simplex = Simplex(**task)
    simplex()

    print(simplex.pretty_history())


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    control = StockBuyLpSolverControl(show=True)
    status = app.exec()
    sys.exit(status)
