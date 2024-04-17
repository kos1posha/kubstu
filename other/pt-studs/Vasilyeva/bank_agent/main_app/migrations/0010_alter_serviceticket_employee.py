# Generated by Django 5.0.1 on 2024-01-06 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_serviceticket_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceticket',
            name='employee',
            field=models.ForeignKey(help_text='Вы можете сразу назначить сотрудника, обойдя очередь обслуживания.', on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.employee', verbose_name='Ответственный сотрудник'),
        ),
    ]
