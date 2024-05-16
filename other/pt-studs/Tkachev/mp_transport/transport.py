import sys
from typing import List, Tuple


class BaseTransportProblemSolver:
    verbose_name = 'База'

    def __init__(self, costs: List[List[int]], supply: List[int], demand: List[int]):
        if not self._problem_is_valid(costs, supply, demand):
            raise ValueError('Problem\'s given is not valid')
        if not self._problem_is_balanced(supply, demand):
            # TODO чета там сделать, чтобы чики пики было
            raise NotImplementedError('Unbalanced problems are not supported')

        self.given_costs = costs
        self.given_supply = supply
        self.given_demand = demand

        self._height = len(supply)
        self._width = len(demand)
        self._solution = [[0 for _ in range(self._width)] for _ in range(self._height)]
        self._output = []

    def __call__(self) -> Tuple[int, List[List[int]]]:
        return self.solve()

    def solve(self) -> Tuple[int, List[List[int]]]:
        if not self._solution:
            return self.calculate_cost(self._solution), self._solution

        self._solve_implementation(self.given_costs.copy(), self.given_supply.copy(), self.given_demand.copy())
        return self.calculate_cost(self._solution), self._solution

    def calculate_cost(self, solution: List[List[int]]) -> int:
        return sum(sum(s * c for s, c in zip(s, c)) for s, c in zip(solution, self.given_costs))

    def _problem_is_valid(self, table: List[List[int]], supply: List[int], demand: List[int]) -> bool:
        lengths = [len(row) for row in table]
        lengths_set = set(lengths)
        return len(lengths_set) == 1 and len(supply) == len(lengths) and len(demand) == lengths_set.pop()

    def _problem_is_balanced(self, supply: List[int], demand: List[int]) -> bool:
        return sum(supply) == sum(demand)

    def _solve_implementation(self, costs: List[List[int]], supply: List[int], demand: List[int]) -> None:
        raise NotImplementedError('Solve method should be implemented in subclasses')

    def _calculate_diff(self, i: int, j: int, supply: List[int], demand: List[int]) -> int:
        diff = min(supply[i], demand[j])
        demand[j] -= diff
        supply[i] -= diff
        return diff


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
