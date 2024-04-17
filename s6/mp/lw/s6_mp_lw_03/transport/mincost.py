from transport import BaseTransportProblemSolver


class MinimalCostTransportProblemSolver(BaseTransportProblemSolver):
    def _solve_implementation(self, costs, supply, demand):
        inline_costs = sum([[(cost, i, j) for j, cost in enumerate(row)] for i, row in enumerate(costs)], [])
        sorted_costs = sorted(inline_costs, key=lambda c: c[0])
        for _, i, j in sorted_costs:
            self._solution[i][j] = self._calculate_cell(i, j, supply, demand)
            self._output
