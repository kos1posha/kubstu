from PySide6 import QtWidgets as qtw
import sympy as sp

from qt.py.main import Ui_GeneticAlgorithmForm
import genetic as g
import visualizer as v


class GeneticAlgorithmControl(Ui_GeneticAlgorithmForm, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.valid_message = True
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.setFixedSize(self.sizeHint().width(), self.sizeHint().height())

    def connect_ui(self):
        self.pb_start.clicked.connect(self.start_genetic_algorithm)
        self.pb_check.clicked.connect(self.validate_function)

    def validate_function(self):
        try:
            expr = sp.parse_expr(self.le_function.text())
        except:
            qtw.QMessageBox.critical(self, 'Невалидная функция!', 'Вы ввели невалидную функцию. Проверьте, что она'
                                                                  'содержит x и y, а так же не прерывается.')
            return False
        if expr.free_symbols == set(sp.symbols('x y')):
            if self.valid_message:
                qtw.QMessageBox.information(self, 'Валидная функция!', 'Можно оптимизировать.')
            return True
        qtw.QMessageBox.critical(self, 'Невалидная функция!', 'Вы ввели невалидную функцию. Проверьте, что она'
                                                              'содержит x и y, а так же не прерывается.')
        return False

    def fetch_data(self):
        x, y = sp.symbols('x y')
        func = sp.parse_expr(self.le_function.text())
        bounds = {x: (self.dsb_xmin.value(), self.dsb_xmax.value()), y: (self.dsb_ymin.value(), self.dsb_ymax.value())}
        opt_dir = 'max' if self.cmb_opt_dir.currentIndex() == 0 else 'min'
        population_size = self.sb_population_size.value()
        max_iteration = 1000
        return func, bounds, opt_dir, population_size, max_iteration

    def start_genetic_algorithm(self):
        self.valid_message = False
        if not self.validate_function():
            self.valid_message = True
            return
        self.valid_message = True
        func, bounds, opt_dir, population_size, max_iteration = self.fetch_data()
        visualizer = v.GeneticAlgorithmPlotVisualizer(func, bounds, True)
        g.genetic(
            func=func,
            bounds=bounds,
            population_size=population_size,
            max_iteration=max_iteration,
            visualizer=visualizer
        )
