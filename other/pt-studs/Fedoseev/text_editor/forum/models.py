from django.contrib.auth.models import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    user = models.ForeignKey(verbose_name='Отправитель', to=User, on_delete=models.CASCADE)
    content = CKEditor5Field(verbose_name='', config_name='extends')
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
