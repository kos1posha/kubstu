from django.urls import reverse_lazy

from hotels.forms import AdministratorRegistrationForm
from django.views.generic import CreateView


class AdministratorRegistrationView(CreateView):
    form_class = AdministratorRegistrationForm
    template_name = 'administrator_registration.html'
    success_url = reverse_lazy('hotels:manage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branch_id'] = self.kwargs['branch_id']
        return context
