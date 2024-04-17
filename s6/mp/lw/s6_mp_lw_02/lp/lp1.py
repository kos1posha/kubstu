import pulp as pp


# Объявляем переменные злп
T = pp.LpVariable(name='Столы', lowBound=0, cat=pp.LpInteger)
C = pp.LpVariable(name='Шкафы', lowBound=0, cat=pp.LpInteger)


def task():
    # Целевая функция (цена пакета акций)
    Stonks = 60 * T + 80 * C
    # Ограничения
    constraints = [
        (0.2 * T + 0.1 * C <= 40, 'Количество_дуба'),
        (0.1 * T + 0.3 * C <= 60, 'Количество_ореха'),
        (1.2 * T + 1.5 * C <= 371.4, 'Трудоемкость_(чел/час)'),
    ]
    # Объявляем и заполняем модель, после чего находим решение
    problem = pp.LpProblem(name='Прибыль_от_производства_столов_и_шкафов', sense=pp.LpMaximize)
    for c in [Stonks] + constraints: problem += c
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
