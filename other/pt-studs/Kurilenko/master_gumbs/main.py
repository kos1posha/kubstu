import sys

from PySide6 import QtWidgets as qtw

from qt import MrGumbsControl

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv + ['-platform', 'windows:darkmode=1'])
    app.setStyle('windows')
    control = MrGumbsControl()
    control.show()
    status = app.exec()
    sys.exit(status)
