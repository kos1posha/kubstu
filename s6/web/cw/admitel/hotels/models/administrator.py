from django.contrib.auth import get_user_model
from django.db import models as m


class Administrator(m.Model):
    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'

    user = m.OneToOneField(verbose_name='Пользователь', to='hotels.User', on_delete=m.CASCADE)
    contact_phone = m.CharField(verbose_name='Контактный номер', max_length=11)
    hotel_branch = m.ForeignKey(verbose_name='Филиал', to='hotels.Branch', on_delete=m.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'contact_phone']

    def save(self, *args, **kwargs):
        if not self.user_id:
            User = get_user_model()
            self.user = User.objects.create_user(
                email=self.user.email,
                password=self.user.password,
                first_name=self.user.first_name,
                last_name=self.user.last_name
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.hotel_branch.hotel}: {self.user}'

    @property
    def full_name(self):
        return f'{self.user.last_name} {self.user.first_name}'
    