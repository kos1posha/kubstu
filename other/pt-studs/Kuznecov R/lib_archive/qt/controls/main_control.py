from qt.py.main import Ui_LibArchiveWindow
from PySide6 import QtWidgets as qtw


class LibArchiveControl(Ui_LibArchiveWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        super().setupUi(self)
