import sys

from PySide6.QtWidgets import QApplication

from control import GraphEDAControl


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    control = GraphEDAControl()
    control.show()
    sys.exit(app.exec())
