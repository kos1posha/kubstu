from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import TemplateView

from main_app.forms import CreateEmployeeForm, CreateServiceTicketForm
from main_app.models import Employee, ServiceState, ServiceTicket, User


class AdministratorPanelView(TemplateView):
    template_name = 'bank_agent/administrator_panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        administrator = User.objects.filter(pk=self.request.user.pk).first()
        services = ServiceTicket.objects.all()
        employees = Employee.objects.filter(brunch=administrator.brunch)
        context.update({
            'administrator': administrator,
            'actual_services': services.filter(Q(brunch=administrator.brunch) & Q(state__in=[ServiceState.IN_QUEUE, ServiceState.PROCESSING])),
            'history_services': services.filter(Q(brunch=administrator.brunch) & Q(state__in=[ServiceState.DONE, ServiceState.FAIL])),
            'employees': employees,
            'create_service_ticket_form': CreateServiceTicketForm(employees=employees.filter(Q(serviceticket__state__in=[ServiceState.DONE, ServiceState.FAIL]) | Q(serviceticket=None))),
            'create_employee_form': CreateEmployeeForm(),
        })
        return context

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(pk=request.user.pk).first()
        if not user.is_administrator:
            messages.error(request, 'У вас нет доступа к панели администратора.')
            return redirect('index')
        return super().get(request, *args, **kwargs)
