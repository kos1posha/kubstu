from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import FormView

from app_profile.models import Agent
from app_profile.proxies import ApiUser, ApiKey


def profile(request, username):
    user = request.user
    api_user = ApiUser.get(user.email)
    if api_user == 404:
        api_user = ApiUser.new(user.first_name, user.last_name, user.email)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'edit-user-info':
            user.first_name = request.POST.get('user-first-name')
            user.last_name = request.POST.get('user-last-name')
            user.email = request.POST.get('user-email')
            if user.agent is None:
                user.agent = Agent()
            user.agent.group_code = request.POST.get('user-group-code')
            user.save()
            user.agent.save()
        elif action == 'get-api-key':
            ApiKey.new(user.email)
        elif action == 'del-api-key':
            key = request.POST.get('key')
            ApiKey.get(key).toggle()
    api_keys = []
    for api_key in api_user.keys():
        if api_key.is_active:
            api_keys.append(api_key)
    return render(request, 'profile/profile.html', context={'api_keys': api_keys})


class RegistrationView(FormView):
    form_class = UserCreationForm
    success_url = '/profile/login'

    def form_valid(self, form):
        form.save()
        form.non_field_errors()
        return super(RegistrationView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationView, self).form_invalid(form)
