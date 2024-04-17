from django.contrib.auth.forms import UserCreationForm

from sklad_app.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        field_classes = {}
