import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from control import ClfControl


if __name__ == '__main__':
    app = QApplication(sys.argv)
    control = ClfControl(QMainWindow())
    control.widget.show()
    status = app.exec()
    sys.exit(status)
