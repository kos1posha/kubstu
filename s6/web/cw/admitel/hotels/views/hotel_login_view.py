from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import FormView

from hotels.forms import HotelLoginForm, HotelLogoutForm


class HotelLoginView(FormView):
    http_method_names = ['post']
    success_url = reverse_lazy('hotels:manage')
    form_class = HotelLoginForm

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            logout(self.request)
        self.request.session.modified = True
        self.request.session['hotel_id'] = form.instance.id
        self.request.session.save()
        return super().form_valid(form)


class HotelLogoutView(FormView):
    http_method_names = ['post']
    success_url = reverse_lazy('welcome')
    form_class = HotelLogoutForm

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            logout(self.request)
        if 'hotel_id' in self.request.session:
            self.request.session.modified = True
            self.request.session.pop('hotel_id')
            self.request.session.save()
        return super().form_valid(form)
