import sys

from PySide6 import QtWidgets
from control import FuncToGraphControl


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    control = FuncToGraphControl(QtWidgets.QWidget())
    control.widget.show()
    sys.exit(app.exec())
