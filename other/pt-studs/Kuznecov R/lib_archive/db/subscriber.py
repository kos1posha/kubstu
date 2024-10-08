from datetime import datetime

import peewee as pw

from db.base import BaseModel


class Subscriber(BaseModel):
    first_name = pw.CharField(verbose_name='Имя', max_length=32)
    last_name = pw.CharField(verbose_name='Фамилия', max_length=32)
    sur_name = pw.CharField(verbose_name='Отчество', max_length=32, null=True)
    email = pw.CharField(verbose_name='Почтовый адрес', max_length=253, unique=True)
    home_address = pw.CharField(verbose_name='Домашний адрес', max_length=512)
    phone_number = pw.FixedCharField(verbose_name='Телефонный номер', max_length=10, unique=True)
    rating = pw.IntegerField(verbose_name='Рейтинг', default=50)
    registration_datetime = pw.DateTimeField(verbose_name='Дата регистрации', default=datetime.now())

    @classmethod
    def create(cls, first_name: str, last_name: str, sur_name: str, email: str, home_address: str, phone_number: str, **query):
        return super().create(
            first_name=first_name,
            last_name=last_name,
            sur_name=sur_name,
            email=email,
            home_address=home_address,
            phone_number=phone_number,
            **query
        )

    @property
    def full_name(self) -> str:
        return f'{self.last_name} {self.first_name}' + f' {self.sur_name}' if self.sur_name else ''

    @property
    def short_name(self) -> str:
        return f'{self.last_name} {self.first_name[0]}.' + f' {self.sur_name[0]}.' if self.sur_name else ''

    @property
    def phone_number_f(self):
        p = self.phone_number
        return f'8 ({p[:3]}) {p[3:6]} {p[6:8]}-{p[8:10]}'

    def increase_rating(self, value: int = 1) -> None:
        self.rating += value
        if self.rating > 100:
            raise ValueError('Рейтинг не может быть больше 100')
        self.save()

    def reduce_rating(self, value: int = 1) -> None:
        self.rating -= value
        if self.rating < 0:
            raise ValueError('Рейтинг не может быть больше 0')
        self.save()
