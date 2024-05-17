import pulp as pp


x1 = pp.LpVariable(name='x1', lowBound=0, cat=pp.LpInteger)
x2 = pp.LpVariable(name='x2', lowBound=0, cat=pp.LpInteger)
x3 = pp.LpVariable(name='x3', lowBound=0, cat=pp.LpInteger)
x4 = pp.LpVariable(name='x4', lowBound=0, cat=pp.LpInteger)
x5 = pp.LpVariable(name='x5', lowBound=0, cat=pp.LpInteger)
x6 = pp.LpVariable(name='x6', lowBound=0, cat=pp.LpInteger)


def get_expr(a, b, c, d, e, f):
    return a * x1 + b * x2 + c * x3 + d * x4 + e * x5 + f * x6


def fabric_lp_task(t1, t2, d1_args, d2_args):
    d1, d2 = get_expr(*d1_args), get_expr(*d2_args)
    obj_func = d1
    constraints = [
        pp.LpConstraint(d1 - d2, rhs=0, sense=pp.LpConstraintEQ, name='Количество деталей 1 вида равно количество деталей 2 вида'),
        pp.LpConstraint(x1 + x2 + x3, rhs=t1, sense=pp.LpConstraintLE, name=f'Количество ткани 1 вида не больше {t1}'),
        pp.LpConstraint(x4 + x5 + x6, rhs=t2, sense=pp.LpConstraintLE, name=f'Количество ткани 2 вида не больше {t2}'),
    ]
    problem = pp.LpProblem(name='Поиск максимального количества изделий', sense=pp.LpMaximize)
    for c in [obj_func] + constraints: problem += c
    return problem


def pformat_problem(problem):
    return '\n'.join([
        f'Статус: {pp.LpStatus[problem.status]} ({problem.status})',
        f'Результат: {problem.objective.value()}',
        *[f'{var.name:<2} = {int(var.value())}' for var in problem.variables()],
        *[f'{constraint}: {int(constraint.value() - constraint.constant)} ({int(constraint.value())})' for name, constraint in problem.constraints.items()],
    ])


if __name__ == '__main__':
    problem = fabric_lp_task(
        t1=300, t2=150,
        d1_args=(8, 0, 4, 12, 0, 6), d2_args=(0, 3, 1, 0, 4, 2)
    )
    problem.solve()
    print(pformat_problem(problem))
