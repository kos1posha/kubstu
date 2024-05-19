import sys

from PySide6 import QtWidgets as qtw

from qt import LibPControl


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv + ['-platform', 'windows:darkmode=1'])
    app.setStyle('windowsvista')
    control = LibPControl()
    control.show()
    status = app.exec()
    sys.exit(status)
