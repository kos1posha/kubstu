import numpy as np
import sympy as sp


class OptDir:
    MAXIMIZATION = 'max'
    MINIMIZATION = 'min'

    @classmethod
    def index(cls, index: int) -> str:
        return [OptDir.MAXIMIZATION, OptDir.MINIMIZATION][index]


symbols = sp.symbols('x y')
rng = np.random.default_rng()


class GeneticAlgorithmIterator:

    def __init__(self, func: sp.Expr, bounds: dict[str, tuple[float, float]], opt_dir: str, population_size: int, max_iteration: int) -> None:
        if func.free_symbols != set(symbols):
            raise ValueError('The given function must have the form f(x, y)')
        if bounds.keys() != {'x', 'y'}:
            raise ValueError('Given  bounds must have x and y keys')

        self.func = func
        self.bounds = bounds
        self.opt_dir = opt_dir
        self.population_size = population_size
        self.max_iteration = max_iteration

        self.population: np.ndarray = np.empty((population_size, 2))
        self.health: np.ndarray = np.empty(population_size)

        self._np_func = sp.lambdify(symbols, self.func, 'numpy')
        self._initialization()
        self._evaluation()

        self.current_iteration = 0

    def __iter__(self) -> 'GeneticAlgorithmIterator':
        return self

    def __next__(self) -> tuple[list[tuple[float, float]], list[float]]:
        if self.current_iteration < self.max_iteration:
            self._selection()
            self._recombination()
            self._evaluation()
            self.current_iteration += 1
            return self.population, self.health
        else:
            raise StopIteration

    def _initialization(self) -> None:
        low, high = zip(self.bounds['x'], self.bounds['y'])
        self.population[:] = rng.uniform(low, high, (self.population_size, 2))

    def _evaluation(self) -> None:
        self.health[:] = self._np_func(self.population[:, 0], self.population[:, 1])

    def _selection(self) -> None:
        match self.opt_dir:
            case OptDir.MAXIMIZATION:
                shift = -self.health.min()
                total_health = self.health.sum() + self.population_size * shift
                weights = (self.health + shift) / total_health
            case OptDir.MINIMIZATION:
                shift = self.health.max()
                total_health = -self.health.sum() + self.population_size * shift
                weights = (shift - self.health) / total_health
            case _:
                raise NotImplementedError()
        
        if not 0.9999 < abs(weights.sum()) < 1.0001:
            raise StopIteration
        self.population[:] = rng.choice(self.population, self.population_size, p=weights, shuffle=False)

    def _recombination(self) -> None:
        couples = self.population[rng.choice(self.population_size, (self.population_size, 2))]
        gene_choices = np.random.choice([True, False], self.population_size)
        children_xs = np.where(gene_choices, couples[:, 0, 0], couples[:, 1, 0])
        children_ys = np.where(gene_choices, couples[:, 1, 1], couples[:, 0, 1])
        self.population[:] = np.column_stack([children_xs, children_ys])
