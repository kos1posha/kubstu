import sympy as sp
import sympy.parsing.sympy_parser as spp

from genetic_algorithm import GeneticAlgorithmIterator, OptDir, symbols
from qt.controls.widgets import PlotWidget, FunctionBoundsTableWidget, ask
from qt.py.genetic_algorithm_window import Ui_GeneticAlgorithmWindow

from PySide6 import QtWidgets as qtw, QtCore as qtc
from copy import deepcopy


class GeneticAlgorithmControl(Ui_GeneticAlgorithmWindow, qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.plot_widget = PlotWidget()
        self.tw_function_bounds = FunctionBoundsTableWidget([-100, 100, -100, 100])

        self.start_iter_state = True
        self.stop_restart_state = True
        self.iterator = None
        self.iterations = []
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self) -> None:
        super().setupUi(self)
        self.setFixedSize(self.sizeHint().width(), self.sizeHint().height())
        self.vl_plot.addWidget(self.plot_widget)
        self.tw_function_bounds.setFixedHeight(80)
        self.vl_function_bounds.addWidget(self.tw_function_bounds)
        self.tw_iterations.horizontalHeader().setSectionResizeMode(0, qtw.QHeaderView.ResizeMode.ResizeToContents)
        self.tw_iterations.horizontalHeader().setDefaultAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

    def connect_ui(self) -> None:
        self.le_function.textChanged.connect(lambda: self.pb_apply_function.setEnabled(bool(self.validate_function())))
        self.tw_function_bounds.text_changed_connect(lambda: self.pb_apply_function.setEnabled(bool(self.validate_function_bounds())))
        self.tw_iterations.itemSelectionChanged.connect(self.show_iteration)
        self.pb_apply_function.clicked.connect(self.apply_function)
        self.pb_start_iter_genetic.clicked.connect(self.start_genetic)
        self.pb_stop_restart_genetic.clicked.connect(self.stop_genetic)

    def validate_function(self) -> sp.Expr | None:
        try:
            expr = sp.parse_expr(self.le_function.text(), transformations='all', evaluate=False)
        except:
            return None
        else:
            return expr if expr.free_symbols == set(symbols) else None

    def validate_function_bounds(self) -> dict[str, tuple[int, int]] | None:
        bounds = self.tw_function_bounds.fetch_data()
        for s_min, s_max in bounds.values():
            if s_min >= s_max:
                return None
        return bounds

    def fetch_function_data(self) -> tuple[sp.Expr, dict[str, tuple[int, int]]]:
        function = self.validate_function()
        bounds = self.validate_function_bounds()
        if function is None or bounds is None:
            return
        return function, bounds

    def apply_function(self) -> None:
        function_data = self.fetch_function_data()
        self.plot_widget.put_function(*function_data)
        self.pb_start_iter_genetic.setEnabled(True)

    def fetch_genetic_data(self) -> tuple[str, int, int]:
        opt_dir = OptDir.index(self.cmb_opt_dir.currentIndex())
        population_size = self.sb_population_size.value()
        max_iterations = self.sb_max_iterations.value()
        return opt_dir, population_size, max_iterations

    def start_genetic(self) -> None:
        function_data = self.plot_widget.function_data()
        genetic_data = self.fetch_genetic_data()
        if function_data is None or genetic_data is None:
            return
        self.iterator = GeneticAlgorithmIterator(*function_data, *genetic_data)
        self.set_start_iter_state(False)
        self.pb_stop_restart_genetic.setEnabled(True)
        self.tab_function.setEnabled(False)
        self.w_genetic_attrs.setEnabled(False)
        self.w_iterations.setEnabled(True)
        self.iter_genetic()

    def iter_genetic(self) -> None:
        try:
            old_population, old_health = deepcopy((self.iterator.population, self.iterator.health))
            population, health = next(self.iterator)
            self.iterations.insert(0, old_population)
            self.tw_iterations.insertRow(0)
            iter_n = f'{self.tw_iterations.rowCount()}'
            iter_metric = f'{self.iterator.health.min() - self.iterator.health.max(): .2f}'
            self.tw_iterations.setItem(0, 0, qtw.QTableWidgetItem(iter_n))
            self.tw_iterations.setItem(0, 1, qtw.QTableWidgetItem(iter_metric))
            self.tw_iterations.item(0, 0).setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
            self.tw_iterations.selectRow(0)
            self.tw_iterations.setFocus()
        except StopIteration:
            self.stop_genetic(True)
            qtw.QMessageBox.information(self, 'Конец', 'Генетический алгоритм завершил свою работу')
        else:
            self.plot_widget.population = population
            self.plot_widget.health = health
            self.plot_widget.update_plot()

    def set_start_iter_state(self, state: bool) -> None:
        self.start_iter_state = state
        attrs = ['Начать', self.iter_genetic, self.start_genetic] if self.start_iter_state else \
                ['Дальше', self.start_genetic, self.iter_genetic]
        self.pb_start_iter_genetic.setText(attrs[0])
        self.pb_start_iter_genetic.clicked.disconnect(attrs[1])
        self.pb_start_iter_genetic.clicked.connect(attrs[2])

    def stop_genetic(self, force: bool = False) -> None:
        if not force and not ask('Остановить кластеризацию?', 'Вы больше не сможете итерировать метод', 'Остановить', 'Отмена'):
            return

        self.pb_start_iter_genetic.setEnabled(False)
        self.set_stop_restart_state(False)

    def restart_genetic(self) -> None:
        if not ask('Перезапустить генетический алгоритм?', 'Текущая популяция будет удалена', 'Перезапустить', 'Отмена'):
            return

        self.iterations = []
        self.set_start_iter_state(True)
        self.set_stop_restart_state(True)
        self.pb_start_iter_genetic.setEnabled(True)
        self.pb_stop_restart_genetic.setEnabled(False)
        self.w_genetic_attrs.setEnabled(True)
        self.tab_function.setEnabled(True)
        self.tw_iterations.setRowCount(0)

    def set_stop_restart_state(self, state: bool) -> None:
        self.stop_restart_state = state
        attrs = ['Остановить', self.restart_genetic, self.stop_genetic] if self.stop_restart_state else \
                ['Перезапустить', self.stop_genetic, self.restart_genetic]
        self.pb_stop_restart_genetic.setText(attrs[0])
        self.pb_stop_restart_genetic.clicked.disconnect(attrs[1])
        self.pb_stop_restart_genetic.clicked.connect(attrs[2])

    def show_iteration(self) -> None:
        index = self.tw_iterations.currentRow()
        if index == -1:
            return
        self.plot_widget.population = self.iterations[index]
        self.plot_widget.update_plot()
