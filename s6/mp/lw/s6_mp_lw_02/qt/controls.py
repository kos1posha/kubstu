from typing import Callable

from PySide6 import QtGui as qtg, QtWidgets as qtw
from sympy import Eq, Expr, Ge, Le, symbols

from qt.result import Ui_ResultDialog
from qt.view import Ui_StockBuyLpSolverWindow
from simplex import SHK, Search, Simplex


x, y, A, B = symbols('x y A B')
x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 = symbols('x0:10')
y0, y1, y2, y3, y4, y5, y6, y7, y8, y9 = symbols('y0:10')

tasks = {
    'clear': {
        'search': Search.MAX,
        'obj_func': '',
        'constraints': [],
    },
    '1': {
        'search': Search.MAX,
        'obj_func': 60 * x + 80 * y,
        'constraints': [
            0.2 * x + 0.1 * y <= 40,
            0.1 * x + 0.3 * y <= 60,
            1.2 * x + 1.5 * y <= 371.4
        ],
    },
    '3': {
        'search': Search.MAX,
        'obj_func': A + B,
        'constraints': [
            27 * A + 23 * B <= 930,
            A - B >= 10
        ],
    },
    '6': {
        'search': Search.MAX,
        'obj_func': 1.5 * x1 + 1.2 * x2,
        'constraints': [
            50 * x1 + 70 * x2 <= 1020,
            45 * x1 + 25 * x2 <= 500
        ]
    },
    '19': {
        'search': Search.MAX,
        'obj_func': 14 * x1 + 12 * x2 + 5 * x3 + 6 * x4,
        'constraints': [
            0.5 * x1 + 0.5 * x2 <= 290,
            0.5 * x3 + 0.5 * x4 <= 150,
            0.125 * x1 + 0.125 * x4 <= 50,
            2 * x1 + 1 * x2 + 1 * x3 + 1 * x4 <= 1280
        ]
    }
}


class ResultDialog(Ui_ResultDialog, qtw.QDialog):
    def __init__(self, simplex_history=None):
        super().__init__()
        self.setup_ui()
        if simplex_history:
            self.put_result(simplex_history)

    def setup_ui(self):
        super().setupUi(self)

    def split_history(self, simplex_history):
        return simplex_history[SHK.OBJ_FUNC], simplex_history[SHK.SEARCH], simplex_history[SHK.CONSTRAINTS], simplex_history[SHK.POINT], simplex_history[SHK.EXTR], simplex_history[SHK.STATUS], simplex_history[SHK.START_SIMPLEX_TABLE], simplex_history[SHK.ITERS_COUNT], simplex_history[SHK.ITERS]

    def put_result(self, simplex_history):
        tab = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        h3 = lambda text: f'<h3 style="font-style: italic">{text}</h3>'
        p = lambda text: f'<p>{text}</p>'

        def insert_table(table, bv, nbv, highlight=None):
            bv, nbv = bv + ['rhs'], [''] + nbv + ['F']
            if highlight:
                highlight = [h + 1 for h in highlight]

            cursor = self.te_result.textCursor()
            cursor.movePosition(qtg.QTextCursor.MoveOperation.End)
            cursor.insertTable(len(table) + 1, len(table[0]) + 1)

            a_fmt, h_fmt, c_fmt = qtg.QTextBlockFormat(), qtg.QTextBlockFormat(), qtg.QTextBlockFormat()
            h_fmt.setBackground(qtg.QColor.fromRgbF(91, 0, 186, 0.4))
            c_fmt.setBackground(qtg.QColor.fromRgbF(91, 0, 186, 0.8))
            for fmt in [a_fmt, h_fmt, c_fmt]:
                fmt.setAlignment(qtg.Qt.AlignmentFlag.AlignCenter)

            table = [bv] + table
            for i, row in enumerate(table):
                row = [nbv[i]] + row
                for j, value in enumerate(row):
                    if highlight and [i, j] == highlight:
                        cursor.setBlockFormat(c_fmt)
                    elif i == 0 or j == 0:
                        cursor.setBlockFormat(h_fmt)
                    else:
                        cursor.setBlockFormat(a_fmt)
                    cursor.insertText(str(value).center(19))
                    cursor.movePosition(qtg.QTextCursor.MoveOperation.NextCell)

        obj_func, search, constraints, point, extr, status, start_table, iterations_count, iterations = self.split_history(simplex_history)

        search = 'min' if search == Search.MIN else 'max'
        constraints = '<br>'.join([f'{tab}{i}) {c}' for i, c in enumerate(constraints, 1)])
        point = ', '.join([f'{k} = {v}' for k, v in point.items()])
        end_table = iterations[-1]

        self.te_result.insertHtml(h3('Дано'))
        self.te_result.insertHtml(p(
            f'<br>Целевая функция:<br>{tab}{obj_func} → {search}'
            f'<br>Ограничения:<br>{constraints}<br><br>'
        ))
        self.te_result.insertHtml(h3('Результат'))
        self.te_result.insertHtml(p(
            f'<br>Статус решения: {status}'
            f'<br>Точка экстремума: {point}'
            f'<br>Экстремум: {extr}<br><br>'
        ))
        self.te_result.insertHtml(h3('Решение'))
        self.te_result.insertHtml(p(
            f'<br>Количество итераций: {iterations_count}'
            f'<br>Начальная симплекс-таблица:'
        ))
        insert_table(start_table[SHK.ITER_SIMPLEX_TABLE], start_table[SHK.ITER_BASIS_VARS], start_table[SHK.ITER_NONBASIS_VARS])
        self.te_result.insertHtml(p(
            f'<br>Конечная симплекс-таблица:'
        ))
        insert_table(end_table[SHK.ITER_SIMPLEX_TABLE], end_table[SHK.ITER_BASIS_VARS], end_table[SHK.ITER_NONBASIS_VARS])
        self.te_result.insertHtml('<br>' + h3(SHK.ITERS))
        for i in iterations:
            insert_table(i[SHK.ITER_SIMPLEX_TABLE], i[SHK.ITER_BASIS_VARS], i[SHK.ITER_NONBASIS_VARS], i[SHK.ITER_GEN_CELL])


