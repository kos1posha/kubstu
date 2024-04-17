from django.contrib.auth import forms

from main_app.models import Employee, User


class CreateEmployeeForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
        field_classes = {}

    username = forms.UsernameField(label='Уникальный код сотрудника', help_text='Используется для входа в систему.')

    def save(self, commit=True):
        user = super().save()
        employee = Employee(user=user)
        return employee
