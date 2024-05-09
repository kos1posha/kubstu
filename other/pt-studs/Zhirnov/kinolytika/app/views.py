from django.contrib.auth import authenticate, login
import django.contrib.auth.forms as auth_forms
import django.contrib.auth.views as auth_views
from django.urls import reverse_lazy
from django.utils import timezone
import django.views.generic as generic_views

from app.models import FilmShow


class LoginView(auth_views.LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        register_form: auth_forms.UserCreationForm = context.get('register_form')
        if register_form:
            context['register_form'] = auth_forms.UserCreationForm(data=register_form.data)
        else:
            context['register_form'] = auth_forms.UserCreationForm()
        context['register_form'].fields['username'].help_text = 'Только буквы, цифры и символы @/./+/-/_'
        context['register_form'].fields['password1'].help_text = 'Ваш пароль должен содержать как минимум 8 символов'
        context['register_form'].fields['password2'].help_text = 'Для подтверждения введите, пожалуйста, пароль ещё раз'
        return context


class RegisterView(generic_views.FormView):
    form_class = auth_forms.UserCreationForm
    success_url = reverse_lazy('index')
    http_method_names = ['post']

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class FilmsView(generic_views.ListView):
    template_name = 'films.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        active_films = sorted(FilmShow.objects.all().filter(datetime__gt=timezone.now()), key=lambda f: f.datetime)
        return active_films
