from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import DeleteView

from hotels.models import Room


class RoomDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy('hotels:manage')
    http_method_names = ['post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms_modal'] = self.object.branch.id
        return context

    def get_object(self, queryset=None):
        return Room.objects.filter(id=self.request.POST.get('id')).first()

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return redirect('hotels:manage')
