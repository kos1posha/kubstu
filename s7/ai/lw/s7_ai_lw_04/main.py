import sympy as sp

from genetic_algorithm import GeneticAlgorithmIterator
from visualizer import GeneticAlgorithmPlotVisualizer


def main() -> None:
    x, y = sp.symbols('x y')
    func = x * y
    bounds = {'x_min': -10, 'x_max': 10, 'y_min': -10, 'y_max': 10}
    iterator = GeneticAlgorithmIterator(func, bounds, 'max', population_size=1000, max_iteration=100)
    visualizer = GeneticAlgorithmPlotVisualizer(iterator)

    visualizer.visualize_population()
    for _ in iterator:
        visualizer.visualize_population()


if __name__ == "__main__":
    main()
