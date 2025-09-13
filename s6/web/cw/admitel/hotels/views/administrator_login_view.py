from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect


class AdministratorLoginView(LoginView):
    http_method_names = ['post']

    def form_invalid(self, form):
        return redirect('welcome')

    def form_valid(self, form):
        if 'hotel_id' in self.request.session:
            self.request.session.modified = True
            self.request.session.pop('hotel_id')
            self.request.session.save()
        return super().form_valid(form)


class AdministratorLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        if 'hotel_id' in self.request.session:
            self.request.session.modified = True
            self.request.session.pop('hotel_id')
            self.request.session.save()
        return super().post(request, *args, **kwargs)
