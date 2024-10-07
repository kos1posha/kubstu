import sys

from PySide6 import QtWidgets as qtw
from qt.controls.main import GeneticAlgorithmControl


def main():
    app = qtw.QApplication(sys.argv + ['-platform', 'windows:darkmode=1'])
    app.setStyle('fusion')
    control = GeneticAlgorithmControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
