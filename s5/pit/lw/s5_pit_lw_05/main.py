import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from geometric_control import GeometricControl


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    control = GeometricControl(QMainWindow())
    control.widget.show()
    status = app.exec()
    sys.exit(status)
