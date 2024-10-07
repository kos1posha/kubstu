class Chromosome:
    def __init__(self, **kwargs):
        self.kw_dict = kwargs
        self.attrs = list(self.kw_dict.keys())
        self.vals = list(self.kw_dict.values())

    def __getitem__(self, item):
        return self.kw_dict[item]

    def __str__(self):
        return f'<C: {", ".join([f"{k}={w:.2f}" for k, w in self.kw_dict.items()])}>'

    def __repr__(self):
        return self.__str__()
