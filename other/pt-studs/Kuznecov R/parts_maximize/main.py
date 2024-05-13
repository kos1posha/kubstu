import sys

from PySide6 import QtWidgets as qtw

from qt.controls.parts_maximize import PartsMaximizeControl


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle('fusion')
    control = PartsMaximizeControl()
    control.show()
    status = app.exec()
    sys.exit(status)
