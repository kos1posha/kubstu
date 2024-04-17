from math import *

# задание 1
def digit_last(numb):
    return numb % 10

# задание 2
def mkad(speed, time):
    return speed * time % 109

# задание 3
def fraction(numb):
    return numb % 1

# задание 4
def fraction_first(numb):
    return numb % 1 // 0.1

# задание 5
def lesson_end(lesson_number):
    return [(lesson_number * 45 + ((lesson_number - 1) * 10 - (lesson_number - 1) % 2 * 5)) // 60 + 9,
            (lesson_number * 45 + ((lesson_number - 1) * 10 - (lesson_number - 1) % 2 * 5)) % 60]

# задание 6
def automileage(daily_path, total_path):
    return ceil(total_path / daily_path)

# задание 7
def pattys(cost_rub, cost_kop, pattys_count):
    return (cost_rub + cost_kop / 100) * pattys_count

# задание 8
def time_difference(h1, m1, s1, h2, m2, s2):
    return 60 * ((h2 - h1) * 60 + (m2 - m1)) + (s2 - s1)

# задание 9
def escargot(pole_height, daily_climb, nightly_discent):
    return pole_height // daily_climb - nightly_discent

# задание 10
def tens(numb):
    return numb % 100 // 10

# задание 11
def sum_of_digits(numb):
    return numb // 100 + numb % 100 // 10 + numb % 10

# задание 12
def triangle_hypotenuse(leg1, leg2):
    return sqrt(leg1 ** 2 + leg2 ** 2)

# задание 13
def clock_1(h, m, s):
    return h * 30 + m * (1/2) + s * (1/120)

# задание 14
def clock_2(angle):
    return angle % 30 * 2

# задание 15
def clock_3(angle):
    return [angle // 30 + 0.2, angle % 30 // (1/2) + 0.2, angle % (1/2) // (1/120)]

# задание 16
def deposit(rub, kop, percent):
    return [int(rub * (1 + percent/100) + kop * (1 + percent/100) // 100), int(kop * (1 + percent/100) % 100)]