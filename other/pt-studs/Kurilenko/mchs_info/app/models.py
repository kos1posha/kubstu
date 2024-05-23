import datetime

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

    def date_views(self, date=None):
        date_views = ArticleDateViews.objects.filter(article=self, date=date or datetime.date.today()).first()
        if date_views is None:
            date_views = ArticleDateViews(article=self, date=date)
            date_views.save()
        return date_views

    def views(self):
        return sum(ArticleDateViews.objects.filter(article=self).values_list('views', flat=True))

    def increment_date_views(self):
        date_views = self.date_views()
        date_views.views += 1
        date_views.save()


class ArticleDateViews(models.Model):
    class Meta:
        verbose_name = 'Просмотры за день'
        verbose_name_plural = 'Просмотры за дни'
        unique_together = ('article', 'date')

    article = models.ForeignKey(verbose_name='Статья', to=Article, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата', auto_now_add=True)
    views = models.IntegerField(verbose_name='Количество просмотров', default=0)
