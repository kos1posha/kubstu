# Generated by Django 5.0.4 on 2024-05-05 15:22

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='', verbose_name='Превью')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('duration', models.TimeField(verbose_name='Продолжительность')),
                ('description', models.TextField(verbose_name='Описание')),
                ('genres', models.ManyToManyField(to='app.genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='FilmShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=16, validators=[django.core.validators.MinValueValidator(limit_value=1)], verbose_name='Стоимость билета')),
                ('datetime', models.DateField(verbose_name='Время показа')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.film', verbose_name='Фильм')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hall', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Киносеанс',
                'verbose_name_plural': 'Киносеансы',
            },
        ),
        migrations.CreateModel(
            name='HallPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1)], verbose_name='Номер')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hall', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Место в зале',
                'verbose_name_plural': 'Места в залах',
                'unique_together': {('number', 'hall')},
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата приобретения')),
                ('filmshow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.filmshow', verbose_name='На сеанс')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hallplace', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
                'unique_together': {('filmshow', 'place')},
            },
        ),
    ]
