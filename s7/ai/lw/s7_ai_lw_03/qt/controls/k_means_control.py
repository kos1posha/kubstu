from qt.controls.widgets import PlotWidget, LimSpinBox
from qt.py.k_means_window import Ui_KMeansWindow

from PySide6 import QtWidgets as qtw


class KMeansControl(Ui_KMeansWindow, qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.plot_widget = PlotWidget()
        self.setup_ui()

    def setup_ui(self) -> None:
        super().setupUi(self)
        self.setFixedSize(self.sizeHint().width(), self.sizeHint().height())
        self.vl_plot.addWidget(self.plot_widget)
        self.setup_tw_random_points()

    def setup_tw_random_points(self) -> None:
        self.tw_random_points.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.tw_random_points.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        default_values = iter([-100, 100, -100, 100])
        for r in range(2):
            for c in range(2):
                sb_lim = LimSpinBox(value=next(default_values))
                sb_lim.setStyleSheet('border:none;background:transparent')
                self.tw_random_points.setCellWidget(r, c, sb_lim)
                self.tw_random_points.item(r, c).setText('')
