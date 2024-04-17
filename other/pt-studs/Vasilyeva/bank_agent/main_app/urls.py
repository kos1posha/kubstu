from django.contrib.auth import views as auth_views
from django.urls import path

from main_app import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('brunch/create/', views.CreateBankBrunchView.as_view(), name='create-brunch'),
    path('administrator/', views.AdministratorPanelView.as_view(), name='administrator-panel'),
    path('employee/', views.EmployeePanelView.as_view(), name='employee-panel'),
    path('employee/create/', views.CreateEmployeeView.as_view(), name='create-employee'),
    path('employee/<int:pk>/delete/', views.DeleteEmployeeView.as_view(), name='delete-employee'),
    path('service/create/', views.CreateServiceTicketView.as_view(), name='create-service'),
    path('service/<int:pk>/delete/', views.DeleteServiceTicketView.as_view(), name='delete-service'),
    path('service/<int:pk>/state/', views.SetServiceStateView.as_view(), name='set-service-state'),
]
