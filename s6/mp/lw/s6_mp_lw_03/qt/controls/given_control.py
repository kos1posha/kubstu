from pprint import pprint
from typing import List

from PySide6 import QtWidgets as qtw

from qt.controls.widgets import TransportTableWidget
from qt.ui.given_view import Ui_TransportProblemGivenWindow
from transport import MinCostSolver, NWCSolver, VogelsSolver


class TransportProblemGivenControl(Ui_TransportProblemGivenWindow, qtw.QMainWindow):
    def __init__(self, costs: List[List[int]], supply: List[int], demand: List[int]):
        super().__init__()
        self.costs, self.supply, self.demand = costs, supply, demand
        self.tw_given = TransportTableWidget(costs, supply, demand)

        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.tw_given.setSizePolicy(qtw.QSizePolicy.Policy.Expanding, qtw.QSizePolicy.Policy.Expanding)
        self.vl_main.insertWidget(2, self.tw_given)

    def connect_ui(self):
        self.pb_supply_add.clicked.connect(self.supply_add)
        self.pb_supply_remove.clicked.connect(self.supply_remove)
        self.pb_demand_add.clicked.connect(self.demand_add)
        self.pb_demand_remove.clicked.connect(self.demand_remove)
        self.pb_solve.clicked.connect(self.solve)

    def solve(self):
        data = self.fetch_data()
        solvers = [MinCostSolver, NWCSolver, VogelsSolver]
        solver = solvers[self.cb_solvers.currentIndex()](**data)
        solution = solver.solve()
        pprint(solution)

    def fetch_data(self):
        rows = self.tw_given.rowCount() - 1
        columns = self.tw_given.columnCount() - 1
        return {
            'costs': [[int(self.tw_given.item(i, j).text()) for j in range(columns)] for i in range(rows)],
            'supply': [int(self.tw_given.item(i, columns).text()) for i in range(rows)],
            'demand': [int(self.tw_given.item(rows, j).text()) for j in range(columns)],
        }

    def put_data(self, costs, supply, demand):
        self.costs, self.supply, self.demand = costs, supply, demand
        self.tw_given.put_data(costs, supply, demand)
        self.l_supply_count.setText(str(len(supply)))
        self.l_demand_count.setText(str(len(demand)))

    def supply_add(self):
        row = self.tw_given.rowCount()
        if row == 10:
            return self.sb_main.showMessage('Количество поставщиков не может быть больше девяти.', 2500)

        self.costs.append([1 for _ in range(len(self.demand))])
        self.supply.append(1)
        self.put_data(self.costs, self.supply, self.demand)

    def supply_remove(self):
        row = self.tw_given.rowCount()
        if row == 3:
            return self.sb_main.showMessage('Количество поставщиков не может быть меньше двух.', 2500)

        self.costs.pop()
        self.supply.pop()
        self.put_data(self.costs, self.supply, self.demand)

    def demand_add(self):
        column = self.tw_given.columnCount()
        if column == 10:
            return self.sb_main.showMessage('Количество магазинов не может быть больше девяти.', 2500)

        [row.append(1) for row in self.costs]
        self.demand.append(1)
        self.put_data(self.costs, self.supply, self.demand)

    def demand_remove(self):
        column = self.tw_given.columnCount()
        if column == 3:
            return self.sb_main.showMessage('Количество магазинов не может быть меньше двух.', 2500)

        [row.pop() for row in self.costs]
        self.demand.pop()
        self.put_data(self.costs, self.supply, self.demand)
