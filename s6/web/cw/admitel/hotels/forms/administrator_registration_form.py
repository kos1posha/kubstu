from django import forms
from django.contrib.auth.forms import UserCreationForm

from hotels.models import Branch, Administrator, User


class AdministratorRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        error_messages = {
            'email': {
                'unique': 'Данный почтовый адрес уже занят',
            },
            'password2': {
                'password_mismatch': 'Пароли не совпадают'
            }
        }

    contact_phone = forms.CharField(required=True)
    branch = forms.ModelChoiceField(required=True, queryset=Branch.objects.all())

    def save(self, commit=True):
        user = super().save(commit=True)
        admin = Administrator(user=user)
        admin.contact_phone = self.cleaned_data['contact_phone']
        admin.hotel_branch = self.cleaned_data['branch']
        if commit:
            admin.save()
        return admin
