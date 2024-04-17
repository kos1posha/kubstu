import pulp as pp


# Объявляем переменные злп
A = pp.LpVariable(name='A', lowBound=0, cat=pp.LpInteger)
B = pp.LpVariable(name='B', lowBound=0, cat=pp.LpInteger)


def task():
    # Целевая функция (цена пакета акций)
    Count = A + B
    # Ограничения
    Price = (27 * A + 23 * B <= 930, 'Суммарная цена акций')
    B_max = (A >= B + 10, 'Число B превышает А')
    # Объявляем и заполняем модель, после чего находим решение
    problem = pp.LpProblem(name='Закупка_акций', sense=pp.LpMaximize)
    for f in [Count, Price, B_max]: problem += f
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
