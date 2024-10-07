from genetic_algorithm import GeneticAlgorithmIterator
from qt.py.genetic import Ui_GeneticWindow
from PySide6 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc

import sympy as sp


class PopulationWidget(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.genetic_iterator = None
        self.x_min = None
        self.x_max = None
        self.y_min = None
        self.y_max = None
        self.selected_chromosome_index = -1

    @property
    def chromosomes(self):
        return [] if not self.genetic_iterator else self.genetic_iterator.population

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = qtg.QPainter(self)

        if not self.genetic_iterator:
            self.draw_empty_message(painter)
            return

        self.draw_axes(painter)
        self.draw_chromosomes(painter)

    def set_genetic_iterator(self, genetic_iterator):
        x, y = sp.symbols('x y')
        self.genetic_iterator = genetic_iterator
        self.x_min, self.x_max = genetic_iterator.bounds[x]
        self.y_min, self.y_max = genetic_iterator.bounds[y]
        self.repaint()

    def unset_genetic_iterator(self):
        self.genetic_iterator = None
        self.x_min = None
        self.x_max = None
        self.y_min = None
        self.y_max = None
        self.repaint()

    def set_selected_chromosome_index(self, index):
        self.selected_chromosome_index = index
        self.repaint()

    def draw_axes(self, painter):
        painter.setPen(qtg.QColor(255, 0, 0))
        x_center = self.width() * abs(self.x_min) / (abs(self.x_min) + abs(self.x_max))
        y_center = self.height() * abs(self.y_max) / (abs(self.y_min) + abs(self.y_max))
        painter.drawLine(0, y_center, self.width(), y_center)
        painter.drawLine(x_center, 0, x_center, self.height())

    def draw_chromosomes(self, painter):
        painter.setBrush(qtg.QColor(0, 0, 0))
        for i, chromosome in enumerate(self.chromosomes):
            x, y = chromosome.vals
            x_pos = int((x - self.x_min) / (self.x_max - self.x_min) * self.width())
            y_pos = int((self.y_max - y) / (self.y_max - self.y_min) * self.height())
            if i == self.selected_chromosome_index:
                painter.setPen(qtg.QColor(255, 0, 0))
                painter.drawEllipse(x_pos - 5, y_pos - 5, 10, 10)
            else:
                painter.setPen(qtg.QColor(0, 0, 0))
                painter.drawEllipse(x_pos - 2, y_pos - 2, 4, 4)

    def draw_empty_message(self, painter):
        painter.setPen(qtg.QColor(120, 120, 120))
        painter.setFont(qtg.QFont('Arial', 12))
        text = 'Генетический алгоритм не инициирован'
        text_rect = painter.boundingRect(0, 0, self.width(), self.height(), qtc.Qt.AlignmentFlag.AlignCenter, text)
        painter.drawText((self.width() - text_rect.width()) / 2, (self.height() + text_rect.height()) / 2, text)


class GeneticControl(Ui_GeneticWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.genetic_iterator = None
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.population_widget = PopulationWidget()
        self.gl_population.addWidget(self.population_widget)
        self.tw_health.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.setFixedSize(self.sizeHint().width(), self.sizeHint().height())

    def connect_ui(self):
        self.pb_start.clicked.connect(self.start)
        self.pb_stop.clicked.connect(self.stop)
        self.pb_next.clicked.connect(self.next)
        self.tw_health.itemSelectionChanged.connect(lambda: self.population_widget.set_selected_chromosome_index(self.tw_health.currentRow()))

    def start(self):
        data = self.fetch_data()
        if not data:
            return

        f, lim = data
        self.genetic_iterator = GeneticAlgorithmIterator(f, lim, population_size=100, max_iteration=100)
        self.population_widget.set_genetic_iterator(self.genetic_iterator)
        self.pb_next.setEnabled(True)
        self.pb_stop.setEnabled(True)
        self.update_population_health()

    def stop(self):
        self.genetic_iterator = None
        self.population_widget.unset_genetic_iterator()
        self.tw_health.setRowCount(0)
        self.pb_next.setEnabled(False)
        self.pb_stop.setEnabled(False)

    def next(self):
        next(self.genetic_iterator)
        self.population_widget.repaint()
        self.update_population_health()

    def update_population_health(self):
        self.tw_health.setRowCount(0)
        self.tw_health.setRowCount(self.genetic_iterator.population_size)
        for row, (chromosome, health) in enumerate(zip(self.genetic_iterator.population, self.genetic_iterator.health)):
            row_data = [*chromosome.vals, float(health)]
            for col, col_data in enumerate(row_data):
                item = qtw.QTableWidgetItem()
                item.setData(qtc.Qt.ItemDataRole.EditRole, col_data)
                item.setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
                self.tw_health.setItem(row, col, item)

    def fetch_data(self):
        errors = []
        if not (f := self.parse_function()):
            errors.append('• Функция')
        lim = {}
        if not (xlim := self.parse_lim('x')):
            errors.append('• Границы для x')
        else:
            lim.update(xlim)
        if not (ylim := self.parse_lim('y')):
            errors.append('• Границы для y')
        else:
            lim.update(ylim)
        if errors:
            qtw.QMessageBox.critical(self, 'Ошибка', '\n'.join(['Данные указаны неверно:'] + errors))
            return
        return f, lim

    def parse_function(self):
        try:
            f = sp.parse_expr(self.le_function.text())
            return f if f.free_symbols == set(sp.symbols('x y')) else None
        except:
            return None

    def parse_lim(self, s):
        le_lim = self.le_xlim if s == 'x' else self.le_ylim
        try:
            symbol = sp.symbols(s)
            lim = {symbol: tuple(float(b) for b in le_lim.text().split())}
            return lim if len(lim[symbol]) == 2 and lim[symbol][0] < lim[symbol][1] else None
        except:
            return None
