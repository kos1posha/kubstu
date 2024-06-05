from qt.controls.one_off_result import OneOffResultDialog
from qt.py.long_term_result import Ui_LongTermResultDialog
from PySide6 import QtWidgets as qtw


class LongTermResultDialog(Ui_LongTermResultDialog, qtw.QDialog):
    def __init__(self, plans: list[dict]):
        super().__init__()
        self.setup_ui()
        self.put_result(plans)

    def setup_ui(self):
        super().setupUi(self)

    def put_result(self, plans: list[dict]) -> None:
        for i, plan in enumerate(plans, 1):
            oo_result = OneOffResultDialog(**plan)
            self.tabw_plans.addTab(oo_result, str(i))
