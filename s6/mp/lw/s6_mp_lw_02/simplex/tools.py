from typing import Any, Union

from sympy import Basic, Eq, Float, Ge, Le, Rational, Symbol
from sympy.utilities.misc import as_int


def is_int(i):
    try:
        as_int(i, strict=False)
    except:
        return False
    return True


def num(x: Any):
    def tryfloat(x):
        try:
            return float(x)
        except:
            return x

    def tryint(x):
        try:
            return int(x)
        except:
            return x

    if isinstance(x, str):
        if '.' in x:
            return round(tryfloat(x), 2)
        else:
            return tryint(x)
    if is_int(x):
        return int(x)
    if isinstance(x, (Rational, Float)):
        return round(float(x), 2)
    return x


def sort_symbols(symbols: set[Basic]) -> list[Basic]:
    return sorted(symbols, key=lambda s: s.name)


def ineq_to_eq(ineq: Union[Ge, Le], sym: Symbol) -> Eq:
    if ineq.rel_op == '>=':
        return Eq(ineq.lhs - sym, ineq.rhs)
    elif ineq.rel_op == '<=':
        return Eq(ineq.lhs + sym, ineq.rhs)


def canonicalize_eq(eq: Eq) -> Eq:
    expr = eq.lhs - eq.rhs
    const = sum(x for x in expr.as_ordered_terms() if x.is_number)
    if const < 0:
        const, expr = -const, -expr
    return Eq(const - expr, const)


def range_exclude(stop: int, exclude: int) -> list[int]:
    return list(range(exclude)) + list(range(exclude + 1, stop))
