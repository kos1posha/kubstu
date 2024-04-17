from django.forms import ModelForm

from sklad_app.models import Product


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'weight']
