from simplex import Sign, SimplexMethod
from tools import matrix_format, simplex_state_format, success


task1 = {
    'function': [4, 2, 1, 4],
    'constraints': [
        ([5, 4, 6, 2], Sign.LE, 140),
        ([2, 6, 7, 4], Sign.LE, 200),
    ],
    'direction': 'max'
}

task2 = {
    'function': [12, 4],
    'constraints': [
        ([1, 2], Sign.LE, 800),
        ([1, 3], Sign.LE, 600),
        ([2, 3], Sign.LE, 2000),
    ],
    'direction': 'max'
}

task3 = {
    'function': [31, 23, 20],
    'constraints': [
        ([170, 110, 110], Sign.ME, 700),
        ([340, 240, 300], Sign.ME, 800),
        ([380, 440, 480], Sign.ME, 900),
    ],
    'direction': 'min'
}

if __name__ == '__main__':
    simplex = SimplexMethod(**task2)
    print(simplex_state_format(simplex))

    result = simplex()
    print(success('\nВычисления прошли успешно...\n'))
    print(simplex_state_format(simplex))

    print(success('\nРезультат:'))
    print(matrix_format([[f'X{i}' for i in range(1, simplex.c + 1)]] + [result]), end='')
