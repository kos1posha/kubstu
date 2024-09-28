import sys

import numpy as np


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def as_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def square_distance(self, other: 'Point') -> float:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def distance(self, other: 'Point') -> float:
        return self.square_distance(other) ** 0.5

    @classmethod
    def mean(cls, points: list['Point']) -> 'Point':
        x_mean, y_mean = 0, 0
        for point in points:
            x_mean += point.x
            y_mean += point.y
        return Point(x_mean / len(points), y_mean / len(points))

    def __str__(self) -> str:
        return f'.({self.x}; {self.y})'


def generate_points(count: int, x_min: float, x_max: float, y_min: float, y_max: float) -> list[Point]:
    xs = np.random.uniform(x_min, x_max, count)
    ys = np.random.uniform(y_min, y_max, count)
    return [Point(x, y) for x, y in zip(xs, ys)]


def find_bounds(points: list[Point]) -> dict[str, float]:
    x_min = y_min = sys.maxsize
    x_max = y_max = -sys.maxsize
    for point in points:
        x_min, y_min = min(x_min, point.x), min(y_min, point.y)
        x_max, y_max = max(x_max, point.x), max(y_max, point.y)
    return {'x_min': x_min, 'x_max': x_max, 'y_min': y_min, 'y_max': y_max}
