import random
import sympy as sp

from chromosome import Chromosome, generate_population


class OptDir:
    MAXIMIZATION = 'max'
    MINIMIZATION = 'min'


class GeneticAlgorithmIterator:
    def __init__(self, func: sp.Expr, bounds: dict[str, float], opt_dir: str, population_size: int, max_iteration: int) -> None:
        self.func = func
        self.bounds = bounds
        self.opt_dir = opt_dir
        self.population_size = population_size
        self.max_iteration = max_iteration

        self.population = []
        self.health = []
        self._initialization()
        self._evaluation()

        self.current_iteration = 0

    def __iter__(self) -> 'GeneticAlgorithmIterator':
        return self

    def __next__(self) -> tuple[list[Chromosome], list[float]]:
        if self.current_iteration < self.max_iteration:
            self._selection()
            self._recombination()
            self._evaluation()
            self.current_iteration += 1
            return self.population, self.health
        else:
            raise StopIteration

    def _initialization(self) -> None:
        self.population.clear()
        self.population.extend(generate_population(self.population_size, **self.bounds))

    def _evaluation(self) -> None:
        self.health.clear()
        self.health.extend(self.func.subs(ch.as_dict()) for ch in self.population)

    def _selection(self) -> None:
        match self.opt_dir:
            case OptDir.MAXIMIZATION:
                shift = -min(self.health)
                total_health = sum(self.health, start=len(self.population) * shift)
                weights = [(shift + health) / total_health for health in self.health]
            case OptDir.MINIMIZATION:
                shift = max(self.health)
                total_health = -sum(self.health, start=-len(self.population) * shift)
                weights = [(shift - health) / total_health for health in self.health]
            case _:
                raise NotImplementedError()

        population = self.population.copy()
        self.population = random.choices(population, weights, k=len(population))

    def _recombination(self) -> None:
        parents = self.population.copy()
        self.population.clear()

        while len(parents) != len(self.population):
            parent1, parent2 = random.choices(parents, k=2)
            genes = (parent1.x, parent2.y) if random.choice([True, False]) else (parent2.x, parent1.y)
            self.population.append(Chromosome(*genes))
