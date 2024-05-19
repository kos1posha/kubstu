from PySide6 import QtWidgets as qtw

from qt.py.lib_p import Ui_LibPWindow


class LibPControl(Ui_LibPWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)

    def connect_ui(self):
        pass
