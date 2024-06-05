import pulp as pp


def master_gumbs_problem(obj_func: tuple[int], constraints: tuple[tuple[int]], supply: int):
    of = obj_func
    a, b, = pp.LpVariable('А', lowBound=0, cat=pp.LpInteger), pp.LpVariable('Б', lowBound=0, cat=pp.LpInteger)
    v, v_cl = pp.LpVariable('В', lowBound=0, cat=pp.LpInteger), pp.LpVariable('Вₓ', lowBound=0, cat=pp.LpInteger)
    objective_func = of[0] * a + of[1] * b + of[2] * v + of[3] * v_cl
    constraints = [
        (c1 * a + c2 * b + c3 * v + c4 * v_cl <= supply, name)
        for c1, c2, c3, c4, name
        in [(*constraints[0], 'Потрачено чел/дней на заготовки'),
            (*constraints[1], 'Потрачено чел/дней на сборку'),
            (*constraints[2], 'Потрачено чел/дней на покраску')]
    ]
    problem = pp.LpProblem('Мастер Гамбс', sense=pp.LpMaximize)
    problem.setObjective(objective_func)
    for c in constraints:
        problem.addConstraint(*c)
    problem.solve()
    return problem


def big_master_gumbs_problem(obj_func: tuple[int], constraints: tuple[tuple[int]], supply: int, step: int, period: int):
    problems = []
    for _ in range(period):
        problems.append(master_gumbs_problem(obj_func, constraints, supply))
        supply += step
    return problems
