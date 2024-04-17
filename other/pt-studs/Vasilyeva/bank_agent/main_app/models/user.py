from django.contrib.auth.models import User

from main_app.models.bank_brunch import BankBrunch

from main_app.models.employee import Employee


class User(User):
    class Meta:
        proxy = True
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.get_full_name()

    @property
    def verbose_type(self):
        if self.is_administrator:
            return 'Администратор'
        elif self.is_employee:
            return 'Сотрудник'
        return ''

    @property
    def brunch(self):
        if self.is_administrator:
            return BankBrunch.objects.get(administrator=self)
        elif self.is_employee:
            return Employee.objects.get(user=self).brunch
        return None

    @property
    def is_administrator(self):
        return BankBrunch.objects.filter(administrator=self).exists()

    @property
    def is_employee(self):
        return Employee.objects.filter(user=self).exists()
