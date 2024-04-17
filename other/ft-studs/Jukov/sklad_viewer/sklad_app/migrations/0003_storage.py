# Generated by Django 5.0.1 on 2024-01-03 18:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0002_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название хранилища')),
                ('description', models.TextField(help_text='При необходимости, вы можете указать дополнительную информацию', verbose_name='Описание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Хранилище',
                'verbose_name_plural': 'Хранилища',
            },
        ),
    ]
