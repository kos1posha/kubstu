import sys

from PySide6 import QtWidgets as qtw

from qt.control import VitaminsLpSolverControl


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv + ['-platform', 'windows:darkmode=1'])
    app.setStyle('Fusion')
    control = VitaminsLpSolverControl(show=True)
    status = app.exec()
    sys.exit(status)
