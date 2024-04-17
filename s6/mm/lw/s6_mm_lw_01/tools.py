from simplex import SimplexMethod


def info(s):
    return f'\033[96m{s}\033[0m'


def success(s):
    return f'\033[92m{s}\033[0m'


def tryint(num: float):
    if isinstance(num, float) and num.is_integer():
        return int(num)
    return num


def simplex_state_format(simplex: SimplexMethod) -> str:
    return ''.join(map(str, [
        info(f'Симплекс-таблица ({simplex.m}x{simplex.n}): '), '\n',
        matrix_format(simplex.table), '\n',
        info(f'Базисный вектор: '), tuple(simplex.basis)
    ]))


def matrix_format(target: list[list]) -> str:
    return '\n'.join(['  '.join([str(tryint(x))[:4].ljust(4) for x in row]) for row in target])
