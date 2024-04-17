from functools import reduce

from sympy import Eq, symbols

from lagrange import lagrange


def example():
    x1, x2 = symbols('x1 x2')
    func = x1 ** 2 + x2 ** 2
    constraints = [Eq(2 * x1 + x2 - 2, 0)]
    return lagrange(func, constraints)


def task1(a=(3, 2, 1), b=(1, 3, 2), d=2):
    x1, x2 = symbols('x1 x2')
    func = (a[0] + a[1] * x1 + a[2] * x1 ** 2) + (b[0] + b[1] * x2 + b[2] * x2 ** 2)
    constraints = [Eq(x1 + x2, d)]
    return lagrange(func, constraints)


def task2(sd=(6, 4, 5, 4, 4), mr=(3, 5, 2, 5, 3), mp=4):
    o = symbols(f'o1:{len(mr) + 1}')
    func = reduce(lambda f1, f2: f1 + f2, [sdi ** 2 * oi ** 2 for sdi, oi in zip(sd, o)])
    constraints = [Eq(sum(o), 1), Eq(sum([mri * oi for mri, oi in zip(mr, o)]), mp)]
    return lagrange(func, constraints)


if __name__ == '__main__':
    extr, point = task2(sd=(5, 5, 8, 4), mr=(3, 5, 7, 7), mp=6)
    print(f'Экстремум функции достигается в точке {point} при значении {extr}')
