from sympy import ln, pretty, symbols

from probability_model import ProbabilityModel


def pretty_list(lst, w=5):
    return '[' + ', '.join([str(i).rjust(w) for i in lst]) + ']'


def task1(xy=None):
    if not xy:
        xy = {
            'xs': [10.85, 10.32, 9.43, 9.4, 9.21, 8.65, 8.63, 8.22],
            'ys': [12.77, 11.59, 10.37, 10.36, 10.32, 9.43, 9.07, 9.04]
        }

    xs, ys = xy['xs'], xy['ys']
    model = ProbabilityModel(xs, ys)
    print(
        f'xs: {pretty_list(xs)}',
        f'ys: {pretty_list(ys)}',
        f'Количество бросков: {model.n}',
        f'Среднее xs: {model.x_mean:.4f}',
        f'Среднее ys: {model.y_mean:.4f}',
        f'Коэффициент корреляции: {model.corr_coeff:.4f}',
        f'Предикатная функция: {pretty(model.func)}',
        f'Коэффициент детерминации: {model.deter_coeff:.4f}',
        sep='\n'
    )


def task2(xy=None, func=None, a=0.01):
    if not xy:
        xy = {
            'xs': [3, 6, 6, 9, 12, 13, 13, 14, 15, 19, 24, 26, 26, 26, 27, 28, 30, 31, 31, 33, 34, 35, 66, 36, 36, 37, 67, 38, 39, 40, 40, 40, 41, 44, 47, 48, 48, 49, 52, 54],
            'ys': [12, 14, 11, 17, 13, 11, 15, 20, 19, 19, 25, 26, 19, 21, 12, 15, 26, 24, 16, 17, 21, 18, 16, 19, 20, 25, 14, 26, 29, 18, 29, 22, 24, 26, 18, 17, 16, 18, 25, 24]
        }
    if not func:
        x = symbols('x')
        func = 5 + 4 * ln(x)

    xs, ys = xy['xs'], xy['ys']
    model = ProbabilityModel(xs, ys, func, a)
    print(
        f'xs: {pretty_list(xs, 2)}',
        f'ys: {pretty_list(ys, 2)}',
        f'Количество бросков: {model.n}',
        f'Среднее xs: {model.x_mean:.3f}',
        f'Среднее ys: {model.y_mean:.3f}',
        f'Коэффициент корреляции: {model.corr_coeff:.6f}',
        f'Предикатная функция: {pretty(model.func)}',
        f'Коэффициент детерминации: {model.deter_coeff:.6f}',
        f'Индекс детерминации: {model.deter_index:.6f}',
        f't_r: {model.t_r:.6f}',
        f't_crit: {model.t_crit:.6f}',
        f'F_r: {model.F_r:.6f}',
        f'F_crit: {model.F_crit:.6f}',
        f't1: {model.t_obr:.6f}',
        f't2: {model.t_norm:.6f}',
        f'z-: {model.z_minus:.6f}',
        f'z+: {model.z_plus:.6f}',
        f'r-: {model.r_minus:.6f}',
        f'r+: {model.r_plus:.6f}',
        sep='\n'
    )


if __name__ == '__main__':
    task2()
