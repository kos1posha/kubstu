import pulp as pp


# Объявляем переменные злп
x1 = pp.LpVariable(name='x1', lowBound=0, cat=pp.LpInteger)
x2 = pp.LpVariable(name='x2', lowBound=0, cat=pp.LpInteger)
x3 = pp.LpVariable(name='x3', lowBound=0, cat=pp.LpInteger)
x4 = pp.LpVariable(name='x4', lowBound=0, cat=pp.LpInteger)
x5 = pp.LpVariable(name='x5', lowBound=0, cat=pp.LpInteger)


def task():
    # Целевая функция (цена пакета акций)
    q = lambda a, b, c, d, e: a * x1 + b * x2 + c * x3 + d * x4 + e * x5
    d1 = q(0, 2, 9, 6, 5)
    d2 = q(4, 3, 4, 5, 4)
    d3 = q(10, 16, 0, 8, 0)
    obj_f = (d1 / 4 + d2 / 3 + d3 / 2) / 3
    # Ограничения
    constraints = [
        pp.LpConstraint(3 * d1 - 4 * d2, sense=0, name='1', rhs=0),
        pp.LpConstraint(2 * d2 - 3 * d3, sense=0, name='2', rhs=0),
        pp.LpConstraint(4 * d3 - 2 * d1, sense=0, name='3', rhs=0),
        (x1 + x2 + x3 <= 500, '4'),
        (x4 + x5 <= 300, '5'),
    ]
    # Объявляем и заполняем модель, после чего находим решение
    problem = pp.LpProblem(name='aaaa', sense=pp.LpMaximize)
    for c in [obj_f] + constraints: problem += c
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
    task()
