import sys

from PySide6 import QtWidgets as qtw

from qt.controls.given import GivenControl


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv + ['-platform', 'windows:darkmode=1'])
    app.setStyle('Fusion')
    control = GivenControl()
    control.show()
    status = app.exec()
    sys.exit(status)
