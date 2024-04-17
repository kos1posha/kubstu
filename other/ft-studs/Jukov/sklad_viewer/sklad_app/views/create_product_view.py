from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from sklad_app.forms import CreateProductForm
from sklad_app.models import Product
from sklad_app.utils import get_index_forms


class CreateProductView(FormView):
    form_class = CreateProductForm
    success_url = reverse_lazy('index')
    http_method_names = ['post', 'options']

    def form_valid(self, form):
        product = form.save(False)
        storage_id = self.kwargs['storage_id']
        self.request.session['init_storage_id'] = storage_id
        unique_constraint_check = Product.objects.filter(storage_id=storage_id, vendor_code=form.cleaned_data['vendor_code']).first()
        if unique_constraint_check:
            form.add_error('vendor_code', 'Товар с таким артикулом уже есть в данном хранилище.')
            return self.form_invalid(form)
        product.storage_id = storage_id
        product.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        self.request.session['init_storage_id'] = self.kwargs['storage_id']
        context = get_index_forms(self.request, cpf=form)
        return render(self.request, 'index.html', context)
