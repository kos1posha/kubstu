from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from main_app.forms import CreateServiceTicketForm
from main_app.models import ServiceState, User


class CreateServiceTicketView(FormView):
    form_class = CreateServiceTicketForm
    http_method_names = ['post']
    success_url = reverse_lazy('administrator-panel')

    def form_valid(self, form):
        administrator = User.objects.filter(pk=self.request.user.pk).first()
        service = form.save(False)
        service.brunch = administrator.brunch
        if service.employee:
            if service.employee.current_service:
                messages.error(self.request, 'Данный сотрудник уже обслуживает талон.')
                return redirect('administrator-panel')
            service.state = ServiceState.PROCESSING
        service.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Данные обслуживаемого талона не валидны.')
        return redirect('administrator-panel')
