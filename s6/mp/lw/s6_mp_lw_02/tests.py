from copy import deepcopy
import time

from sympy import Eq, Integer as I, Rational as R, symbols

from simplex import Search, Simplex


x1, x2, x3, x4, x5 = symbols('x1:6')

test1 = {
    'search': Search.MAX,
    'obj_func': 3 * x1 + x2,
    'constraints': [
        x1 - 2 * x2 <= 1,
        -2 * x1 + x2 <= 2,
        2 * x1 + x2 <= 6
    ],

    'name': '1',
    'expected': ({x1: R(13, 5), x2: R(4, 5)}, R(43, 5))
}

test2 = {
    'search': Search.MAX,
    'obj_func': 2 * x1 - x2 + 3 * x3 - 2 * x4 + x5,
    'constraints': [
        Eq(-x1 + x2 + x3, 1),
        Eq(x1 - x2 + x4, 1),
        Eq(x1 - 2 * x2 + x5, 2)
    ],

    'name': '2',
    'expected': ({x1: I(1), x2: 0, x3: I(2), x4: 0, x5: I(1)}, I(9))
}

test3 = {
    'search': Search.MAX,
    'obj_func': -2 * x1 - x2,
    'constraints': [
        Eq(-x1 - x2 - x3, -2),
        -4 * x2 - 2 * x5 >= -10,
        Eq(-2 * x2 - x3 - x4, -1)
    ],

    'name': '3',
    'expected': ({x1: I(1), x2: 0}, I(-2))
}

test4 = {
    'search': Search.MAX,
    'obj_func': x1 + 2 * x2,
    'constraints': [
        x1 + 2 * x2 <= 6,
        2 * x1 + x2 <= 8,
        x2 <= 2,
        x1 >= 0
    ],

    'name': '4',
    'expected': ({x1: I(2), x2: I(2)}, I(6))
}


def run_test(test, p=False):
    test = deepcopy(test)
    name, expected = test.pop('name'), test.pop('expected')

    exec_time = -time.time()
    simplex = Simplex(**test)
    point, expr = simplex.solve()
    exec_time += time.time()

    assert (point, expr) == expected, f'Тест {name} не пройден!\n\t\tactual: {(point, expr)}\n\t\texpected:{expected}'
    if p: print(simplex.pretty_history())
    print(f'Тест {name} пройден! [{exec_time * 1000:.0f}ms]')
    return True


def run_all(p=False):
    for test in [test1, test2, test3, test4]:
        run_test(test, p)


if __name__ == '__main__':
    run_all()
