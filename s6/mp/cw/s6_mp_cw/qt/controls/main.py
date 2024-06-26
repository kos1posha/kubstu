from typing import Union, Optional

from PySide6 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc

from qt.controls.long_term_result import LongTermResultDialog
from qt.controls.one_off_result import OneOffResultDialog
from qt.py.main import Ui_MainWindow
from solution import master_gumbs_problem, big_master_gumbs_problem


class NumericDelegate(qtw.QStyledItemDelegate):
    def __init__(self, table: qtw.QTableWidget):
        super().__init__()
        self.table = table

    def createEditor(self, parent: qtw.QWidget, option: qtw.QStyleOptionViewItem, index: Union[qtc.QModelIndex, qtc.QPersistentModelIndex]) -> qtw.QWidget:
        editor = super().createEditor(parent, option, index)
        if isinstance(editor, qtw.QLineEdit):
            validator = qtg.QIntValidator(bottom=1)
            editor.setValidator(validator)
        return editor


class MrGumbsControl(Ui_MainWindow, qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.supply = 0
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self) -> None:
        super().setupUi(self)
        self.tw_model.setItemDelegate(NumericDelegate(self.tw_model))
        for header in [self.tw_model.horizontalHeader(), self.tw_model.verticalHeader()]:
            header.setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)

        pos_validator = qtg.QIntValidator(bottom=0)
        validator = qtg.QIntValidator()
        self.le_oo_supply.setValidator(pos_validator)
        self.le_lt_supply.setValidator(pos_validator)
        self.le_lt_step.setValidator(validator)
        self.le_lt_period.setValidator(pos_validator)

    def connect_ui(self) -> None:
        self.le_oo_supply.textChanged.connect(lambda: self.le_oo_supply.setStyleSheet(''))
        self.le_lt_supply.textChanged.connect(lambda: self.le_lt_supply.setStyleSheet(''))
        self.le_lt_step.textChanged.connect(lambda: self.le_lt_step.setStyleSheet(''))
        self.le_lt_period.textChanged.connect(lambda: self.le_lt_period.setStyleSheet(''))
        self.pb_oo_solve.clicked.connect(self.find_one_off_plan)
        self.pb_lt_solve.clicked.connect(self.find_long_term_plan)
        self.tw_model.itemChanged.connect(self.tw_model_item_changed)

    def tw_model_item_changed(self, item: qtw.QTableWidgetItem) -> None:
        if item is self.tw_model.item(2, 0):
            self.tw_model.item(3, 0).setText(item.text())
        elif item is self.tw_model.item(2, 1):
            self.tw_model.item(3, 1).setText(item.text())

    def fetch_obj_func(self) -> list[int]:
        rows = self.tw_model.rowCount()
        return [int(self.tw_model.item(row, 3).text()) for row in range(rows)]

    def fetch_constraints(self) -> list[list[int]]:
        rows = self.tw_model.rowCount()
        columns = self.tw_model.columnCount()
        return [
            [int(self.tw_model.item(row, column).text() or 0) for row in range(rows)]
            for column in range(columns)
        ]

    def fetch_oo_data(self) -> Optional[tuple]:
        supply = self.le_oo_supply.text()
        if not supply:
            self.le_oo_supply.setStyleSheet('color:red')
            return self.statusbar.showMessage('Введите запасы на производство', 6500)
        return self.fetch_obj_func(), self.fetch_constraints(), int(supply)

    def fetch_lt_data(self) -> Optional[tuple]:
        supply_step_period = []
        for line_edit in (self.le_lt_supply, self.le_lt_step, self.le_lt_period):
            text = line_edit.text()
            if not text:
                line_edit.setStyleSheet('color:red')
                continue
            supply_step_period.append(int(text))

        if len(supply_step_period) != 3:
            return self.statusbar.showMessage('Для поиска плана заполните все поля', 6500)
        return self.fetch_obj_func(), self.fetch_constraints(), *supply_step_period

    def find_one_off_plan(self) -> None:
        data = self.fetch_oo_data()
        if not data: return
        problem = master_gumbs_problem(*data)
        if problem.status != 1:
            return self.statusbar.showMessage('Оптимальное решение не найдено...', 6000)

        result_dialog = OneOffResultDialog(
            stonks=int(problem.objective.value()),
            supply=data[2],
            plan=[int(var.value()) for var in problem.variables()],
            remains=[-int(constraint.value()) for constraint in problem.constraints.values()]
        )
        result_dialog.exec()

    def find_long_term_plan(self) -> None:
        data = self.fetch_lt_data()
        if not data: return
        problems = big_master_gumbs_problem(*data)

        plans = [
            {
                'stonks': int(problem.objective.value()),
                'supply': data[2] + data[3] * i,
                'plan': [int(var.value()) for var in problem.variables()],
                'remains': [-int(constraint.value()) for constraint in problem.constraints.values()]
            }
            for i, problem in enumerate(problems)
        ]

        result_dialog = LongTermResultDialog(plans)
        result_dialog.exec()
