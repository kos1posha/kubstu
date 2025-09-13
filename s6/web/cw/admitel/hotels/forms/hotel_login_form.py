from django import forms
from django.core.exceptions import ValidationError

from hotels.models import Hotel


class HotelLoginForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('key1', 'key2')

    def clean(self):
        key1 = self.cleaned_data['key1']
        key2 = self.cleaned_data['key2']
        hotel = Hotel.objects.filter(key1=key1, key2=key2).first()
        if not hotel:
            raise ValidationError('Отеля с такими ключами не существует')
        self.instance = hotel
        return super().clean()

    def save(self, commit=True):
        return self.instance


class HotelLogoutForm(forms.Form):
    id = forms.IntegerField()

    def clean(self):
        id = self.cleaned_data['id']
        hotel = Hotel.objects.filter(id=id).first()
        if not hotel:
            raise ValidationError('Че стало?')
        return super().clean()
