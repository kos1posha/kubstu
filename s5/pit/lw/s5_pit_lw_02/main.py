import sys

from PySide6 import QtWidgets
from control import ImageEditorControl

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    control = ImageEditorControl(QtWidgets.QMainWindow())
    control.widget.show()
    sys.exit(app.exec())
