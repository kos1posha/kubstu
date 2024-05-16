import sys

from PySide6 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw

from qt.controls.result import ResultControl
from qt.views.main import Ui_MainWindow
from transport import VogelsApproximationTransportProblemSolver


class MainControl(Ui_MainWindow, qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.o_cost = 100
        self.n_cost = 80
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.setup_lineedits()
        self.setup_table()
        self.update_costs(self.o_cost, self.n_cost)

    def connect_ui(self):
        self.pb_ocost_apply.clicked.connect(lambda: (setattr(self, 'o_cost', int(self.le_ocost_value.text())), self.update_costs(self.o_cost, self.n_cost)))
        self.pb_ncost_apply.clicked.connect(lambda: (setattr(self, 'n_cost', int(self.le_ncost_value.text())), self.update_costs(self.o_cost, self.n_cost)))
        self.pb_ocost_cancel.clicked.connect(lambda: self.le_ocost_value.setText(str(self.o_cost)))
        self.pb_ncost_cancel.clicked.connect(lambda: self.le_ncost_value.setText(str(self.n_cost)))
        self.pb_solve.clicked.connect(self.solve)

    def setup_lineedits(self):
        validator = qtg.QIntValidator(bottom=0, top=999)
        self.le_ocost_value.setText(str(self.o_cost))
        self.le_ncost_value.setText(str(self.n_cost))
        self.le_ocost_value.setValidator(validator)
        self.le_ncost_value.setValidator(validator)

    def setup_table(self):
        self.tw_costs.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.tw_costs.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        cells = [
            (0, 0, 1, 2, ' '), (9, 0, 1, 2, 'Спрос'), (0, 7, 1, 1, 'Производство'),
            (0, 2, 1, 1, 'Июнь'), (0, 3, 1, 1, 'Июль'), (0, 4, 1, 1, 'Август'), (0, 5, 1, 1, 'Сентябрь'), (0, 6, 1, 1, 'Фиктивный'),
            (1, 0, 2, 1, 'Июнь'), (1, 1, 1, 1, 'рег.'), (2, 1, 1, 1, 'св.'),
            (3, 0, 2, 1, 'Июль'), (3, 1, 1, 1, 'рег.'), (4, 1, 1, 1, 'св.'),
            (5, 0, 2, 1, 'Август'), (5, 1, 1, 1, 'рег.'), (6, 1, 1, 1, 'св.'),
            (7, 0, 2, 1, 'Сентябрь'), (7, 1, 1, 1, 'рег.'), (8, 1, 1, 1, 'св.'),
        ]
        for row, col, row_span, col_span, text in cells:
            if text in ['руг.', 'св.']: self.tw_costs.horizontalHeader().setSectionResizeMode(col, qtw.QHeaderView.ResizeMode.ResizeToContents)
            self.tw_costs.setSpan(row, col, row_span, col_span)
            item = self._get_table_item(text)
            item.setBackground(qtg.QColor('#e9e9e9'))
            self.tw_costs.setItem(row, col, item)
        for col, demand in enumerate((100, 140, 170, 90, 100), 2):
            self.tw_costs.setItem(9, col, self._get_table_item(demand))
        for row in range(1, 9, 2):
            self.tw_costs.setItem(row, 7, self._get_table_item(125))
            self.tw_costs.setItem(row + 1, 7, self._get_table_item(25))

    def update_costs(self, o_cost, n_cost):
        for row in range(1, 8, 2):
            for col in range(2 + int(row / 2), 7):
                self.tw_costs.setItem(row, col, self._get_table_item(n_cost * (col - 2 - int(row / 2))))
                self.tw_costs.setItem(row + 1, col, self._get_table_item(o_cost + n_cost * (col - 2 - int(row / 2))))

    def _get_table_item(self, value):
        item = qtw.QTableWidgetItem(str(value))
        item.setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        return item

    def solve(self):
        data = self.fetch_data()
        solver = VogelsApproximationTransportProblemSolver(**data)
        solver.solve()
        result = ResultControl(solver)
        result.exec()

    def fetch_data(self):
        def item_data(i, j):
            return int(self.tw_costs.item(i, j).text()) if self.tw_costs.item(i, j) else 1000

        return {
            'costs': [[item_data(i, j) for j in range(2, 7)] for i in range(1, 9)],
            'supply': [item_data(i, 7) for i in range(1, 9)],
            'demand': [item_data(9, j) for j in range(2, 7)],
        }
