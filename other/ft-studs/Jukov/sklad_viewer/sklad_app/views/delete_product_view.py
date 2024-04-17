from django.urls import reverse_lazy
from django.views.generic import DeleteView

from sklad_app.models import Product


class DeleteProductView(DeleteView):
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        product = Product.objects.filter(id=pk).first()
        if product:
            self.request.session['init_storage_id'] = product.storage_id
        return product
