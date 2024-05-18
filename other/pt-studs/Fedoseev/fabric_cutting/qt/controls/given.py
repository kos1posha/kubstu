from PySide6 import QtWidgets as qtw

from qt.py.given import Ui_GivenWindow


class GivenControl(Ui_GivenWindow, qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)

    def connect_ui(self):
        pass
