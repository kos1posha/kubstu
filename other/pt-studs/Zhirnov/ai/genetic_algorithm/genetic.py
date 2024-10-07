import random

import sympy as sp

import chromosome as ch
import visualizer as v


class OptDir:
    MAXIMIZATION = 'max'
    MINIMIZATION = 'min'


class GeneticAlgorithmIterator:
    def __init__(self, func: sp.Expr, bounds: dict[sp.Symbol, tuple[float, float]], opt_dir: str = OptDir.MAXIMIZATION, population_size: int = 10, max_iteration: int = 1, visualizer: v.BaseGeneticAlgorithmVisualizer = None):
        self.func = func
        self.bounds = bounds
        self.opt_dir = opt_dir
        self.population_size = population_size
        self.max_iteration = max_iteration
        self.visualizer = visualizer

        self.population = initialization(bounds, population_size, v=self.visualizer)
        self.current_iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_iteration < self.max_iteration:
            health = evaluation(self.func, self.population)
            selection(self.population, health, self.opt_dir)
            recombination(self.population, v=self.visualizer)
            self.current_iteration += 1
            return self.population, health
        else:
            raise StopIteration


def genetic(func: sp.Expr, bounds: dict[sp.Symbol, (float, float)], opt_dir: str = OptDir.MAXIMIZATION, population_size: int = 10, max_iteration: int = 1, visualizer: v.BaseGeneticAlgorithmVisualizer = None):
    population = initialization(bounds, population_size, v=visualizer)
    for i in range(max_iteration):
        health = evaluation(func, population)
        selection(population, health, opt_dir)
        recombination(population, v=visualizer)


def initialization(bounds: dict[sp.Symbol, (float, float)], population_size: int, v: v.BaseGeneticAlgorithmVisualizer = None) -> list[ch.Chromosome]:
    population = []
    for _ in range(population_size):
        kwargs = {}
        for symbol, min_max in bounds.items():
            kwargs[str(symbol)] = round(random.uniform(*min_max), 2)
        population.append(ch.Chromosome(**kwargs))

    if v:
        v.visualize_population(population)
    return population


def evaluation(func: sp.Expr, population: list[ch.Chromosome], v: v.BaseGeneticAlgorithmVisualizer = None) -> list[float]:
    health = [func.subs(c.kw_dict) for c in population]

    if v:
        v.visualize_health(population, health)
    return health


def selection(population: list[ch.Chromosome], health: list[float], opt_dir: str, v: v.BaseGeneticAlgorithmVisualizer = None) -> None:
    match opt_dir:
        case OptDir.MAXIMIZATION:
            shift = -min(health)
            total_health = sum(health, start=len(population) * shift)
            probabilities = [(shift + health) / total_health for health in health]
        case OptDir.MINIMIZATION:
            shift = max(health)
            total_health = -sum(health, start=-len(population) * shift)
            probabilities = [(shift - health) / total_health for health in health]
        case _:
            raise NotImplementedError()

    old_population = [*population]
    population.clear()
    population.extend(random.choices(old_population, probabilities, k=len(old_population)))

    if v:
        v.visualize_population(population)


def recombination(population: list[ch.Chromosome], v: v.BaseGeneticAlgorithmVisualizer = None) -> None:
    old_population = [*population]
    population.clear()

    while len(old_population) != len(population):
        parent1, parent2 = random.choices(old_population, k=2)
        child = ch.Chromosome(**{
            parent1.attrs[0]: parent1.vals[0], parent2.attrs[1]: parent2.vals[1]
        } if random.choice([True, False]) else {
            parent2.attrs[0]: parent2.vals[0], parent1.attrs[1]: parent1.vals[1]
        })
        population.append(child)

    if v:
        v.visualize_population(population)
