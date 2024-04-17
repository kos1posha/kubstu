from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from sklad_app.forms import RegisterForm


class LoginView(LoginView):
    http_method_names = ['post', 'options']
    template_name = None

    def get(self, request, *args, **kwargs):
        return redirect('index')

    def form_invalid(self, form):
        context = {
            'auth_form': AuthenticationForm(),
            'register_form': RegisterForm(),
            'auth_error': 'Пользователь не найден'
        }
        return render(self.request, 'index.html', context=context)
