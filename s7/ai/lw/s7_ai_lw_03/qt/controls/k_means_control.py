from k_means import KMeansIterator
from point import generate_points
from qt.controls.widgets import PlotWidget, LimSpinBox, ask
from qt.py.k_means_window import Ui_KMeansWindow

from PySide6 import QtWidgets as qtw, QtCore as qtc
from copy import deepcopy


class KMeansControl(Ui_KMeansWindow, qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.plot_widget = PlotWidget()
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
        self.setup_tw_random_points_lims()
        self.tw_iterations.horizontalHeader().setSectionResizeMode(0, qtw.QHeaderView.ResizeMode.ResizeToContents)
        self.tw_iterations.horizontalHeader().setDefaultAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

    def connect_ui(self) -> None:
        self.pb_delete_all_points.clicked.connect(self.delete_all_points)
        self.pb_add_random_points.clicked.connect(self.add_random_points)
        self.tb_adjust_plot.clicked.connect(self.plot_widget.adjust_bounds)
        self.pb_start_iter_clustering.clicked.connect(self.start_clustering)
        self.pb_stop_restart_clustering.clicked.connect(self.stop_clustering)
        self.tw_iterations.itemSelectionChanged.connect(self.show_iteration)

    def setup_tw_random_points_lims(self) -> None:
        self.tw_random_points_lims.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.tw_random_points_lims.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        default_values = iter([-100, 100, -100, 100])
        for r in range(2):
            for c in range(2):
                sb_lim = LimSpinBox(value=next(default_values))
                sb_lim.setStyleSheet('border:none;background:transparent')
                self.tw_random_points_lims.setCellWidget(r, c, sb_lim)
                self.tw_random_points_lims.item(r, c).setText('')

    def show_iteration(self) -> None:
        index = self.tw_iterations.currentRow()
        if index == -1:
            return
        iteration = self.iterations[index]
        self.plot_widget.old_centroids, self.plot_widget.centroids, self.plot_widget.points = iteration
        self.plot_widget.update_plot()

    def fetch_random_points_data(self) -> tuple[int, int, int, int]:
        cells = [(0, 0), (0, 1), (1, 0), (1, 1)]
        x_min, x_max, y_min, y_max = [self.tw_random_points_lims.cellWidget(r, c).value() for r, c in cells]
        errors = []
        for s, s_min, s_max in [('x', x_min, x_max), ('y', y_min, y_max)]:
            if s_min > s_max:
                errors.append(f'{s}: Нижняя граница ({s_min}) диапазона должна быть строго меньше верхней ({s_max})')
        if errors:
            qtw.QMessageBox.critical(self, 'Ошибка', '\n'.join(errors))
            return None
        count = self.sb_random_points_count.value()
        return count, x_min, x_max, y_min, y_max

    def delete_all_points(self) -> None:
        if not ask('Подтвердите действие', 'Удалить все точки на графике?', 'Подтвердить', 'Отмена'):
            return

        self.plot_widget.points = []
        self.plot_widget.update_plot()

    def add_random_points(self) -> None:
        data = self.fetch_random_points_data()
        if not data:
            return
        count, x_min, x_max, y_min, y_max = data
        random_points = generate_points(count, x_min, x_max, y_min, y_max)
        self.plot_widget.points.extend(random_points)
        self.plot_widget.fit_bounds(x_min, x_max, y_min, y_max)

    def fetch_clustering_data(self) -> None:
        points = self.plot_widget.points
        if not points:
            qtw.QMessageBox.critical(self, 'Ошибка', 'Вы не указали ни единой точки')
            return
        clusters_count = self.sb_clusters_count.value()
        max_iterations = self.sb_max_iterations.value()
        return points, clusters_count, max_iterations

    def start_clustering(self) -> None:
        data = self.fetch_clustering_data()
        if not data:
            return
        self.iterator = KMeansIterator(*data)
        self.set_start_iter_state(False)
        self.pb_stop_restart_clustering.setEnabled(True)
        self.w_clustering_attrs.setEnabled(False)
        self.tab_edit_points.setEnabled(False)
        self.w_iterations.setEnabled(True)
        self.plot_widget.set_interactive_mode(PlotWidget.InteractiveMode.SHOW_CLUSTERS)
        self.iter_clustering()

    def iter_clustering(self) -> None:
        try:
            old_centroids = deepcopy(self.iterator.centroids)
            centroids, clusters = next(self.iterator)
            self.iterations.insert(0, (old_centroids, deepcopy(centroids), deepcopy(clusters)))
            self.tw_iterations.insertRow(0)
            self.tw_iterations.setItem(0, 0, qtw.QTableWidgetItem(str(self.tw_iterations.rowCount())))
            self.tw_iterations.setItem(0, 1, qtw.QTableWidgetItem(f'{self.iterator.wcss:.2f}'))
            self.tw_iterations.item(0, 0).setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
            self.tw_iterations.selectRow(0)
            self.tw_iterations.setFocus()
        except StopIteration:
            self.stop_clustering(True)
            qtw.QMessageBox.information(self, 'Конец', 'Метод кластеризации завершил свою работу')
        else:
            self.plot_widget.old_centroids = old_centroids
            self.plot_widget.centroids = centroids
            self.plot_widget.points = clusters
            self.plot_widget.update_plot()

    def set_start_iter_state(self, state: bool) -> None:
        self.start_iter_state = state
        attrs = ['Начать', self.iter_clustering, self.start_clustering] if self.start_iter_state else \
                ['Дальше', self.start_clustering, self.iter_clustering]
        self.pb_start_iter_clustering.setText(attrs[0])
        self.pb_start_iter_clustering.clicked.disconnect(attrs[1])
        self.pb_start_iter_clustering.clicked.connect(attrs[2])

    def stop_clustering(self, force: bool = False) -> None:
        if not force and not ask('Остановить кластеризацию?', 'Вы больше не сможете итерировать метод', 'Остановить', 'Отмена'):
            return

        self.pb_start_iter_clustering.setEnabled(False)
        self.set_stop_restart_state(False)

    def restart_clustering(self) -> None:
        if not ask('Перезапустить кластеризацию?', 'Текущие центроиды будут удалены', 'Перезапустить', 'Отмена'):
            return

        self.iterations = []
        self.set_start_iter_state(True)
        self.set_stop_restart_state(True)
        self.pb_start_iter_clustering.setEnabled(True)
        self.pb_stop_restart_clustering.setEnabled(False)
        self.w_clustering_attrs.setEnabled(True)
        self.tab_edit_points.setEnabled(True)
        self.tw_iterations.setRowCount(0)
        self.plot_widget.set_interactive_mode(PlotWidget.InteractiveMode.EDIT_POINTS)

    def set_stop_restart_state(self, state: bool) -> None:
        self.stop_restart_state = state
        attrs = ['Остановить', self.restart_clustering, self.stop_clustering] if self.stop_restart_state else \
                ['Перезапустить', self.stop_clustering, self.restart_clustering]
        self.pb_stop_restart_clustering.setText(attrs[0])
        self.pb_stop_restart_clustering.clicked.disconnect(attrs[1])
        self.pb_stop_restart_clustering.clicked.connect(attrs[2])
