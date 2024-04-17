from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect


class LogoutView(LogoutView):
    template_name = None

    def get(self, request, *args, **kwargs):
        return redirect('index')
