from django.db import models

from main_app.models.employee import Employee


class BankBrunch(models.Model):
    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    name = models.CharField(verbose_name='Название филиала', max_length=60, help_text='Обязательное поле. Не более 60 символов.')
    administrator = models.OneToOneField(
        verbose_name='Администратор', to='main_app.User', help_text='Администратор отвечает за создание обслуживающих талонов.', on_delete=models.CASCADE,
        error_messages={'unique': 'Данный администратор уже отвечает за один филиал.'},
    )

    def __str__(self):
        return f'{self.name} ({self.administrator.username})'

    @property
    def employees(self):
        return Employee.objects.filter(brunch=self)
