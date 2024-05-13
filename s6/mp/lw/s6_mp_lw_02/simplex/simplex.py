from pprint import pformat
import sys
from typing import Optional

from sympy import Eq, Function, Ge, Integer as I, Le, Number as N, Rational as R, Symbol, pretty as _, symbols

from simplex.tools import canonicalize_eq, ineq_to_eq, is_int, num, range_exclude, sort_symbols


class Search:
    MAX = 'Максимум'
    MIN = 'Минимум'


class Status:
    NOT_SOLVED = 'Поиск решения еще не был произведен'
    NOT_EXPECTED_RESULT = 'Функция в найденной точке экстремума дала неожиданный результат...'
    SOLUTION_FOUND = 'Экстремум функции найден'
    LOCAL_SOLUTION_FOUND = 'Экстремум функции находится за пределами области допустимых значений (найденное значение является локальным экстремумом)'


class SimplexHistoryKeys:
    OBJ_FUNC = 'Целевая функция'
    SEARCH = 'Направление поиска'
    CONSTRAINTS = 'Ограничения'
    POINT = 'Точка экстремума'
    EXTR = 'Значение экстремума'
    STATUS = 'Статус решения'
    START_SIMPLEX_TABLE = 'Начальная симплекс-таблица'
    ITERS_COUNT = 'Количество итераций'
    ITERS = 'Итерации'
    ITER_GEN_CELL = 'Разрешающая ячейка'
    ITER_GEN_VAL = 'Разрешающий элемент'
    ITER_SIMPLEX_TABLE = 'Симплекс-таблица'
    ITER_BASIS_VARS = 'Базисные переменные'
    ITER_NONBASIS_VARS = 'Небазисные переменные'


SHK = SimplexHistoryKeys


