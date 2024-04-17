from django.urls import reverse_lazy
from django.views.generic import UpdateView

from sklad_app.forms.edit_product_form import EditProductForm
from sklad_app.models import Product


class EditProductView(UpdateView):
    form_class = EditProductForm
    success_url = reverse_lazy('index')
    http_method_names = ['post', 'options']

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        product = Product.objects.filter(id=pk).first()
        if product:
            self.request.session['init_storage_id'] = product.storage_id
        return product
