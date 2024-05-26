from typing import Dict, List

from PySide6 import QtWidgets as qtw

from qt.controls.result_control import ResultControl
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

    def setup_ui(self) -> None:
        super().setupUi(self)
        self.tw_given.setSizePolicy(qtw.QSizePolicy.Policy.Expanding, qtw.QSizePolicy.Policy.Expanding)
        self.vl_main.insertWidget(2, self.tw_given)

    def connect_ui(self) -> None:
        self.pb_supply_add.clicked.connect(self.supply_add)
        self.pb_supply_remove.clicked.connect(self.supply_remove)
        self.pb_demand_add.clicked.connect(self.demand_add)
        self.pb_demand_remove.clicked.connect(self.demand_remove)
        self.pb_solve.clicked.connect(self.solve)

    def solve(self) -> None:
        data = self.fetch_data()
        solvers = [MinCostSolver, NWCSolver, VogelsSolver]
        try:
            solver = solvers[self.cb_solvers.currentIndex()](**data)
        except NotImplementedError:
            return self.sb_main.showMessage(f'Общее количество груза ({sum(data["supply"])}) должно быть равно сумме всех требований ({sum(data["demand"])}).', 4000)
        solver.solve()
        result = ResultControl(solver)
        result.exec()

    def fetch_data(self) -> Dict:
        rows = self.tw_given.rowCount() - 1
        columns = self.tw_given.columnCount() - 1
        return {
            'costs': [[int(self.tw_given.item(i, j).text()) for j in range(columns)] for i in range(rows)],
            'supply': [int(self.tw_given.item(i, columns).text()) for i in range(rows)],
            'demand': [int(self.tw_given.item(rows, j).text()) for j in range(columns)],
        }

    def put_data(self, costs: List[List[int]], supply: List[int], demand: List[int]) -> None:
        self.costs, self.supply, self.demand = costs, supply, demand
        self.tw_given.put_data(costs, supply, demand)
        self.l_supply_count.setText(str(len(supply)))
        self.l_demand_count.setText(str(len(demand)))

    def update_data(self):
        data = self.fetch_data()
        self.costs = data['costs']
        self.supply = data['supply']
        self.demand = data['demand']

    def supply_add(self) -> None:
        row = self.tw_given.rowCount()
        if row == 10:
            return self.sb_main.showMessage('Количество поставщиков не может быть больше девяти.', 2500)

        self.update_data()
        self.costs.append([1 for _ in range(len(self.demand))])
        self.supply.append(1)
        self.put_data(self.costs, self.supply, self.demand)

    def supply_remove(self) -> None:
        row = self.tw_given.rowCount()
        if row == 3:
            return self.sb_main.showMessage('Количество поставщиков не может быть меньше двух.', 2500)

        self.update_data()
        self.costs.pop()
        self.supply.pop()
        self.put_data(self.costs, self.supply, self.demand)

    def demand_add(self) -> None:
        column = self.tw_given.columnCount()
        if column == 10:
            return self.sb_main.showMessage('Количество магазинов не может быть больше девяти.', 2500)

        self.update_data()
        [row.append(1) for row in self.costs]
        self.demand.append(1)
        self.put_data(self.costs, self.supply, self.demand)

    def demand_remove(self) -> None:
        column = self.tw_given.columnCount()
        if column == 3:
            return self.sb_main.showMessage('Количество магазинов не может быть меньше двух.', 2500)

        self.update_data()
        [row.pop() for row in self.costs]
        self.demand.pop()
        self.put_data(self.costs, self.supply, self.demand)
