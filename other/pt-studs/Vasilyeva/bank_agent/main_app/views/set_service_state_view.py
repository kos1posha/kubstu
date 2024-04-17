from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from main_app.models import ServiceTicket


class SetServiceStateView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        service = ServiceTicket.objects.get(pk=pk)
        state = request.POST.get('state')
        if state == 'Обслуживание успешно завершено':
            service.set_to_done()
            messages.success(request, f'Обслуживание успешно завершено в {service.end_process}')
        elif state == 'Обслуживание перенесено на неопределенный срок':
            service.set_to_fail()
            messages.success(request, f'Обслуживание перенесено на неопределенный срок в {service.end_process}')
        return redirect('employee-panel')
