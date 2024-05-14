from PySide6 import QtGui as qtg, QtWidgets as qtw
import pulp as pp

import pulp_solution as pps
from qt.views.parts_maximize import Ui_PartsMaximizeWindow
import tools as ts


x1 = pp.LpVariable(name='x1', lowBound=0, cat=pp.LpInteger)
x2 = pp.LpVariable(name='x2', lowBound=0, cat=pp.LpInteger)
x3 = pp.LpVariable(name='x3', lowBound=0, cat=pp.LpInteger)
x4 = pp.LpVariable(name='x4', lowBound=0, cat=pp.LpInteger)
x5 = pp.LpVariable(name='x5', lowBound=0, cat=pp.LpInteger)


class NumericDelegate(qtw.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)
        if isinstance(editor, qtw.QLineEdit):
            validator = qtg.QDoubleValidator(bottom=0)
            validator.setNotation(qtg.QDoubleValidator.Notation.StandardNotation)
            editor.setValidator(validator)
        return editor


class PartsMaximizeControl(Ui_PartsMaximizeWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.setup_task_table()
        self.tw_task_args_changed()

    def connect_ui(self):
        pass

    def setup_task_table(self):
        self.tw_task_args.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.tw_task_args.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        for span in [(0, 0, 4, 1), (0, 1, 1, 3), (0, 4, 1, 2), (1, 1, 1, 5), (3, 1, 1, 5)]:
            self.tw_task_args.setSpan(*span)
        for cell in [(0, 0), (0, 1), (0, 4), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (4, 0), (5, 0), (6, 0)]:
            self.tw_task_args.item(*cell).setBackground(qtg.QColor(40, 40, 40))
        self.tw_task_args.setItemDelegate(NumericDelegate())
        self.tw_task_args.itemChanged.connect(self.tw_task_args_changed)

    def tw_task_args_changed(self):
        c_exprs = self.get_tw_task_exprs()
        l_defs = [self.l_obj_func_def_1, self.l_obj_func_def_2, self.l_obj_func_def_3]
        l_constrs = [self.l_constraints_details_1, self.l_constraints_details_2, self.l_constraints_details_3]
        l_lp_constrs = [self.l_lp_constraints_details_1, self.l_lp_constraints_details_2, self.l_lp_constraints_details_3]
        l_lpa_constrs = [self.l_lpa_constraints_details_1, self.l_lpa_constraints_details_2, self.l_lpa_constraints_details_3]
        self.l_lp_obj_func.setText(ts.xi_to_subscripts(f'&nbsp; F(x1, x2, x3, x4, x5) = {c_exprs[0]}').replace('*', ''))
        self.l_lpa_obj_func.setText(ts.xi_to_subscripts(f'&nbsp; F(x1, x2, x3, x4, x5) = {c_exprs[0]}').replace('*', ''))
        for l_def, c_expr in zip(l_defs, c_exprs):
            l_def.setText(ts.xi_to_subscripts(f'&nbsp; F(x1, x2, x3, x4, x5) = {c_expr}').replace('*', ''))
        for l_constr, l_lp_constr, c_expr, c_expr_next, ds, ds_next in zip(l_constrs, l_lp_constrs, c_exprs, ts.shift_prev(c_exprs), pps.details_set, ts.shift_prev(pps.details_set)):
            text = ts.xi_to_subscripts(f'&nbsp; {ds_next}({c_expr}) = {ds}({c_expr_next})').replace('*', '')
            l_constr.setText(text)
            l_lp_constr.setText(text)
        for l_lpa_constr, c_expr, c_expr_next, ds, ds_next in zip(l_lpa_constrs, c_exprs, ts.shift_prev(c_exprs), (4, 3, 3), ts.shift_prev((4, 3, 3))):
            text = ts.xi_to_subscripts(f'&nbsp; {ds_next}({c_expr}) = {ds}({c_expr_next})').replace('*', '')
            l_lpa_constr.setText(text)

    def get_tw_task_args(self):
        c1_args, c2_args, c3_args = [[ts.num(self.tw_task_args.item(row, column).text()) for column in range(1, 6)] for row in range(4, 7)]
        return c1_args, c2_args, c3_args

    def get_tw_task_exprs(self):
        c1_args, c2_args, c3_args = self.get_tw_task_args()
        c1, c2, c3 = pps.get_expr(*c1_args), pps.get_expr(*c2_args), pps.get_expr(*c3_args)
        return c1, c2, c3
