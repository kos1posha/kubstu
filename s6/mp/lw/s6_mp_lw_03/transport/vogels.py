import sys

from transport import BaseTransportProblemSolver


def transpose_matrix(mtx):
    return [list(row) for row in zip(*mtx)]


class VogelsApproximationTransportProblemSolver(BaseTransportProblemSolver):
    verbose_name = 'Метод аппроксимации Фогеля'

    def _solve_implementation(self, costs, supply, demand):
        costs_transposed = transpose_matrix(costs)

        while any(supply) and any(demand):
            supply_max_penalty, supply_max_penalty_i = self._calculate_penalties(costs, supply, demand)
            demand_max_penalty, demand_max_penalty_i = self._calculate_penalties(costs_transposed, demand, supply)

            if supply_max_penalty > demand_max_penalty:
                i = supply_max_penalty_i
                j = self._find_min_penalty(costs, i, demand)
                cell = self._calculate_cell(i, j, supply, demand)
                self._solution[i][j] = cell
            else:
                j = demand_max_penalty_i
                i = self._find_min_penalty(costs_transposed, j, supply)
                cell = self._calculate_cell(i, j, supply, demand)
                self._solution[i][j] = cell

    def _calculate_penalties(self, costs, passed_rows, passed_cols):
        max_penalty, max_penalty_i = 1 - sys.maxsize, -1
        for i, row in [(i, row) for i, row in enumerate(costs) if passed_rows[i] != 0]:
            sorted_row = sorted(el for j, el in enumerate(row) if passed_cols[j] != 0)
            current = sorted_row[1] - sorted_row[0] if len(sorted_row) > 1 else 0
            if max_penalty < current:
                max_penalty, max_penalty_i = current, i
            max_penalty = max(max_penalty, current)
        return max_penalty, max_penalty_i

    def _find_min_penalty(self, costs, max_penalty_i, passed_indexes):
        penalties = [(i, el) for i, el in enumerate(costs[max_penalty_i]) if passed_indexes[i] != 0]
        return min(penalties, key=lambda p: p[1])[0]
