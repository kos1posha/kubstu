import mplcursors
import sympy as sp

import matplotlib.pyplot as plt
import chromosome as ch


class BaseGeneticAlgorithmVisualizer:
    def __init__(self):
        pass

    def visualize_population(self, population: list[ch.Chromosome]):
        raise NotImplementedError()

    def visualize_health(self, population: list[ch.Chromosome], health: list[float]):
        raise NotImplementedError()


class GeneticAlgorithmPlotVisualizer(BaseGeneticAlgorithmVisualizer):
    def __init__(self, func: sp.Expr, bounds: dict[sp.Symbol, (float, float)], activated: bool = True):
        super().__init__()
        self.func = func
        self.z_func = sp.Eq(sp.symbols('z'), func)
        self.bounds = {str(s): b for s, b in bounds.items()}
        self.activated = activated

    def activate(self):
        self.activated = True

    def deactivate(self):
        self.activated = False

    def visualize_population(self, population: list[ch.Chromosome]):
        if not self.activated:
            return

        sample = population[0]
        if len(sample.kw_dict) != 2:
            raise NotImplementedError('Доступна визуализация только двумерных сущностей')

        plt.plot()
        xs, ys = zip(*[[c[attr] for attr in c.attrs] for c in population])
        scatter = plt.scatter(xs, ys, color='black', s=10)

        plt.xlabel(sample.attrs[0])
        plt.ylabel(sample.attrs[1])
        plt.xlim(*self.bounds[sample.attrs[0]])
        plt.ylim(*self.bounds[sample.attrs[1]])
        plt.title(sp.pretty(self.z_func))
        plt.get_current_fig_manager().set_window_title(f'Популяция ({len(population)} хром.)')

        cursor = mplcursors.cursor(scatter, hover=True)

        @cursor.connect('add')
        def on_add(sel):
            index = sel.index
            x, y = xs[index], ys[index]
            result = self.func.subs({sample.attrs[0]: x, sample.attrs[1]: y})
            sel.annotation.set(
                text=f'Точка ({x:.2f}, {y:.2f})\nЗначение функции: {result:.2f}',
                alpha=1, backgroundcolor='lightgray'
            )

        plt.show()

    def visualize_health(self, population: list[ch.Chromosome], health: list[float]):
        if not self.activated:
            return

        headers = [['Хромосома', *population[0].attrs, 'Здоровье']]
        data = [[f'C{i}', *c.vals, f'{h:.2f}'] for i, (c, h) in enumerate(zip(population, health))]

        fig, ax = plt.subplots()
        ax.table(cellText=headers + data, cellLoc='center', loc='center')

        ax.axis('off')
        plt.title(sp.pretty(self.z_func))
        plt.get_current_fig_manager().set_window_title(f'Здоровье популяции')

        plt.show()
