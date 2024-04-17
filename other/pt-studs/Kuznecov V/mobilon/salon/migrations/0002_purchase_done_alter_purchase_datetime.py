# Generated by Django 5.0.1 on 2024-01-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='done',
            field=models.BooleanField(default=0, verbose_name='Состояние'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='datetime',
            field=models.DateTimeField(verbose_name='Дата сделки'),
        ),
    ]
