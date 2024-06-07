import sympy

A = 2.0
B = 16.0
M = 87.0


def find_y(a=A, b=B, m=M):
    y = [3]
    for i in range(1, 101):
        y.append((a * y[i - 1] + b) % m)

    y.pop(0)
    return y


def find_z(y):
    z = []
    for yi in y:
        z.append(yi / (M - 1))
    return z


def ravn(z):
    ravn_list = []
    for zi in z:
        ravn_list.append((7 - 3) * zi + 3)
    return ravn_list


def pokaz(z):
    pokaz_list = []
    for zi in z:
        pokaz_list.append(-sympy.ln(zi) / 8)
    return pokaz_list


def rel(z):
    rel_list = []
    for zi in z:
        rel_list.append(-2 * 3 * sympy.ln(zi))
    return rel_list


def norm(z):
    sup = 0
    for zi in z[:12]:
        sup += zi - 0.5
    m_norm = 3 * sup + 1
    return m_norm


if __name__ == '__main__':
    print(Y := find_y())
    print(Z := find_z(Y))
    print('Распределение по равномерному закону на интервале [3,7]:', ravn(Z))
    print('Распределение по показательному закону с λ=8:', pokaz(Z))
    print('Распределение по закону Релея с ϭ=3:', rel(Z))
    print('Распределение по нормальному закону:', norm(Z))
