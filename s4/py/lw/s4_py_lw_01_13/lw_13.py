from math import sqrt


class Point:
    x: float = None
    y: float = None

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x:.2f}; {self.y:.2f})'

    def __eq__(self, other):
        return self is other or self.x == other.x and self.y == other.y

    def is_relatively(self, other):
        result = ''
        if self.y > other.y:
            result += 't'
        elif self.y < other.y:
            result += 'b'
        if self.x > other.x:
            result += 'r'
        elif self.x < other.x:
            result += 'l'
        return result


class Shape:
    start: Point = None
    color: str = None

    def __init__(self, start: Point = Point(0, 0), color: str = ''):
        self.start = start
        self.color = color

    def __str__(self):
        return '{' + f'{self.start}, {self.color}' + '}' if self.color != '' else '{' + f'{self.start}' + '}'

    def area(self):
        return None

    def perimeter(self):
        return None

    def move(self, shift_x: float = 0, shift_y: float = 0):
        self.start.x += shift_x
        self.start.y += shift_y

    def fill(self, color: str):
        self.color = color

    def compare(self, other):
        if self.area() > other.area():
            return 1
        elif self.area() == other.area():
            return 0
        else:
            return -1

    def is_intersect(self, other):
        return self.to_quadrangle().is_intersect_quadrangle(other.to_quadrangle())

    def is_include(self, other):
        return self.to_quadrangle().is_include_quadrangle(other.to_quadrangle())

    def to_quadrangle(self):
        return Quadrangle(Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0))


class LineSegment(Shape):
    end: Point = None

    def __new__(cls, end: Point = Point(1, 1), start: Point = Point(0, 0), color: str = ''):
        if end == start: return None
        return super().__new__(cls)

    def __init__(self, end: Point = Point(1, 1), start: Point = Point(0, 0), color: str = ''):
        super().__init__(start, color)
        self.end = end

    def __str__(self):
        return f'-{self.start}, {self.end}-'

    def __eq__(self, other):
        return self is other \
               or self.start == other.start and self.end == other.end \
               or self.start == other.end and self.end == other.start

    def reverse(self):
        self.start, self.end = self.start, self.end

    def move(self, shift_x: float = 0, shift_y: float = 0):
        super().move(shift_x, shift_y)
        self.end.x += shift_x
        self.end.y += shift_y

    def is_intersect_point(self, pt):
        pass

    def is_intersect(self, other, return_code: bool = True, for_segments: bool = True):
        if self == other: return 1 if return_code else self
        p = [..., ..., ..., ...]
        if self.start.x < other.start.x:
            (p[0], p[1]) = (self.start, self.end) if self.start.x < self.end.x else (self.end, self.start)
            (p[2], p[3]) = (other.start, other.end) if other.start.x < other.end.x else (other.end, other.start)
        elif self.start.x > other.start.x:
            (p[0], p[1]) = (other.start, other.end) if other.start.x < other.end.x else (other.end, other.start)
            (p[2], p[3]) = (self.start, self.end) if self.start.x < self.end.x else (self.end, self.start)
        else:
            if self.end.x < other.end.x:
                (p[0], p[1]) = (self.start, self.end) if self.start.x < self.end.x else (self.end, self.start)
                (p[2], p[3]) = (other.start, other.end) if other.start.x < other.end.x else (other.end, other.start)
            else:
                (p[0], p[1]) = (other.start, other.end) if other.start.x < other.end.x else (other.end, other.start)
                (p[2], p[3]) = (self.start, self.end) if self.start.x < self.end.x else (self.end, self.start)
        if p[0].x == p[1].x:
            k1 = 0
            b1 = p[0].x
        else:
            k1 = (p[1].y - p[0].y) / (p[1].x - p[0].x)
            b1 = p[0].y - k1 * p[0].x
        if p[2].x == p[3].x:
            k2 = 0
            b2 = p[2].x
        else:
            k2 = (p[3].y - p[2].y) / (p[3].x - p[2].x)
            b2 = p[2].y - k2 * p[2].x
        if k1 == k2:
            if b1 == b2:
                if for_segments:
                    if p[1] == p[2]: return 0 if return_code else p[1]
                    if p[0] == p[2]: return 1 if return_code else LineSegment(p[0], p[1])
                    if p[1] == p[3]: return 1 if return_code else LineSegment(p[1], p[3])
                    if p[1].x < p[2].x: return -1
                    if p[1].x < p[3].x:
                        return 1 if return_code else LineSegment(p[2], p[1])
                    else:
                        return 1 if return_code else LineSegment(p[2], p[3])
                else:
                    return 1
            else:
                return -1
        if k1 == 0:
            x = p[0].x
            y = k2 * x + b2
        elif k2 == 0:
            x = p[2].x
            y = k1 * x + b1
        else:
            x = (b2 - b1) / (k1 - k2)
            y = k1 * x + b1
        if for_segments:
            if p[0].x <= x <= p[1].x and p[2].x <= x <= p[3].x:
                return 0 if return_code else Point(x, y)
        else:
            return 0 if return_code else Point(x, y)
        return -1

    def is_include(self, other):
        intersect = self.is_intersect(other)
        if intersect is not LineSegment: return False
        return True if intersect == other else False


