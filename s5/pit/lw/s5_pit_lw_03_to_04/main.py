import sys

from control import PainterControl

from PySide6.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    sys.setrecursionlimit(1000)
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    control = PainterControl(QMainWindow())
    control.widget.show()
    sys.exit(app.exec())
