from django.urls import path

from app_schedule.views import schedule_group

app_name='schedule'
urlpatterns = [
    path('', schedule_group, name='schedule'),
]
