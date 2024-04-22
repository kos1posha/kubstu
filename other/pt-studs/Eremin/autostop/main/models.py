from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class District(models.TextChoices):
    VMR = 'ВМР', 'Витаминкомбинат'
    GMR = 'ГМР', 'Гидростроителей'
    ZIP = 'ЗИП', 'Завод измерительных приборов'
    KMR = 'КМР', 'Комсомольский'
    PMR = 'ПМР', 'Пашковский'
    SMR = 'СМР', 'Славянский'
    CHMR = 'ЧМР', 'Черемушки'
    UMR = 'ЮМР', 'Юбилейный'
    FMR = 'ФМР', 'Фестивальный'
    CMR = 'ЦМР', 'Центральный'


class BusStation(models.Model):
    class Meta:
        verbose_name = 'Автовокзал'
        verbose_name_plural = 'Автовокзалы'

    name = models.CharField(verbose_name='Название', max_length=32)
    district = models.CharField(verbose_name='Район', max_length=4, choices=District)
    street = models.CharField(verbose_name='Улица', max_length=32)
    number = models.CharField(verbose_name='Номер дома', max_length=8)
    gis_link = models.CharField(verbose_name='Ссылка на 2gis', max_length=128)

    def __str__(self):
        return self.name

    @property
    def address(self):
        return f'{self.street}, {self.number}'

    @property
    def contacts(self):
        return Contact.objects.filter(station=self)


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    phone = models.CharField(verbose_name='Номер телефона', max_length=11)
    description = models.TextField(verbose_name='Описание')
    station = models.ForeignKey(verbose_name='Автовокзал', to=BusStation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.phonef} ({self.station})'

    @property
    def phonef(self):
        return f'+7 ({self.phone[1:4]}) {self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}'


class To(models.Model):
    class Meta:
        verbose_name = 'Направление из Краснодара'
        verbose_name_plural = 'Направления из Краснодара'

    city = models.CharField(verbose_name='Куда', max_length=32)

    def __str__(self):
        return self.city

    @property
    def trips(self):
        return Trip.objects.filter(to=self)

    @property
    def owned_tickets(self):
        return Ticket.objects.filter(trip__in=self.trips, owned=True)


class Trip(models.Model):
    class Meta:
        verbose_name = 'Поездка'
        verbose_name_plural = 'Поездки'

    to = models.ForeignKey(verbose_name='Куда', to=To, on_delete=models.CASCADE)
    station = models.ForeignKey(verbose_name='Станция', to=BusStation, on_delete=models.CASCADE)
    start_dt = models.DateTimeField(verbose_name='Время начала поездки')
    end_dt = models.DateTimeField(verbose_name='Время конца поездки')
    ticket_price = models.DecimalField(verbose_name='Цена билета (руб.)', max_digits=7, decimal_places=2)
    ticket_count = models.PositiveIntegerField(verbose_name='Количество билетов')

    def __str__(self):
        return f'{self.direction} на {self.start_dt.strftime("%H:%M %d.%m.%Y")}, мест: {self.ticket_count}'

    @property
    def direction(self):
        return f'Краснодар – {self.to.city}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        creating = not self.id
        super().save(force_insert, force_update, using, update_fields)
        if creating:
            for i in range(1, self.ticket_count + 1):
                ticket = Ticket(trip=self, place=i)
                ticket.save()

    @property
    def free_places(self):
        return self.ticket_set.filter(owned=False)

    @property
    def is_outdated(self):
        return self.start_dt < timezone.now()

    @property
    def left(self):
        return self.start_dt - timezone.now()

    @property
    def leftf(self):
        td = self.left
        left = f'{td.days} д.', f'{td.seconds // 3600} ч.', f'{(td.seconds // 60) % 60} м.'
        return ' '.join(v for v in left if v[0] != '0')

    @property
    def pricef(self):
        r, k = str(self.ticket_price).split('.')
        return f'{r} рублей {k} копеек'

    @property
    def duration(self):
        return self.end_dt - self.start_dt


class Ticket(models.Model):
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        unique_together = ('trip', 'place')

    trip = models.ForeignKey(verbose_name='Поездка', to=Trip, on_delete=models.CASCADE)
    owned = models.BooleanField(verbose_name='Занят', default=False)
    place = models.PositiveIntegerField(verbose_name='Место')

    def __str__(self):
        return f'{self.trip.direction} на {self.start_dt.strftime("%H:%M %d.%m.%Y")}, место №{self.place}, {self.ownedf}'

    @property
    def start_dt(self):
        return self.trip.start_dt

    @property
    def end_dt(self):
        return self.trip.end_dt

    @property
    def price(self):
        return self.trip.ticket_price

    @property
    def ownedf(self):
        return 'занято' if self.owned else 'свободно'
