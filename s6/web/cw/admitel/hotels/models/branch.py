from django.db import models as m


class Branch(m.Model):
    class Meta:
        verbose_name = 'Филиал отеля'
        verbose_name_plural = 'Филиалы отелей'

    name = m.CharField(verbose_name='Название', max_length=150, default='н/д')
    hotel = m.ForeignKey(verbose_name='Отель', to='hotels.Hotel', on_delete=m.CASCADE)
    country = m.CharField(verbose_name='Страна', max_length=150)
    city = m.CharField(verbose_name='Город', max_length=150)
    street = m.CharField(verbose_name='Улица', max_length=150)
    number = m.CharField(verbose_name='Номер дома', max_length=150)

    def __str__(self):
        return f'{self.hotel}: {self.full_address}'

    @property
    def full_address(self):
        return f'{self.country}, г. {self.street}, ул. {self.street}, д. {self.number}'
