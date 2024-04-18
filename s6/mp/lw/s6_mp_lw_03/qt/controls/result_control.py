from copy import deepcopy
import sys

from PySide6 import QtGui as qtg, QtWidgets as qtw

from qt.controls.widgets import TransportTableWidget
from qt.ui.result_view import Ui_ResultWindow
from transport import BaseTransportProblemSolver, MinCostSolver, NWCSolver, VogelsSolver


class ResultControl(Ui_ResultWindow, qtw.QDialog):
    def __init__(self, solver: BaseTransportProblemSolver):
        super().__init__()
        self.setup_ui()
        self.output_iteration = None
        if isinstance(solver, MinCostSolver):
            self.output_iteration = self._mincost_iteration
        elif isinstance(solver, NWCSolver):
            self.output_iteration = self._nwc_iteration
        elif isinstance(solver, VogelsSolver):
            self.output_iteration = self._vogels_iteration
        self.put_data(solver)

    def setup_ui(self):
        super().setupUi(self)

    def put_data(self, solver: BaseTransportProblemSolver):
        costs, supply, demand = deepcopy(solver.given_costs), deepcopy(solver.given_supply), deepcopy(solver.given_demand)
        self.put_given(costs, supply, demand, solver.verbose_name)
        highlight = self.put_iterations(costs, solver._output)
        self.put_result(costs, len(solver._output), solver.calculate_cost(solver._solution), highlight)

    def put_given(self, costs, supply, demand, solver_verbose_name):
        label_text = f'Для поиска оптимального решения используется {solver_verbose_name}.\nТак как общие запасы ({sum(supply)}) равны требованиям ({sum(demand)}) задача сбалансирована и имеет решение.\n'
        w_given = self.create_tab(costs, supply, demand, label_text)[0]
        self.tw_iterations.addTab(w_given, 'Дано')

    def put_iterations(self, costs, iterations):
        highlight = []
        for i, iteration in enumerate(iterations):
            self.output_iteration(costs, i, highlight, **iteration)
        return highlight

    def put_result(self, costs, n, result, highlight):
        costs = [[c if isinstance(c, str) else f'{c}\n[0]' for c in row] for row in costs]
        label_text = f'Опорное решение найдено за {n} шагов.\nНа перевозки будет затрачено {result} у. е. ресурсов.\n'
        w_given = self.create_tab(costs, [0 for _ in range(len(costs))], [0 for _ in range(len(costs[0]))], label_text, highlight, False)[0]
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
            for i, j in highlight[:-1] if last_active else highlight:
                tw_given.item(i, j).setBackground(qtg.QColor(120, 135, 240, 45))
            if last_active:
                tw_given.item(*highlight[-1]).setBackground(qtg.QColor(120, 135, 240, 120))
        return w_given, tw_given

    def _mincost_iteration(self, costs, i, highlight, min_cost, cell, diff, supply, demand):
        current_cost, current_supply, current_demand = costs[cell[0]][cell[1]], supply[cell[0]], demand[cell[1]]
        costs[cell[0]][cell[1]] = f'{current_cost}\n[{diff}]'
        supply[cell[0]], demand[cell[1]] = f'{diff + current_supply} - {diff}\n{current_supply}', f'{diff + current_demand} - {diff}\n{current_demand}'
        label_text = ''.join([f'Наименьшая доступная стоимость равна {min_cost} (П{cell[0] + 1}; М{cell[1] + 1}).\n',
                              f'Из запасов П{cell[0] + 1} перемещено {diff} единиц груза в М{cell[1] + 1}.\n',
                              f'Требования М{cell[1] + 1} полностью удовлетворены. ' if current_demand == 0 else '',
                              f'Запасы П{cell[0] + 1} полностью истощены.' if current_supply == 0 else ''])
        highlight.append(cell)
        w_iteration = self.create_tab(costs, supply, demand, label_text, highlight)[0]
        self.tw_iterations.addTab(w_iteration, f'{i + 1}')

    def _nwc_iteration(self, costs, i, highlight, cell, diff, supply, demand):
        current_cost, current_supply, current_demand = costs[cell[0]][cell[1]], supply[cell[0]], demand[cell[1]]
        costs[cell[0]][cell[1]] = f'{current_cost}\n[{diff}]'
        supply[cell[0]], demand[cell[1]] = f'{diff + current_supply} - {diff}\n{current_supply}', f'{diff + current_demand} - {diff}\n{current_demand}'
        label_text = ''.join([f'Доступный крайний северо-западный элемент находится в ячейке П{cell[0] + 1}; М{cell[1] + 1}.\n',
                              f'Из запасов П{cell[0] + 1} перемещено {diff} единиц груза в М{cell[1] + 1}.\n',
                              f'Требования М{cell[1] + 1} полностью удовлетворены. ' if current_demand == 0 else '',
                              f'Запасы П{cell[0] + 1} полностью истощены.' if current_supply == 0 else ''])
        highlight.append(cell)
        w_iteration = self.create_tab(costs, supply, demand, label_text, highlight)[0]
        self.tw_iterations.addTab(w_iteration, f'{i + 1}')

    def _vogels_iteration(self, costs, i, highlight, cell, diff, supply, demand, min_max, supply_penalties, demand_penalties):
        current_cost, current_supply, current_demand = costs[cell[0]][cell[1]], supply[cell[0]], demand[cell[1]]
        costs[cell[0]][cell[1]] = f'{current_cost}\n[{diff}]'
        supply[cell[0]], demand[cell[1]] = f'{diff + current_supply} - {diff}\n{current_supply}', f'{diff + current_demand} - {diff}\n{current_demand}'
        label_text = ''.join([f'Максимальный штраф: ', f'столбец М{cell[1] + 1}. ' if min_max else f'строка П{cell[0] + 1}. ',
                              f'Минимальная цена: ', f'столбец М{cell[1] + 1}.\n' if not min_max else f'строка П{cell[0] + 1}.\n',
                              f'Из запасов П{cell[0] + 1} перемещено {diff} единиц груза в М{cell[1] + 1}.\n',
                              f'Требования М{cell[1] + 1} полностью удовлетворены. ' if current_demand == 0 else '',
                              f'Запасы П{cell[0] + 1} полностью истощены.' if current_supply == 0 else ''])
        highlight.append(cell)
        w_iteration, tw_given = self.create_tab(costs, supply, demand, label_text, highlight)

        for s_i, s in supply_penalties[0]:
            item = tw_given.verticalHeaderItem(s_i)
            item.setText(f'{item.text()}\n[{s}]')
        for d_j, d in demand_penalties[0]:
            item = tw_given.horizontalHeaderItem(d_j)
            item.setText(f'{item.text()} [{d}]')
        if min_max:
            tw_given.verticalHeaderItem(cell[0]).setForeground(qtg.QColor(51, 153, 255, 255))
            tw_given.horizontalHeaderItem(cell[1]).setForeground(qtg.QColor(255, 102, 102, 255))
        else:
            tw_given.verticalHeaderItem(cell[0]).setForeground(qtg.QColor(255, 102, 102, 255))
            tw_given.horizontalHeaderItem(cell[1]).setForeground(qtg.QColor(51, 153, 255, 255))

        self.tw_iterations.addTab(w_iteration, f'{i + 1}')


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
