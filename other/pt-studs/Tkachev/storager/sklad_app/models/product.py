from django.core.validators import MinValueValidator
from django.db.models import CASCADE, CharField, DecimalField, ForeignKey, IntegerField, Model

from sklad_app.models.storage import Storage


class Product(Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    name = CharField(verbose_name='Название', max_length=40)
    count = IntegerField(verbose_name='Количество', validators=[MinValueValidator(limit_value=0)], default=0)
    weight = DecimalField(verbose_name='Вес (кг.)', max_digits=9, decimal_places=2, default=1)
    storage = ForeignKey(Storage, verbose_name='Хранилище', on_delete=CASCADE)

    @property
    def total_weight(self):
        return self.weight * self.count
