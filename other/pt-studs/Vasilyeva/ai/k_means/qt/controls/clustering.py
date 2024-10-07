from PySide6 import QtWidgets as qtw

from kmeans import k_means
from qt.controls.plot_widget import PlotWidget
from qt.py.clustering import Ui_KMeansWindow


class KMeansControl(Ui_KMeansWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.plot = PlotWidget(self)
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        self.setupUi(self)
        self.setFixedSize(self.sizeHint().width(), self.sizeHint().height())
        self.vl_plot.addWidget(self.plot)

    def connect_ui(self):
        self.rb_add_point.toggled.connect(lambda state: self.set_plot_action('add', state))
        self.rb_delete_point.toggled.connect(lambda state: self.set_plot_action('delete', state))
        self.rb_do_nothing.toggled.connect(lambda state: self.set_plot_action('', state))
        self.pb_clustering.clicked.connect(self.start)

    def set_plot_action(self, value, state):
        if state:
            self.plot.plot_action = value

    def update_points_list(self):
        self.lw_points.clear()
        self.lw_points.addItems(str(point) for point in self.plot.points)
        self.lw_points.scrollToBottom()

    def start(self):
        clusters_count = self.sb_clusters_count.value()
        iterations = self.sb_iterations.value()
        k_means(self.plot.points, clusters_count, iterations)
