from django import forms

from hotels.models import Hotel


class HotelCreateForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
        error_messages = {
            'name': {
                'max_length': 'Название отеля не должно превышать 150 символов',
                'unique': 'Похоже, у нас уже зарегистрирован отель с таким названием...'
            }
        }

    def clean(self):
        key1 = self.cleaned_data.get('key1')
        key2 = self.cleaned_data.get('key2')
        if key1 == key2:
            self.add_error('key2', 'Ключи доступа должны отличаться')
        return super().clean()
