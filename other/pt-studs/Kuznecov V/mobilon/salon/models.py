from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def int_f(x):
    return '{:,}'.format(x).replace(',', ' ')


class MoneyField(models.DecimalField):
    def __init__(self, verbose_name, **kwargs):
        super().__init__(verbose_name=verbose_name, **kwargs)
        self.max_digits = 19
        self.decimal_places = 2

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value < 0:
            raise ValidationError('Данное поле не может быть отрицательным.', code='negative')


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название', max_length=100)
    name_plural = models.CharField('В множественном числе', max_length=100)

    def __str__(self):
        return self.name_plural

    @property
    def products(self):
        return Product.objects.filter(category=self)


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    image = models.ImageField('Картинка', max_length=300)
    name = models.CharField('Название', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField('Описание')
    cost = models.PositiveIntegerField('Цена')

    def __str__(self):
        return f'{self.category.name if self.category.name != "Другое" else ""} {self.name} за {self.cost_format}'

    @property
    def cost_format(self):
        return f'{int_f(self.cost)} ₽'


class Purchase(models.Model):
    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    basket = models.ManyToManyField(Product, verbose_name='Корзина')
    done = models.BooleanField('Состояние', default=False)
    datetime = models.DateTimeField('Дата сделки', blank=True, null=True)

    def __str__(self):
        return f'Корзина на сумму {self.total_cost_format}' + (f' от {timezone.localtime(self.datetime)}' if self.done else '')

    def set_done(self, commit=True):
        self.done = True
        self.datetime = timezone.now()
        if commit:
            self.save()

    @property
    def is_clear(self):
        return self.basket.count() == 0

    @property
    def total_cost(self):
        return sum([p.cost for p in self.basket.all()])

    @property
    def total_cost_format(self):
        return f'{int_f(self.total_cost)} ₽'

    @property
    def product_count(self):
        return self.basket.count()
