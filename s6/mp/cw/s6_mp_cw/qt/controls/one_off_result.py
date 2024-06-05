from qt.py.one_off_result import Ui_OneOffResultDialog
from PySide6 import QtWidgets as qtw


class OneOffResultDialog(Ui_OneOffResultDialog, qtw.QDialog):
    def __init__(self, supply: int, stonks: int, plan: list[int], remains: list[int]):
        super().__init__()
        self.setup_ui()
        self.l_remains_list = [
            self.l_remains_blank_value,
            self.l_remains_building_value,
            self.l_remains_painting_value
        ]
        self.put_result(supply, stonks, plan, remains)

    def setup_ui(self):
        super().setupUi(self)
        self.tw_plan.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.tw_plan.verticalHeader().setStretchLastSection(True)

    def put_result(self, supply: int, stonks: int, plan: list[int], remains: list[int]) -> None:
        self.le_supply.setText(f'{supply}')
        self.l_stonks_value.setText(f'{stonks} тыс. рублей')
        for i, p in enumerate(plan):
            self.tw_plan.item(0, i).setText(str(p))
        for i, r in enumerate(remains):
            self.l_remains_list[i].setText(str(r))
