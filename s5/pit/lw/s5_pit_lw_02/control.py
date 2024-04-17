import os.path
import pyqtgraph as pg
from PIL import Image, ImageQt

from PySide6 import QtWidgets, QtGui, QtCore

from ui.design import Ui_ImageEditorWindow
from hsv import HSVEditorControl


class ImageEditorControl(Ui_ImageEditorWindow, QtWidgets.QWidget):
    def __init__(self, widget: QtWidgets.QMainWindow):
        super().__init__()
        self.widget = widget
        self.i_path = ''
        self.i_width = 0
        self.i_height = 0
        self.i_pixmap = QtGui.QPixmap()
        self.setupUi(widget)
        self.connectUi()
        pg.setConfigOptions(background='w', foreground='k', antialias=True)

    def setupUi(self, widget: QtWidgets.QMainWindow):
        super().setupUi(widget)

    def connectUi(self):
        self.widget.resizeEvent = self.resizeEvent
        self.a_open.triggered.connect(self.open_image)
        self.a_close.triggered.connect(self.close_image)
        self.a_save.triggered.connect(self.save_image)
        self.a_save_as.triggered.connect(self.save_image_as)
        self.a_gs_simple.triggered.connect(lambda: self.i.setPixmap(QtGui.QPixmap(self.convert_image_to_gs(self.gs_simple))))
        self.a_gs_ntscrgb.triggered.connect(lambda: self.i.setPixmap(QtGui.QPixmap(self.convert_image_to_gs(self.gs_ntscrgb))))
        self.a_gs_srgb.triggered.connect(lambda: self.i.setPixmap(QtGui.QPixmap(self.convert_image_to_gs(self.gs_srgb))))
        self.a_gs_difference.triggered.connect(lambda: self.i.setPixmap(QtGui.QPixmap(self.convert_image_to_gs(self.gs_difference))))
        self.a_gs_histogram.triggered.connect(self.gs_histogram)
        self.a_rgb_red.triggered.connect(lambda: self.convert_image_to_rgb(self.rgb_red))
        self.a_rgb_green.triggered.connect(lambda: self.convert_image_to_rgb(self.rgb_green))
        self.a_rgb_blue.triggered.connect(lambda: self.convert_image_to_rgb(self.rgb_blue))
        self.a_rgb_histogram.triggered.connect(self.rgb_histogram)
        self.a_hsv_edit.triggered.connect(self.hsv_edit)
        self.a_return.triggered.connect(self.return_image)

    def convert_image_to_gs(self, formula):
        image = self.i_pixmap.toImage()
        for i in range(image.width()):
            for j in range(image.height()):
                old = image.pixelColor(i, j)
                new = QtGui.QColor()
                gs = formula(old.red(), old.green(), old.blue())
                new.setRgb(gs, gs, gs)
                image.setPixelColor(i, j, new)
        return image

    def gs_simple(self, r, g, b):
        return (r + g + b) / 3

    def gs_ntscrgb(self, r, g, b):
        return r * 0.3 + g * 0.59 + b * 0.11

    def gs_srgb(self, r, g, b):
        return r * 0.21 + g * 0.72 + b * 0.07

    def gs_difference(self, r, g, b):
        return abs((r * 0.3 + g * 0.59 + b * 0.11) - (r * 0.21 + g * 0.72 + b * 0.07))

    def convert_image_to_rgb(self, color):
        image = ImageQt.fromqpixmap(self.i_pixmap)
        rgb = color(image.convert('RGB').split())
        self.i.setPixmap(Image.merge('RGB', rgb).toqpixmap())

    def rgb_zero(self, p):
        return 0

    def rgb_red(self, rgb):
        return rgb[0], rgb[1].point(self.rgb_zero), rgb[2].point(self.rgb_zero)

    def rgb_green(self, rgb):
        return rgb[0].point(self.rgb_zero), rgb[1], rgb[2].point(self.rgb_zero)

    def rgb_blue(self, rgb):
        return rgb[0].point(self.rgb_zero), rgb[1].point(self.rgb_zero), rgb[2]

    def get_saturation_histogram(self):
        image = self.convert_image_to_gs(self.gs_simple)
        saturation = [0] * 256
        for i in range(self.i_width):
            for j in range(self.i_height):
                color = image.pixelColor(i, j)
                saturation[color.value()] += 1
        return saturation

    def get_rgb_histograms(self):
        image = self.i_pixmap.toImage()
        red = [0] * 256
        green = [0] * 256
        blue = [0] * 256
        for i in range(self.i_width):
            for j in range(self.i_height):
                color = image.pixelColor(i, j)
                red[color.red()] += 1
                green[color.green()] += 1
                blue[color.blue()] += 1
        return red, green, blue

    def gs_histogram(self):
        dialog = QtWidgets.QDialog(self, QtCore.Qt.WindowType.Dialog)
        layout = pg.GraphicsLayoutWidget(dialog, True)
        histogram = layout.addPlot()
        histogram.plot(x=range(256), y=self.get_saturation_histogram(), pen=pg.mkPen(color=(0, 0, 0), width=2))
        histogram.showGrid(x=True, y=True)
        dialog.setFixedSize(768, 600)
        dialog.setWindowTitle('Гистограмма интенсивности')
        dialog.setLayout(QtWidgets.QGridLayout())
        dialog.layout().setContentsMargins(0, 0, 0, 0)
        dialog.layout().addWidget(layout)
        dialog.exec()

    def rgb_histogram(self):
        red, green, blue = self.get_rgb_histograms()
        dialog = QtWidgets.QDialog(self, QtCore.Qt.WindowType.Dialog)
        layout = pg.GraphicsLayoutWidget(dialog, True)
        histogram = layout.addPlot()
        histogram.plot(x=range(256), y=red, pen=pg.mkPen(color='r', width=2))
        histogram.plot(x=range(256), y=green, pen=pg.mkPen(color='g', width=2))
        histogram.plot(x=range(256), y=blue, pen=pg.mkPen(color='b', width=2))
        histogram.showGrid(x=True, y=True)
        dialog.setFixedSize(768, 600)
        dialog.setWindowTitle('Гистограмма по цветам')
        dialog.setLayout(QtWidgets.QGridLayout())
        dialog.layout().setContentsMargins(0, 0, 0, 0)
        dialog.layout().addWidget(layout)
        dialog.exec()

    def hsv_edit(self):
        dialog = QtWidgets.QDialog(self, QtCore.Qt.WindowType.Dialog)
        HSVEditorControl(dialog, self.i, self.i_pixmap)
        dialog.exec()

    def open_image(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self.widget, 'Выберите изображение', r'D:\Project Repositories\kubstu\s5\pit\lw\s5_pit_lw_02\img', 'Изображения (*.png *.jpeg *.jpg)')[0]
        if path:
            self.load_image(path)
            self.resize_i()

    def close_image(self):
        self.i_path = ''
        self.i_width = 0
        self.i_height = 0
        self.i.setPixmap(QtGui.QPixmap())
        self.resize_i()
        self.widget.setWindowTitle('Редактор изображений')

    def save_image(self, path=None):
        if path is not None:
            self.i_path = path
        if self.i_path:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information, 'Подтвердите действие', 'Вы уверены, что хотите сохранить изображение?', QtWidgets.QMessageBox.StandardButton.NoButton)
            message.addButton('Да', QtWidgets.QMessageBox.ButtonRole.YesRole)
            message.addButton('Нет', QtWidgets.QMessageBox.ButtonRole.NoRole)
            message.buttonClicked.connect(lambda button: self.i.pixmap().save(self.i_path) if button.text() == 'Да' else None)
            message.exec()

    def save_image_as(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self.widget, 'Сохранить изображение', '', 'Изображения (*.png *.jpeg *.jpg)')[0]
        if path:
            self.save_image(path)

    def load_image(self, path):
        self.i_path = path
        self.i_width = QtGui.QPixmap(path).width()
        self.i_height = QtGui.QPixmap(path).height()
        self.i_pixmap = QtGui.QPixmap(path)
        self.i.setPixmap(self.i_pixmap)
        new_size = self.pr_resize(new_width=500)
        self.i.resize(new_size[0], new_size[1])
        self.resize_i()
        self.widget.showMaximized()
        self.widget.setWindowTitle(os.path.abspath(path))

    def return_image(self):
        if self.i_path:
            self.load_image(self.i_path)

    def pr_resize(self, old_size=None, new_width=None, new_height=None):
        if old_size is None: old_size = (self.i_width, self.i_height)
        if new_width:
            return new_width, int(new_width * old_size[1] / old_size[0])
        elif new_height:
            return int(new_height * old_size[0] / old_size[1]), new_height
        raise AttributeError('Set at least one of the parameters')

    def resize_i(self):
        new_size = (self.i_width, self.i_height)
        if self.i.width() < self.i_width and self.i.height() < self.i_height:
            if self.i.width() > self.i.height():
                new_size = self.pr_resize(new_height=self.i.height())
                if self.i.width() < new_size[0]:
                    new_size = self.pr_resize(new_width=self.i.width())
            else:
                new_size = self.pr_resize(new_width=self.i.width())
                if self.i.height() < new_size[1]:
                    new_size = self.pr_resize(new_height=self.i.height())
        elif self.i.width() < self.i_width:
            new_size = self.pr_resize(new_width=self.i.width())
        elif self.i.height() < self.i_height:
            new_size = self.pr_resize(new_height=self.i.height())
        self.i.resize(new_size[0], new_size[1])

    def resizeEvent(self, event: QtGui.QResizeEvent):
        self.resize_i()
        super().resizeEvent(event)
