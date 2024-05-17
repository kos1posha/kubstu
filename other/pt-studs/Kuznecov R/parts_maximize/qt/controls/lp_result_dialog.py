from PySide6 import QtWidgets as qtw
import pulp as pp

from qt.py.lp_result_dialog import Ui_LpResultDialog
import tools as ts


class LpResultDialog(Ui_LpResultDialog, qtw.QDialog):
    def __init__(self, problem, is_main):
        super().__init__()
        self.problem = problem
        self.is_main = is_main
        self.setup_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.l_title.setText(f'Решение {"основной" if self.is_main else "дополнительной"} задачи')
        self.put_data(self.problem)
        self.setMaximumSize(self.size())

    def put_data(self, problem):
        self.l_lp_status.setText(f'&nbsp; {pp.LpStatus[problem.status]} ({problem.status})')
        self.l_extr_value.setText(f'&nbsp; {problem.objective.value()}')
        self.l_extr_point.setText('<br>'.join(ts.xi_to_subscripts(f'&nbsp; {var.name:<2} = {int(var.value())}') for var in problem.variables()))
        self.l_constraints_default.setText('<br>'.join([ts.xi_to_subscripts(f'&nbsp; {constraint}: {int(constraint.value() - constraint.constant)} ({int(constraint.value())})') for name, constraint in problem.constraints.items()][-2:]))
        print(self.l_constraints_default.text())
