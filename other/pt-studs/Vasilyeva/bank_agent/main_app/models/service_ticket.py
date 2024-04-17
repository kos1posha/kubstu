from django.db import models
from django.utils import timezone


class Service(models.IntegerChoices):
    OTHER = 1, 'Другое'
    CARDS = 2, 'Выдача и поддержка пластиковых карт'
    INSURANCES = 3, 'Страхование'
    DEPOSITS = 4, 'Вклады для физических лиц'
    LOANS = 5, 'Кредиты'
    RECEIPT_PAYMENTS = 6, 'Оплата квитанций'
    CONSULTATIONS = 7, 'Консультации'
    CURRENCY_EXCHANGE = 8, 'Обмен валют'
    MONEY_TRANSFERS = 9, 'Денежные переводы'
    BROKER_CONSULTATION = 10, 'Консультация брокера'


class ServiceState(models.IntegerChoices):
    IN_QUEUE = 1, 'В очереди'
    PROCESSING = 2, 'Обрабатывается'
    DONE = 3, 'Успешно обработан'
    FAIL = 4, 'Был отложен на неопределенный срок'


class ServiceTicket(models.Model):
    class Meta:
        verbose_name = 'Обслуживаемый талон'
        verbose_name_plural = 'Обслуживаемые талоны'

    employee = models.ForeignKey(verbose_name='Ответственный сотрудник', help_text='Вы можете сразу назначить сотрудника, обойдя очередь обслуживания.', to='main_app.Employee', on_delete=models.DO_NOTHING)
    client = models.CharField(verbose_name='ФИО клиента', max_length=100)
    brunch = models.ForeignKey(verbose_name='Филиал', to='main_app.BankBrunch', on_delete=models.DO_NOTHING)
    service = models.IntegerField(verbose_name='Услуга', choices=Service.choices, default=Service.OTHER)
    state = models.IntegerField(verbose_name='Состояние', choices=ServiceState.choices, default=ServiceState.IN_QUEUE)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True, editable=False)
    start_process = models.DateTimeField(verbose_name='Начало обслуживания', blank=True, null=True)
    end_process = models.DateTimeField(verbose_name='Конец обслуживания', blank=True, null=True)

    def set_employee_to_processing(self, employee):
        self.employee = employee
        self.state = ServiceState.PROCESSING
        self.start_process = timezone.now()
        self.save()

    def set_to_done(self):
        if self.employee:
            self.state = ServiceState.DONE
            self.end_process = timezone.now()
            self.save()

    def set_to_fail(self):
        if self.employee:
            self.state = ServiceState.FAIL
            self.end_process = timezone.now()
            self.save()
