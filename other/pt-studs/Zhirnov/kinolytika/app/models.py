from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models as m
from django.utils import timezone


class Hall(m.Model):
    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'

    title = m.CharField(verbose_name='Название', max_length=100)

    def __str__(self):
        return f'{self.title}, {self.hallplace_set.count()} мест'

    @classmethod
    def create_with_places(cls, title, place_count):
        hall = Hall(title=title)
        hall.save()
        for p in range(1, place_count + 1):
            place = HallPlace(number=p, hall=hall)
            place.save()

    def places(self):
        return HallPlace.objects.filter(hall=self)


class HallPlace(m.Model):
    class Meta:
        verbose_name = 'Место в зале'
        verbose_name_plural = 'Места в залах'
        unique_together = ('number', 'hall')

    number = m.IntegerField(verbose_name='Номер', validators=[MinValueValidator(limit_value=1)])
    hall = m.ForeignKey(verbose_name='Зал', to=Hall, on_delete=m.CASCADE)

    def __str__(self):
        return f'{self.hall.title}, место {self.number}'


class Genre(m.Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    title = m.CharField(verbose_name='Название', max_length=100)
    description = m.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Film(m.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    thumbnail = m.ImageField(verbose_name='Превью')
    title = m.CharField(verbose_name='Название', max_length=100)
    genres = m.ManyToManyField(verbose_name='Жанры', to=Genre)
    duration = m.TimeField(verbose_name='Продолжительность')
    description = m.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    def genres_lower(self):
        return [str(g).lower() for g in self.genres.all()]


class FilmShow(m.Model):
    class Meta:
        verbose_name = 'Киносеанс'
        verbose_name_plural = 'Киносеансы'

    film = m.ForeignKey(verbose_name='Фильм', to=Film, on_delete=m.CASCADE)
    hall = m.ForeignKey(verbose_name='Зал', to=Hall, on_delete=m.CASCADE)
    ticket_price = m.DecimalField(verbose_name='Стоимость билета', max_digits=16, decimal_places=2, validators=[MinValueValidator(limit_value=1)])
    datetime = m.DateTimeField(verbose_name='Время показа')

    def __str__(self):
        return f'{self.hall.title}: {self.film.title} на {self.datetime.date().strftime("%d.%m.%Y")}'

    def owned_places(self):
        tickets = Ticket.objects.filter(filmshow=self)
        return HallPlace.objects.filter(ticket__in=tickets)

    def free_places(self):
        tickets = Ticket.objects.filter(filmshow=self)
        return HallPlace.objects.filter(hall=self.hall).exclude(ticket__in=tickets)


class Ticket(m.Model):
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        unique_together = ('filmshow', 'place')

    owner = m.ForeignKey(verbose_name='Владелец', to=User, on_delete=m.CASCADE)
    filmshow = m.ForeignKey(verbose_name='Сеанс', to=FilmShow, on_delete=m.CASCADE)
    place = m.ForeignKey(verbose_name='Место', to=HallPlace, on_delete=m.CASCADE)
    datetime = m.DateTimeField(verbose_name='Дата приобретения', default=timezone.now())

    def __str__(self):
        return f'{self.owner}: {self.filmshow.film.title} на {self.filmshow.datetime.date().strftime("%d.%m.%Y")}'
