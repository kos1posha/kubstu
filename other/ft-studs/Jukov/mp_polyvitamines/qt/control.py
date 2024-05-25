import os

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
        for tw in [self.tw_model, self.tw_point]:
            tw.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
            tw.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)

    def connect_ui(self):
        self.pb_clear.clicked.connect(self.clear_output)
        self.pb_task.clicked.connect(self.show_task)
        self.pb_defaults.clicked.connect(self.defaults)
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

    def clear_output(self):
        self.l_extr.setText(f'Стоимость курса: н/д')
        self.l_a.setText(f'Витамин A: н/д')
        self.l_c.setText(f'Витамин C: н/д')
        self.l_b6.setText(f'Витамин B₆: н/д')
        for col in range(7):
            self.tw_point.item(0, col).setText('н/д')

    def defaults(self):
        defaults = [
            [5, 0, 2, 0, 3, 1, 2, 100],
            [3, 1, 5, 0, 2, 0, 1, 80],
            [1, 0, 3, 1, 2, 0, 6, 120],
            [4, 1, 5, 6, 3.5, 7, 4]
        ]
        for row, d_row in enumerate(defaults):
            for col, d in enumerate(d_row):
                self.tw_model.item(row, col).setText(str(d))

    def show_task(self):
        pixmap = qtg.QPixmap(os.path.abspath(r'task.png'))
        label = qtw.QLabel()
        label.setPixmap(pixmap)
        layout = qtw.QHBoxLayout()
        layout.addWidget(label)
        dialog = qtw.QDialog()
        dialog.setLayout(layout)
        dialog.setWindowTitle('Задание')
        dialog.setStyleSheet('background:white')
        dialog.exec()

    def print_output(self, problem):
        self.l_extr.setText(f'Стоимость курса: {problem.objective.value()} тыс. руб.')
        pv_values = [int(constr.value() - constr.constant) for constr in problem.constraints.values()]
        self.l_a.setText(f'Витамин A: {pv_values[0]} гр.')
        self.l_c.setText(f'Витамин C: {pv_values[1]} гр.')
        self.l_b6.setText(f'Витамин B₆: {pv_values[2]} гр.')
        for col, var in enumerate(problem.variables()):
            self.tw_point.item(0, col).setText(str(int(var.value())))
