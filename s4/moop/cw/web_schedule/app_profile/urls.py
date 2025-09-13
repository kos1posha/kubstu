from django.contrib.auth.views import *
from django.urls import path

from app_profile.views import *

app_name = 'profile'
urlpatterns = [
    path('registration', RegistrationView.as_view(template_name='profile/registration.html'), name='registration'),
    path('login', LoginView.as_view(template_name='profile/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    # path('password_reset', PasswordResetView.as_view(template_name='profile/password_reset.html'), name='password_reset'),
    path('<str:username>', profile, name='profile'),
]
