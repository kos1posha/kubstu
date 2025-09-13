from django.db import models as m


class Hotel(m.Model):
    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    key1 = m.CharField(verbose_name='Первый ключ', max_length=50)
    key2 = m.CharField(verbose_name='Второй ключ', max_length=50)
    name = m.CharField(verbose_name='Название', max_length=150, unique=True)

    def __str__(self):
        return self.name
