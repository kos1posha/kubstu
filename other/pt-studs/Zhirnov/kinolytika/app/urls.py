from django.urls import path

import app.views as views


app_name = 'kino'
urlpatterns = [
    path('entry/', views.LoginView.as_view(template_name='login_logup.html'), name='login'),
    path('register/', views.RegisterView.as_view(), name='register')
]
