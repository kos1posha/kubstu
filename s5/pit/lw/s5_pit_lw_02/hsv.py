from PIL import Image, ImageQt

from PySide6 import QtWidgets, QtGui

from ui.hsv import Ui_HSVEditorWindow


class HSVEditorControl(Ui_HSVEditorWindow, QtWidgets.QWidget):
    def __init__(self, widget: QtWidgets.QDialog, i: QtWidgets.QLabel, i_pixmap: QtGui.QPixmap):
        super().__init__()
        self.widget = widget
        self.i = i
        self.i_pixmap = i_pixmap
        self.setupUi(widget)
        self.connectUi()

    def setupUi(self, widget: QtWidgets.QDialog):
        super().setupUi(widget)

    def connectUi(self):
        self.hs_hue.valueChanged.connect(lambda: self.hsv_changed())
        self.hs_saturation.valueChanged.connect(lambda: self.hsv_changed())
        self.hs_value.valueChanged.connect(lambda: self.hsv_changed())

    def hsv_changed(self):
        self.l_hue_v.setText(str(self.hs_hue.value() / 100)[:4].ljust(4, '0'))
        self.l_saturation_v.setText(str(self.hs_saturation.value() / 100)[:4].ljust(4, '0'))
        self.l_value_v.setText(str(self.hs_value.value() / 100)[:4].ljust(4, '0'))
        image = ImageQt.fromqpixmap(self.i_pixmap)
        h, s, v = image.convert('HSV').split()
        mh, ms, mv = float(self.l_hue_v.text()), float(self.l_saturation_v.text()), float(self.l_value_v.text())
        h, s, v = h.point(lambda p: p + mh * 255), s.point(lambda p: p + ms * 255), v.point(lambda p: p + mv * 255)
        self.i.setPixmap(Image.merge('HSV', (h, s, v)).convert('RGB').toqpixmap())
