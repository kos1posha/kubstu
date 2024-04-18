from transport.base import BaseTransportProblemSolver


class NorthWestCornerTransportProblemSolver(BaseTransportProblemSolver):
    verbose_name = 'Метод северо-западного угла'

    def _solve_implementation(self, costs, supply, demand):
        next_demand_i = 0
        for i, row in enumerate(self.given_costs):
            for j in range(next_demand_i, self._width):
                if supply[i] == 0 or demand[j] == 0:
                    break
                next_demand_i += int(supply[i] > demand[j])
                diff = self._calculate_diff(i, j, supply, demand)
                self._solution[i][j] = diff
                self._output.append({
                    'cell': (i, j),
                    'diff': diff,
                    'supply': supply.copy(),
                    'demand': demand.copy(),
                })
