from django.urls import reverse_lazy

from hotels.forms import HotelCreateForm
from django.views.generic import CreateView


class HotelCreateView(CreateView):
    form_class = HotelCreateForm
    template_name = 'hotel_create.html'
    success_url = reverse_lazy('hotels:manage')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['hotel_id'] = form.instance.id
        self.request.session.save()
        return response
