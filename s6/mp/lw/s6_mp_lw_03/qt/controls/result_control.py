from copy import deepcopy
from typing import Dict, List, Tuple

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

    def setup_ui(self) -> None:
        super().setupUi(self)

    def put_data(self, solver: BaseTransportProblemSolver) -> None:
        costs, supply, demand = deepcopy(solver.given_costs), deepcopy(solver.given_supply), deepcopy(solver.given_demand)
        self.put_given(costs, supply, demand, solver.verbose_name)
        highlight = self.put_iterations(costs, solver._output)
        self.put_result(costs, len(solver._output), solver.calculate_cost(solver._solution), highlight)

    def put_given(self, costs: List[List[int]], supply: List[int], demand: List[int], solver_verbose_name: str) -> None:
        label_text = f'Для поиска оптимального решения используется {solver_verbose_name}.\nТак как общие запасы ({sum(supply)}) равны требованиям ({sum(demand)}) задача сбалансирована и имеет решение.\n'
        w_given = self.create_tab(costs, supply, demand, label_text)[0]
        self.tw_iterations.addTab(w_given, 'Дано')

    def put_iterations(self, costs: List[List[int]], iterations: List[Dict]) -> List[Tuple[int, int]]:
        highlight = []
        for i, iteration in enumerate(iterations):
            self.output_iteration(i, costs, highlight, **iteration)
        return highlight

    def put_result(self, costs: List[List[int]], n: int, result: int, highlight: List[Tuple[int, int]]) -> None:
        costs = [[c if isinstance(c, str) else f'{c}\n[0]' for c in row] for row in costs]
        label_text = f'Опорное решение найдено за {n} шагов.\nНа перевозку груза затрачено {result} у. е. ресурсов.\n'
        w_given = self.create_tab(costs, [0 for _ in range(len(costs))], [0 for _ in range(len(costs[0]))], label_text, highlight, False)[0]
        self.tw_iterations.addTab(w_given, 'Результат')

    def create_tab(self, costs: List[List[int | str]], supply: List[int], demand: List[int], label_text: str, highlight: List[Tuple[int, int]] = None, last_active: bool = True) -> Tuple[qtw.QWidget, TransportTableWidget]:
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

    def _base_iteration(self, label: str, costs: List[List[int | str]], highlight: List[Tuple[int, int]], cell: Tuple[int, int], diff: int, supply: List[int], demand: List[int]):
        current_cost, current_supply, current_demand = costs[cell[0]][cell[1]], supply[cell[0]], demand[cell[1]]
        costs[cell[0]][cell[1]] = f'{current_cost}\n[{diff}]'
        supply[cell[0]], demand[cell[1]] = f'{diff + current_supply} - {diff}\n{current_supply}', f'{diff + current_demand} - {diff}\n{current_demand}'
        label_text = ''.join([label, '\n',
                              f'Из запасов П{cell[0] + 1} перемещено {diff} единиц груза в М{cell[1] + 1}.\n',
                              f'Требования М{cell[1] + 1} полностью удовлетворены. ' if current_demand == 0 else '',
                              f'Запасы П{cell[0] + 1} полностью истощены.' if current_supply == 0 else ''])
        highlight.append(cell)
        return self.create_tab(costs, supply, demand, label_text, highlight)

    def _mincost_iteration(self, i: int, costs: List[List[int | str]], highlight: List[Tuple[int, int]], cell: Tuple[int, int], diff: int, supply: List[int], demand: List[int], min_cost: int) -> None:
        label = f'Наименьшая доступная стоимость равна {min_cost} и находится в ячейке П{cell[0] + 1}:М{cell[1] + 1}.'
        w, tw = self._base_iteration(label, costs, highlight, cell, diff, supply, demand)
        self.tw_iterations.addTab(w, f'{i + 1}')

    def _nwc_iteration(self, i: int, costs: List[List[int | str]], highlight: List[Tuple[int, int]], cell: Tuple[int, int], diff: int, supply: List[int], demand: List[int], ):
        label = f'Крайний доступный северо-западный элемент находится в ячейке П{cell[0] + 1}:М{cell[1] + 1}.'
        w, tw = self._base_iteration(label, costs, highlight, cell, diff, supply, demand)
        self.tw_iterations.addTab(w, f'{i + 1}')

    def _vogels_iteration(self, i: int, costs: List[List[int | str]], highlight: List[Tuple[int, int]], cell: Tuple[int, int], diff: int, supply: List[int], demand: List[int], min_max: bool, supply_penalties: List[int], demand_penalties: List[int]) -> None:
        max_penalty = f'столбец М{cell[1] + 1}' if min_max else f'строка П{cell[0] + 1}'
        min_cost = f'столбец М{cell[1] + 1}' if not min_max else f'строка П{cell[0] + 1}'
        label = f'Максимальный штраф: {max_penalty}. Минимальная цена: {min_cost}.'
        w, tw = self._base_iteration(label, costs, highlight, cell, diff, supply, demand)

        for s_i, s in supply_penalties:
            item = tw.verticalHeaderItem(s_i)
            item.setText(f'{item.text()}\n[{s}]')
        for d_j, d in demand_penalties:
            item = tw.horizontalHeaderItem(d_j)
            item.setText(f'{item.text()} [{d}]')
        v_color, h_color = (qtg.QColor(51, 153, 255, 255), qtg.QColor(255, 102, 102, 255)) if min_max else (qtg.QColor(255, 102, 102, 255), qtg.QColor(51, 153, 255, 255))
        tw.verticalHeaderItem(cell[0]).setForeground(v_color)
        tw.horizontalHeaderItem(cell[1]).setForeground(h_color)

        self.tw_iterations.addTab(w, f'{i + 1}')
