class Direction:
    MAX = 'max'
    MIN = 'min'


class Sign:
    EQ = '='
    LE = '<='
    ME = '>='

    @staticmethod
    def to_int(sign):
        match sign:
            case '=' | '<=':
                return 1
            case '>=':
                return -1


class SimplexMethod:
    def __init__(self, function: list[int], constraints: list[list], direction=Direction.MIN, all_positive=True):
        self.not_first = False
        self.a = True
        if direction == Direction.MAX:
            function = [-x for x in function]
        if all_positive:
            l = len(function)
            for i in range(l):
                c = [0] * l
                c[i] = 1
                constraints.append([c, Sign.ME, 0])
        self.k, self.c = sum(map(lambda v: 1 if v is not Sign.EQ else 0, [ct[1] for ct in constraints])), len(function)
        m, n = self._constraints_length(constraints)
        self.m, self.n = m + 1, self.k + self.c + 1
        self.table = [[0] * self.n for _ in range(self.m - 1)] + [[0] + function + [0] * (self.n - len(function) - 1)]
        self.basis = []
        for i in range(self.m - 1):
            sign = Sign.to_int(constraints[i][1])
            self.table[i][0] = sign * constraints[i][2]
            for j in range(n):
                self.table[i][j + 1] = sign * constraints[i][0][j]
            if n + i < self.n and constraints[i][1] != Sign.EQ:
                self.table[i][n + i + 1] = 1
                self.basis.append(n + i + 1)

    def __call__(self) -> list[float]:
        return self._solve()

    def _solve(self):
        result = [0.0] * self.c
        while not self._is_end():
            self.not_first = True
            cur_row, cur_col = self._cur_cell()
            try:
                self.basis[cur_row] = cur_col
            except: pass
            new_table = [[0.0] * self.n for _ in range(self.m)]
            for j in range(self.n):
                new_table[cur_row][j] = self.table[cur_row][j] / self.table[cur_row][cur_col]
            for i in range(self.m):
                if i == cur_row: continue
                for j in range(self.n):
                    new_table[i][j] = self.table[i][j] - self.table[i][cur_col] * new_table[cur_row][j]
            self.table = new_table
        for i in range(len(result)):
            try:
                k = self.basis.index(i + 1)
                result[i] = self.table[k][0]
            except ValueError:
                result[i] = 0
        return result

    def _is_end(self):
        for j in range(self.n):
            if self.table[self.m - 1][j] < 0:
                return False
        return self.not_first and True

    def _cur_cell(self):
        cur_row, cur_col = 0, 1
        for j in range(2, self.n):
            if self.table[self.m - 1][j] < self.table[self.m - 1][cur_col]:
                cur_col = j
        for i in range(self.m - 1):
            if self.table[i][cur_col] > 0:
                cur_row = i
                break
        for i in range(cur_row + 1, self.m - 1):
            if self.table[i][cur_col] > 0 and (self.table[i][0] / self.table[i][cur_col]) < (self.table[cur_row][0] / self.table[cur_row][cur_col]):
                cur_row = i
        return cur_row, cur_col

    def _constraints_length(self, target: list[list]) -> (int, int):
        return len(target), len(target[0][0])
