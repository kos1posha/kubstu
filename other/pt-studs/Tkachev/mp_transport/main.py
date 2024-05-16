import sys

from PySide6 import QtWidgets as qtw

from qt.controls.main import MainControl


if __name__ == '__main__':
    sys.argv += ['-platform', 'windows:darkmode=1']
    app = qtw.QApplication(sys.argv)
    app.setStyle('windowsvista')
    control = MainControl()
    control.show()
    status = app.exec()
    sys.exit(status)
