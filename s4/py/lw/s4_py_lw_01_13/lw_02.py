# задание 1
def min_of_two(op1, op2):
    if op1 <= op2: return op1
    return op2

# задание 2
def sgn(x):
    if x > 0: return 1
    if x < 0: return -1
    return 0

# задание 3
def chess_colors(clmn1, row1, clmn2, row2):
    if clmn1 + row1 // 2 == clmn2 + clmn2 // 2: return true
    return false

# задание 4
def bisextile(year):
    if (year % 400 == 0): return true
    if (year % 100 == 0): return false
    if (year % 4 == 0): return true
    return false

# задание 5
def min_of_three(op1, op2, op3):
    if op1 < op2 and op1 < op3: return op1
    if op2 < op1 and op2 < op3: return op2
    return op3

# задание 6
def same_of_three(op1, op2, op3):
    if op1 == op2 or op2 == op3 or op3 == op1: return 2
    if op1 == op2 and op2 == op3 and op3 == op1: return 3
    return 0

# задание 7
def chess_castle(clmn1, row1, clmn2, row2):
    if clmn1 == clmn2 or row1 == row2: return true
    return false

# задание 8
def chess_king(clmn1, row1, clmn2, row2):
    if clmn1 - clmn2 > 1 or row1 - row2 > 1: return false
    return true

# задание 9
def chess_elephant(clmn1, row1, clmn2, row2):
    if clmn1 - clmn2 == row1 - row2: return true
    return false

# задание 10
def chess_queen(clmn1, row1, clmn2, row2):
    if clmn1 == clmn2 or row1 == row2: return true
    if clmn1 - clmn2 == row1 - row2: return true
    return false

# задание 11
def chess_horse(clmn1, row1, clmn2, row2):
    if (abs(clmn1 - clmn2) == 2 and abs(row1 - row2) == 1): return true
    if (abs(clmn1 - clmn2) == 1 and abs(row1 - row2) == 2): return true
    return false

# задание 12
def chocolate(clmns, rows, slices):
    if slices % clmns == 0 or slices % rows == 0: return true
    return false

# задание 13
def yasha(pool_width, pool_height,  yasha_x, yasha_y):
    return min(pool_width - yasha_x, pool_height - yasha_y)