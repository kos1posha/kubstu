import re
import pyqtgraph as pg

from PySide6 import QtWidgets, QtCore
from ui.design import Ui_FuncToGraphWindow
from math import *


def calculate(function: str, start, end, step):
    xs, ys = [], []
    while start < end:
        try:
            ys.append(eval(re.sub(r'\bx\b', str(start), function)))
            xs.append(start)
        except: pass
        finally: start += step
    return xs, ys


class FuncToGraphControl(Ui_FuncToGraphWindow, QtWidgets.QMainWindow):
    def __init__(self, widget: QtWidgets.QWidget):
        super().__init__()
        self.widget = widget
        self.setupUi(widget)
        self.connectUi()
        pg.setConfigOptions(background='w', foreground='k', antialias=True)

    def setupUi(self, widget: QtWidgets.QWidget):
        super().setupUi(widget)
        self.widget.setFixedHeight(widget.height() + 60)
        self.l_invalid.setVisible(False)

    def connectUi(self):
        self.le_function.textChanged.connect(self.validate_function)
        self.pb_draw.clicked.connect(self.draw)
        self.pb_pi.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'pi'))
        self.pb_e.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'e'))
        self.pb_exp.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'exp(x)'))
        self.pb_pow.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'pow(x, 2)'))
        self.pb_sqrt.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'sqrt(x)'))
        self.pb_rad.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + '(x*pi)/180'))
        self.pb_sin.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'sin(x)'))
        self.pb_cos.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'cos(x)'))
        self.pb_tan.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'tan(x)'))
        self.pb_abs.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'abs(x)'))
        self.pb_log.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'log(x)'))
        self.pb_log10.clicked.connect(lambda: self.le_function.setText(self.le_function.text() + 'log10(x)'))

    def draw(self):
        xs, ys = calculate(self.le_function.text(), self.dsb_start.value(), self.dsb_end.value(), self.dsb_step.value())
        dialog = QtWidgets.QDialog(self, QtCore.Qt.WindowType.Dialog)
        layout = pg.GraphicsLayoutWidget(dialog, True)
        histogram = layout.addPlot()
        histogram.plot(x=xs, y=ys, pen=pg.mkPen(color=(0, 0, 0), width=2))
        histogram.showGrid(x=True, y=True)
        dialog.setFixedSize(768, 600)
        dialog.setWindowTitle(f'График функции y(x) = {self.le_function.text()}')
        dialog.setLayout(QtWidgets.QGridLayout())
        dialog.layout().setContentsMargins(0, 0, 0, 0)
        dialog.layout().addWidget(layout)
        dialog.exec()

    def validate_function(self):
        def valid(s):
            self.pb_draw.setEnabled(s)
            self.l_invalid.setVisible(not s)
        valid(False)
        for x in ['100', '-1', '0', '1', '-100']:
            try: eval(re.sub(r'\bx\b', x, self.le_function.text()))
            except: pass
            else: valid(True)
