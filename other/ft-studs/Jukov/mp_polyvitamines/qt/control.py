from PySide6 import QtGui as qtg, QtWidgets as qtw

import lpp
from qt.view import Ui_VitaminsLpSolverWindow


class NumericDelegate(qtw.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)
        if isinstance(editor, qtw.QLineEdit):
            validator = qtg.QDoubleValidator(bottom=0)
            validator.setNotation(qtg.QDoubleValidator.Notation.StandardNotation)
            editor.setValidator(validator)
        return editor


class VitaminsLpSolverControl(Ui_VitaminsLpSolverWindow, qtw.QWidget):
    def __init__(self, show=False):
        super().__init__()
        self.setup_ui()
        self.connect_ui()
        if show:
            self.show()

    def setup_ui(self):
        super().setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.tw_model.setItemDelegate(NumericDelegate(self.tw_model))
        self.tw_model.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Fixed)
        self.tw_model.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Fixed)

    def connect_ui(self):
        self.pb_solve.clicked.connect(self.test)

    def get_tw_row(self, row):
        tw_row = []
        for column in range(self.tw_model.columnCount()):
            try:
                tw_row.append(float(self.tw_model.item(row, column).text().replace(',', '.')))
            except:
                pass
        return tw_row

    def fetch_data(self):
        data = []
        for row in range(self.tw_model.rowCount()):
            data.append(self.get_tw_row(row))
        return data

    def test(self):
        a, c, b6, p = self.fetch_data()
        problem = lpp.vit_solve(a, c, b6, p)
        self.print_output(problem)

    def print_output(self, problem):
        self.te_output.clear()
        self.te_output.insertPlainText(f'Статус: {"Оптимальный" if problem.status == 1 else "Нет решения"}\nРезультат: {problem.objective.value()}\nЗначения переменных:')
        cursor = self.te_output.textCursor()
        cursor.insertTable(2, 7)
        for c in ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']:
            cursor.insertText(f'  {c}  ')
            cursor.movePosition(qtg.QTextCursor.MoveOperation.NextCell)
        for var in problem.variables():
            cursor.insertText(f'  {int(var.value()):>2}  ')
            cursor.movePosition(qtg.QTextCursor.MoveOperation.NextCell)
        constraints = '\n'.join(f'{name:<2} = {int(constraint.value() - constraint.constant)} ({int(constraint.value())})' for name, constraint in problem.constraints.items())
        self.te_output.insertPlainText(f'Ограничения:\n{constraints}')
