import sympy as sp
import matplotlib.pyplot as plt
import mplcursors

from genetic_algorithm import GeneticAlgorithmIterator


class GeneticAlgorithmPlotVisualizer:
    def __init__(self, genetic_iterator: GeneticAlgorithmIterator) -> None:
        super().__init__()
        self.i = genetic_iterator
        self.func_pretty = sp.pretty(sp.Eq(sp.Symbol('f(x, y)'), genetic_iterator.func))

    def visualize_population(self) -> None:
        plt.plot()
        xs, ys = zip(*[ch.as_tuple() for ch in self.i.population])
        scatter = plt.scatter(xs, ys, color='black', s=10)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.xlim(self.i.bounds['x_min'], self.i.bounds['x_max'])
        plt.ylim(self.i.bounds['y_min'], self.i.bounds['y_max'])
        plt.title(self.func_pretty)
        plt.get_current_fig_manager().set_window_title(f'Популяция ({len(self.i.population)} хром.)')

        cursor = mplcursors.cursor(scatter, hover=True)

        @cursor.connect('add')
        def _(sel) -> None:
            index = sel.index
            ch, ht = self.i.population[index], self.i.health[index]
            sel.annotation.set(text=f'Хромосома ({ch.x:.2f}, {ch.y:.2f})\nЗдоровье: {ht:.2f}', backgroundcolor='lightgray',
                               alpha=1)

        plt.show()
