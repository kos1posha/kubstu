from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView

from hotels.models import Branch


class BranchCreateView(CreateView):
    model = Branch
    fields = '__all__'
    success_url = reverse_lazy('hotels:manage')
    http_method_names = ['post']

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return redirect('hotels:manage')
    