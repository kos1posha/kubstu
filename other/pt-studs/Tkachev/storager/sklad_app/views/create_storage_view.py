from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from sklad_app.forms import CreateStorageForm
from sklad_app.utils import get_index_forms


class CreateStorageView(FormView):
    form_class = CreateStorageForm
    success_url = reverse_lazy('index')
    http_method_names = ['post', 'options']

    def form_valid(self, form):
        storage = form.save(False)
        storage.user = self.request.user
        storage.save()
        self.request.session['init_storage_id'] = storage.id
        return super().form_valid(form)

    def form_invalid(self, form):
        context = get_index_forms(self.request, csf=form)
        return render(self.request, 'index.html', context)
