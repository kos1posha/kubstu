import os.path

from PySide6 import QtGui as qtg, QtWidgets as qtw

import pulp_solution as pps
from qt.py.given import Ui_GivenWindow


class GivenControl(Ui_GivenWindow, qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.d1_xs = []
        self.d2_xs = []
        self.setup_ui()
        self.put_default_values()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.centralwidget.setFocus()
        self.d1_xs = [self.le_d1_x1, self.le_d1_x2, self.le_d1_x3, self.le_d1_x4, self.le_d1_x5, self.le_d1_x6]
        self.d2_xs = [self.le_d2_x1, self.le_d2_x2, self.le_d2_x3, self.le_d2_x4, self.le_d2_x5, self.le_d2_x6]
        validator = qtg.QIntValidator(bottom=0)
        for le in self.d1_xs + self.d2_xs + [self.le_t1_rhs]:
            le.setValidator(validator)

    def connect_ui(self):
        for le in self.d1_xs + self.d2_xs + [self.le_t1_rhs, self.le_t2_rhs]:
            le.textChanged.connect(self.fetch_data)
        self.a_find_solution.triggered.connect(self.solve)
        self.a_put_task.triggered.connect(self.put_default_values)
        self.a_show_task.triggered.connect(self.show_task)

    def fetch_data(self):
        correct = True
        d1_args, d2_args, ts = [], [], []
        for args, xs in [(d1_args, self.d1_xs), (d2_args, self.d2_xs), (ts, [self.le_t1_rhs, self.le_t2_rhs])]:
            for le in xs:
                arg = le.text()
                if arg == '':
                    le.setStyleSheet('background:rgba(255,150,150,0.8)')
                    correct = False
                else:
                    le.setStyleSheet('')
                    args.append(int(arg))
        if not correct:
            self.statusbar.showMessage('Заполните поля', 2500)
            return None
        return d1_args, d2_args, ts[0], ts[1]

    def put_default_values(self):
        for le, arg in zip(self.d1_xs, pps.default_d1_args):
            le.setText(str(arg))
        for le, arg in zip(self.d2_xs, pps.default_d2_args):
            le.setText(str(arg))

    def solve(self):
        data = self.fetch_data()
        if not data: return
        d1_args, d2_args, t1, t2 = data
        problem = pps.fabric_lp_task(t1=t1, t2=t2, d1_args=d1_args, d2_args=d2_args)
        problem.solve()
        t = '     '
        output = '\n'.join([
            f'Результат:',
            f'{t}{int(problem.objective.value())}',
            f'Переменные:',
            *[f'{t}{var.name:<2} = {int(var.value())}' for var in problem.variables()],
            f'Ограничения:',
            *[f'{t}{constraint}\n{t}{t}LHS: {int(constraint.value() - constraint.constant)}' for name, constraint in problem.constraints.items()][1:],
        ])
        msg = qtw.QMessageBox(qtw.QMessageBox.Icon.Information, 'Результат', output, qtw.QMessageBox.StandardButton.NoButton)
        msg.exec()

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
