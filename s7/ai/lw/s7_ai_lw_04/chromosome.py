import numpy as np
import sympy as sp


class Chromosome:
    attrs = sp.symbols('x y')

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def as_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def as_dict(self) -> dict[sp.Symbol, float]:
        return {k: w for k, w in zip(self.attrs, self.as_tuple())}

    def __str__(self) -> str:
        return f'.({self.x}; {self.y})'


def generate_population(count: int, x_min: float, x_max: float, y_min: float, y_max: float) -> list[Chromosome]:
    xs = np.random.uniform(x_min, x_max, count)
    ys = np.random.uniform(y_min, y_max, count)
    return [Chromosome(x, y) for x, y in zip(xs, ys)]
