import sys

from PySide6 import QtWidgets as qtw

from qt import TransportProblemGivenControl


task = {
    'costs': [
        [3, 5, 7, 2, 8],
        [6, 5, 6, 8, 7],
        [9, 1, 2, 4, 6],
        [3, 5, 8, 9, 6]
    ],
    'supply': [500, 400, 800, 500],
    'demand': [300, 500, 500, 600, 300],
}


def main() -> None:
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    control = TransportProblemGivenControl(**task)
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
