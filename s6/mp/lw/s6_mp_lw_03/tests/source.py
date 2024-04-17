from transport import MinCostSolver, NWCSolver, VogelsSolver


def test1(name, solver, expected):
    return {
        'costs': [
            [10, 7, 4, 1, 4],
            [2, 7, 10, 6, 11],
            [8, 5, 3, 2, 2],
            [11, 8, 12, 16, 13],
        ],
        'supply': [100, 250, 200, 300],
        'demand': [200, 200, 100, 100, 250],

        'name': name,
        'solver': solver,
        'expected': expected
    }


def test2(name, solver, expected):
    return {
        'costs': [
            [2, 3, 8, 7],
            [2, 0, 7, 3],
            [5, 7, 5, 8],
        ],
        'supply': [70, 10, 80],
        'demand': [60, 40, 40, 20],

        'name': name,
        'solver': solver,
        'expected': expected
    }


mincost1 = test1(
    name='mincost1',
    solver=MinCostSolver,
    expected=(4300, [
        [0, 0, 0, 100, 0],
        [200, 50, 0, 0, 0],
        [0, 0, 0, 0, 200],
        [0, 150, 100, 0, 50],
    ])
)
mincost2 = test2(
    name='mincost2',
    solver=MinCostSolver,
    expected=(650, [
        [60, 10, 0, 0],
        [0, 10, 0, 0],
        [0, 20, 40, 20],
    ])
)

nwc1 = test1(
    name='nwc1',
    solver=NWCSolver,
    expected=(6950, [
        [100, 0, 0, 0, 0],
        [100, 150, 0, 0, 0],
        [0, 50, 100, 50, 0],
        [0, 0, 0, 50, 250],
    ])
)

nwc2 = test2(
    name='nwc2',
    solver=NWCSolver,
    expected=(650, [
        [60, 10, 0, 0],
        [0, 10, 0, 0],
        [0, 20, 40, 20],
    ])
)

vogels1 = test1(
    name='vogels1',
    solver=VogelsSolver,
    expected=(4150, [
        [0, 0, 0, 50, 50],
        [200, 0, 0, 50, 0],
        [0, 0, 0, 0, 200],
        [0, 200, 100, 0, 0],
    ])
)

vogels2 = test2(
    name='vogels2',
    solver=VogelsSolver,
    expected=(640, [
        [30, 40, 0, 0],
        [0, 0, 0, 10],
        [30, 0, 40, 10],
    ])
)

mincost_tests = [mincost1, mincost2]
nwc_tests = [nwc1, nwc2]
vogels_tests = [vogels1, vogels2]
all_tests = mincost_tests + nwc_tests + vogels_tests
