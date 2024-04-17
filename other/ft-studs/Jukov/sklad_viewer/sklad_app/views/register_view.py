from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from sklad_app.forms import RegisterForm
from sklad_app.utils import get_index_forms


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('index')
    http_method_names = ['post', 'options']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        context = get_index_forms(self.request, rf=form)
        return render(self.request, 'index.html', context)
