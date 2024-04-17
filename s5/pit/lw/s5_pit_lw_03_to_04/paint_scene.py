from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QUndoCommand, QUndoStack, QPainter, QPen, QColor, QPainterPath, QImage, QBrush
from PySide6.QtWidgets import QWidget


class UndoCommand(QUndoCommand):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.previous = parent.image.copy()
        self.current = parent.image.copy()

    def undo(self):
        self.current = self.parent.image.copy()
        self.parent.image = self.previous
        self.parent.update()

    def redo(self):
        self.parent.image = self.current
        self.parent.update()


class PaintScene(QWidget):
    class Action:
        Pen = 'pen'
        Fill = 'fill'
        Bound = 'bound'
        Allocation = 'allocation'
        Erase = 'erase'

    def __init__(self, width, height):
        super().__init__()
        self.undo_stack = QUndoStack(self)
        self.undo_stack.setUndoLimit(20)
        self.image = QImage(width, height, QImage.Format.Format_RGB16)
        self.image.fill(Qt.GlobalColor.white)
        self.action = PaintScene.Action.Pen
        self.pen = QPen(QColor(0, 0, 0), 3, Qt.PenStyle.SolidLine)
        self.is_pressed = False
        self.drawing_path = None
        self.allocation_start = None
        self.allocation_end = None
        self.use_pattern = False
        self.pattern_image = QImage(width, height, QImage.Format.Format_RGB16)
        self.pattern_image.fill(Qt.GlobalColor.black)

    def draw(self, parent):
        if self.is_pressed:
            painter = QPainter(parent)
            if self.drawing_path:
                painter.setPen(self.pen)
                if self.action == PaintScene.Action.Erase:
                    painter.pen().setColor(Qt.GlobalColor.white)
                painter.drawPath(self.drawing_path)
        if self.allocation_start and self.allocation_end:
            self.allocation(parent)

    def fill(self, x, y):
        target_color = self.image.pixelColor(x, y)
        fill_color = self.pen.color()
        if target_color == fill_color and not self.use_pattern: return
        stack = [(x, y)]
        visited = set()
        while stack:
            x, y = stack.pop()
            if self.use_pattern: fill_color = self.pattern_image.pixelColor(x, y)
            if 0 > x > self.image.width() and 0 > y > self.image.height() or self.image.pixelColor(x, y) == target_color:
                self.image.setPixelColor(x, y, fill_color)
                visited.add((x, y))
                stack.extend({(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)} - visited)

    def highlight_boundary(self, x, y):
        target_color = self.image.pixelColor(x, y)
        bound_color = self.pen.color()
        stack = [(x, y)]
        visited = set()
        while stack:
            x, y = stack.pop()
            if 0 > x > self.image.width() and 0 > y > self.image.height() or self.image.pixelColor(x, y) == target_color:
                for px, py in [(x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
                    if self.image.pixelColor(px, py) != target_color:
                        self.image.setPixelColor(px, py, bound_color)
                visited.add((x, y))
                stack.extend({(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)} - visited)

    def allocation(self, parent, color=Qt.GlobalColor.blue, style=Qt.PenStyle.DashLine, width=1, brush=None):
        painter = QPainter(parent)
        pen = QPen()
        pen.setColor(color)
        pen.setStyle(style)
        pen.setWidth(width)
        painter.setPen(pen)
        if brush: painter.fillRect(QRect(self.allocation_start, self.allocation_end), QBrush(color, brush))
        else: painter.drawRect(QRect(self.allocation_start, self.allocation_end))

    def allocation_fill(self):
        if not self.allocation_start: return
        self.undo_stack.push(UndoCommand(self))
        self.allocation(self.image, self.pen.color(), Qt.PenStyle.SolidLine, self.pen.width(), Qt.BrushStyle.SolidPattern)
        self.allocation_start, self.allocation_end = None, None
        self.update()

    def allocation_bound(self):
        if not self.allocation_start: return
        self.undo_stack.push(UndoCommand(self))
        self.allocation(self.image)
        self.allocation(self.image, self.pen.color(), Qt.PenStyle.SolidLine, self.pen.width())
        self.allocation_start, self.allocation_end = None, None
        self.update()

    def allocation_fix(self):
        if not self.allocation_start: return
        self.undo_stack.push(UndoCommand(self))
        self.allocation(self.image)
        self.allocation_start, self.allocation_end = None, None
        self.update()

    def clear(self):
        self.undo_stack.push(UndoCommand(self))
        self.image.fill(Qt.GlobalColor.white)
        self.update()

    def load_image(self, file_name):
        self.undo_stack.push(UndoCommand(self))
        self.image = QImage(file_name)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.draw(self)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.allocation_start, self.allocation_end = None, None
            if self.action in [PaintScene.Action.Pen, PaintScene.Action.Erase]:
                self.is_pressed = True
                self.drawing_path = QPainterPath()
                self.drawing_path.moveTo(event.position())
            elif self.action == PaintScene.Action.Fill:
                self.undo_stack.push(UndoCommand(self))
                self.fill(event.x(), event.y())
            elif self.action == PaintScene.Action.Bound:
                self.undo_stack.push(UndoCommand(self))
                self.highlight_boundary(event.x(), event.y())
            elif self.action == PaintScene.Action.Allocation:
                self.allocation_start = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        if self.action in [PaintScene.Action.Fill, PaintScene.Action.Bound]: return
        if event.buttons() and Qt.LeftButton:
            if self.action in [PaintScene.Action.Pen, PaintScene.Action.Erase]:
                self.drawing_path.lineTo(event.position())
            elif self.action == PaintScene.Action.Allocation:
                self.allocation_end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        if self.action in [PaintScene.Action.Fill, PaintScene.Action.Bound, PaintScene.Action.Allocation]: return
        if self.action in [PaintScene.Action.Pen, PaintScene.Action.Erase]:
            self.undo_stack.push(UndoCommand(self))
            self.draw(self.image)
            self.is_pressed = False
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z and event.modifiers() == Qt.ControlModifier:
            self.undo_stack.undo()
        elif event.key() == Qt.Key_Y and event.modifiers() == Qt.ControlModifier:
            self.undo_stack.redo()
