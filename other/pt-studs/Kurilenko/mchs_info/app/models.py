from django.db import models
from django.utils import timezone


class Article(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    slug = models.SlugField(verbose_name='Ссылка на статью', unique=True)
    title = models.CharField(max_length=300, verbose_name='Название статьи')
    main_photo = models.ImageField(verbose_name='Фото', blank=True, null=True, max_length=300)
    preview = models.CharField(max_length=300, verbose_name='Превью')
    content = models.TextField(verbose_name='Контент')
    create = models.DateTimeField(verbose_name='Написана', auto_now_add=True)

    def get_absolute_url(self):
        return f'{self.slug}'

    @property
    def createf(self):
        delta = (timezone.now().date() - self.create.date()).days
        match delta:
            case 0:
                return f'сегодня в {timezone.localtime(self.create).strftime("%H:%M")}'
            case 1:
                return f'вчера в {timezone.localtime(self.create).strftime("%H:%M")}'
            case 2:
                return f'позавчера в {timezone.localtime(self.create).strftime("%H:%M")}'
            case _:
                return self.create
