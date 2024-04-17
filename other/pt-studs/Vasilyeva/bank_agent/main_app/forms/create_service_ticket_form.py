from django import forms

from main_app.models import Employee, ServiceTicket


class CreateServiceTicketForm(forms.ModelForm):
    class Meta:
        model = ServiceTicket
        fields = ['client', 'service', 'employee']

    def __init__(self, employees=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if employees is None:
            employees = Employee.objects.all()
        self.fields['employee'].queryset = employees
        self.fields['employee'].empty_label = None
        if employees:
            self.fields['employee'].initial = employees.first().id
