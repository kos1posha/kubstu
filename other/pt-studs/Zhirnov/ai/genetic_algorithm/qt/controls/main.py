from PySide6 import QtWidgets as qtw
import sympy as sp

from qt.controls.plot_widget import GeneticAlgorithmPlotWidget
from qt.py.main import Ui_GeneticAlgorithmForm
import genetic as g


class GeneticAlgorithmControl(Ui_GeneticAlgorithmForm, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.w_plot = GeneticAlgorithmPlotWidget()
        self.g_iterator = None
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.setFixedSize(self.sizeHint().width(), self.sizeHint().height())

    def connect_ui(self):
        self.le_function.textChanged.connect(self.validate_function)
        self.pb_start.clicked.connect(self.start_genetic_algorithm)
        self.pb_next_iter.clicked.connect(self.next_iteration)

    def validate_function(self):
        try:
            expr = sp.parse_expr(self.le_function.text())
        except:
            self.pb_start.setEnabled(False)
        else:
            self.pb_start.setEnabled(expr.free_symbols == set(sp.symbols('x y')))

    def fetch_data(self):
        x, y = sp.symbols('x y')
        func = sp.parse_expr(self.le_function.text())
        bounds = {x: (self.dsb_xmin.value(), self.dsb_xmax.value()), y: (self.dsb_ymin.value(), self.dsb_ymax.value())}
        opt_dir = 'max' if self.cmb_opt_dir.currentIndex() == 0 else 'min'
        population_size = self.sb_population_size.value()
        max_iteration = self.sb_max_iteration.value()
        return func, bounds, opt_dir, population_size, max_iteration

    def start_genetic_algorithm(self):
        self.l_plot_placeholder.setVisible(False)
        self.vl_plot.addWidget(self.w_plot, 1)
        func, bounds, opt_dir, population_size, max_iteration = self.fetch_data()
        self.w_plot.set_v_data(func, bounds)
        self.g_iterator = g.GeneticAlgorithmIterator(func=func, bounds=bounds, opt_dir=opt_dir, population_size=population_size, max_iteration=max_iteration, visualizer=self.w_plot)
        self.pb_next_iter.setEnabled(True)

    def next_iteration(self):
        try:
            next(self.g_iterator)
        except StopIteration:
            qtw.QMessageBox.information(self, 'Конец', 'Превышено максимальное количество итераций')
