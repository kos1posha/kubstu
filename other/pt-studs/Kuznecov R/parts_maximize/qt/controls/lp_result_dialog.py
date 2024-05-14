from PySide6 import QtWidgets as qtw
import pulp as pp

from qt.views.lp_result_dialog import Ui_LpResultDialog


def ss(problem):
    '\n'.join([
        f'Статус: {pp.LpStatus[problem.status]} ({problem.status})',
        f'Результат: {problem.objective.value()}',
        *[f'{var.name:<2} = {int(var.value())}' for var in problem.variables()],
        *[f'{constraint}: {int(constraint.value() - constraint.constant)} ({int(constraint.value())})' for name, constraint in problem.constraints.items()],
    ])


class LpResultDialog(Ui_LpResultDialog, qtw.QDialog):
    def __init__(self, problem):
        super().__init__()
        self.setup_ui()
        self.put_data(problem)

    def setup_ui(self):
        super().setupUi(self)

    def put_data(self, problem):
        self.l_lp_status.setText(f'{pp.LpStatus[problem.status]} ({problem.status})')
        self.l_extr_value.setText(f'{problem.objective.value()}')
        self.l_extr_point.setText('\n'.join(f'{var.name:<2} = {int(var.value())}' for var in problem.variables()))
        self.l_constraints_default.setText('\n'.join(f'{constraint}: {int(constraint.value() - constraint.constant)} ({int(constraint.value())})' for name, constraint in problem.constraints.items()))
