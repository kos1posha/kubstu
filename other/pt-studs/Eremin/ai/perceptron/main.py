import sys

from PySide6 import QtWidgets as qtw

from qt import PerceptronControl


def main() -> None:
    app = qtw.QApplication(sys.argv)
    control = PerceptronControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
