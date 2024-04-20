from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from autostop import settings
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('trips/', views.FindTripsView.as_view(), name='trips'),
    path('analytics/', views.AnalyticsView.as_view(), name='analytics')
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    for prefix, root in settings.STATICFILES_DIRS:
        urlpatterns.extend(static(f'{settings.STATIC_URL}{prefix}/',  document_root=root))
