# Generated by Django 5.0.1 on 2024-01-18 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0009_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(editable=False, max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(editable=False, max_length=50, verbose_name='Фамилия'),
        ),
    ]
