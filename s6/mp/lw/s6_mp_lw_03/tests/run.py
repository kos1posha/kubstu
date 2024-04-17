from copy import deepcopy
import time
from typing import List

from tests.source import all_tests


def pretty_list(lst: List, w: int = 5):
    return '[' + ', '.join([str(i).rjust(w) for i in lst]) + ']'


def pretty_matrix(mtx: List[List], w: int = 3):
    return '\n'.join([pretty_list(lst, w) for lst in mtx])


def run_test(test, p=False):
    test = deepcopy(test)
    name, solver, expected = test.pop('name'), test.pop('solver'), test.pop('expected')

    exec_time = -time.time()
    transport = solver(**test)
    total_cost, solution = transport.solve()
    exec_time += time.time()

    assert (total_cost, solution) == expected, f'Тест {name} не пройден!\n\t\tactual: {(total_cost, solution)}\n\t\texpected:{expected}'
    if p: print(pretty_matrix(solution))
    print(f'Тест {name} пройден! [{exec_time * 1000:.0f}ms]')
    return True


def run_tests(tests, p=False):
    for test in tests:
        run_test(test, p)


if __name__ == '__main__':
    run_tests(all_tests)
