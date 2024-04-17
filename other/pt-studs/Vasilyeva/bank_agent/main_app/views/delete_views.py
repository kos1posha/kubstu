from django.urls import reverse_lazy
from django.views.generic import DeleteView

from main_app.models import Employee, ServiceTicket


class DeleteEmployeeView(DeleteView):
    success_url = reverse_lazy('administrator-panel')

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        return Employee.objects.get(pk=pk)


class DeleteServiceTicketView(DeleteView):
    success_url = reverse_lazy('administrator-panel')

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        return ServiceTicket.objects.get(pk=pk)
