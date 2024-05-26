from PySide6 import QtWidgets as qtw, QtGui as qtg

from qt.py.main import Ui_MainWindow
import pulp as pp


def master_gumbs_problem(x):
    a, b, = pp.LpVariable('А', lowBound=0, cat=pp.LpInteger), pp.LpVariable('Б', lowBound=0, cat=pp.LpInteger)
    v, v_cl = pp.LpVariable('В', lowBound=0, cat=pp.LpInteger), pp.LpVariable('Вₓ', lowBound=0, cat=pp.LpInteger)
    objective_func = 25 * a + 20 * b + 50 * v + 30 * v_cl
    constraints = [
        (c1 * a + c2 * b + c3 * v + c4 * v_cl <= x, name)
        for c1, c2, c3, c4, name
        in [(3, 1, 4, 4, 'Потрачено чел/дней на заготовки'),
            (4, 2, 5, 5, 'Потрачено чел/дней на сборку'),
            (5, 5, 4, 0, 'Потрачено чел/дней на покраску')]
    ]
    problem = pp.LpProblem('Мастер Гамбс', sense=pp.LpMaximize)
    problem.setObjective(objective_func)
    for c in constraints:
        problem.addConstraint(*c)
    return problem


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

    def show_result_dialog(self, problem):
        dialog = qtw.QDialog()
        dialog.setWindowTitle('План производства')
        layout = qtw.QVBoxLayout()
        status_label = qtw.QLabel(f'Найдено оптимальное решение при X = {self.demand}')
        result_label = qtw.QLabel(f'Прибыль составит: {int(problem.objective.value()) * 1000:,} руб.')
        variables_labels = [qtw.QLabel(f'Столов модели {var.name}: {int(var.value())}') for var in problem.variables()]
        constraints_labels = [qtw.QLabel(f'{name.replace("_", " ")}:\n{int(constraint.value() - constraint.constant)}, осталось {-int(constraint.value())}') for name, constraint in problem.constraints.items()]
        layout.addWidget(status_label)
        layout.addWidget(result_label)
        for label in variables_labels:
            layout.addWidget(label)
        for label in constraints_labels:
            layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.exec()

    def solve(self):
        if not self.demand:
            self.le_demand.setStyleSheet('background:#ffcccc')
            return self.statusbar.showMessage('Не задано значение запасов чел/дней на текущий месяц', 6000)
        self.le_demand.setStyleSheet('')
        problem = master_gumbs_problem(self.demand)
        problem.solve()
        self.show_result_dialog(problem)
