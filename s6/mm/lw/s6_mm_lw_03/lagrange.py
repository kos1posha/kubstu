from functools import reduce
import sys
from typing import Dict, List, Union

from sympy import Eq, Function, Ge, Le, solve, symbols


def dict_exclude(target: Dict, excluded: List) -> Dict:
    return {k: v for k, v in target.items() if k not in excluded}


def lagrange(func: Function, constraints: List[Union[Eq, Ge, Le]]) -> (float, Dict):
    # Шаг 1: Составление функции Лагранжа
    lambdas = symbols(f'λ:{len(constraints)}')
    constraint_exprs = [l * (c.rhs - c.lhs) for l, c in zip(lambdas, constraints)]
    constraint_sigma = reduce(lambda c1, c2: c1 + c2, constraint_exprs)
    composed_func = func + constraint_sigma

    # Шаг 2: Составление системы условий Куна-Таккера
    kt_equalities = []
    kt_inequalities = constraints
    for s in func.free_symbols:
        part_diff = composed_func.diff(s)
        kt_equalities.append(Eq(part_diff.simplify(), 0))
    for i, ce in enumerate(constraint_exprs):
        kt_equalities.append(Eq(ce, 0))
        if i == 0:
            kt_equalities.append(Eq(lambdas[i], 0))
        else:
            kt_inequalities.append(Ge(lambdas[i], 0))

    # Шаг 3: Решение системы условий Куна-Таккера
    points = solve(kt_equalities, composed_func.free_symbols)
    for p in points:
        res = func.subs(p)
    if not isinstance(points, list):
        points = [points]
    for p in reversed(points):
        if not all([ineq.subs(p) for ineq in kt_inequalities]):
            points.remove(p)

    # Если система не имеет решений, значит целевая функция не имеет решений при данных ограничениях
    if not points:
        return None, None

    # Шаг 4: Расчет и возврат экстремума
    extr = sys.maxsize
    point = None
    for p in points[:1]:
        p_val = func.subs(p)
        if p_val < extr:
            extr = p_val
            point = p
    return extr, dict_exclude(point, lambdas)
