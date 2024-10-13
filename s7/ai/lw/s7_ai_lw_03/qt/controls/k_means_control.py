from k_means import KMeansIterator
from point import generate_points
from qt.controls.widgets import PlotWidget, LimSpinBox
from qt.py.k_means_window import Ui_KMeansWindow

from PySide6 import QtWidgets as qtw


class KMeansControl(Ui_KMeansWindow, qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.plot_widget = PlotWidget()
        self.iterator = None
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self) -> None:
        super().setupUi(self)
        self.setFixedSize(self.sizeHint().width(), self.sizeHint().height())
        self.vl_plot.addWidget(self.plot_widget)
        self.setup_tw_random_points_lims()

    def connect_ui(self) -> None:
        self.pb_add_random_points.clicked.connect(self.add_random_points)
        self.tb_adjust_plot.clicked.connect(self.plot_widget.adjust_bounds)
        self.pb_clustering.clicked.connect(self.start_clustering)

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
        self.tab_edit_points.setEnabled(False)
        self.plot_widget.interactive_mode = PlotWidget.InteractiveMode.SHOW_CLUSTERS
        self.pb_clustering.setText('Дальше')
        self.pb_clustering.clicked.disconnect(self.start_clustering)
        self.pb_clustering.clicked.connect(self.iter_clustering)
        self.iter_clustering()

    def iter_clustering(self) -> None:
        try:
            centroids, clusters = next(self.iterator)
        except StopIteration:
            qtw.QMessageBox.information(self, 'Конец', 'Метод кластеризации завершил свою работу')
        else:
            self.plot_widget.centroids = centroids
            self.plot_widget.points = clusters
            self.plot_widget.update_plot()
