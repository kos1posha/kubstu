from copy import deepcopy
import sys

from PySide6 import QtGui as qtg, QtWidgets as qtw

from qt.controls.widgets import TransportTableWidget
from qt.ui.result_view import Ui_ResultWindow
from transport import BaseTransportProblemSolver, MinCostSolver


class ResultControl(Ui_ResultWindow, qtw.QDialog):
    def __init__(self, solver: BaseTransportProblemSolver):
        super().__init__()
        self.setup_ui()
        self.put_data(solver)

    def setup_ui(self):
        super().setupUi(self)

    def put_data(self, solver: BaseTransportProblemSolver):
        costs, supply, demand = deepcopy(solver.given_costs), deepcopy(solver.given_supply), deepcopy(solver.given_demand)
        self.put_given(costs, supply, demand, solver.verbose_name.lower())
        highlight = self.put_iterations(costs, solver._output)
        self.put_result(costs, len(solver._output), solver.calculate_cost(solver._solution), highlight)

    def put_given(self, costs, supply, demand, solver_verbose_name):
        label_text = f'Для поиска оптимального решения использовался {solver_verbose_name}.\nТак как общие запасы ({sum(supply)}) равны требованиям ({sum(demand)}) задача сбалансирована и имеет решение.\n'
        w_given = self.create_tab(costs, supply, demand, label_text)
        self.tw_iterations.addTab(w_given, 'Дано')

    def put_iterations(self, costs, iterations):
        highlight = []
        for i, r in enumerate(iterations):
            min_cost, cell, diff, supply, demand = r['min_cost'], r['cell'], r['diff'], r['supply'], r['demand']
            current_cost, current_supply, current_demand = costs[cell[0]][cell[1]], supply[cell[0]], demand[cell[1]]
            costs[cell[0]][cell[1]] = f'{current_cost}\n[{diff}]'
            supply[cell[0]], demand[cell[1]] = f'{diff + current_supply} - {diff}\n{current_supply}', f'{diff + current_demand} - {diff}\n{current_demand}'
            label_text = ''.join([f'Наименьшая доступная стоимость равна {min_cost} (П{cell[0] + 1}; М{cell[1] + 1}).\n',
                                  f'Из запасов П{cell[0] + 1} перемещено {diff} единиц груза в М{cell[1] + 1}.\n',
                                  f'Запасы П{cell[0] + 1} полностью истощены. ' if current_supply == 0 else '',
                                  f'Требования М{cell[1] + 1} полностью удовлетворены.' if current_demand == 0 else ''])
            highlight.append(cell)
            w_iteration = self.create_tab(costs, supply, demand, label_text, highlight)
            self.tw_iterations.addTab(w_iteration, f'{i + 1}')
        return highlight

    def put_result(self, costs, n, result, highlight):
        costs = [[c if isinstance(c, str) else f'{c}\n[0]' for c in row] for row in costs]
        label_text = f'Опорное решение найдено за {n} шагов.\nНа перевозки будет затрачено {result} у. е. ресурсов.\n'
        w_given = self.create_tab(costs, [0 for _ in range(len(costs))], [0 for _ in range(len(costs[0]))], label_text, highlight, False)
        self.tw_iterations.addTab(w_given, 'Результат')

    def create_tab(self, costs, supply, demand, label_text, highlight=None, last_active=True):
        highlight = highlight or []
        tw_given = TransportTableWidget(costs, supply, demand, True)
        tw_given.setEditTriggers(qtw.QAbstractItemView.EditTrigger.NoEditTriggers)
        l_given = qtw.QLabel(label_text)
        vl_given = qtw.QVBoxLayout()
        vl_given.setContentsMargins(0, 0, 0, 0)
        vl_given.addWidget(tw_given)
        vl_given.addWidget(l_given)
        w_given = qtw.QWidget()
        w_given.setLayout(vl_given)
        if highlight:
            for i, j in highlight[:-1]:
                tw_given.item(i, j).setBackground(qtg.QColor(120, 135, 240, 45))
            if last_active:
                tw_given.item(*highlight[-1]).setBackground(qtg.QColor(120, 135, 240, 120))
        return w_given


if __name__ == '__main__':
    solver = MinCostSolver(**{
        'costs': [
            [3, 5, 7, 2, 8],
            [6, 5, 6, 8, 7],
            [9, 1, 2, 4, 6],
            [3, 5, 8, 9, 6]
        ],
        'supply': [500, 400, 800, 500],
        'demand': [300, 500, 500, 600, 300],
    })
    result = solver.solve()
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    control = ResultControl(solver)
    control.exec()
    status = app.exec()
    sys.exit(status)
