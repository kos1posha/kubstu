from sympy import Ge, symbols

from lagrange import lagrange


def task1(a=(4, 5), c=(6, 7, 1)):
    x, y = symbols('x y')
    func = a[0] * x ** 2 + a[1] * y ** 2
    constraints = [Ge(c[0] * x + c[1] * y, c[2])]
    return lagrange(func, constraints)


def task2(a=(1, 5, 6, 1), cs=((2, 7, 4), (5, 3, 3))):
    x, y = symbols('x y')
    func = a[0] * x ** 2 + a[1] * x + a[2] * y ** 2 + a[3] * y
    constraints = [Ge(c[0] * x + c[1] * y, c[2]) for c in cs]
    return lagrange(func, constraints)


if __name__ == '__main__':
    extr, point = task2()
    print(f'Экстремум функции достигается в точке {point} при значении {extr}')
