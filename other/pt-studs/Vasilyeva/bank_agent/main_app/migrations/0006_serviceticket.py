# Generated by Django 5.0.1 on 2024-01-05 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_employee_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.IntegerField(choices=[(1, 'Другое'), (2, 'Выдача и поддержка пластиковых карт'), (3, 'Страхование'), (4, 'Вклады для физических лиц'), (5, 'Кредиты'), (6, 'Оплата квитанций'), (7, 'Консультации'), (8, 'Обмен валют'), (9, 'Денежные переводы'), (10, 'Консультация брокера')], default=1, verbose_name='Услуга')),
                ('state', models.IntegerField(choices=[(1, 'В очереди'), (2, 'Обрабатывается'), (3, 'Успешно обработан'), (4, 'Был отложен на неопределенный срок')], default=1, verbose_name='Состояние')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('start_process', models.DateTimeField(blank=True, null=True, verbose_name='Начало обслуживания')),
                ('end_process', models.DateTimeField(blank=True, null=True, verbose_name='Конец обслуживания')),
                ('employee', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.employee', verbose_name='Ответственный сотрудник')),
            ],
            options={
                'verbose_name': 'Обслуживаемые талоны',
            },
        ),
    ]
