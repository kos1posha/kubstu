import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import mplcursors

from genetic_algorithm import GeneticAlgorithmIterator


cmap = cm.get_cmap('Reds_r')


class GeneticAlgorithmPlotVisualizer:
    def __init__(self, genetic_iterator: GeneticAlgorithmIterator) -> None:
        super().__init__()
        self.i = genetic_iterator
        self.X, self.Y = np.meshgrid(np.linspace(*self.i.bounds['x'], 25), np.linspace(*self.i.bounds['y'], 25))
        self.C = self.i._np_func(self.X, self.Y)
        self.func_pretty = sp.pretty(sp.Eq(sp.Symbol('f(x, y)'), genetic_iterator.func))

    def visualize_population(self) -> None:
        plt.plot()
        xs, ys = zip(*self.i.population)
        plt.pcolormesh(self.X, self.Y, self.C, cmap=cmap)
        scatter = plt.scatter(xs, ys, color='black', s=5)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.xlim(self.i.bounds['x'])
        plt.ylim(self.i.bounds['y'])
        plt.title(self.func_pretty)
        plt.get_current_fig_manager().set_window_title(f'Популяция ({self.i.population_size} хром.)')

        cursor = mplcursors.cursor(scatter, hover=True)

        @cursor.connect('add')
        def _(sel) -> None:
            index = sel.index
            ch, ht = self.i.population[index], self.i.health[index]
            sel.annotation.set_text(f'Хромосома ({ch[0]:.2f}, {ch[1]:.2f})\nЗдоровье: {ht:.2f}')
            sel.annotation.get_bbox_patch().set(fc='lightgray', alpha=1)

        plt.show()
