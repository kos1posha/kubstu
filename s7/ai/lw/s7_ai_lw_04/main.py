import sympy as sp

from genetic_algorithm import GeneticAlgorithmIterator
from visualizer import GeneticAlgorithmPlotVisualizer


def main() -> None:
    x, y = sp.symbols('x y')
    func = x * y
    bounds = {'x': (-10, 10), 'y': (-10, 10)}
    iterator = GeneticAlgorithmIterator(func, bounds, 'min', population_size=5000, max_iteration=100)
    visualizer = GeneticAlgorithmPlotVisualizer(iterator)

    visualizer.visualize_population()
    for _ in iterator:
        for _ in range(10):
            next(iterator)
        visualizer.visualize_population()


if __name__ == "__main__":
    main()
