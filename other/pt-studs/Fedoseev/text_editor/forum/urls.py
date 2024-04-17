from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from forum.views import IndexView, RegisterView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
