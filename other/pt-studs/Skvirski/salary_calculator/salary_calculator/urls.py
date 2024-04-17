from django.contrib import admin
from django.urls import path

from calculator import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CalculateSalaryView.as_view(), name='calculate_salary'),
    path('position/create/', views.CreatePositionView.as_view(), name='create_position'),
    path('position/<int:pk>/update/', views.UpdatePositionView.as_view(), name='update_position'),
    path('position/<int:pk>/delete/', views.DeletePositionView.as_view(), name='delete_position'),
    path('employee/create/', views.CreateEmployeeView.as_view(), name='create_employee'),
    path('employee/<int:pk>/update/', views.UpdateEmployeeView.as_view(), name='update_employee'),
    path('employee/<int:pk>/delete/', views.DeleteEmployeeView.as_view(), name='delete_employee'),
    path('taxes/update/', views.UpdateDefaultTaxesView.as_view(), name='update_taxes'),
]
