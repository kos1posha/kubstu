import sys

from matplotlib import pyplot as plt
from qt import GeneticAlgorithmControl

from PySide6 import QtWidgets as qtw


def main() -> None:
    plt.style.use('dark_background')
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    control = GeneticAlgorithmControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
