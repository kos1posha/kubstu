from django.contrib.auth import models as djmodels
from django.db import models as m
from django.utils import timezone as djtz


class UserManager(djmodels.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(djmodels.AbstractBaseUser, djmodels.PermissionsMixin):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    email = m.EmailField(verbose_name='Адрес электронной почты', max_length=254, unique=True)
    password = m.CharField(verbose_name='Пароль', max_length=128)

    first_name = m.CharField(verbose_name='Имя', max_length=150)
    last_name = m.CharField(verbose_name='Фамилия', max_length=150)
    is_active = m.BooleanField(verbose_name='Активен', default=True)
    is_staff = m.BooleanField(verbose_name='Персонал', default=False)
    is_superuser = m.BooleanField(verbose_name='Суперпользователь', default=False)
    last_login = m.DateTimeField(verbose_name='Последний вход', blank=True, null=True)
    date_joined = m.DateTimeField(verbose_name='Зарегистрирован', default=djtz.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def is_admin(self):
        return self.is_staff or self.is_superuser

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
