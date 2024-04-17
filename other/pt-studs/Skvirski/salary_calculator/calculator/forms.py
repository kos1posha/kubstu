from django import forms
from django.core.exceptions import ValidationError
from django.db.models import TextChoices
from django.forms import NumberInput

from calculator.models import DefaultTaxes, Employee


def get_days_in_month(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


class MonthChoices(TextChoices):
    EMPTY_LABEL = '', 'Выберите месяц'
    JANUARY = '1', 'Январь'
    FEBRUARY = '2', 'Февраль'
    MARCH = '3', 'Март'
    APRIL = '4', 'Апрель'
    MAY = '5', 'Май'
    JUNE = '6', 'Июнь'
    JULY = '7', 'Июль'
    AUGUST = '8', 'Август'
    SEPTEMBER = '9', 'Сентябрь'
    OCTOBER = '10', 'Октябрь'
    NOVEMBER = '11', 'Ноябрь'
    DECEMBER = '12', 'Декабрь'


class CalculateSalaryForm(forms.Form):
    employee = forms.ModelChoiceField(label='Сотрудник', queryset=Employee.objects.filter(position__isnull=False), empty_label='Выберите сотрудника')
    personal_taxes = forms.IntegerField(label='НДФЛ', min_value=0, max_value=99, step_size=1, initial=DefaultTaxes.personal_tax, help_text='Вычитается из ставки сотрудника.',
                                        widget=NumberInput(attrs={'placeholder': 'Налог на доходы физических лиц'}))
    pensionary_taxes = forms.IntegerField(label='Пенсионные отчисления', min_value=0, max_value=99, step_size=1, initial=DefaultTaxes.pensionary_tax, help_text='Не вычитается из ставки сотрудника.')
    month = forms.ChoiceField(label='Месяц', choices=MonthChoices.choices)
    worked_days = forms.IntegerField(label='Количество рабочих дней', min_value=0, step_size=1, initial=24, help_text='Не может превышать количество дней в выбранном месяце.',
                                     widget=NumberInput(attrs={'placeholder': 'Введите количество рабочих дней'}))
    missed_days = forms.IntegerField(label='Количество пропущенных дней', min_value=0, step_size=1, help_text='Не может превышать количество рабочих дней.',
                                     widget=NumberInput(attrs={'placeholder': 'Нет'}), required=False)
    bonus = forms.DecimalField(label='Премия', max_digits=19, decimal_places=2, min_value=0, help_text='Является инициативой работодателя. Не влияет на налоговые отчисления.',
                               widget=NumberInput(attrs={'placeholder': 'Отсутствуют'}), required=False)

    def clean_worked_days(self):
        month = self.cleaned_data.get('month')
        worked_days = self.cleaned_data.get('worked_days')
        if month and worked_days:
            month = int(month)
            month_days = get_days_in_month(month)
            if worked_days > month_days:
                raise ValidationError(f'Убедитесь, что это значение меньше либо равно {month_days}.')
        return worked_days

    def clean_missed_days(self):
        month = self.cleaned_data.get('month')
        worked_days = self.cleaned_data.get('worked_days')
        missed_days = self.cleaned_data.get('missed_days')
        if worked_days and missed_days:
            if month:
                month = int(month)
                month_days = get_days_in_month(month)
                if missed_days > month_days:
                    raise ValidationError(f'Убедитесь, что это значение меньше либо равно {month_days}.')
            if missed_days > worked_days:
                raise ValidationError(f'Убедитесь, что это значение меньше либо равно {worked_days}.')
        return missed_days or 0
