from django.forms import ModelForm

from sklad_app.models import Product


class ProductCountForm(ModelForm):
    class Meta:
        model = Product
        fields = ['count']
