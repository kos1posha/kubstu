from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import DeleteView

from hotels.models import Branch


class BranchDeleteView(DeleteView):
    model = Branch
    success_url = reverse_lazy('hotels:manage')
    http_method_names = ['post']

    def get_object(self, queryset=None):
        return Branch.objects.filter(id=self.request.POST.get('id')).first()

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return redirect('hotels:manage')
