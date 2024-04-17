# задание 2
def snowflake(size):
    lst = [['.'] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if (i == j or j + 1 == size - i) or (i == size // 2 or j == size // 2):
                lst[i][j] = '*'
    return lst


# задание 4
def diagonals(size):
    lst = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            lst[i][j] = abs(i - j)
    return lst
