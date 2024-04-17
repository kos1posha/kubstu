from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from main_app.models import User


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        user = User.objects.filter(pk=self.request.user.pk).first()
        context = super().get_context_data(**kwargs)
        context.update({
            'user': user,
        })
        return context

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(pk=request.user.pk).first()
        if not user:
            messages.error(request, 'Для работы с сервисом, вам необходимо войти.')
            return redirect('login')
        elif user.is_administrator:
            return redirect('administrator-panel')
        elif user.is_employee:
            return redirect('employee-panel')
        else:
            return redirect('create-brunch')
