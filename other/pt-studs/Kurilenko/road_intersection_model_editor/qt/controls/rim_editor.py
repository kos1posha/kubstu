from qt.py.rim_editor import Ui_RIMEditor
from PySide6 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc


class LRim(qtw.QLabel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        sizePolicy1 = qtw.QSizePolicy(qtw.QSizePolicy.Policy.Expanding, qtw.QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy1)
        self.setFrameShape(qtw.QFrame.Shape.Panel)
        self.setFrameShadow(qtw.QFrame.Shadow.Sunken)
        self.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = qtg.QPainter(self)

        for road in self.parent.roads:
            self.draw_road(painter, *road)
        if self.parent.drawing:
            self.draw_road(painter, *self.parent.new_road)

    def draw_road(self, painter, points, pc, sc):
        rect_size = 4
        painter.setBrush(qtg.QColor.fromString(sc))
        for p1, p2 in zip(points, points[1:] + [points[-1]]):
            p1c = p1 + self.get_pixmap_pos()
            p2c = p2 + self.get_pixmap_pos()
            painter.setPen(sc)
            painter.drawRect(p1c.x() - rect_size / 2, p1c.y() - rect_size / 2, rect_size, rect_size)
            painter.setPen(pc)
            painter.drawLine(p1c, p2c)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if (event.button() == qtc.Qt.MouseButton.LeftButton
                and self.parent.raw_pixmap is not None and self.pos_in_pixmap(event.pos())):
            if self.parent.rb_road_add.isChecked():
                pos = event.pos() - self.get_pixmap_pos()
                if not self.parent.drawing:
                    self.parent.drawing = True
                    self.parent.new_road = [[pos], self.parent.primary_color, self.parent.secondary_color]
                    self.parent.status_bar.showMessage('Чтобы установить последний узел дороги, удерживайте ctrl при нажатии на левую кнопку мыши.')
                else:
                    if event.modifiers() == qtc.Qt.KeyboardModifier.ControlModifier:
                        self.parent.drawing = False
                        self.parent.new_road[0].append(pos)
                        self.parent.roads.append(self.parent.new_road)
                        self.parent.new_road = None
                        self.parent.status_bar.clearMessage()
                    else:
                        self.parent.new_road[0].append(pos)
            self.update()

    def get_pixmap_pos(self):
        ql_rect = self.rect()
        pm_rect = self.pixmap().rect()
        pm_pos = qtc.QPoint(
            int((ql_rect.width() - pm_rect.width()) / 2),
            int((ql_rect.height() - pm_rect.height()) / 2)  # sheesh
        )
        return pm_pos

    def pos_in_pixmap(self, pos):
        if not self.pixmap():
            return False

        pm_rect = self.pixmap().rect()
        pm_pos = self.get_pixmap_pos()
        pm_rect.moveTo(pm_pos)
        return pm_rect.contains(pos)


class RIMEditorControl(Ui_RIMEditor, qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.primary_color = '#0000ff'
        self.secondary_color = '#00ff00'
        self.raw_pixmap = None
        self.roads = []
        self.new_road = None
        self.drawing = False

        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.set_toolbar_enabled(False)
        self.l_rim.deleteLater()
        self.l_rim = LRim(self)
        self.l_rim.setFocusPolicy(qtc.Qt.FocusPolicy.StrongFocus)
        self.gl_main.addWidget(self.l_rim, 2, 0)

    def connect_ui(self):
        self.a_load_image.triggered.connect(self.load_image)
        self.a_clear_image.triggered.connect(self.clear_image)
        self.a_clear_model.triggered.connect(self.clear_model)

        self.w_road_primary_color.mouseDoubleClickEvent = self.primary_color_picker
        self.w_road_secondary_color.mouseDoubleClickEvent = self.secondary_color_picker

    def load_image(self):
        file_path, _ = qtw.QFileDialog.getOpenFileName(self, 'Выберите изображение дороги', '', 'Изображения (*.png *.jpg)')
        if not file_path:
            return

        self.raw_pixmap = qtg.QPixmap(file_path)
        self.l_rim.setPixmap(self.raw_pixmap)
        self.set_toolbar_enabled(True)

    def clear_model(self):
        self.roads = []
        self.new_road = None
        self.drawing = False

    def clear_image(self):
        self.raw_pixmap = None
        self.l_rim.clear()
        self.set_toolbar_enabled(False)

    def primary_color_picker(self, _):
        color = qtw.QColorDialog.getColor(self.primary_color, self, 'Основной цвет')
        if not color.isValid():
            return

        hex_color = color.name(qtg.QColor.NameFormat.HexRgb)
        self.primary_color = hex_color
        self.w_road_primary_color.setStyleSheet(f'background-color:{hex_color};border:1px solid lightgrey;border-radius:20px;')
        if self.drawing:
            self.new_road[1] = hex_color

    def secondary_color_picker(self, _):
        color = qtw.QColorDialog.getColor(self.secondary_color, self, 'Цвет узлов')
        if not color.isValid():
            return

        hex_color = color.name(qtg.QColor.NameFormat.HexRgb)
        self.secondary_color = hex_color
        self.w_road_secondary_color.setStyleSheet(f'background-color:{hex_color};border:1px solid lightgrey;border-radius:20px;')
        if self.drawing:
            self.new_road[2] = hex_color

    def set_toolbar_enabled(self, enabled):
        self.w_road.setEnabled(enabled)
        self.w_road_color.setEnabled(enabled)
