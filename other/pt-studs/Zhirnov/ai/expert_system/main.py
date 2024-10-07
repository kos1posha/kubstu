import sys

from PySide6 import QtWidgets as qtw

from qt import LanguageExpertControl


def main():
    app = qtw.QApplication(sys.argv)
    control = LanguageExpertControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
