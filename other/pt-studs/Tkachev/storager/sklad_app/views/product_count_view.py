from django.urls import reverse_lazy
from django.views.generic import UpdateView

from sklad_app.forms import ProductCountForm
from sklad_app.models import Product


class ProductCountView(UpdateView):
    form_class = ProductCountForm
    success_url = reverse_lazy('index')
    http_method_names = ['post', 'options']

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        product = Product.objects.filter(id=pk).first()
        if product:
            self.request.session['init_storage_id'] = product.storage_id
        return product
