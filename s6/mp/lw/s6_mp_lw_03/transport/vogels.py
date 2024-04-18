import sys
from typing import List, Tuple

from transport import BaseTransportProblemSolver


def transpose_matrix(mtx):
    return [list(row) for row in zip(*mtx)]


class VogelsApproximationTransportProblemSolver(BaseTransportProblemSolver):
    verbose_name = 'Метод аппроксимации Фогеля'

    def _solve_implementation(self, costs: List[List[int]], supply: List[int], demand: List[int]) -> None:
        costs_transposed = transpose_matrix(costs)

        while any(supply) and any(demand):
            supply_max_penalty, supply_max_penalty_i, supply_penalties = self._calculate_penalties(costs, supply, demand)
            demand_max_penalty, demand_max_penalty_i, demand_penalties = self._calculate_penalties(costs_transposed, demand, supply)

            min_max = supply_max_penalty < demand_max_penalty
            if not min_max:
                i, j = supply_max_penalty_i, self._find_min_penalty(costs, supply_max_penalty_i, demand)
            else:
                i, j = self._find_min_penalty(costs_transposed, demand_max_penalty_i, supply), demand_max_penalty_i

            diff = self._calculate_diff(i, j, supply, demand)
            self._solution[i][j] = diff
            self._output.append({
                'supply_penalties': supply_penalties,
                'demand_penalties': demand_penalties,
                'min_max': min_max,
                'cell': (i, j),
                'diff': diff,
                'supply': supply.copy(),
                'demand': demand.copy(),
            })

    def _calculate_penalties(self, costs: List[List[int]], passed_rows: List[int], passed_cols: List[int]) -> Tuple[int, int, List[Tuple[int, int]]]:
        penalties = []
        max_penalty, max_penalty_i = 1 - sys.maxsize, -1
        for i, row in [(i, row) for i, row in enumerate(costs) if passed_rows[i] != 0]:
            sorted_row = sorted(el for j, el in enumerate(row) if passed_cols[j] != 0)
            current = sorted_row[1] - sorted_row[0] if len(sorted_row) > 1 else 0
            penalties.append((i, current))
            if max_penalty < current:
                max_penalty, max_penalty_i = current, i
            max_penalty = max(max_penalty, current)
        return max_penalty, max_penalty_i, penalties

    def _find_min_penalty(self, costs: List[List[int]], max_penalty_i: int, passed_indexes: List[int]) -> int:
        penalties = [(i, el) for i, el in enumerate(costs[max_penalty_i]) if passed_indexes[i] != 0]
        return min(penalties, key=lambda p: p[1])[0]
