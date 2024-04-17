# Generated by Django 5.0.1 on 2024-01-03 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0004_alter_storage_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=16, verbose_name='Артикул')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('count', models.IntegerField(verbose_name='Название')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Вес (кг.)')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad_app.storage', verbose_name='Хранилище')),
            ],
        ),
    ]
