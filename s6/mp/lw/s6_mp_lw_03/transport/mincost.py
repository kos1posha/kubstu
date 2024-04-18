from transport import BaseTransportProblemSolver


class MinimalCostTransportProblemSolver(BaseTransportProblemSolver):
    verbose_name = 'Метод наименьшей стоимости'

    def _solve_implementation(self, costs, supply, demand):
        inline_costs = sum([[(cost, i, j) for j, cost in enumerate(row)] for i, row in enumerate(costs)], [])
        sorted_costs = sorted(inline_costs, key=lambda c: c[0])
        for c, i, j in sorted_costs:
            if supply[i] == 0 or demand[j] == 0:
                continue
            diff = self._calculate_cell(i, j, supply, demand)
            self._solution[i][j] = diff
            self._output.append({
                'min_cost': c,
                'cell': (i, j),
                'diff': diff,
                'supply': supply.copy(),
                'demand': demand.copy(),
            })
