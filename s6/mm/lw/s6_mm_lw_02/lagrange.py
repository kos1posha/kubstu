from functools import reduce

from sympy import *


def dict_exclude(target: dict, excluded: list):
    return {k: v for k, v in target.items() if k not in excluded}


def lagrange(func: Function, constraints: list[Eq]) -> (float, dict):
    # Шаг 1: Составление функции Лагранжа
    lambdas = symbols(f'λ:{len(constraints)}')
    constraint_exprs = [l * (c.rhs - c.lhs) for l, c in zip(lambdas, constraints)]
    constraint_sigma = reduce(lambda c1, c2: c1 + c2, constraint_exprs)
    composed_func = func + constraint_sigma

    # Шаг 2: Составление и решение системы частных производных, приравненных к нулю
    diff_system = []
    for s in composed_func.free_symbols:
        part_diff = composed_func.diff(s)
        diff_system.append(Eq(part_diff.simplify(), 0))
    point = solve(diff_system, composed_func.free_symbols)

    # Если система не имеет решений, значит целевая функция не имеет решений при данных ограничениях
    if not point:
        return None, None

    # Шаг 3: Расчет и возврат экстремума
    extr = func.subs(point)
    return extr, dict_exclude(point, lambdas)
