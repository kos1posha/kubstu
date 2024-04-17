from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QResizeEvent
from PySide6.QtWidgets import QColorDialog, QMainWindow, QMessageBox, QTableWidgetItem

from paint_scene import PaintScene, Action
from ui.view import Ui_GeometricWindow


class GeometricControl(QMainWindow, Ui_GeometricWindow):
    def __init__(self, widget: QMainWindow):
        super().__init__()
        self.widget = widget
        self.intersection_mode = False
        self.include_mode = False
        self.indexes = [-1, -1]
        self.paint_scene = PaintScene(self)
        self.setupUi(widget)

    def setupUi(self, widget: QMainWindow):
        super().setupUi(widget)
        self.connectUi()
        self.rb_point.setChecked(True)
        self.vl_ps.addWidget(self.paint_scene)
        self.paint_scene.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def connectUi(self):
        self.widget.resizeEvent = self.resizeEvent
        self.widget.keyPressEvent = self.keyPressEvent
        self.tw_primitives.currentItemChanged.connect(lambda: self.current_primitive_changed(self.get_current()))
        self.rb_point.toggled.connect(lambda: self.paint_scene.set_action(Action.Point))
        self.rb_line.toggled.connect(lambda: self.paint_scene.set_action(Action.Line))
        self.rb_polygon.toggled.connect(lambda: self.paint_scene.set_action(Action.Polygon))
        self.pb_remove_primitive.clicked.connect(lambda: self.paint_scene.remove_primitive(self.get_current()))
        self.pb_switch_color.clicked.connect(self.set_color)
        self.pb_clear.clicked.connect(self.clear)
        self.pb_size_default.clicked.connect(lambda: self.cmb_size_choose.setCurrentIndex(1))
        self.pb_rotate.clicked.connect(lambda: self.paint_scene.rotate(self.get_current(), self.get_rotate_angle()))
        self.pb_instersection.clicked.connect(lambda: self.find_intersection(self.get_current()))
        self.pb_include.clicked.connect(lambda: self.find_include(self.get_current()))
        self.cmb_size_choose.currentIndexChanged.connect(lambda: self.paint_scene.pen.setWidth(self.get_width()))
        self.widget.showMaximized()

    def resizeEvent(self, event: QResizeEvent):
        self.paint_scene.resize(self.w_ps.width(), self.w_ps.height())
        super().resizeEvent(event)

    def clear(self):
        self.tw_primitives.setRowCount(0)
        self.paint_scene.clear()

    def add_primitive(self, *args):
        row = self.tw_primitives.rowCount()
        self.tw_primitives.insertRow(self.tw_primitives.rowCount())
        for col, arg in enumerate(args):
            self.tw_primitives.setItem(row, col, QTableWidgetItem(arg))
        for i in range(4):
            self.tw_primitives.resizeColumnToContents(i)

    def find_intersection(self, index: int):
        if self.tw_primitives.rowCount() < 2:
            self.stb_main.showMessage('Для поиска пересечений необходимо хотя бы 2 примитива на сцене', 8000)
            return
        if index == -1:
            self.stb_main.showMessage('Выберите первый примитив, после чего снова нажмите кнопку "Пересечение"', 12000)
            return
        self.intersection_mode = True
        self.indexes[0] = index
        self.stb_main.showMessage('Выберите второй примитив или нажмите Ctrl+Z, чтобы отменить действие')
        self.set_choose_primitive_mode(True)

    def find_include(self, index: int):
        if self.tw_primitives.rowCount() < 2:
            self.stb_main.showMessage('Для поиска вхождения необходимо хотя бы 2 примитива на сцене', 8000)
            return
        if index == -1:
            self.stb_main.showMessage('Выберите первый примитив, после чего снова нажмите кнопку "Вхождение"', 12000)
            return
        self.include_mode = True
        self.indexes[0] = index
        self.stb_main.showMessage('Выберите второй примитив или нажмите Ctrl+Z, чтобы отменить действие')
        self.set_choose_primitive_mode(True)

    def set_choose_primitive_mode(self, mode):
        self.w_toolbar.setEnabled(not mode)
        self.w_ps.setEnabled(not mode)

    def update_primitive(self, index: int, ps_str: str):
        self.tw_primitives.setItem(index, 3, QTableWidgetItem(ps_str))

    def remove_primitive(self, index: int):
        self.tw_primitives.removeRow(index)

    def current_primitive_changed(self, index: int):
        if self.intersection_mode or self.include_mode:
            self.indexes[1] = index
        self.paint_scene.highlight_primitive(index)
        if len(self.indexes) == 2:
            if self.intersection_mode:
                intersections = [str(p) for p in self.paint_scene.primitive_intersection(*self.indexes)]
                if intersections is None:
                    return
                message = QMessageBox(QMessageBox.Icon.NoIcon, f'Найдено точек пересечения: {len(intersections)}', '\n'.join(intersections))
                message.exec()
                self.intersection_mode = False
                self.set_choose_primitive_mode(False)
            if self.include_mode:
                include = self.paint_scene.point_in_polygon(*self.indexes)
                message = QMessageBox(QMessageBox.Icon.NoIcon, f'Вхождение', 'Входит' if include else 'Не входит')
                message.exec()
                self.include_mode = False
                self.set_choose_primitive_mode(False)
            self.indexes = [-1, -1]
            self.stb_main.clearMessage()

    def set_color(self):
        dialog = QColorDialog()
        if dialog.exec():
            selected_color = dialog.selectedColor()
            self.paint_scene.pen.setColor(selected_color)
            self.w_color_preview.setStyleSheet(f'background-color: rgb({selected_color.red()}, {selected_color.green()}, {selected_color.blue()})')

    def get_width(self):
        return int(self.cmb_size_choose.currentText())

    def get_current(self):
        return self.tw_primitives.currentRow()

    def get_rotate_angle(self):
        return self.sb_rotate_angle.value()

    def keyPressEvent(self, event: QKeyEvent):
        if self.intersection_mode:
            if event.key() == Qt.Key.Key_Z and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
                self.stb_main.clearMessage()
                self.intersection_mode = False
                self.include_mode = False
                self.indexes = [-1, -1]
                self.set_choose_primitive_mode(False)
