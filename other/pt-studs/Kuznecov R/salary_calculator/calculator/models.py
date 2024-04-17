from django.core import exceptions
from django.core.validators import MaxValueValidator
from django.db import models


class MoneyField(models.DecimalField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_digits = 19
        self.decimal_places = 2

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value < 0:
            raise exceptions.ValidationError('Данное поле не может быть отрицательным.', code='negative')


class BonusField(models.DecimalField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_digits = 19
        self.decimal_places = 2
        self.help_text = 'Вы можете ввести отрицательное значения для штрафа.'


class Position(models.Model):
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    name = models.CharField(verbose_name='Название', max_length=100)
    salary = MoneyField(verbose_name='Заработная ставка (за месяц)')

    @property
    def salary_initial(self):
        try:
            r, k = self.salary.__str__().split('.')
            return f'{r}.{k}'
        except:
            return ''

    @property
    def salary_f(self):
        r, k = self.salary.__str__().split('.')
        return f'{r}.{k} рублей'

    def __str__(self):
        return f'{self.name} - {self.salary_f}'


class Employee(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    position = models.ForeignKey(verbose_name='Должность', to=Position, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def position_f(self):
        return self.position.name if self.position else 'Не определена'

    def __str__(self):
        return self.full_name


class BonusTypeChoices(models.TextChoices):
    PERCENT = 'Процентная', 'Процентная'
    NUMERIC = 'Сумма', 'Сумма'


class Bonus(models.Model):
    class Meta:
        verbose_name = 'Надбавка/Штраф'
        verbose_name_plural = 'Надбавки/Штрафы'

    employee = models.ForeignKey(verbose_name='Сотрудник', to=Employee, on_delete=models.CASCADE)
    type = models.CharField(verbose_name='Тип', choices=BonusTypeChoices.choices, max_length=20)
    value = BonusField(verbose_name='Значение')

    @property
    def unit(self):
        if self.type == BonusTypeChoices.PERCENT:
            return '%'
        return 'руб.'

    def __str__(self):
        return f'{self.employee.full_name} - {self.value} {self.unit}'


percent_validator = MaxValueValidator(limit_value=100, message='Проценты не могут превышать сотни.')


# noinspection PyPropertyDefinition
class DefaultTaxes(models.Model):
    class Meta:
        verbose_name = 'Налоги'
        verbose_name_plural = 'Налоги'

    _singleton = models.BooleanField(default=True, editable=False, unique=True)

    personal = models.PositiveIntegerField(verbose_name='НДФЛ', default=13, validators=[percent_validator])
    pensionary = models.PositiveIntegerField(verbose_name='Пенсионные отчисления', default=22, validators=[percent_validator])

    @classmethod
    @property
    def personal_tax(cls):
        return cls.objects.first().personal

    @classmethod
    @property
    def pensionary_tax(cls):
        return cls.objects.first().pensionary

    def __str__(self):
        return f'НДФЛ: {self.personal}% Пенсионные: {self.pensionary}%'
