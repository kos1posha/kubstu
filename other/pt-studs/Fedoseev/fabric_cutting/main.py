import sys

from PySide6 import QtWidgets as qtw


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv + ['--platform', 'windows:darkmode = 2'])
    control = object()
    control.show()
    status = app.exec()
    sys.exit(status)
