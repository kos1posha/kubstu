from PySide6 import QtWidgets as qtw, QtCore as qtc


plot_range = 10000


class LimSpinBox(qtw.QSpinBox):
    def __init__(self, value: int = 0, *args, **kwargs):
        super(LimSpinBox, self).__init__(*args, **kwargs)
        self.setButtonSymbols(qtw.QSpinBox.ButtonSymbols.NoButtons)
        self.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.setMinimum(-plot_range)
        self.setMaximum(plot_range)
        self.setValue(value)
