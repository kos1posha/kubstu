from typing import List


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

    def __call__(self) -> List[List[int]]:
        return self.solve()

    def solve(self) -> (List[List[int]], int):
        if not self._solution:
            return self._solution
        self._solve_implementation(self.given_costs.copy(), self.given_supply.copy(), self.given_demand.copy())
        return self.calculate_cost(self._solution), self._solution

    def calculate_cost(self, solution: List[List[int]]):
        return sum(sum(s * c for s, c in zip(s, c)) for s, c in zip(solution, self.given_costs))

    def _problem_is_valid(self, table: List[List[int]], supply: List[int], demand: List[int]) -> bool:
        lengths = [len(row) for row in table]
        lengths_set = set(lengths)
        return len(lengths_set) == 1 and len(supply) == len(lengths) and len(demand) == lengths_set.pop()

    def _problem_is_balanced(self, supply: List[int], demand: List[int]) -> bool:
        return sum(supply) == sum(demand)

    def _solve_implementation(self, costs, supply, demand):
        raise NotImplementedError('Solve method should be implemented in subclasses')

    def _calculate_cell(self, i, j, supply, demand):
        diff = min(supply[i], demand[j])
        demand[j] -= diff
        supply[i] -= diff
        return diff