class Trapezoid(Shape):
    left_rib: int = None
    top_base: int = None
    right_rib: int = None
    bottom_base: int = None

    def __new__(cls, left_rib: int = 1, top_base: int = 1, right_rib: int = 1, bottom_base: int = 1,
                start: Point = Point(0, 0), color: str = ''):
        if (left_rib > top_base + right_rib + bottom_base or
                top_base > right_rib + bottom_base + left_rib or
                right_rib > bottom_base + left_rib + top_base or
                bottom_base > left_rib + top_base + right_rib): return None
        try:
            a, b, c, d = left_rib, top_base, right_rib, bottom_base
            height = sqrt(a ** 2 - (((d - b) ** 2 + a ** 2 - c ** 2) / (2 * (d - b))) ** 2)
            if height == 0: return None
        except:
            return None
        return super().__new__(cls)

    def __init__(self, left_rib: int = 1, top_base: int = 1, right_rib: int = 1, bottom_base: int = 1,
                 start: Point = Point(0, 0), color: str = ''):
        super().__init__(start, color)
        self.left_rib = left_rib
        self.top_base = top_base
        self.right_rib = right_rib
        self.bottom_base = bottom_base

    def height(self):
        a, b, c, d = self.left_rib, self.top_base, self.right_rib, self.bottom_base
        return sqrt(a ** 2 - (((d - b) ** 2 + a ** 2 - c ** 2) / (2 * (d - b))) ** 2)

    def area(self):
        return (self.top_base + self.bottom_base) * 0.5 * self.height

    def perimeter(self):
        return self.left_rib + self.top_base + self.right_rib + self.bottom_base


class Rhombus(Shape):
    vertical: int = None
    horizontal: int = None

    def __init__(self, vertical: int = 1, horizontal: int = 1, start: Point = Point(0, 0), color: str = ''):
        super().__init__(start, color)
        self.vertical = vertical
        self.horizontal = horizontal

    def __str__(self):
        return f'<{self.start}, {self.vertical}, {self.horizontal}>'

    def area(self):
        return self.vertical * self.horizontal * 0.5

    def perimeter(self):
        return 4 * sqrt((self.vertical * 0.5) ** 2 + (self.horizontal * 0.5) ** 2)

    def to_quadrangle(self):
        return Quadrangle(Point(self.start.x + self.horizontal * 0.5, self.start.y),
                          Point(self.start.x + self.horizontal, self.start.y - self.vertical * 0.5),
                          Point(self.start.x + self.horizontal * 0.5, self.start.y - self.vertical),
                          Point(self.start.x, self.start.y - self.vertical * 0.5))


class Rectangle(Shape):
    height: int = None
    width: int = None

    def __init__(self, height: int = 1, width: int = 1, start: Point = Point(0, 0)):
        super().__init__(start)
        self.height = height
        self.width = width
        self.start = start

    def __str__(self):
        return f'[{self.start}, {self.height}, {self.width}]'

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * self.height + 2 * self.width

    def to_quadrangle(self):
        return Quadrangle(Point(self.start.x, self.start.y), Point(self.start.x + self.width, self.start.y),
                          Point(self.start.x + self.width, self.start.y - self.height),
                          Point(self.start.x, self.start.y - self.height))


class Quadrangle:
    pt_tl: Point = None  # top left
    pt_tr: Point = None  # top right
    pt_br: Point = None  # bottom right
    pt_bl: Point = None  # bottom left

    def __init__(self, pt_tl: Point, pt_tr: Point, pt_br: Point, pt_bl: Point):
        self.pt_tl = pt_tl
        self.pt_tr = pt_tr
        self.pt_br = pt_br
        self.pt_bl = pt_bl

    def __str__(self):
        return f'[{self.pt_tl}, {self.pt_tr}, {self.pt_br}, {self.pt_bl}]'

    def is_intersect_point(self, pt: Point):
        lss = self.get_line_segments()
        for ls in lss:
            flag = ls.start.x == ls.end.x and ls.start.x == pt.x and min(ls.start.y, ls.end.y) <= pt.y <= max(
                ls.start.y, ls.end.y)
            if not flag: flag = ls.start.y == ls.end.y and ls.start.y == pt.y and min(ls.start.x,
                                                                                      ls.end.x) <= pt.x <= max(
                ls.start.x, ls.end.x)
            if not flag: flag = ls.start.y - ls.end.y * pt.x + ls.end.x - ls.start.x * pt.y + ls.start.x * ls.end.y - ls.end.x * ls.start.y == 0
            return flag

    def is_include_point(self, pt: Point):
        result = 0
        pts = self.get_points()
        for i in [0, 1, 2, 3]:
            if (((pts[i].y <= pt.y < pts[i - 1].y) or (pts[i - 1].y <= pt.y < pts[i].y)) and
                    (pt.x > (pts[i - 1].x - pts[i].x) * (pt.y - pts[i].y) / (pts[i - 1].y - pts[i].y) + pts[i].x)):
                result = 1 - result
        return True if result == 1 else False

    def is_intersect_quadrangle(self, other):
        for pt in other.get_points():
            if self.is_include_point(pt):
                return True
        return False

    def is_include_quadrangle(self, other):
        for pt in other.get_points():
            if not self.is_include_point(pt) and not self.is_intersect_point(pt):
                return False
        return True

    def get_points(self):
        return [self.pt_tl, self.pt_tr, self.pt_br, self.pt_bl]

    def get_line_segments(self):
        return [LineSegment(self.pt_tl, self.pt_tr),
                LineSegment(self.pt_tr, self.pt_br),
                LineSegment(self.pt_br, self.pt_bl),
                LineSegment(self.pt_bl, self.pt_tl)]
