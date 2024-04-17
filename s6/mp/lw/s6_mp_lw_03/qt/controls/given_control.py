from pprint import pprint

from PySide6 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw

from qt.ui.given_view import Ui_TransportProblemGivenWindow
from transport import MinCostSolver, NWCSolver, VogelsSolver


class NumericDelegate(qtw.QStyledItemDelegate):
    def __init__(self, table):
        super().__init__()
        self.table = table

    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)
        if isinstance(editor, qtw.QLineEdit):
            validator = qtg.QIntValidator(bottom=1)
            editor.setValidator(validator)
        return editor

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        if (index.column() == self.table.columnCount() - 1) or (index.row() == self.table.rowCount() - 1):
            option.backgroundBrush = qtg.QBrush(qtg.QColor('#242424'))


class TransportProblemGivenControl(Ui_TransportProblemGivenWindow, qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.tw_given.setItemDelegate(NumericDelegate(self.tw_given))
        self.tw_given.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.tw_given.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)

    def connect_ui(self):
        self.pb_supply_add.clicked.connect(self.supply_add)
        self.pb_supply_remove.clicked.connect(self.supply_remove)
        self.pb_demand_add.clicked.connect(self.demand_add)
        self.pb_demand_remove.clicked.connect(self.demand_remove)
        self.pb_solve.clicked.connect(self.solve)

    def solve(self):
        data = self.fetch_data()
        solvers = [MinCostSolver, NWCSolver, VogelsSolver]
        solver = solvers[self.cb_solvers.currentIndex()](**data)
        solution = solver.solve()
        pprint(solution)

    def fetch_data(self):
        rows = self.tw_given.rowCount() - 1
        columns = self.tw_given.columnCount() - 1
        return {
            'costs': [[int(self.tw_given.item(i, j).text()) for j in range(columns)] for i in range(rows)],
            'supply': [int(self.tw_given.item(i, columns).text()) for i in range(rows)],
            'demand': [int(self.tw_given.item(rows, j).text()) for j in range(columns)],
        }

    def supply_add(self):
        row = self.tw_given.rowCount()
        if row == 10:
            return self.sb_main.showMessage('Количество поставщиков не может быть больше девяти.', 2500)

        self.tw_given.insertRow(row - 1)
        self.tw_given.setVerticalHeaderItem(row - 1, qtw.QTableWidgetItem(f'П{row}'))
        for column in range(self.tw_given.columnCount()):
            item = qtw.QTableWidgetItem('1')
            item.setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
            self.tw_given.setItem(row - 1, column, item)
        self.l_supply_count.setText(f'{row}')

    def supply_remove(self):
        row = self.tw_given.rowCount()
        if row == 3:
            return self.sb_main.showMessage('Количество поставщиков не может быть меньше двух.', 2500)

        self.tw_given.removeRow(row - 2)
        self.l_supply_count.setText(f'{row - 2}')

    def demand_add(self):
        column = self.tw_given.columnCount()
        if column == 10:
            return self.sb_main.showMessage('Количество магазинов не может быть больше девяти.', 2500)

        self.tw_given.insertColumn(column - 1)
        self.tw_given.setHorizontalHeaderItem(column - 1, qtw.QTableWidgetItem(f'М{column}'))
        for row in range(self.tw_given.rowCount()):
            item = qtw.QTableWidgetItem('1')
            item.setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
            self.tw_given.setItem(row, column - 1, item)
        self.l_demand_count.setText(f'{column}')

    def demand_remove(self):
        column = self.tw_given.columnCount()
        if column == 3:
            return self.sb_main.showMessage('Количество магазинов не может быть меньше двух.', 2500)

        self.tw_given.removeColumn(column - 2)
        self.l_demand_count.setText(f'{column - 2}')
