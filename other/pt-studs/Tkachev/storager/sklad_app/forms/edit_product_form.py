from django.forms import ModelForm

from sklad_app.models import Product


class EditProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'weight']