class Simplex:
    def __init__(self, obj_func: Function, constraints: list[Eq, Ge, Le], search=Search.MAX):
        self.obj_func = obj_func
        self.constraints = constraints
        self.search = search

        self.ineq_additional_vars = []
        self._lp_to_canonical()

        self.basis_cis = {}
        self.basis_vars, self.nonbasis_vars = [], []
        self._find_basis_vars()
        self._old_bv, self._old_nbv = self.basis_vars.copy(), self.nonbasis_vars.copy()

        self.table = []
        self.height, self.width = len(self.basis_vars) + 1, len(self.nonbasis_vars) + 1
        self._build_simplex_table()

        self.solved = False
        self.is_local_extr = False
        self.result = None
        self.history = {
            SHK.OBJ_FUNC: _(obj_func),
            SHK.SEARCH: search,
            SHK.CONSTRAINTS: [_(c) for c in constraints],
            SHK.POINT: {},
            SHK.EXTR: 0.0,
            SHK.STATUS: Status.NOT_SOLVED,
            SHK.START_SIMPLEX_TABLE: {
                SHK.ITER_SIMPLEX_TABLE: [[num(val) for val in row] for row in self.table],
                SHK.ITER_BASIS_VARS: self._old_bv,
                SHK.ITER_NONBASIS_VARS: self._old_nbv,
            },
            SHK.ITERS_COUNT: 0,
            SHK.ITERS: []
        }

    def __call__(self) -> tuple[dict[Symbol, N], N]:
        return self.solve()

    def solve(self) -> tuple[dict[Symbol, N], N]:
        if self.solved:
            return self.result

        while not self._is_optimal():
            gen_cell = self._get_gen_cell()
            if not gen_cell:
                self.is_local_extr = True
                break
            self._iterate_simplex_table(*gen_cell)

        self.solved = True
        self.result = self._interpret_result()
        return self.result

    def _lp_to_canonical(self) -> None:
        self.obj_func *= -1 if self.search == Search.MIN else 1

        ineq_constraints: list[Ge] = [ineq for ineq in self.constraints if isinstance(ineq, (Ge, Le))]
        self.ineq_additional_vars = symbols(f'δ1:{len(ineq_constraints) + 1}')
        for ineq, sym in zip(ineq_constraints, self.ineq_additional_vars):
            eq = ineq_to_eq(ineq.simplify(), sym)
            self.constraints.append(eq)
            self.constraints.remove(ineq)

        for i, c in enumerate(self.constraints):
            c = canonicalize_eq(c)
            if c.rhs < 0:
                c = Eq(-c.lhs, -c.rhs)
            self.constraints[i] = c

    def _find_basis_vars(self) -> None:
        all_vars = sort_symbols(self._get_all_vars())
        basis_rows = []
        for var in all_vars:
            is_basis, basis_c, basis_i = False, None, None
            for i, c in enumerate(self.constraints):
                match c.lhs.coeff(var):
                    case 0:
                        continue
                    case 1 | -1:
                        is_basis, basis_c, basis_i = not is_basis, c, i
                        if not is_basis: break
                    case _:
                        is_basis = False
                        break
            if is_basis and len(self.basis_cis) != len(self.constraints):
                self.basis_vars.append(var)
                if basis_i not in basis_rows:
                    if basis_c.lhs.coeff(var) == -1:
                        self.constraints[basis_i] = basis_c = Eq(-basis_c.lhs, -basis_c.rhs)
                    self.basis_cis[var] = {'c': basis_c, 'i': basis_i}
                    basis_rows.append(basis_i)
            else:
                self.nonbasis_vars.append(var)

    def _build_simplex_table(self) -> None:
        last = [0 for _ in range(self.width)]

        for c, basis in enumerate(self.basis_vars):
            row = [self.basis_cis[basis]['c'].lhs.coeff(nonbasis) for nonbasis in self.nonbasis_vars] + [self.basis_cis[basis]['c'].rhs]
            obj_coeff = self.obj_func.coeff(basis)
            for i in range(self.width):
                last[i] += row[i] * obj_coeff
            self.table.append(row)
        for c, nonbasis in enumerate(self.nonbasis_vars):
            last[c] -= self.obj_func.coeff(nonbasis)

        self.table.append(last)

    def _iterate_simplex_table(self, gen_r: int, gen_c: int) -> None:
        gen_val = self.table[gen_r][gen_c]
        self.basis_vars[gen_r], self.nonbasis_vars[gen_c] = self.nonbasis_vars[gen_c], self.basis_vars[gen_r]

        new_simplex_table = []
        for r in range_exclude(self.height, gen_r):
            row = []
            for c in range(self.width):
                if c == gen_c:
                    new_val = -self.table[r][gen_c] / gen_val
                else:
                    new_val = self.table[r][c] - ((self.table[gen_r][c] * self.table[r][gen_c]) / gen_val)
                row.append(new_val)
            new_simplex_table.append(row)

        new_simplex_table.insert(gen_r, [(val if c != gen_c else 1) / gen_val for c, val in enumerate(self.table[gen_r])])
        self.table = new_simplex_table
        self.history[SHK.ITERS_COUNT] += 1
        self.history[SHK.ITERS].append({
            SHK.ITER_GEN_CELL: (num(gen_r), num(gen_c)),
            SHK.ITER_GEN_VAL: num(gen_val),
            SHK.ITER_SIMPLEX_TABLE: [[I(val) if is_int(val) else R(val) for val in row] for row in new_simplex_table],
            SHK.ITER_BASIS_VARS: self.basis_vars.copy(),
            SHK.ITER_NONBASIS_VARS: self.nonbasis_vars.copy(),
        })

    def _interpret_result(self) -> tuple[dict[Symbol, N], N]:
        val = lambda v: 0 if v in self.nonbasis_vars else self.table[self.basis_vars.index(v)][-1]
        point = {var: val(var) for var in sort_symbols(self.obj_func.free_symbols)}
        extr = self.table[-1][-1]

        assert extr == self.obj_func.subs(point), Status.NOT_EXPECTED_RESULT

        self.history[SHK.POINT] = {_(k): num(v) for k, v in point.items()}
        self.history[SHK.EXTR] = num(extr)
        self.history[SHK.STATUS] = Status.SOLUTION_FOUND if not self.is_local_extr else Status.LOCAL_SOLUTION_FOUND
        return point, extr

    def _is_optimal(self) -> bool:
        return all(score >= 0 for score in self.table[-1][:-1])

    def _get_gen_cell(self) -> Optional[tuple[int, int]]:
        r, c = -1, self.table[-1].index(min(self.table[-1][:-1]))

        min_val = sys.maxsize
        for i, cur_r in enumerate(self.table[:-1]):
            if cur_r[c] > 0:
                cur_val = self.table[i][-1] / cur_r[c]
                if cur_val < min_val:
                    min_val = cur_val
                    r = i

        if r == -1:
            return None
        return r, c

    def _get_all_vars(self):
        all_vars = self.obj_func.free_symbols.union(self.ineq_additional_vars)
        for c in self.constraints:
            all_vars.update(c.free_symbols)
        return all_vars

    def pretty_history(self) -> str:
        return pformat(self.history, sort_dicts=False)
