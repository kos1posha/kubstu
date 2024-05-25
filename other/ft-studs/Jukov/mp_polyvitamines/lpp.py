import pulp as pp


# Объявляем переменные злп
C1 = pp.LpVariable(name='C1', lowBound=0, cat=pp.LpInteger)
C2 = pp.LpVariable(name='C2', lowBound=0, cat=pp.LpInteger)
C3 = pp.LpVariable(name='C3', lowBound=0, cat=pp.LpInteger)
C4 = pp.LpVariable(name='C4', lowBound=0, cat=pp.LpInteger)
C5 = pp.LpVariable(name='C5', lowBound=0, cat=pp.LpInteger)
C6 = pp.LpVariable(name='C6', lowBound=0, cat=pp.LpInteger)
C7 = pp.LpVariable(name='C7', lowBound=0, cat=pp.LpInteger)

problem_name = 'Курс_витаминов'


def vit_expr(c1, c2, c3, c4, c5, c6, c7):
    """ Возвращает выражение суммы витаминов с заданными коэффициентами """
    return c1 * C1 + c2 * C2 + c3 * C3 + c4 * C4 + c5 * C5 + c6 * C6 + c7 * C7


def vit_me(c1, c2, c3, c4, c5, c6, c7, rhs):
    """ Возвращает неравенство (>=) суммы витаминов с заданными коэффициентами и правой частью """
    return vit_expr(c1, c2, c3, c4, c5, c6, c7) >= rhs


def vit_solve(a, c, b6, p):
    problem = pp.LpProblem(name=problem_name, sense=pp.LpMinimize)
    problem += (vit_me(*a), 'A')
    problem += (vit_me(*c), 'C')
    problem += (vit_me(*b6), 'B6')
    problem += vit_expr(*p)
    problem.solve()
    return problem


def task():
    # Целевая функция (цена курса витаминов)
    Price = 4 * C1 + 1 * C2 + 5 * C3 + 6 * C4 + 3.5 * C5 + 7 * C6 + 4 * C7
    # Ограничения
    A_req = (5 * C1 + 0 * C2 + 2 * C3 + 0 * C4 + 3 * C5 + 1 * C6 + 2 * C7 >= 100, 'A')
    C_req = (3 * C1 + 1 * C2 + 5 * C3 + 0 * C4 + 2 * C5 + 0 * C6 + 1 * C7 >= 80, 'C')
    B6_req = (1 * C1 + 0 * C2 + 3 * C3 + 1 * C4 + 2 * C5 + 0 * C6 + 6 * C7 >= 120, 'B6')
    # Объявляем и заполняем модель, после чего находим решение
    problem = pp.LpProblem(name=problem_name, sense=pp.LpMinimize)
    for f in [Price, A_req, C_req, B6_req]: problem += f
    problem.solve()
    # Вывод результата
    print(
        f'Статус: {pp.LpStatus[problem.status]} ({problem.status})',
        f'Результат: {problem.objective.value()}',
        *[f'{var.name:<2} = {int(var.value())}' for var in problem.variables()],
        *[f'{name:<2} = {int(constraint.value() - constraint.constant)} ({int(constraint.value())})' for name, constraint in problem.constraints.items()],
        sep='\n', end=''
    )


if __name__ == '__main__':
    a = [5, 0, 2, 0, 3, 1, 2, 100]
    c = [3, 1, 5, 0, 2, 0, 1, 80]
    b6 = [1, 0, 3, 1, 2, 0, 6, 120]
    p = [4, 1, 5, 6, 3.5, 7, 4]
    vit_solve(a, c, b6, p)
