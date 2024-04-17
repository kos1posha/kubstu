from typing import Any, Union

from PySide6.QtCore import QPointF, Qt, QLineF
from PySide6.QtGui import QColor, QImage, QKeyEvent, QMouseEvent, QPaintEvent, QPainter, QPen, QPolygon, QResizeEvent, QPolygonF, QTransform
from PySide6.QtWidgets import QSizePolicy, QWidget

from ui.view import Ui_GeometricWindow


class Ui_GW(Ui_GeometricWindow):
    def add_primitive(self, *args, **kwargs):
        pass

    def update_primitive(self, *args, **kwargs):
        pass

    def remove_primitive(self, *args, **kwargs):
        pass

    def set_choose_primitive_mode(self, *args, **kwargs):
        pass


class Action:
    Point = 'Point'
    Line = 'Line'
    Polygon = 'Polygon'


def cls_name(obj: Any):
    return obj.__class__.__name__


class PaintScene(QWidget):
    def __init__(self, parent: Union[Ui_GW, Ui_GeometricWindow]):
        super().__init__()
        self.parent = parent
        self.action = Action.Point
        self.primitives = []
        self.excluded = []
        self.old_index = None
        self.old_color = None
        self.pen = QPen(Qt.GlobalColor.black, 2)
        self.canvas = QImage(100, 100, QImage.Format.Format_RGB16)
        self.setup()

    @property
    def intermediate(self):
        return [i[0] for i in self.excluded]

    def setup(self):
        self.canvas.fill(Qt.GlobalColor.white)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMouseTracking(True)

    def clear(self):
        self.primitives.clear()
        self.update()

    def painter(self, parent=None, color=None, width=None, brush=True):
        parent = parent or self.canvas
        color = color or self.pen.color()
        width = width or self.pen.width()
        painter = QPainter(parent)
        painter.setPen(QPen(color, width))
        if brush: painter.setBrush(color)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        return painter

    def draw_primitive(self, painter: QPainter, primitive, color: QColor, width: float):
        painter.setPen(QPen(color, width))
        match cls_name(primitive):
            case 'QPointF':
                painter.setBrush(color)
                painter.drawEllipse(primitive, width, width)
            case 'QLineF':
                painter.setBrush(color)
                painter.drawLine(primitive)
            case 'QPolygonF':
                painter.setBrush(Qt.BrushStyle.NoBrush)
                painter.drawPolygon(primitive)

    def show_excluded(self, painter: QPainter):
        def point(p, c, w):
            w *= 0.5
            painter.setPen(QPen(c, w))
            painter.drawEllipse(p, w, w)
        def line(p1, p2, c, w):
            w *= 1.1
            painter.setPen(QPen(c, w))
            painter.drawLine(p1, p2)
        match len(self.excluded):
            case 0: return
            case 1: point(*self.excluded[0])
            case _:
                p1 = self.excluded[0][0]
                for p2, c, w in self.excluded[1:]:
                    line(p1, p2, c, w)
                    p1 = p2

    def center(self, primitive: Any):
        match cls_name(primitive):
            case 'QPointF':
                return primitive
            case 'QLineF':
                return primitive.center()
            case 'QPolygonF':
                return self.polygon_centroid(primitive)

    def rotate(self, index: int, angle: int, rotate_point='center'):
        primitive = self.primitives[index][0]
        rotate_point = self.center(primitive) if rotate_point == 'center' else rotate_point
        transform = QTransform()
        transform.translate(rotate_point.x(), rotate_point.y())
        transform.rotate(angle)
        transform.translate(-rotate_point.x(), -rotate_point.y())
        self.primitives[index][0] = transform.map(primitive)
        self.update()

    def paintEvent(self, event: QPaintEvent):
        self.canvas.fill(Qt.GlobalColor.white)
        painter = QPainter(self.canvas)
        painter.setRenderHint(QPainter.Antialiasing)
        for primitive, color, width in self.primitives:
            self.draw_primitive(painter, primitive, color, width)
        self.show_excluded(painter)
        QPainter(self).drawImage(0, 0, self.canvas)

    def mousePressEvent(self, event: QMouseEvent):
        if self.old_index and self.primitives[self.old_index]:
            try: self.primitives[self.old_index][1] = self.old_color
            except: pass
        point = event.position()
        if event.button() == Qt.LeftButton:
            match self.action:
                case Action.Point:
                    self.add_primitive(point, 0.5)
                case Action.Line:
                    self.excluded.append([point, self.pen.color(), self.pen.width()])
                    if len(self.excluded) == 2:
                        self.add_primitive(QLineF(*self.intermediate), 1.1)
                        self.excluded.clear()
                case Action.Polygon:
                    self.excluded.append([point, self.pen.color(), self.pen.width()])
                    if len(self.excluded) > 2:
                        self.parent.stb_main.showMessage('Нажмите Ctrl+X, чтобы закрыть полигон')
            self.update()

    def keyPressEvent(self, event: QKeyEvent):
        if self.action == Action.Polygon:
            if event.key() == Qt.Key.Key_X and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
                if len(self.excluded) < 3:
                    self.parent.stb_main.showMessage('Для создания полигона необходимо указать хотя бы 3 вершины')
                    return
                self.add_primitive(QPolygonF(self.intermediate), 1.1)
                self.excluded.clear()
                self.update()
                self.parent.stb_main.clearMessage()

    def add_primitive(self, primitive, w_mul=1.0):
        self.primitives.append([primitive, self.pen.color(), self.pen.width() * w_mul])
        color = f'{self.pen.color().toTuple()[:-1]}'[1:-1]
        width = f'{self.pen.width()} px'
        name, koord = self.string_from_primitive(primitive)
        self.parent.add_primitive(name, width, color, koord)

    def update_primitive(self, index: int):
        primitive = self.primitives[index]
        name, string = self.string_from_primitive(primitive)
        self.parent.update_primitive(index, string)

    def remove_primitive(self, index: int):
        if index == -1:
            return
        self.primitives.pop(index)
        self.parent.remove_primitive(index)
        self.update()

    def string_from_primitive(self, primitive: Any):
        def f(ps):
            return ' -> '.join(f'{p.toTuple()}' for p in ps)
        match cls_name(primitive):
            case 'QPointF':
                return 'Точка', f'{primitive.toTuple()}'
            case 'QLineF':
                return 'Отрезок', f([primitive.p1(), primitive.p2()])
            case 'QPolygonF':
                return 'Полигон', f([primitive[i] for i in range(primitive.size())])

    def highlight_primitive(self, index: int):
        if self.old_index:
            self.primitives[self.old_index][1] = self.old_color
        if index == -1:
            return
        self.old_color = self.primitives[-1][1]
        self.primitives[index][1] = QColor(0, 0, 255)
        self.old_index = index
        self.update()

    def polygon_centroid(self, polygon: QPolygonF):
        assert polygon.size() > 2, 'Необходимо хотя бы 3 точки'
        area = cx = cy = 0
        for i in list(range(1, polygon.size())) + [0]:
            p1, p2 = polygon[i - 1], polygon[i]
            shoelace = p1.x() * p2.y() - p2.x() * p1.y()
            area += shoelace
            cx += (p1.x() + p2.x()) * shoelace
            cy += (p1.y() + p2.y()) * shoelace
        factor = 1 / (3 * area)
        return QPointF(int(cx * factor), int(cy * factor))

    def polygon_lines(self, polygon: QPolygonF):
        segments = []
        for i in range(polygon.size()):
            start = polygon[i]
            end = polygon[(i + 1) % polygon.size()]
            segment = QLineF(start, end)
            segments.append(segment)
        return segments

    def point_in_polygon(self, index1, index2):
        primitive1 = self.primitives[index1][0]
        primitive2 = self.primitives[index2][0]
        if cls_name(primitive1) == 'QPointF' and cls_name(primitive2) == 'QPolygonF':
            return primitive2.containsPoint(primitive1, Qt.FillRule.OddEvenFill)
        elif cls_name(primitive1) == 'QPolygonF' and cls_name(primitive2) == 'QPointF':
            return primitive1.containsPoint(primitive2, Qt.FillRule.OddEvenFill)
        else:
            self.parent.stb_main.showMessage('Для вхождения выберите точку и полигон')
            self.parent.include_mode = False
            self.parent.indexes = [-1, -1]
            self.parent.set_choose_primitive_mode(False)
            return


    def point_in_segment(self, point: QPointF, segment: QLineF):
        x, y, x1, y1, x2, y2 = point.x(), point.y(), segment.x1(), segment.y1(), segment.x2(), segment.y2()
        if (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1):
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
                return point
        return None

    def find_segment_intersection(self, segment1: QLineF, segment2: QLineF):
        def line_equation(x1, y1, x2, y2):
            a = y2 - y1
            b = x1 - x2
            c = x2 * y1 - x1 * y2
            return a, b, -c
        def do_lines_intersect(a1, b1, c1, a2, b2, c2):
            determinant = a1 * b2 - a2 * b1
            if determinant == 0:
                return False
            else:
                x = (b2 * c1 - b1 * c2) / determinant
                y = (a1 * c2 - a2 * c1) / determinant
                return x, y
        line1 = line_equation(segment1.x1(), segment1.y1(), segment1.x2(), segment1.y2())
        line2 = line_equation(segment2.x1(), segment2.y1(), segment2.x2(), segment2.y2())
        intersection = do_lines_intersect(*line1, *line2)
        if intersection:
            x, y = intersection
            if (min(segment1.x1(), segment1.x2()) <= x <= max(segment1.x1(), segment1.x2()) and
                min(segment1.y1(), segment1.y2()) <= y <= max(segment1.y1(), segment1.y2()) and
                min(segment2.x1(), segment2.x2()) <= x <= max(segment2.x1(), segment2.x2()) and
                min(segment2.y1(), segment2.y2()) <= y <= max(segment2.y1(), segment2.y2())):
                return x, y
        return None

    def primitive_intersection(self, index1, index2):
        primitive1 = [self.primitives[index1][0]]
        primitive2 = [self.primitives[index2][0]]
        if cls_name(primitive1) == 'QPointF' or  cls_name(primitive2) == 'QPointF':
            self.parent.stb_main.showMessage('Пересечение доступно только между отрезками и полигонами')
            self.parent.intersection_mode = False
            self.parent.include_mode = False
            self.parent.indexes = [-1, -1]
            self.parent.set_choose_primitive_mode(False)
            return
        if cls_name(primitive1[0]) == 'QPolygonF':
            primitive1 = self.polygon_lines(primitive1[0])
        if cls_name(primitive2[0]) == 'QPolygonF':
            primitive2 = self.polygon_lines(primitive2[0])
        intersections = []
        for line1 in primitive1:
            for line2 in primitive2:
                intersection = self.find_segment_intersection(line1, line2)
                if intersection is not None:
                    intersections.append(intersection)
        return intersections

    def set_action(self, action: Action):
        self.action = action
        self.intermediate.clear()
        self.excluded.clear()
        self.parent.stb_main.clearMessage()

    def resizeEvent(self, event: QResizeEvent):
        canvas = QImage(event.size(), QImage.Format.Format_RGB16)
        canvas.fill(Qt.GlobalColor.white)
        QPainter(canvas).drawImage(0, 0, self.canvas)
        self.canvas = canvas
        self.update()
