from django.apps import apps
from django.core.exceptions import ValidationError
from django.db import models

from main_app.models.service_ticket import ServiceState, ServiceTicket


def cant_be_administrator(user_id):
    User = apps.get_model('main_app', 'User')
    user = User.objects.get(id=user_id)
    if user.is_administrator:
        raise ValidationError(
            'Профиль администратора не может одновременно выполнять обязанности сотрудника.'
        )


class Employee(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    user = models.OneToOneField(verbose_name='Пользователь', to='main_app.User', on_delete=models.CASCADE, validators=[cant_be_administrator])
    brunch = models.ForeignKey(verbose_name='Филиал', to='main_app.BankBrunch', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user)

    @property
    def username(self):
        return self.user.username

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def current_service(self):
        return self.serviceticket_set.filter(state=ServiceState.PROCESSING).first()
