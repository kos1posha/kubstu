import re


def num(x):
    def tryfloat(x):
        try:
            return float(x)
        except:
            return x

    def tryint(x):
        try:
            return int(x)
        except:
            return x

    if isinstance(x, str):
        if ',' in x:
            return round(tryfloat(x.replace(',', '.')), 2)
        else:
            return tryint(x)

    return x


subs = {f'x{i}': f'x<sub>{i}</sub>' for i in range(1, 6)}
subs.update({'<=': '≤', '>=': '≥'})
replace = lambda match: subs[match.group(0)]


def xi_to_subscripts(string):
    return re.sub(r'x[1-5]|<=|>=', replace, string)


def shift_next(lst):
    return lst[-1:] + lst[:-1]


def shift_prev(lst):
    return lst[1:] + lst[:1]
