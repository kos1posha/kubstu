from datetime import datetime

from django import forms
from django.utils import timezone

from main.models import To


class FiltersForm(forms.Form):
    to = forms.ModelChoiceField(label='Куда', queryset=To.objects.all(), empty_label='Куда угодно')
    date = forms.DateField(label='Когда', required=False, initial='Когда угодно')

    def __init__(self, to=None, date=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cleaned_data = []
        self.fields['date'].widget.input_type = 'date'
        if to:
            self.fields['to'].initial = to
        if date:
            self.fields['date'].initial = date
            if date != 'Когда угодно':
                dt = datetime.strptime(date, '%Y-%m-%d')
                if dt.date() < timezone.now().date():
                    self.add_error('date', 'На прошедшие даты поездок вы точно не сыщите')
