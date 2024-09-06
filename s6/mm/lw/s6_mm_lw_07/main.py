import math

import numpy as np

number_call = 15
time_match = 3


def f_rrv(z, a_l, b_r):
    return (b_r - a_l) * z + a_l


A = 2.3
B = 23
M = 40

y = [0] * (number_call + 1)
y[0] = 3

for i in range(1, number_call + 1):
    y[i] = (y[i - 1] * A + B) % M

Y = np.array(y[1:], dtype=float)
Z = Y / (M - 1)

a = 0
b = 1
uniformly = f_rrv(Z, a, b)

print(f'+-----+---------+---------+-----------------+---------+---------+')
print(f'|  №  |    y    |   z_i   |  Равномерно на  |    t    |    T    |')
print(f'|     |         |         |      [0, 1]     |         |         |')
print(f'|-----+---------+---------+-----------------+---------+---------|')

lamb = time_match / 24
t = [0] * number_call
T = [0] * number_call
start = 0
result = 0

for i in range(Y.shape[0]):
    t[i] = -1 / lamb * math.log(uniformly[i])
    T[i] = start + t[i]
    start = T[i]
    if T[i] < time_match:
        result += 1
    print(f'|{i + 1:^5}|{Y[i]:^9.3f}|{Z[i]:^9.3f}|{uniformly[i]:^17.3f}| {t[i]:8.3f}| {T[i]:8.3f}|')
print(f'+-----+---------+---------+-----------------+---------+---------+')
print(f'Количество пропущенных звонков: {result}')
