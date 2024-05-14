import pulp as pp


x1 = pp.LpVariable(name='x1', lowBound=0, cat=pp.LpInteger)
x2 = pp.LpVariable(name='x2', lowBound=0, cat=pp.LpInteger)
x3 = pp.LpVariable(name='x3', lowBound=0, cat=pp.LpInteger)
x4 = pp.LpVariable(name='x4', lowBound=0, cat=pp.LpInteger)
x5 = pp.LpVariable(name='x5', lowBound=0, cat=pp.LpInteger)


def get_expr(a, b, c, d, e):
    return a * x1 + b * x2 + c * x3 + d * x4 + e * x5


def details_lp_task(details_set, c1_args, c2_args, c3_args, p=False):
    ds = details_set
    c1, c2, c3 = get_expr(*c1_args), get_expr(*c2_args), get_expr(*c3_args)
    obj_func = c1
    constraints = [
        pp.LpConstraint(ds[1] * c1 - ds[0] * c2, rhs=0, sense=pp.LpConstraintEQ, name='Отношение деталей 1 к деталям 2'),
        pp.LpConstraint(ds[2] * c2 - ds[1] * c3, rhs=0, sense=pp.LpConstraintEQ, name='Отношение деталей 2 к деталям 3'),
        pp.LpConstraint(ds[0] * c3 - ds[2] * c1, rhs=0, sense=pp.LpConstraintEQ, name='Отношение деталей 3 к деталям 1'),
        pp.LpConstraint(x1 + x2 + x3, rhs=500, sense=pp.LpConstraintLE, name='Количество листов металла 1 размера не больше 500'),
        pp.LpConstraint(x4 + x5, rhs=300, sense=pp.LpConstraintLE, name='Количество листов металла 2 размера не больше 300'),
    ]
    problem = pp.LpProblem(name='Поиск максимального количества комплектов деталей', sense=pp.LpMaximize)
    for c in [obj_func] + constraints: problem += c
    problem.solve()
    if p:
        print(
            f'Статус: {pp.LpStatus[problem.status]} ({problem.status})',
            f'Результат: {problem.objective.value()}',
            *[f'{var.name:<2} = {int(var.value())}' for var in problem.variables()],
            *[f'{name:<2} = {int(constraint.value() - constraint.constant)} ({int(constraint.value())})' for name, constraint in problem.constraints.items()],
            sep='\n', end=''
        )


details_set = (4, 3, 2)
if __name__ == '__main__':
    details_lp_task(
        details_set=details_set,
        c1_args=(0, 2, 9, 6, 5),
        c2_args=(4, 3, 4, 5, 4),
        c3_args=(10, 16, 0, 8, 0),
        p=True,
    )
