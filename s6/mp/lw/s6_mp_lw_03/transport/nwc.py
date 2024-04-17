from transport.base import BaseTransportProblemSolver


class NorthWestCornerTransportProblemSolver(BaseTransportProblemSolver):
    def _solve_implementation(self, costs, supply, demand):
        next_demand_i = 0
        for i, row in enumerate(self.given_costs):
            for j in range(next_demand_i, self._width):
                self._solution[i][j] = self._calculate_cell(i, j, supply, demand)
                next_demand_i += int(supply[i] > demand[j])
