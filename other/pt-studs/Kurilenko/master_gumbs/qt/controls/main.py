from PySide6 import QtWidgets as qtw, QtGui as qtg

from qt.py.main import Ui_MainWindow


class MrGumbsControl(Ui_MainWindow, qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.demand = 0
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        validator = qtg.QIntValidator(bottom=0)
        self.le_demand.setValidator(validator)
        for header in [self.tw_model.horizontalHeader(), self.tw_model.verticalHeader()]:
            header.setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
            header.setStyleSheet('background:#f8f8f8')
        for row in range(5):
            self.tw_model.item(row, 0).setBackground(qtg.QColor('#f8f8f8'))

    def connect_ui(self):
        self.pb_apply.clicked.connect(self.apply_demand)
        self.pb_solve.clicked.connect(self.solve)

    def apply_demand(self):
        if not self.le_demand.text() or self.le_demand.text() == self.demand:
            self.le_demand.setStyleSheet('background:#ffcccc')
            return self.statusbar.showMessage('Введите значение', 6000)
        self.le_demand.setStyleSheet('')
        self.demand = int(self.le_demand.text())
        for col in range(1, 4):
            self.tw_model.item(4, col).setText(self.le_demand.text())

    def solve(self):
        if not self.demand:
            self.le_demand.setStyleSheet('background:#ffcccc')
            return self.statusbar.showMessage('Не задано значение запасов чел/дней на текущий месяц', 6000)
        self.le_demand.setStyleSheet('')
