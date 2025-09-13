from django.db import models as m


class Room(m.Model):
    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    branch = m.ForeignKey(verbose_name='Филиал', to='Branch', on_delete=m.CASCADE)
    name = m.CharField(verbose_name='Название', max_length=150)
    thumbnail = m.ImageField(verbose_name='Фото', upload_to='photos/')
    description = m.TextField(verbose_name='Описание')
    is_busy = m.BooleanField(verbose_name='Занят', default=False)

    @property
    def state(self):
        return 'Занят' if self.is_busy else 'Свободно'

    def __str__(self):
        return self.name
