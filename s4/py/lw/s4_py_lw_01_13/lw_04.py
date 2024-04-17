from lw_02 import sgn

# задание 1
def range_1(a, b):
    for i in range(a, b + 1):
        print(i)

# задание 2
def range_2(a, b):
    for i in range(a, b + sgn(b - a), sgn(b - a)):
        print(i)

# задание 3
def range_3(a, b):
    for i in range(a + (a - 1) % 2, b + 1, 2):
        print(i)

# задание 4
def sum_of_ten(op1, op2, op3, op4, op5, op6, op7, op8, op9, op10):
    res = 0
    for i in [op1, op2, op3, op4, op5, op6, op7, op8, op9, op10]:
        res += i
    return res

# задание 5
def sum_of_n(list):
    res = 0
    for i in list:
        res += i
    return res

# задание  6
def sum_of_cubes(list):
    res = 0
    for i in list:
        res += i ** 3
    return res

# задание  7
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

# задание  8
def sum_of_factorials(n):
    res = 0
    cur = 1
    for i in range(1, n + 1):
        cur *= i
        res += cur
    return res

# задание  9
def zeros(list):
    res = 0
    for i in list:
        if i == 0:
            res += 1
    return res

# задание  10
def ladder(stair_count):
    res = ""
    for i in range(1, stair_count + 1):
        for j in range(1, i + 1):
            res += str(j)
        res += "\n"
    return res

def ladder_konch(stair_count):
    return "\n".join(str(i) for i in range(1, stair_count + 1) for i in ["".join(str(i) for i in range(1, i + 1))])

# задание  11
def lost_card(cards):
    for indx, item in enumerate(cards):
        if item != indx + 1: return indx + 1