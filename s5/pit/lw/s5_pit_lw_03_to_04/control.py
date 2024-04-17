from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QColorDialog, QFileDialog

from ui.view import Ui_PainterWindow
from paint_scene import PaintScene


class PainterControl(Ui_PainterWindow, QMainWindow):
    def __init__(self, widget: QMainWindow):
        super().__init__()
        self.widget = widget
        self.eraser = False
        self.color = Qt.GlobalColor.black
        self.pattern_pixmap = QPixmap()
        self.paint_scene = PaintScene(600, 400)
        self.setupUi(widget)
        self.connectUi()

    def setupUi(self, widget):
        super().setupUi(widget)
        self.w_main.layout().addWidget(self.paint_scene)
        self.paint_scene.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def connectUi(self):
        self.pb_color_choose.clicked.connect(self.show_color_dialog)
        self.pb_size_default.clicked.connect(lambda: self.cmb_size_choose.setCurrentIndex(2))
        self.pb_pattern_choose.clicked.connect(self.show_pattern_dialog)
        self.a_addictions_clear.triggered.connect(self.paint_scene.clear)
        self.a_allocation_fill.triggered.connect(self.paint_scene.allocation_fill)
        self.a_allocation_bound.triggered.connect(self.paint_scene.allocation_bound)
        self.a_allocation_fix.triggered.connect(self.paint_scene.allocation_fix)
        self.a_file_open.triggered.connect(self.file_open)
        self.a_file_close.triggered.connect(self.file_close)
        self.a_file_save.triggered.connect(self.file_save)
        self.a_file_save_as.triggered.connect(self.file_save_as)
        self.cmb_size_choose.currentIndexChanged.connect(lambda: self.paint_scene.pen.setWidth(int(self.cmb_size_choose.currentText())))
        self.rb_pen.toggled.connect(lambda checked: self.change_paint_scene_action(PaintScene.Action.Pen, checked))
        self.rb_fill.toggled.connect(lambda checked: self.change_paint_scene_action(PaintScene.Action.Fill, checked))
        self.rb_bound.toggled.connect(lambda checked: self.change_paint_scene_action(PaintScene.Action.Bound, checked))
        self.rb_allocation.toggled.connect(lambda checked: self.change_paint_scene_action(PaintScene.Action.Allocation, checked))
        self.rb_erase.toggled.connect(lambda checked: self.change_paint_scene_action(PaintScene.Action.Erase, checked))
        self.cb_pattern.toggled.connect(lambda checked: self.paint_scene.__setattr__('use_pattern', checked))

    def change_paint_scene_action(self, action, checked):
        if checked: self.paint_scene.action = action
        self.paint_scene.pen.setColor(Qt.GlobalColor.white if action == PaintScene.Action.Erase else self.color)

    def show_color_dialog(self):
        dialog = QColorDialog()
        if dialog.exec():
            selected_color = dialog.selectedColor()
            self.color = selected_color
            if self.paint_scene.action != PaintScene.Action.Erase:
                self.paint_scene.pen.setColor(selected_color)
            self.w_color_preview.setStyleSheet(f'background-color: rgb({selected_color.red()}, {selected_color.green()}, {selected_color.blue()})')

    def show_pattern_dialog(self):
        dialog = QFileDialog.getOpenFileName(self, 'Выберите паттерн', filter='Изображение (*.png *.jpg *.bmp)')
        if dialog:
            self.paint_scene.pattern_image = QImage(dialog[0])
            self.l_pattern_preview.setPixmap(QPixmap.fromImage(self.paint_scene.pattern_image))
            self.cb_pattern.setChecked(True)

    def file_open(self):
        dialog = QFileDialog.getOpenFileName(self, 'Выберите рисунок', filter='Изображения (*.png *.jpg *.bmp)')[0]
        self.widget.setWindowTitle(dialog)
        if dialog:
            self.paint_scene.load_image(dialog)

    def file_close(self):
        self.widget.setWindowTitle('Рисование')
        self.paint_scene.clear()

    def file_save(self):
        if self.widget.windowTitle() == 'Рисование': self.file_save_as()
        else: self.paint_scene.image.save(self.widget.windowTitle())

    def file_save_as(self):
        dialog = QFileDialog.getSaveFileName(self, 'Сохранить изображение', filter='Изображения (*.png *.jpg *.bmp)')[0]
        if dialog:
            self.paint_scene.image.save(dialog)
            self.widget.setWindowTitle(dialog)
