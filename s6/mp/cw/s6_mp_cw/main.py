import sys

from PySide6 import QtWidgets as qtw

from qt import MrGumbsControl


def main() -> None:
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    control = MrGumbsControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
