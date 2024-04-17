from math import exp, log

from scipy.stats import f, norm, t
from sympy import Eq, solve, symbols


class ProbabilityModel:
    def __init__(self, xs, ys, c_func=None, a=None):
        if len(ys) != len(xs):
            raise ValueError('Длина списков должна быть одинаковой')

        self.xs = xs
        self.ys = ys
        self.c_func = c_func
        self.a = a

    def calc_yt(self, func):
        return [func.subs({'x': x}) for x in self.xs]

    @property
    def n(self):
        return len(self.ys)

    @property
    def func(self):
        if self.c_func:
            return self.c_func
        a1, a2, x = symbols('a1 a2 x')
        sq_x_sum = sum(x ** 2 for x in self.xs)
        mul_x_y_sum = sum(x * y for x, y in zip(self.xs, self.ys))
        coeffs = solve([
            Eq(self.n * a1 + self.x_sum * a2, self.y_sum),
            Eq(self.x_sum * a1 + sq_x_sum * a2, mul_x_y_sum)
        ])
        return coeffs[a1].round(2) + coeffs[a2].round(2) * x

    @property
    def x_sum(self):
        return sum(self.xs)

    @property
    def y_sum(self):
        return sum(self.ys)

    @property
    def x_mean(self):
        return self.x_sum / self.n

    @property
    def y_mean(self):
        return self.y_sum / self.n

    @property
    def x_stddev(self):
        x_mean = self.x_mean
        n = self.n
        return (sum((self.xs[i] - x_mean) ** 2 for i in range(n)) / n) ** 0.5

    @property
    def y_stddev(self):
        y_mean = self.y_mean
        n = self.n
        return (sum((self.ys[i] - y_mean) ** 2 for i in range(n)) / n) ** 0.5

    @property
    def covariance(self):
        y_mean = self.y_mean
        x_mean = self.x_mean
        return sum((self.ys[i] - y_mean) * (self.xs[i] - x_mean) for i in range(self.n))

    @property
    def corr_coeff(self):
        return self.covariance / (self.n * self.y_stddev * self.x_stddev)

    @property
    def deter_coeff(self):
        func = self.func
        yt = [func.subs({'x': x}).round(3) for x in self.xs]
        y_mean = self.y_mean
        return 1 - sum((y - y_t) ** 2 for y, y_t in zip(self.ys, yt)) / sum((y - y_mean) ** 2 for y in self.ys)

    @property
    def deter_index(self):
        return self.deter_coeff ** 0.5

    @property
    def t_r(self):
        corr_coeff = self.corr_coeff
        n = self.n
        return corr_coeff / ((1 - corr_coeff ** 2) / (n - 2)) ** 0.5

    @property
    def t_crit(self):
        a = self.a
        n = self.n
        return t.ppf(q=1 - a / 2, df=n - 2)

    @property
    def F_r(self):
        deter_coeff = self.deter_coeff
        n = self.n
        return (deter_coeff / (1 - deter_coeff)) * (n - 2)

    @property
    def F_crit(self):
        a = self.a
        n = self.n
        return f.ppf(q=1 - a, dfn=1, dfd=n - 2)

    @property
    def Z_index(self):
        corr_coeff = self.corr_coeff
        return 0.5 * log((1 + corr_coeff) / (1 - corr_coeff))

    @property
    def t_obr(self):
        a = self.a
        return norm.ppf(q=1 - a / 2)

    @property
    def t_norm(self):
        n = self.n
        return self.t_obr * (1 / (n - 3)) ** 0.5

    @property
    def z_minus(self):
        Z_index = self.Z_index
        t_norm = self.t_norm
        return Z_index - t_norm

    @property
    def z_plus(self):
        Z_index = self.Z_index
        t_norm = self.t_norm
        return Z_index + t_norm

    @property
    def r_minus(self):
        z_minus = self.z_minus
        e = exp(2 * z_minus)
        return (e - 1) / (e + 1)

    @property
    def r_plus(self):
        z_plus = self.z_plus
        e = exp(2 * z_plus)
        return (e - 1) / (e + 1)
