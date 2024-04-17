import sys

from PySide6 import QtWidgets as qtw

from qt import TransportProblemGivenControl


def main() -> None:
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    control = TransportProblemGivenControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
