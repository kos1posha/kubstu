from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from project import settings

urlpatterns = [
    path('', include('app_schedule.urls')),
    path('profile/', include('app_profile.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
