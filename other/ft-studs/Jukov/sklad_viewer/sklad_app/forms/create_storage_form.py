from django.forms import ModelForm

from sklad_app.models import Storage


class CreateStorageForm(ModelForm):
    class Meta:
        model = Storage
        fields = ['name', 'description']