class StockBuyLpSolverControl(Ui_StockBuyLpSolverWindow, qtw.QWidget):
    def __init__(self, show=False):
        super().__init__()
        self.setup_ui()
        self.connect_ui()
        if show:
            self.show()

    def setup_ui(self):
        super().setupUi(self)

    def connect_ui(self):
        self.le_obj_func.textEdited.connect(lambda: self.le_validator(self.le_obj_func, self.validate_obj_func, self.pb_solve))
        self.le_new_constraint.textEdited.connect(lambda: self.le_validator(self.le_new_constraint, self.validate_constraint, self.pb_add_new_constraint))
        self.lw_constraints.currentRowChanged.connect(lambda: self.pb_delete_constraint.setEnabled(self.lw_constraints.currentRow() != -1))
        self.pb_add_new_constraint.clicked.connect(lambda: self.add_new_constraint(self.le_new_constraint.text(), True))
        self.pb_delete_constraint.clicked.connect(lambda: self.lw_constraints.takeItem(self.lw_constraints.currentRow()))
        self.pb_clear.clicked.connect(lambda: self.put_task('clear'))
        self.pb_task1.clicked.connect(lambda: self.put_task('1'))
        self.pb_task3.clicked.connect(lambda: self.put_task('3'))
        self.pb_task6.clicked.connect(lambda: self.put_task('6'))
        self.pb_task19.clicked.connect(lambda: self.put_task('19'))
        self.pb_solve.clicked.connect(self.solve)

    def add_new_constraint(self, constraint_string, clear_le=False):
        constraint = self.validate_constraint(constraint_string)[1]
        if not constraint: return
        self.lw_constraints.addItem(constraint_string)
        if clear_le: self.le_new_constraint.setText('')

    def le_validator(self, le: qtw.QLineEdit, validator: Callable, mutable_button: qtw.QPushButton):
        mutable_button.setEnabled(validator(le.text())[1])

    def validate_obj_func(self, obj_func_string):
        try:
            obj_func = eval(obj_func_string)
            if issubclass(obj_func.__class__, Expr):
                return obj_func, True
        except:
            pass
        return None, False

    def validate_constraint(self, constraint_string):
        try:
            constraint = eval(constraint_string)
            if issubclass(constraint.__class__, (Ge, Le, Eq)):
                return constraint, True
        except:
            pass
        return None, False

    def fetch_data(self):
        return {
            'search': Search.MAX if self.cmb_search.currentIndex() == 0 else Search.MIN,
            'obj_func': self.validate_obj_func(self.le_obj_func.text())[0],
            'constraints': [
                self.validate_constraint(self.lw_constraints.item(r).text())[0] for r in range(self.lw_constraints.count())
            ]
        }

    def put_task(self, task_key):
        task = tasks.get(task_key)
        if task:
            search, obj_func, constraints = task['search'], task['obj_func'], task['constraints']
            self.cmb_search.setCurrentIndex(0 if search == Search.MAX else 1)
            self.le_obj_func.setText(str(obj_func))
            self.lw_constraints.clear()
            self.lw_constraints.insertItems(0, [str(c) for c in constraints])

    def solve(self):
        given = self.fetch_data()
        simplex = Simplex(**given)
        simplex()
        res_dialog = ResultDialog(simplex.history)
        res_dialog.exec()
