from PySide6 import QtGui as qtg, QtWidgets as qtw

from qt.views.parts_maximize import Ui_PartsMaximizeWindow


class PartsMaximizeControl(Ui_PartsMaximizeWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.setup_task_table()

    def setup_task_table(self):
        self.tw_task.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.tw_task.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        for span in [(0, 0, 4, 1), (0, 1, 1, 3), (0, 4, 1, 2), (1, 1, 1, 5), (3, 1, 1, 5)]:
            self.tw_task.setSpan(*span)
        for cell in [(0, 0), (0, 1), (0, 4), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (4, 0), (5, 0), (6, 0)]:
            self.tw_task.item(*cell).setBackground(qtg.QColor(40, 40, 40))

    def connect_ui(self):
        pass
