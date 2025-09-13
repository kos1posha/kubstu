class TimetableWeek:
    even: bool
    days: list

    def __init__(self, even, days):
        self.even = even
        self.days = days

    @property
    def week_even(self):
        if self.even:
            return 'четная'
        else:
            return  'нечетная'


class TimetableDay:
    day: int
    pairs: list

    def __init__(self, day, pairs):
        self.day = day
        self.pairs = pairs

    @property
    def day_week(self):
        if self.day == 1:
            return 'Понедельник'
        elif self.day == 2:
            return 'Вторник'
        elif self.day == 3:
            return 'Среда'
        elif self.day == 4:
            return 'Четверг'
        elif self.day == 5:
            return 'Пятница'
        elif self.day == 6:
            return 'Суббота'
        elif self.day == 7:
            return 'Воскресенье'
        else:
            return '-'


class TimetablePair:
    title: str
    teacher_first_name: str
    teacher_last_name: str
    teacher_patronymic: str
    number: int
    type: int
    classroom: str
    period_start: str
    period_end: str

    def __init__(self, title, teacher_first_name, teacher_last_name, teacher_patronymic, number, type, classroom, period_start, period_end):
        self.title = title
        self.teacher_first_name = teacher_first_name
        self.teacher_last_name = teacher_last_name
        self.teacher_patronymic = teacher_patronymic
        self.number = number
        self.type = type
        self.classroom = classroom
        self.period_start = period_start
        self.period_end = period_end

    @property
    def teacher_full_name(self):
        return f'{self.teacher_last_name} {self.teacher_first_name} {self.teacher_patronymic}'

    @property
    def full_type(self):
        if self.type == 0:
            return 'Лекция'
        elif self.type == 1:
            return 'Практическое занятие'
        elif self.type == 2:
            return 'Лаболаторное занятие'
        else:
            return '-'

    @property
    def time(self):
        if self.number == 1:
            return '8:00 - 9:30'
        elif self.number == 2:
            return '9:40 - 11:10'
        elif self.number == 3:
            return '11:20 - 12:50'
        elif self.number == 4:
            return '13:20 - 14:50'
        elif self.number == 5:
            return '15:00 - 16:30'
        elif self.number == 6:
            return '16:40 - 18:10'
        elif self.number == 7:
            return '18:20 - 19:50'
        elif self.number == 8:
            return '20:00 - 21:30'
        else:
            return 'спать в вузе что ли?'

    @property
    def period(self):
        return f'с {self.period_start} по {self.period_end} недели'
