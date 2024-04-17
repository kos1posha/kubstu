from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from main_app.forms import CreateEmployeeForm
from main_app.models import User


class CreateEmployeeView(FormView):
    form_class = CreateEmployeeForm
    http_method_names = ['post']
    success_url = reverse_lazy('administrator-panel')

    def form_valid(self, form):
        administrator = User.objects.filter(pk=self.request.user.pk).first()
        employee = form.save()
        employee.brunch = administrator.brunch
        employee.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Данные нового сотрудника не валидны.')
        return redirect('administrator-panel')
