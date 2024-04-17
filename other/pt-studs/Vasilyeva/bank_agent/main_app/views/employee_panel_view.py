from django.shortcuts import redirect
from django.views.generic import TemplateView

from main_app.models import Employee, User


class EmployeePanelView(TemplateView):
    template_name = 'bank_agent/employee_panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.filter(pk=self.request.user.pk).first()
        employee = Employee.objects.filter(user=user).first()
        context.update({
            'user': user,
            'employee': employee,
        })
        return context

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(pk=request.user.pk).first()
        if not user.is_employee:
            return redirect('index')
        return super().get(request, *args, **kwargs)
