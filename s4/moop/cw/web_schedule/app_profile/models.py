from django.contrib.auth.models import User
from django.db import models


class Agent(models.Model):
    user = models.OneToOneField(
        to=User,
        to_field='id',
        on_delete=models.CASCADE,
        unique=True,
        editable=False,
        verbose_name='Веб-пользователь',
        help_text='Ссылка на веб-пользователя, представляющего апи-пользователя в данной системе.'
    )
    group_code = models.CharField(
        max_length=31,
        null=True,
        verbose_name='Группа',
        help_text='Номер группы пользователя.'
    )

    class Meta:
        verbose_name = 'Посредник'
        verbose_name_plural = 'Посредники'

    def __str__(self):
        return f'Agent for {self.user.username}[{self.user.id}]'
